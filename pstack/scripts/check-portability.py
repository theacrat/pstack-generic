#!/usr/bin/env python3
"""Check the shared plugin's packaging and dependency links without a harness install."""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


for relative in [".cursor-plugin/plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json", "plugin.json"]:
    path = ROOT / relative
    if not path.exists():
        errors.append(f"Missing {relative}")
        continue
    manifest = json.loads(path.read_text())
    require(manifest.get("name") == "pstack", f"{relative}: name must be pstack")
    for key in ["skills", "agents"]:
        value = manifest.get(key)
        if isinstance(value, str):
            require((ROOT / value).exists(), f"{relative}: missing {key} path {value}")

versions = {json.loads((ROOT / directory / "plugin.json").read_text())["version"]
            for directory in [".cursor-plugin", ".codex-plugin", ".claude-plugin"]
            if (ROOT / directory / "plugin.json").exists()}
require(len(versions) == 1, "Plugin manifest versions differ")
antigravity = json.loads((ROOT / "plugin.json").read_text())
require(set(antigravity) <= {"name", "description"}, "Antigravity manifest has unsupported fields")
marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
require(marketplace["plugins"][0]["source"] == {"source": "local", "path": "./"}, "Codex marketplace must install the complete plugin root")

for name in ["cursor", "codex", "claude", "gemini", "copilot", "antigravity", "grok", "grok-bot", "opencode"]:
    require((ROOT / f"docs/harnesses/{name}.md").is_file(), f"Missing {name} profile")

skills = {path.parent.name: path for path in (ROOT / "skills").glob("*/SKILL.md")}
for name in ["create-skill", "deslop", "control-cli", "control-ui", "verify-this", "loop", "goal", "automate"]:
    require(name in skills, f"Missing bundled dependency {name}")

for name, path in skills.items():
    text = path.read_text()
    frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    require(frontmatter is not None, f"{name}: missing frontmatter")
    if not frontmatter:
        continue
    declared = re.search(r"^name: (.+)$", frontmatter[1], re.M)
    require(declared is not None and declared[1].strip('\"\'') == name, f"{name}: name must match directory")
    require(re.search(r"^description: ?\S", frontmatter[1], re.M) is not None, f"{name}: missing description")
    body = text[frontmatter.end():]
    if re.search(r"Cursor|cursor|<model-config>|<project-skills>|<user-skills>|\bTask\b|AskQuestion|transcript|`/loop`|`/goal`", body):
        require("../../docs/harnesses.md" in body, f"{name}: missing harness entry point")

for path in ROOT.rglob("*.md"):
    text = path.read_text()
    require("/Users/thea/" not in text, f"{path.relative_to(ROOT)}: private absolute path")
    # Examples can deliberately link to files in a future generated skill.
    text = re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$", "", text, flags=re.S | re.M)
    for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith(("#", "/")):
            continue
        target = target.split("#", 1)[0]
        if not target or target == "url" or any(token in target for token in ["<", ">", "*", "{"]):
            continue
        require((path.parent / target).exists(), f"{path.relative_to(ROOT)}: missing link {target}")

require(".cursor/projects" not in (ROOT / "skills/poteto-mode/scripts/worktree-audit.sh").read_text(), "Worktree audit must use an explicit workspace transcript directory")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(skills)} skill entry points, bundled dependencies, links, and harness manifests")
