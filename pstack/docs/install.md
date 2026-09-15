# Install pstack

Keep the complete plugin directory so skills can read shared profiles, agents and resources. Choose the active harness below. Runtime mappings are in [harness mapping](harnesses.md).

## Cursor

Install pstack through Cursor's plugin UI using its `.cursor-plugin/plugin.json`. Confirm `poteto-mode` appears in Skills and the agent roles appear in the agent catalogue. Keep the entire plugin directory. See [plugins](https://cursor.com/docs/plugins) and the [manifest reference](https://cursor.com/docs/reference/plugins).

## Codex

Pstack includes a local marketplace and `.codex-plugin/plugin.json`. Keep the complete bundle and run:

```sh
codex plugin marketplace add /absolute/path/to/cursor-plugins/pstack
codex plugin add pstack@pstack-local
```

These commands and all bundled skills were checked with Codex CLI 0.154.0 in isolated local state. Check `codex plugin --help` on other versions. Plugin skills are namespaced; the tested CLI shows `pstack:poteto-mode`. Pstack's `/skill` notation is not a guarantee of a Codex slash command. [Plugins](https://developers.openai.com/codex/plugins), [packaging and marketplaces](https://developers.openai.com/plugins/build/plugins).

## Claude Code

From a checkout of this repository, test the bundle with `claude --plugin-dir /absolute/path/to/cursor-plugins/pstack`. For a persistent local installation:

```sh
claude plugin validate /absolute/path/to/cursor-plugins/pstack/.claude-plugin/plugin.json
claude plugin marketplace add /absolute/path/to/cursor-plugins/pstack
claude plugin install pstack@pstack-local
```

Start a new session and invoke `/pstack:poteto-mode`. Plugin skills are namespaced; `/how` in pstack prose means `/pstack:how`. The manifest uses default `skills/` and `agents/` discovery. Copying only `SKILL.md` files loses shared references. [Plugin installation](https://code.claude.com/docs/en/plugins), [plugin reference](https://code.claude.com/docs/en/plugins-reference).

## Gemini CLI

Keep the repository checkout and link the pstack directory:

```sh
gemini extensions link /absolute/path/to/cursor-plugins/pstack
gemini extensions list
```

Start a new session and check `/skills list`. Ask Gemini to activate `poteto-mode`; skill names are not guaranteed to become slash commands. `gemini-extension.json` packages the existing `skills/` directory without loading the whole workflow into global context. This is a Gemini extension, not a Cursor or Claude plugin installation. [Extension reference](https://geminicli.com/docs/extensions/reference/).

## GitHub Copilot

Pstack provides an Agent Skills installation here, not a Copilot plugin manifest. Skill support and subagent support differ across Copilot CLI, VS Code and GitHub cloud agent. Check the client's supported customisations before using a delegated workflow. [Support matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).

Copy the contents of this repository's entire `pstack/` directory into the target repository's `.github/` directory, so `skills/`, `docs/`, `agents/`, `automations/` and supporting resources retain their relative layout. Keep each directory's contents and relative layout intact. Check for collisions first and merge existing directories deliberately; do not overwrite unrelated skills or instructions. Keeping the companion `docs/` and `agents/` directories makes `../../docs/harnesses.md` and sibling role references resolve from an installed skill. The Cursor/Claude/Codex manifests in the copied bundle do not register a Copilot plugin.

Restart the client and ask it to use `poteto-mode`. Confirm it reads the installed skill. A slash command in pstack prose is a workflow reference; use the client's skill picker or name the skill explicitly when that command is absent. [Agent Skills installation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## OpenCode

Copy the complete contents of `pstack/` into the target project's `.opencode/` directory, preserving `skills/`, `docs/`, `agents/`, scripts and supporting resources. Check for collisions and merge deliberately; do not overwrite unrelated configuration. Restart OpenCode and ask it to use `poteto-mode`. This uses native skill discovery; OpenCode's JavaScript plugin loader does not load the Cursor, Claude or Codex manifests. [Skills](https://opencode.ai/docs/skills/).

## Antigravity

Pstack includes Antigravity's root `plugin.json`. With the CLI installed, run:

```sh
agy plugin install /absolute/path/to/cursor-plugins/pstack
agy plugin list
```

Restart the agent and select or explicitly request `poteto-mode`. Confirm its shared files remain in the installed bundle. For workspace skill discovery, copy the complete contents of `pstack/` into the workspace's `.agents/` directory, preserving the relative layout. Check for collisions and merge deliberately; use one installation. CLI and IDE discovery paths vary by version. [Plugins](https://antigravity.google/docs/cli/plugins), [skills](https://antigravity.google/docs/skills).

## Grok Build

Keep the complete bundle and launch the coding CLI with:

```sh
grok --plugin-dir /absolute/path/to/cursor-plugins/pstack
```

Grok Build supports Claude Code plugins, so pstack uses its existing `.claude-plugin/plugin.json`. Check `/plugins` and `/skills` for the loaded bundle and invoke `poteto-mode` using the name shown there. For persistence, copy the complete bundle to `.grok/plugins/pstack/` in the project, or `~/.grok/plugins/pstack/` for the user. Use one installation to avoid duplicates from compatibility scanning. [Skills and plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces).

## Grok Bot

Use Settings → Plugins to install the packaged skill through the marketplace when available, then enable it for the current Bot under Yours. This checkout is not published by these instructions. For a private workspace installation, copy the full `pstack/` directory to `/workspace/pstack/` on the Bot's computer, then ask the Bot to save a private skill named `poteto-mode` whose instructions read `/workspace/pstack/skills/poteto-mode/SKILL.md` and follow its linked harness profile. Enable it under Yours and verify `/poteto-mode` reads that file. Keep the bundle on that computer; a path on your laptop is not available there. This uses the documented private-skill flow, not an assumed local-directory plugin loader. [Private skills](https://cursor.com/docs/grok-bot/work), [plugin settings](https://cursor.com/docs/grok-bot/settings).

## Verify a bundle

From this repository, run:

```sh
python3 pstack/scripts/check-portability.py
node --test pstack/skills/poteto-mode/scripts/check-plan.test.mjs
node scripts/validate-plugins.mjs
claude plugin validate pstack/.claude-plugin/plugin.json --strict
claude plugin validate pstack/.claude-plugin/marketplace.json --strict
python3 pstack/scripts/check-codex.py pstack
```

The repository manifest check needs `ajv` and `ajv-formats`, as in its CI workflow. The Codex check needs the installed CLI; it creates isolated temporary state and installs a temporary copy of this plugin, without a model call or changes to your live installation. It checks skill discovery, shared reference files and invocation metadata. Its output names the retained evidence directory.

Native discovery also passed on Claude Code 2.1.270 for all 55 skills and both agents, without a model call. `--bare` omits plugin agents in that version, so use normal plugin loading to exercise agent registration.

OpenCode 1.18.30 discovered exactly all 55 skills and both agents in isolated local state, without a model call. The agents load with mode `all`; set `mode: subagent` in OpenCode's installed copies if they should be available only for delegation. Cursor's `is_background` field does not configure OpenCode scheduling.

Gemini, Copilot, Antigravity and Grok installation is documented against their native skill/extension support; those clients were unavailable for a live loader check. A plugin install does not provision cloud workers, integrations or a scheduler.
