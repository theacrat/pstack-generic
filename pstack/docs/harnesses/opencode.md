# OpenCode

Installation: [instructions](../install.md#opencode). This profile covers OpenCode V2 and OpenChamber, which runs on an OpenCode V2 server. Use V2 documentation at <https://opencode.ai/v2/docs/>; V1 pages describe different tools and fields.

| Reference | OpenCode location |
| --- | --- |
| `<project-skills>` | `.opencode/skills` |
| `<user-skills>` | `~/.config/opencode/skills` |
| `<model-config>` | `~/.config/opencode/pstack-models.md` (pstack convention) |
| Project instructions | `AGENTS.md` only; V2 has no `CLAUDE.md` fallback and does not load the config `instructions` array |
| Agent definitions | `.opencode/agents/*.md`, `~/.config/opencode/agents/*.md`, or `agents` in config |
| Configuration | `opencode.json[c]`, `.opencode/opencode.json[c]`, `~/.config/opencode/opencode.json[c]` |
| CLI preferences | `~/.config/opencode/cli.json` |

OpenCode also discovers skills from `.agents/skills`, `.claude/skills`, `~/.agents/skills` and `~/.claude/skills`, and from paths or URLs in the config `skills` array. The skill ID comes from the directory name, not the frontmatter `name`; a later source with the same ID replaces an earlier one, so keep one installation. OpenCode advertises each skill's description and loads its body through the `skill` tool. Keep pstack's whole directory together so `docs/`, `agents/`, scripts and relative references resolve. The Cursor, Claude and Codex manifests are not OpenCode plugins. [Skills](https://opencode.ai/v2/docs/skills/), [instructions](https://opencode.ai/v2/docs/instructions/), [config](https://opencode.ai/v2/docs/config/).

Write model role lines as plain Markdown in `<model-config>`. OpenCode does not load that file on its own; skills read it when choosing models.

## Agents and tools

`Task` maps to the `subagent` tool: pass the agent ID, a short description and a complete prompt, with `background: true` for concurrent work. Pass the returned `sessionID` to continue that child. `generalPurpose` maps to the built-in `general` subagent. `explore` is the built-in read-only subagent; use it, or an agent whose permissions deny `edit` and `shell`, for `readonly: true`. V2 has no `readonly` flag, and MCP tools stay available under read-only permissions. [Agents](https://opencode.ai/v2/docs/agents/), [tools](https://opencode.ai/v2/docs/tools/).

The default nesting depth is one, and `general` cannot launch subagents. A pstack step that has a subagent spawn its own subagents runs those children from the parent instead, or the child owns the work directly with the same review separation. Say so when that removes a review layer.

The pstack agents load from `agents/` but default to `mode: primary`, and Cursor's `is_background` field is kept as a request-body overlay. In installed copies, set `mode: subagent` (or `all`) and delete `is_background` so `poteto-agent` and `comment-sicko` appear in the subagent catalogue. Background execution comes from the `subagent` tool's `background` argument.

Tool names: `read`, `glob`, `grep`, `edit`, `write`, `patch` (on models that receive it), `shell`, `webfetch`, `websearch`, `question` for `AskQuestion`, `skill` and `subagent`. `execute` runs Code Mode, which exposes MCP servers, the `opencode` session utilities and, in the desktop app, the `browser` namespace for live UI checks. Discover MCP tools from the live catalogue or `opencode mcp list`. Permissions in config or agent frontmatter can hide or deny any tool.

## Models

Run `opencode models` or `/models` and use the reported `provider/model` reference. Effort is a variant: `provider/model#variant`, where variant names such as `high` or `max` come from that model's catalogue and differ between models. Record the variant in `<model-config>` with the reference, pass it as the `subagent` tool's `model` when the tool exposes that argument, and otherwise set `model` in the agent's frontmatter. `opencode run --model provider/model#variant` selects one for a CLI run. Do not invent references or treat a variant as a different model family. [Models](https://opencode.ai/v2/docs/models/).

## Sessions and continuation

`opencode session list --format json` lists the current project's top-level sessions; `opencode session export <sessionID> --sanitize` exports one for handoff. `opencode run --continue`, `--session <id>` and `--fork` resume or branch from the CLI. OpenCode itself has no durable goal, loop or scheduler: a session wait lasts only while the agent stays active. Treat `/goal` and `/loop` as session-scoped unless OpenChamber is available. [CLI commands](https://opencode.ai/v2/docs/cli/commands/).

## OpenChamber

OpenChamber is an independent app that runs OpenCode V2 and adds tools to the agent. Detect it by the `openchamber` and `openchamber_web` tools, called through `execute`. It uses the same skills, agents, config and `AGENTS.md` as OpenCode. The control tools are missing when OpenChamber connects to an external server (`OPENCODE_HOST` or skip-start) or runs in the VS Code extension; use the plain OpenCode mappings then. [OpenChamber](https://github.com/openchamber/openchamber), [agent control tool](https://github.com/openchamber/openchamber/blob/main/packages/docs/content/docs/agent-control-tool.mdx).

- **Goals.** Map `CreateGoal` to `openchamber` `session.create` or `session.send` with `goal: true` and, when the user asked for one, `goalTokenBudget`. An auditor model checks each turn against the objective and continues the session until it is done, blocked or out of budget, while the OpenChamber server keeps running. The auditor sees only the objective and the latest reply, so write a self-contained objective. The UI's target button arms the same goal. [Session goals](https://github.com/openchamber/openchamber/blob/main/packages/docs/content/docs/session-goals.mdx).
- **Loops and schedules.** `schedule.create` with `daily`, `weekly`, `once` or `cron`, plus `timezone`, `model` and `agent`, creates a durable scheduled task. `schedule.run`, `schedule.toggle`, `schedule.list` and `schedule.delete` manage it. A scheduled task starts a new session for each run, so its prompt must stand alone. Committed loops live in `.agents/loops/*.md` with cron `schedule`, `model` and `enabled: true`. Tasks fire only while the OpenChamber server runs. [Scheduled tasks](https://github.com/openchamber/openchamber/blob/main/packages/docs/content/docs/scheduled-tasks.mdx).
- **Isolated workers.** `session.create` with `worktree` (and optional `branch`, `startRef`) starts a top-level session in its own worktree. Use it for per-PR owners and swarm or arena lanes that need a separate checkout or that must spawn their own subagents. These sessions do not report back like `subagent` children: record each session ID and poll with `session.status` or `session.messages` (`last: true`), or pass `wait: true` with `lastAssistant: true`. Uncommitted changes do not carry into a new worktree. `session.fork` branches an existing session. None of these are cloud workers.
- **Browser.** `openchamber_web` drives the browser panel (`browser.open`, `browser.snapshot`, `browser.click`, `browser.type`, `browser.capture`, `browser.inspect`). It meets `control-ui`'s live-surface requirement when no project driver exists; page content is untrusted data.
- **Multi-run.** The UI's Multi-run sends one prompt to up to five models, each in its own session and optionally its own worktree. It is a manual alternative to an arena fan-out, not a judge.
