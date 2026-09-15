# Grok Build

Installation: [instructions](../install.md#grok-build). This is the `grok` coding CLI. Grok models in another host use that host's profile; [Grok Bot](grok-bot.md) has a separate runtime.

| Reference | Grok Build location |
| --- | --- |
| `<project-skills>` | `.grok/skills` |
| `<user-skills>` | `~/.grok/skills` |
| `<model-config>` | `~/.grok/pstack-models.md` |
| Instructions | Project `AGENTS.md`; Claude instruction files are also supported |
| Agent definitions | `.grok/agents/`, `~/.grok/agents/`, enabled plugin `agents/` |
| Settings | `~/.grok/config.toml`; project `.grok/config.toml` supports only MCP, plugins and permissions |

If `GROK_HOME` is set, use it instead of `~/.grok`. Write model role preferences as plain Markdown in `<model-config>`; pstack reads them explicitly. Keep unrelated settings intact. [Settings reference](https://docs.x.ai/build/settings/reference).

Grok loads enabled plugin `skills/` directories and supports Claude Code plugins. Keep the complete pstack bundle and use one installation; compatibility scanners can also find existing Claude/Cursor skills. Check `/skills` for invocation names. `disable-model-invocation` preserves manual invocation; skill `model`, `effort` and `allowed-tools` fields do not enforce those settings. [Skills and plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces).

## Agents and tools

`Task` maps to the exposed `task` delegation tool; `generalPurpose` maps to `general-purpose`. Check `/agents` for registered pstack roles; otherwise give a general worker its bundled role file. Built-in `explore` and `plan` agents cannot run shell commands or edit files. Personas change behaviour, not model family or tool permissions. Check runtime availability rather than assuming subagents are enabled. [Subagents](https://docs.x.ai/build/features/subagents).

Use the live read, search, edit, shell and todo tools; use the native question tool when exposed, otherwise chat. Discover integrations through `/mcps` or `grok mcp list`. Browser verification needs an available integration or project scripts. Use supported permissions and sandbox controls for read-only intent. Local worktrees do not implement Cursor cloud parameters.

## Continuation and models

Resolve models with `grok models`; keep `--effort` separate from `--model`. Custom providers can supply another model family when actually configured. Use `grok inspect --json` to inspect discovered extensions and rules. [CLI reference](https://docs.x.ai/build/cli/reference).

Use `/resume` or `grok sessions list` for the current workspace, then `grok export <id>` for a Markdown transcript. Raw sessions under `~/.grok/sessions/` are keyed by working directory; do not assume Cursor JSONL layout. [Sessions](https://docs.x.ai/build/features/sessions).

Native `/loop` schedules recurring turns, with a minimum interval of 60 seconds and a seven-day expiry. Verify restoration and runtime lifetime before treating a loop as unattended automation. Background commands and monitors are available; they are not Grok Bot routines. Use native Plan Mode when exposed and the router's fallbacks for goal, canvas, durable scheduling or cloud services that are absent. [Background tasks](https://docs.x.ai/build/features/background-tasks).
