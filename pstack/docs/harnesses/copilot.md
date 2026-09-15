# GitHub Copilot

Installation: [instructions](../install.md#github-copilot).

| Reference | Copilot location |
| --- | --- |
| `<project-skills>` | `.github/skills` |
| `<user-skills>` | `~/.copilot/skills` for CLI; check the IDE's supported personal skill location |
| `<model-config>` | Project `.github/instructions/pstack-models.instructions.md` |
| Project instructions | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` |
| Agent profiles | `.github/agents/*.md`; some IDEs use `*.agent.md` |
| CLI configuration | `~/.copilot/config.json`; MCPs in `~/.copilot/mcp-config.json` |

Write `<model-config>` with YAML frontmatter `applyTo: "**"` and plain model role lines. This profile uses project scope because personal rule support varies across clients. Pstack also reads the file explicitly. Do not replace `copilot-instructions.md`. [Customisation reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).

CLI transcripts are `~/.copilot/session-state/<session-id>/events.jsonl`. Select sessions using their workspace metadata. IDE and cloud sessions need their own history/export view; this CLI path does not apply to them. [Session data](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/chronicle).

## Agents and tools

`Task` maps to the exposed delegation tool, such as VS Code's subagent tool or Copilot CLI's agent task tool. Tool names and parameters are client-specific. `generalPurpose` means the client's general worker. Load the relevant pstack role prompt when its custom agent is unavailable. Native profiles need the client's valid frontmatter; Cursor `is_background` and skill `mode` metadata do not enable those features.

Use the client's read, search, terminal and task-list tools (`read_file`, `grep_search`/`file_search`, `run_in_terminal` in VS Code when exposed). Use actual tool allowlists and model options from the client. Read-only review still needs its read tools and MCP connections. Discover MCPs through the client configuration and live tool list, never Cursor's `mcps/` directory. Use its question UI, otherwise chat. Use available terminal and browser tools or project verification scripts. [Custom agents](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents).

## Continuation and models

GitHub cloud agent is a separate service with its own repository access and execution lifecycle. A local subagent is not that service, and Cursor `environment: cloud`, background flags and branch parameters cannot be copied into its API.

Choose from the client's model catalogue. Preserve different available model families for diverse review; if model selection or another family is unavailable, disclose the reduced coverage. Use native planning where available. A local goal note or session loop does not provision a durable job. Cursor canvas, cloud sleepers and Grok Bot webhooks need a separate configured implementation, following the common router's fallbacks.
