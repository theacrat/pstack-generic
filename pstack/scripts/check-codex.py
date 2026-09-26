#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path
import re
import select
import shutil
import subprocess
import tempfile
import time


def run(command, env, cwd, output):
    result = subprocess.run(command, env=env, cwd=cwd, capture_output=True, text=True, timeout=30)
    output.write_text(result.stdout)
    output.with_suffix('.stderr').write_text(result.stderr)
    if result.returncode:
        raise RuntimeError(f'{command!r}: exit {result.returncode}: {result.stderr}')
    return json.loads(result.stdout)


def list_skills(env, workspace, output):
    with output.with_suffix('.stderr').open('w') as stderr:
        server = subprocess.Popen(['codex', 'app-server', '--stdio'], env=env, cwd=workspace,
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=stderr,
                                  text=True, bufsize=1)
        responses = []

        def rpc(request):
            server.stdin.write(json.dumps(request) + '\n')
            server.stdin.flush()
            if 'id' not in request:
                return None
            deadline = time.monotonic() + 30
            while time.monotonic() < deadline:
                if not select.select([server.stdout], [], [], 1)[0]:
                    continue
                line = server.stdout.readline()
                if not line:
                    raise RuntimeError('App server closed before responding')
                response = json.loads(line)
                responses.append(response)
                if response.get('id') == request['id']:
                    if 'error' in response:
                        raise RuntimeError(response['error'])
                    return response['result']
            raise TimeoutError(request['method'])

        try:
            init = rpc({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {
                'clientInfo': {'name': 'pstack_native_probe', 'version': '1.0'},
                'capabilities': {'experimentalApi': True}}})
            assert Path(init['codexHome']).resolve() == Path(env['CODEX_HOME']).resolve(), init
            rpc({'jsonrpc': '2.0', 'method': 'initialized', 'params': {}})
            result = rpc({'jsonrpc': '2.0', 'id': 2, 'method': 'skills/list', 'params': {
                'cwds': [str(workspace)], 'forceReload': True}})
            output.write_text(json.dumps({'initialize': init, 'result': result}, indent=2) + '\n')
            return result
        finally:
            output.with_suffix('.rpc.json').write_text(json.dumps(responses, indent=2) + '\n')
            server.terminate()
            server.wait(timeout=5)


def probe(source, root, layout):
    case = root / layout
    case.mkdir()
    for name in ('state', 'home', 'workspace'):
        (case / name).mkdir()
    market = case / 'market'
    plugin = market if layout == 'embedded' else market / 'plugins' / 'pstack'
    shutil.copytree(source, plugin)
    manifest_dir = market / '.agents' / 'plugins'
    manifest_dir.mkdir(parents=True, exist_ok=True)
    marketplace_name = f'pstack-probe-{layout}'
    marketplace = {'name': marketplace_name, 'plugins': [{'name': 'pstack',
        'source': {'source': 'local', 'path': './' if layout == 'embedded' else './plugins/pstack'},
        'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_USE'},
        'category': 'Productivity'}]}
    (manifest_dir / 'marketplace.json').write_text(json.dumps(marketplace, indent=2) + '\n')
    env = os.environ.copy()
    env['CODEX_HOME'] = str(case / 'state')
    env['HOME'] = str(case / 'home')
    env.pop('CODEX_THREAD_ID', None)
    added = run(['codex', 'plugin', 'marketplace', 'add', str(market), '--json'],
                env, case / 'workspace', case / 'marketplace-add.json')
    installed = run(['codex', 'plugin', 'add', f'pstack@{marketplace_name}', '--json'],
                    env, case / 'workspace', case / 'plugin-add.json')
    cache = Path(installed['installedPath'])
    response = list_skills(env, case / 'workspace', case / 'skills-list.json')
    errors = [error for entry in response['data'] for error in entry['errors']]
    skills = [skill for entry in response['data'] for skill in entry['skills']
              if skill.get('pluginId') == installed['pluginId']]
    expected = {f'pstack:{path.parent.name}' for path in source.glob('skills/*/SKILL.md')}
    actual = {skill['name'] for skill in skills}
    assert not errors, errors
    assert actual == expected, {'missing': sorted(expected - actual), 'extra': sorted(actual - expected)}
    assert all(skill['enabled'] for skill in skills)
    required_docs = ['docs/harnesses.md'] + [f'docs/harnesses/{name}.md'
                     for name in ('cursor', 'codex', 'claude', 'gemini', 'copilot', 'antigravity', 'grok', 'grok-bot', 'opencode')]
    for relative in required_docs:
        assert (cache / relative).is_file(), relative
        assert (cache / relative).read_bytes() == (source / relative).read_bytes(), relative
    links = []
    for file in cache.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', file.read_text()):
            target = target.split('#')[0]
            if 'docs/harnesses' not in target or '://' in target:
                continue
            resolved = (file.parent / target).resolve()
            assert resolved.is_file(), (file, target)
            assert resolved.is_relative_to(cache.resolve()), (file, target)
            links.append({'file': str(file.relative_to(cache)), 'target': target})
    result = {'layout': layout, 'marketplace': added, 'installed': installed, 'skills': len(skills),
              'errors': errors, 'all_enabled': True, 'required_docs': required_docs,
              'resolved_harness_links': links}
    (case / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    return {key: result[key] for key in ('layout', 'skills', 'errors', 'all_enabled')} | {'resolved_harness_links': len(links)}


def main():
    parser = argparse.ArgumentParser(description='Isolated, no-model native Codex plugin discovery probe')
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = args.output or Path(tempfile.mkdtemp(prefix='pstack-native-discovery-'))
    root.mkdir(parents=True, exist_ok=True)
    version = subprocess.check_output(['codex', '--version'], text=True).strip()
    result = {'cli': version, 'source': str(args.source.resolve()), 'root': str(root),
              'cases': [probe(args.source.resolve(), root, layout) for layout in ('outer', 'embedded')]}
    (root / 'summary.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
