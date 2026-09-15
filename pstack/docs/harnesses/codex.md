# Codex

Installation: [instructions](../install.md#codex).

## Paths and preferences

| Reference | Codex location |
| --- | --- |
| `<project-skills>` | `.agents/skills` |
| `<user-skills>` | `~/.agents/skills` |
| `<model-config>` | `~/.codex/pstack-models.md` |
| Project and user instructions | `AGENTS.md`, `~/.codex/AGENTS.md` |
| Native agent definitions | `.codex/agents/*.toml`, `~/.codex/agents/*.toml` on versions supporting these |
| Configuration | `.codex/config.toml`, `~/.codex/config.toml` |

Respect an explicitly configured `CODEX_HOME` in place of `~/.codex`. Write model role lines as plain Markdown in `<model-config>` and read it explicitly. This file is a pstack convention, not a native auto-loaded rule. Do not overwrite `AGENTS.md`, TOML settings or shell execution rules. [Skills](https://developers.openai.com/codex/skills), [configuration](https://developers.openai.com/codex/config-reference).

Use the host's session/history API or `codex resume` to locate current-project history. Older CLI sessions use `~/.codex/sessions/<year>/<month>/<day>/rollout-*.jsonl`; newer builds may use paginated thread storage. Inspect session metadata to confirm workspace ownership and use the supported reader. Do not assume one filesystem layout or parse all projects' messages. The installed CLI's `agents`, `resume` and `migrate-rollouts --help` describe available access.

## Agents and tools

Invoke a bundled skill through the picker or a `$` mention using its registered name; slash notation in these workflows is shorthand.

`Task` maps to the exposed spawn API, commonly `spawn_agent` plus message/wait tools. Use exactly the schema provided by this host. `generalPurpose` maps to its general worker. Codex does not register Cursor Markdown agent files merely because they are in `agents/`. Give an available worker `agents/poteto-agent.md` or `agents/comment-sicko.md` to read first; native registration requires a supported Codex definition. [Subagents](https://developers.openai.com/codex/subagents).

Do not pass unsupported `environment`, `cloud_base_branch`, `readonly` or `run_in_background` fields. Spawned local agents may share a checkout; assign separate worktrees before concurrent writes. A cloud task requires the separate cloud service. Preserve read-only intent using allowed tools and actual sandbox settings, without assuming MCP reads disappear in read-only mode.

`AskQuestion` maps to the available request-input tool only in modes where it is callable, otherwise chat. Discover MCP/apps from the live catalogue and supported search tools. Use `exec_command` or the exposed shell tool for `Read`/`Search` through `cat`/`rg`; use `update_plan` when exposed for todos. Browser control requires an installed integration or project scripts.

## Continuation and models

Map `CreateGoal`, `UpdateGoal` and goal reads to `create_goal`, `update_goal` and `get_goal` when exposed, following their schemas and state-transition rules. Use native scheduling, plan and canvas tools when the runtime supplies them. CLI, desktop and hosted sessions differ. Verify that a schedule survives session exit before calling it durable. Otherwise apply the router's explicit session-only fallback. Cursor cloud sleepers and webhook routines require a separately configured service.

Use the supplied model catalogue and agent-role constraints. Reasoning is normally `model_reasoning_effort` in native configuration, or the exposed spawn tool's `reasoning_effort` when supported; it is not part of a model slug. A fork may prohibit model overrides; respect that limit. Preserve available family diversity, and disclose when this Codex deployment only offers one family. Cursor skill UI metadata is not Codex mode configuration. Native CLI 0.154.0 accepts these skill files. The bundled plugin-creator helper is stricter and rejects the retained `disable-model-invocation` frontmatter flag; report that helper result separately from native installation and skill-loader checks.
