# Install pstack

Keep the complete plugin directory so skills can read shared profiles, agents and resources. Choose the active harness below. Runtime mappings are in [harness mapping](harnesses.md).

## Cursor

Install pstack from the marketplace in Customize, at project or user scope, using its `.cursor-plugin/plugin.json`. To test a local checkout, place it in `~/.cursor/plugins/local/pstack` (symlinks pointing outside that folder are skipped), or run the CLI with `agent --plugin-dir /absolute/path/to/cursor-plugins/pstack`. Confirm `poteto-mode` appears in Skills and the agent roles appear in the agent catalogue. Keep the entire plugin directory. See [plugins](https://cursor.com/docs/plugins) and the [manifest reference](https://cursor.com/docs/reference/plugins).

## Codex

Pstack includes a local marketplace and `.codex-plugin/plugin.json`. Keep the complete bundle and run:

```sh
codex plugin marketplace add /absolute/path/to/cursor-plugins/pstack
codex plugin add pstack@pstack-local
```

These commands and all bundled skills were checked with Codex CLI 0.155.1 in isolated local state. Check `codex plugin --help` on other versions. Plugin skills are namespaced; the tested CLI shows `pstack:poteto-mode`. Pstack's `/skill` notation is not a guarantee of a Codex slash command. [Plugins](https://developers.openai.com/codex/plugins), [packaging and marketplaces](https://developers.openai.com/plugins/build/plugins).

## Claude Code

From a checkout of this repository, test the bundle with `claude --plugin-dir /absolute/path/to/cursor-plugins/pstack`. For a persistent local installation:

```sh
claude plugin validate /absolute/path/to/cursor-plugins/pstack/.claude-plugin/plugin.json
claude plugin marketplace add /absolute/path/to/cursor-plugins/pstack
claude plugin install pstack@pstack-local
```

Start a new session and invoke `/pstack:poteto-mode`. Plugin skills are namespaced; `/how` in pstack prose means `/pstack:how`. The manifest uses default `skills/` and `agents/` discovery. Copying only `SKILL.md` files loses shared references. [Plugin installation](https://code.claude.com/docs/en/plugins), [plugin reference](https://code.claude.com/docs/en/plugins-reference).

## Gemini CLI

Gemini CLI now serves only paid API keys, Vertex AI and Code Assist Standard or Enterprise; free and consumer-plan users should install for Antigravity instead. Gemini rejects agent files with unknown frontmatter, so remove Cursor's `is_background` line from `agents/poteto-agent.md` in the copy you install. Then link it:

```sh
gemini extensions link /absolute/path/to/pstack --consent
gemini extensions list
gemini skills list
```

`--consent` skips the interactive security prompt. Linking a checkout whose `poteto-agent.md` still has `is_background` loads the skills but drops that agent with a validation error. Ask Gemini to activate `poteto-mode`; skill names are not guaranteed to become slash commands. `gemini-extension.json` packages the existing `skills/` directory without loading the whole workflow into global context. [Extension reference](https://geminicli.com/docs/extensions/reference/).

## GitHub Copilot

Copilot CLI loads pstack as a plugin through its existing `.claude-plugin/` manifests:

```sh
copilot plugin marketplace add /absolute/path/to/cursor-plugins/pstack
copilot plugin install pstack@pstack-local
copilot skill list
```

For one session, `copilot --plugin-dir /absolute/path/to/cursor-plugins/pstack` works too. Plugin roles register as `pstack:poteto-agent` and `pstack:comment-sicko`. The installed plugin loads live from that path, so keep the checkout. VS Code reads the same Claude-format plugin through `chat.pluginLocations`, and the cloud agent enables plugins through `enabledPlugins` and `extraKnownMarketplaces` in the repository's `.github/copilot/settings.json`. [CLI plugins](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference), [about plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins), [VS Code agent plugins](https://code.visualstudio.com/docs/copilot/customization/agent-plugins).

Do not copy the whole `pstack/` directory into `.github/`. That copies pstack's `README.md` to `.github/README.md`, which GitHub then shows as the repository's front page. A skills-only install for a client without plugin support copies `skills/`, `docs/` and `agents/` into `.github/`, preserving their layout so `../../docs/harnesses.md` resolves. Check for collisions first and merge deliberately. Skill and subagent support differ across Copilot CLI, VS Code and the cloud agent. [Support matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).

## OpenCode

These steps target OpenCode V2 and OpenChamber, which runs on OpenCode V2. Copy the complete contents of `pstack/` into the target project's `.opencode/` directory, preserving `skills/`, `docs/`, `agents/`, scripts and supporting resources. For every project, copy it into `~/.config/opencode/` instead. Check for collisions and merge deliberately; do not overwrite unrelated configuration. Use one installation, since a later copy of a skill ID replaces an earlier one.

In the installed `agents/*.md`, set `mode: subagent` and delete `is_background`. Without that change the pstack agents load as primary agents and cannot be launched by the `subagent` tool.

Run `opencode reload` or start a new session, then ask OpenCode to use `poteto-mode`. OpenChamber reads the same directories; restart its managed server from Settings if the skills do not appear. The Cursor, Claude and Codex manifests are not OpenCode plugins. [Skills](https://opencode.ai/v2/docs/skills/), [agents](https://opencode.ai/v2/docs/agents/).

## Antigravity

Pstack includes Antigravity's root `plugin.json`. With the CLI installed, run:

```sh
agy plugin install /absolute/path/to/cursor-plugins/pstack
agy plugin list
```

`agy plugin install` copies the bundle to `~/.gemini/config/plugins/pstack/`. Restart the agent and invoke `/pstack:poteto-mode`; plugin skills are namespaced. `agy plugin validate /absolute/path/to/cursor-plugins/pstack` checks the bundle first. Confirm its shared files remain in the installed bundle. For workspace skill discovery, copy the complete contents of `pstack/` into the workspace's `.agents/` directory, preserving the relative layout. Check for collisions and merge deliberately; use one installation. CLI and IDE discovery paths vary by version. [Plugins](https://antigravity.google/docs/plugins?tab=cli), [skills](https://antigravity.google/docs/skills).

## Grok Build

Grok Build supports Claude Code plugins, so pstack uses its existing `.claude-plugin/plugin.json`. Keep the complete bundle and run:

```sh
grok plugin validate /absolute/path/to/cursor-plugins/pstack
grok plugin install /absolute/path/to/cursor-plugins/pstack --trust
grok inspect
```

`plugin install` copies the bundle to `~/.grok/installed-plugins/` and adds it to `[plugins] enabled` in `~/.grok/config.toml`. The top-level `grok` command does not accept `--plugin-dir`; that flag belongs to `grok agent`. A bundle copied by hand into `~/.grok/plugins/pstack/` stays off until `pstack` is listed under `[plugins] enabled`, and a project copy in `.grok/plugins/pstack/` also needs the folder trusted. Check `/plugins` and `/skills` for the loaded bundle and invoke `poteto-mode` using the name shown there. Use one installation to avoid duplicates from compatibility scanning. [Skills and plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces).

## Grok Bot

Use Settings → Plugins to install the packaged plugin through the marketplace when available. Installed plugins are account-wide and available to every Bot. This checkout is not published by these instructions. For a private workspace installation, copy the full `pstack/` directory to `/workspace/pstack/` on the Bot's computer, then ask the Bot to save a private skill named `poteto-mode` whose instructions read `/workspace/pstack/skills/poteto-mode/SKILL.md` and follow its linked harness profile. Enable it under Yours and verify `/poteto-mode` reads that file. Keep the bundle on that computer; a path on your laptop is not available there. This uses the documented private-skill flow, not an assumed local-directory plugin loader. [Private skills](https://cursor.com/docs/grok-bot/work), [plugin settings](https://cursor.com/docs/grok-bot/settings).

## Verify a bundle

From this repository, run:

```sh
python3 pstack/scripts/check-portability.py
claude plugin validate pstack/skills --strict
claude plugin validate pstack/agents --strict
node --test pstack/skills/poteto-mode/scripts/check-plan.test.mjs
node scripts/validate-plugins.mjs
claude plugin validate pstack/.claude-plugin/plugin.json --strict
claude plugin validate pstack/.claude-plugin/marketplace.json --strict
python3 pstack/scripts/check-codex.py pstack
```

The repository manifest check needs `ajv` and `ajv-formats`, as in its CI workflow. The Codex check needs the installed CLI; it creates isolated temporary state and installs a temporary copy of this plugin, without a model call or changes to your live installation. It checks skill discovery, shared reference files and invocation metadata. Its output names the retained evidence directory.

Native discovery was checked on 2026-09-26 in isolated local state, without a model call:

| Harness | Version | Result |
| --- | --- | --- |
| Codex | 0.155.1 | 55 skills in both marketplace layouts |
| Claude Code | 2.1.283 | 55 skills and both agents (`claude plugin details`) |
| OpenCode | 2.0.15 | 55 skills and both agents from `.opencode/`; agents load as `mode: primary` until changed |
| Gemini CLI | 0.61.0 | 55 skills; `poteto-agent` fails validation until `is_background` is removed |
| Copilot CLI | 1.0.88 | 55 skills as a plugin and as `.github/skills` |
| Antigravity CLI | 1.2.9 | 55 skills and both agents (`agy plugin validate`, `agy agents`) |
| Grok Build | 1.0.41 | 55 skills and both agents after `grok plugin install --trust` |

Cursor and Grok Bot were checked against their documentation only. `--bare` in Claude Code omits plugin agents, so use normal plugin loading to exercise agent registration. A plugin install does not provision cloud workers, integrations or a scheduler.
