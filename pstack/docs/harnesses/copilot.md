# GitHub Copilot

Installation: [instructions](../install.md#github-copilot).

| Reference | Copilot location |
| --- | --- |
| `<project-skills>` | `.github/skills` |
| `<user-skills>` | `~/.copilot/skills` or `~/.agents/skills`; VS Code also reads `~/.claude/skills` |
| `<model-config>` | Project `.github/instructions/pstack-models.instructions.md` |
| Project instructions | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`; CLI personal `~/.copilot/instructions/**/*.instructions.md` |
| Agent profiles | `.github/agents/*.md`; VS Code user agents in `~/.copilot/agents` or `~/.claude/agents` |
| CLI settings | `~/.copilot/settings.json`; repository `.github/copilot/settings.json` |

Write `<model-config>` with YAML frontmatter `applyTo: "**"` and plain model role lines. It uses project scope so the CLI, VS Code and cloud agent all see it. Pstack also reads the file explicitly. Do not replace `copilot-instructions.md`. `~/.copilot/config.json` is managed application state; do not edit it. [Customisation reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet), [CLI configuration](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference).

CLI transcripts are `~/.copilot/session-state/<session-id>/events.jsonl`; select sessions by the `cwd` and `git_root` in each `workspace.yaml`. IDE and cloud sessions need their own history/export view; this CLI path does not apply to them. [Session data](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/session-data).

## Agents and tools

Subagents run in Copilot CLI and VS Code, not in the GitHub cloud agent or Visual Studio. `Task` maps to the exposed delegation tool: `runSubagent` in VS Code, or the CLI's agent task tool. Tool names and parameters are client-specific. `generalPurpose` maps to the CLI's `general-purpose` agent; `explore` suits read-only work, and `rubber-duck` runs on a different model. Plugin roles register as `pstack:poteto-agent` and `pstack:comment-sicko`. Load the relevant pstack role prompt when its custom agent is unavailable. CLI concurrency depends on plan (Free 2, Pro 4, Max 8, Business 16, Enterprise 32), which caps swarm and arena fan-out.

Native profiles need the client's valid frontmatter: `tools`, `mcp-servers`, `model`, `models`, `reasoningEffort`, and `include-custom-instructions: true` when a subagent needs `AGENTS.md` or repository instructions, which subagents do not receive by default. Cursor `is_background` and skill `mode` metadata do not enable those features. [Custom agents](https://docs.github.com/en/copilot/reference/custom-agents-configuration).

Use the client's read, search, terminal and task-list tools (`read_file`, `grep_search`/`file_search`, `run_in_terminal` in VS Code when exposed). Use actual tool allowlists and model options from the client. Read-only review still needs its read tools and MCP connections. Discover MCPs through the client configuration and live tool list, never Cursor's `mcps/` directory. Use its question UI, otherwise chat. Use available terminal and browser tools or project verification scripts.

## Continuation and models

GitHub cloud agent is a separate service with its own repository access and execution lifecycle. A local subagent is not that service, and Cursor `environment: cloud`, background flags and branch parameters cannot be copied into its API.

Choose from the client's model catalogue. Set a subagent's model and effort in its frontmatter, in the CLI's `subagents.agents.<name>` settings, or with `runSubagent`'s `model` in VS Code. Preserve different available model families for diverse review; disclose reduced coverage when another family is unavailable. Use native planning where available.

In the CLI, map `CreateGoal` to `/goal <objective>` (alias `/autopilot`), with `--max-ai-credits` for a budget. `/every <interval> <prompt>` and `/after <delay> <prompt>` schedule prompts in the session when experimental mode is on. VS Code has Automations in preview (`chat.automations.enabled`) for recurring saved prompts. Verify the schedule before calling it durable. Cursor canvas, cloud sleepers and Grok Bot webhooks need a separate configured implementation, following the common router's fallbacks. [CLI commands](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference), [VS Code automations](https://code.visualstudio.com/docs/agents/run/automations).
