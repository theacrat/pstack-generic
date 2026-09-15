# Gemini CLI

Installation: [instructions](../install.md#gemini-cli).

| Reference | Gemini CLI location |
| --- | --- |
| `<project-skills>` | `.gemini/skills` |
| `<user-skills>` | `~/.gemini/skills` |
| `<model-config>` | `~/.gemini/pstack-models.md` |
| Instructions | Project `GEMINI.md`, `~/.gemini/GEMINI.md` |
| Agent definitions | `.gemini/agents/*.md`, `~/.gemini/agents/*.md`, extension `agents/` |
| Settings and MCP configuration | `.gemini/settings.json`, `~/.gemini/settings.json` |

`.agents/skills` and `~/.agents/skills` are supported aliases. Use one installation to avoid duplicate names. Write model role lines as plain Markdown in `<model-config>`; pstack reads it explicitly. Do not rewrite `GEMINI.md` or settings to persist these choices. [Skills](https://geminicli.com/docs/cli/skills/), [configuration](https://geminicli.com/docs/reference/configuration/).

Use `gemini --list-sessions` for the current project, then `gemini --resume <id>` or `/resume`. For raw history, use the session path reported by the installed version. The local cache may contain `~/.gemini/tmp/<project>/chats/session-*.json`; verify the association before reading it. This is JSON session data, not Cursor message-per-line JSONL. [Session management](https://geminicli.com/docs/cli/session-management/).

## Agents and tools

`Task` maps to the exposed subagent tool. Gemini registers custom agents as named tools; there is no portable `subagent_type: generalPurpose` call. Use a registered pstack role, otherwise an available general worker instructed to read its bundled role file. If neither exists, apply the router's serial fallback and retain any unmet independent-review requirement.

Agent identifiers use lowercase letters, digits, hyphens or underscores. `kind: local` is the default; `is_background` is not its scheduling control. Set only supported model and tool fields. Remote A2A agents need a configured endpoint and authentication. They do not implement Cursor's `environment: cloud` or `cloud_base_branch`. [Subagents](https://geminicli.com/docs/core/subagents/).

Use `read_file`, `search_file_content`/`glob` and `write_todos` when exposed for file reads, search and task tracking. Use the exposed question tool, otherwise chat. Inspect `/mcp` and the active tool catalogue; use `run_shell_command` for terminal work and an installed browser integration or project verification scripts for UI checks. Read-only work must keep the read tools it needs. Do not assume a Cursor readonly flag controls Gemini MCP access.

## Continuation and models

Use `/model` and actual agent configuration to resolve available models. Gemini model variants do not provide cross-family review by themselves. A separately configured remote agent can supply another family only when it really runs it.

Use native Plan Mode if enabled. Pstack does not register a durable `/goal`, `/loop`, canvas, cloud sleeper or Grok Bot webhook service. Check the live commands and any configured scheduler first; otherwise use the router's session-only goal/loop and local artifact fallbacks. Extension installation alone does not supply those services.
