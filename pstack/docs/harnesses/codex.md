# Codex

Installation: [instructions](../install.md#codex).

## Paths and preferences

| Reference | Codex location |
| --- | --- |
| `<project-skills>` | `.agents/skills` |
| `<user-skills>` | `~/.agents/skills` |
| `<model-config>` | `~/.codex/pstack-models.md` |
| Project and user instructions | `AGENTS.md`, `~/.codex/AGENTS.md` |
| Native agent definitions | `.codex/agents/*.toml`, `~/.codex/agents/*.toml`, or `agents.<name>` in config |
| Configuration | `.codex/config.toml`, `~/.codex/config.toml` |

Respect an explicitly configured `CODEX_HOME` in place of `~/.codex`. Write model role lines as plain Markdown in `<model-config>` and read it explicitly. This file is a pstack convention, not a native auto-loaded rule. Do not overwrite `AGENTS.md`, TOML settings or shell execution rules. [Skills](https://learn.chatgpt.com/docs/build-skills), [configuration](https://learn.chatgpt.com/docs/config-file/config-reference).

Use the host's session/history API or `codex resume` to locate current-project history. Older CLI sessions use `~/.codex/sessions/<year>/<month>/<day>/rollout-*.jsonl`; newer builds may use paginated thread storage. Inspect session metadata to confirm workspace ownership and use the supported reader. Do not assume one filesystem layout or parse all projects' messages.

## Agents and tools

Invoke a bundled skill through the picker or a `$` mention using its registered name; slash notation in these workflows is shorthand.

Codex's skill loader ignores the `disable-model-invocation` frontmatter flag, so skills that set it can still be invoked implicitly. The native control is a per-skill `agents/openai.yaml` with `policy: allow_implicit_invocation: false`. Pstack does not ship those files.

`Task` maps to `spawn_agent`, with `send_input`, `wait_agent`, `resume_agent` and `close_agent`. Use exactly the schema provided by this host. `generalPurpose` maps to the built-in `default` or `worker` role; `explorer` suits read-only exploration. Codex does not register Cursor Markdown agent files merely because they are in `agents/`. Give an available worker `agents/poteto-agent.md` or `agents/comment-sicko.md` to read first; native registration needs a TOML definition with `name`, `description` and `developer_instructions`. [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Do not pass unsupported `environment`, `cloud_base_branch`, `readonly` or `run_in_background` fields. Spawned local agents may share a checkout; assign separate worktrees before concurrent writes, or start the session with `--worktree`. A cloud task requires the separate cloud service. Preserve read-only intent using allowed tools and actual sandbox settings, without assuming MCP reads disappear in read-only mode.

`AskQuestion` maps to the available request-input tool only in modes where it is callable, otherwise chat. Discover MCP/apps from the live catalogue and supported search tools. Use `exec_command` or the exposed shell tool for `Read`/`Search` through `cat`/`rg`; use `update_plan` when exposed for todos. Browser control requires an installed integration or project scripts.

## Continuation and models

Map `CreateGoal`, `UpdateGoal` and goal reads to `create_goal`, `update_goal` and `get_goal`; goals are on by default, with an optional token budget and one unfinished goal per thread. `update_goal` may set `paused`, `blocked` or `complete` only as its schema allows. Durable schedules are Scheduled tasks, created and managed in the ChatGPT desktop app or web, not the CLI; desktop schedules need the app running. Verify that a schedule survives session exit before calling it durable. Otherwise apply the router's explicit session-only fallback. Cursor cloud sleepers and webhook routines require a separately configured service. [Scheduled tasks](https://learn.chatgpt.com/docs/automations).

Use the supplied model catalogue and agent-role constraints. Reasoning is `model_reasoning_effort` in native configuration, `agents.default_subagent_reasoning_effort` for subagents, or the spawn tool's `reasoning_effort`; it is not part of a model slug. A full-history fork (`fork_turns` omitted or `"all"`) inherits the parent's model and effort and rejects overrides, so set `fork_turns` to `none` or a number when a role needs its own model. Preserve available family diversity, and disclose when this Codex deployment only offers one family. Cursor skill UI metadata is not Codex mode configuration. Native CLI 0.155.1 accepts these skill files. The bundled plugin-creator helper is stricter and rejects the retained `disable-model-invocation` frontmatter flag; report that helper result separately from native installation and skill-loader checks.
