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

Grok loads enabled plugin `skills/` directories and supports Claude Code plugins. Plugins are off until listed in `[plugins] enabled`, and project plugins also need a trusted folder. Keep the complete pstack bundle and use one installation; compatibility scanners can also find existing Claude/Cursor skills. Check `/skills` for invocation names. Pstack's `loop` skill collides with the built-in `/loop` and becomes `/pstack:loop`. `disable-model-invocation` preserves manual invocation; skill `model`, `effort` and `allowed-tools` fields do not enforce those settings. [Skills and plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces).

## Agents and tools

`Task` maps to `spawn_subagent` (`prompt`, `description`, `run_in_background`, `isolation: worktree`, `resume_from`, `cwd` and an optional `model`); read results with `get_command_or_subagent_output`. It takes no subagent type, and an omitted type means `general-purpose`, so `generalPurpose` needs no mapping. Subagents cannot spawn their own subagents; run nested fan-out from the parent. Check `/agents` for registered pstack roles; otherwise give a general worker its bundled role file. Built-in `explore` and `plan` agents cannot edit files; shell access varies by version. Personas change behaviour, not model family or tool permissions. Check runtime availability rather than assuming subagents are enabled. [Subagents](https://docs.x.ai/build/features/subagents).

Use the live read, search, edit, shell and todo tools; use the native question tool when exposed, otherwise chat. Discover integrations through `/mcps` or `grok mcp list`. Browser verification needs an available integration or project scripts. Use `--sandbox read-only` or permission modes for read-only intent. Local worktrees do not implement Cursor cloud parameters.

## Continuation and models

Resolve models with `grok models`; keep `--effort` separate from `--model`. The `spawn_subagent` `model` argument is hidden when `subagent_model_inheritance` is on and every picker model is from xAI; then every role runs on the parent model, so disclose it. `[subagents.models]` and `[subagents.personas]` (with `model` and `reasoning_effort`) route roles natively. Custom providers can supply another model family when actually configured. Use `grok inspect --json` to inspect discovered extensions and rules. [CLI reference](https://docs.x.ai/build/cli/reference).

Use `/resume` or `grok sessions list` for the current workspace, then `grok export <id>` for a Markdown transcript. Raw sessions live at `~/.grok/sessions/<url-encoded-cwd>/<id>/updates.jsonl`; do not assume Cursor JSONL layout. [Sessions](https://docs.x.ai/build/features/sessions).

Map `CreateGoal` to native `/goal <objective> [--budget <tokens>]`, with `status`, `pause`, `resume` and `clear`, when goal mode is enabled; a goal completes only after an evidence review. Native `/loop` fires each run in a detached background subagent that cannot see the conversation, so its prompt must stand alone; the minimum interval is 60 seconds and loops expire after seven days. Verify restoration and runtime lifetime before treating a loop as unattended automation. Background commands and `monitor` are available; they are not Grok Bot routines. Use native Plan Mode when exposed and the router's fallbacks for canvas, durable scheduling or cloud services that are absent. [Background tasks](https://docs.x.ai/build/features/background-tasks).
