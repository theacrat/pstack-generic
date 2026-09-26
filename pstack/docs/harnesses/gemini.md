# Gemini CLI

Installation: [instructions](../install.md#gemini-cli).

Since June 2026, Gemini CLI serves only paid API keys, Vertex AI and Code Assist Standard or Enterprise; free and consumer-plan users moved to [Antigravity](antigravity.md).

| Reference | Gemini CLI location |
| --- | --- |
| `<project-skills>` | `.gemini/skills` |
| `<user-skills>` | `~/.gemini/skills` |
| `<model-config>` | `~/.gemini/pstack-models.md` |
| Instructions | Project `GEMINI.md`, `~/.gemini/GEMINI.md` |
| Agent definitions | `.gemini/agents/*.md`, `~/.gemini/agents/*.md`, extension `agents/` |
| Settings and MCP configuration | `.gemini/settings.json`, `~/.gemini/settings.json` |

`.agents/skills` and `~/.agents/skills` are supported aliases. Use one installation to avoid duplicate names. `gemini skills list` checks discovery without a model call. Write model role lines as plain Markdown in `<model-config>`; pstack reads it explicitly. Do not rewrite `GEMINI.md` or settings to persist these choices. [Skills](https://geminicli.com/docs/cli/skills/), [configuration](https://geminicli.com/docs/reference/configuration/).

Use `gemini --list-sessions` for the current project, then `gemini --resume <id>` or `/resume`. For raw history, use the session path reported by the installed version. The local cache contains `~/.gemini/tmp/<project>/chats/session-*.jsonl`, where `<project>` comes from `~/.gemini/projects.json`; verify the association before reading it. Each file starts with a metadata record, followed by update records. [Session management](https://geminicli.com/docs/cli/session-management/).

## Agents and tools

`Task` maps to the exposed subagent tool. Gemini registers custom agents as named tools; `@name` forces one. `generalPurpose` maps to the built-in `generalist`; `codebase_investigator` suits read-only exploration. Use a registered pstack role, otherwise `generalist` instructed to read its bundled role file. Subagents cannot call other subagents, so run nested fan-out from the parent. If no subagent is available, apply the router's serial fallback and retain any unmet independent-review requirement.

Agent frontmatter accepts only `name`, `description`, `kind`, `tools`, `mcpServers`, `model`, `temperature`, `max_turns` and `timeout_mins`. An unknown key such as Cursor's `is_background` fails validation and the agent does not load, so installed copies must drop it. Use `tools` allowlists and `mcpServers` for read-only intent. Remote A2A agents (`kind: remote`) need an `agent_card_url` or `agent_card_json`; `auth` is optional. They do not implement Cursor's `environment: cloud` or `cloud_base_branch`. [Subagents](https://geminicli.com/docs/core/subagents/), [remote agents](https://geminicli.com/docs/core/remote-agents/).

Use `read_file`, `grep_search`/`glob` and `write_todos` for file reads, search and task tracking. Use `ask_user` for questions, otherwise chat. Inspect `/mcp` and the active tool catalogue; use `run_shell_command` for terminal work and an installed browser integration, the `browser_agent` subagent when enabled, or project verification scripts for UI checks. Read-only work must keep the read tools it needs. Do not assume a Cursor readonly flag controls Gemini MCP access. [Tools](https://geminicli.com/docs/reference/tools).

## Continuation and models

`/model` and `--model` change only the main session. Set a subagent's model in its `model` frontmatter. Effort is not a frontmatter field: set it in `settings.json` under `modelConfigs.overrides`, with `thinkingConfig` (`thinkingBudget` for 2.5 models, `thinkingLevel` for 3-series) and `match.overrideScope` naming the agent. Gemini model variants do not provide cross-family review by themselves. A separately configured remote agent can supply another family only when it really runs it. [Models](https://geminicli.com/docs/cli/model/).

Plan Mode is on by default (`/plan` or `--approval-mode plan`), and `-w`/`--worktree` starts a session in a new git worktree. Gemini has no native `/goal`, `/loop`, scheduler, canvas, cloud sleeper or Grok Bot webhook service. Use the router's session-only goal/loop and local artifact fallbacks. Extension installation alone does not supply those services.
