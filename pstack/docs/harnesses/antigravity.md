# Antigravity

Installation: [instructions](../install.md#antigravity). Antigravity natively discovers Agent Skills and plugins; see [skills](https://antigravity.google/docs/skills), [plugins](https://antigravity.google/docs/plugins?tab=cli), and [workflow migration](https://antigravity.google/docs/migration/workflows-to-skills).

| Reference | Antigravity location |
| --- | --- |
| `<project-skills>` | `.agents/skills` |
| `<user-skills>` | `~/.gemini/config/skills` (CLI versions may use `~/.gemini/antigravity-cli/skills`) |
| `<model-config>` | `~/.gemini/antigravity-cli/pstack-models.md` |
| Project rules | `.agents/rules`, with legacy `.agent/rules` support |
| User instructions | `~/.gemini/GEMINI.md` |
| Agent definitions | `.agents/agents/<name>.md` or `<name>/agent.md`; global `~/.gemini/config/agents/` |
| Configuration and plugins | `~/.gemini/antigravity-cli/settings.json`, project `<repo>/.gemini/config.json`; plugins in workspace `.agents/plugins/` or global `~/.gemini/config/plugins/` |

Antigravity now defaults to `.agents/skills` and `.agents/rules`, while retaining the legacy `.agent` aliases. Directory entries in `skills.json`, `agents.json` or `plugins.json` load only their direct children. Plugin skills are namespaced, so `poteto-mode` appears as `/pstack:poteto-mode`. Write model role lines as plain Markdown in `<model-config>` and read it explicitly; this is a pstack convention, not a native auto-loaded rule. Pstack supplies the required root `plugin.json`; installing it does not create a scheduler, cloud worker or other service. [Rules](https://antigravity.google/docs/rules)

## Agents and tools

`Task` maps to the exposed `invoke_subagent` capability. Its `Workspace` option takes `inherit`, `branch` (a git worktree) or `share`; use `branch` for isolated workers. Built-ins include `research` and `self`; `browser` runs only through `/browser`. There is no portable `generalPurpose` identifier. Use a registered custom agent or suitable built-in, otherwise apply the router's serial fallback and retain any unmet independent-review requirement. Custom agents are Markdown files with YAML frontmatter; `tools`, `model` (`inherit`, `flash`, or `pro`), `subagent`, `commandExecutionPolicy`, `mcpServers` and `skills` are supported. `send_message`, `manage_subagents` and `@<subagent> <message>` talk to running subagents. Use exact tool names from the live catalogue: `grep_search`, `find_by_name` and `list_dir` are no longer in the default set. Use `/mcp` and the active tool list for MCPs. Async work uses `invoke_subagent`, `/agents`, `/tasks`, or `/btw`; do not pass Cursor-only `run_in_background`, `environment`, `cloud_base_branch`, or `readonly` fields. Preserve read-only work through allowed tools, permissions, and sandbox policy. [Subagents](https://antigravity.google/docs/subagents), [CLI tools and modes](https://antigravity.google/docs/cli/modes)

## Continuation and models

Use `/resume`, `agy -c`/`agy --continue`, or `agy --conversation <id>` to select workspace-scoped history. Transcripts live at `<app-data>/brain/<conversation-id>/.system_generated/logs/transcript.jsonl`, where `<app-data>` is `~/.gemini/antigravity-cli` for the CLI, `~/.gemini/antigravity-ide` for the IDE and `~/.gemini/antigravity` for the 2.0 app; hooks expose the path as `transcriptPath`. Verify the current session metadata before reading one.

`agy models` lists available model IDs, which can include Claude and GPT-OSS models for cross-family review. Use `/model` or `--model` with one of them; `-p` with an unknown ID fails rather than substituting. `/model <name> <prompt>` runs one prompt on another model. Use `/effort` or `--effort` with levels shown by the runtime. Enter Plan Mode with Shift+Tab or `/plan`; `/planning` was removed. Disclose when the live catalogue cannot provide a separate model family for independent review. [Resume](https://antigravity.google/docs/cli/commands/resume), [headless and models](https://antigravity.google/docs/cli/headless).

`/goal` runs autonomously until the objective is met or cancelled; it is a command the user types, with no agent-callable goal tool. The agent's `schedule` tool takes `DurationSeconds`, `CronExpression`, `MaxIterations` and `Prompt` for in-session loops, and `/schedule` sets one-time or cron jobs. Durable schedules use a `schedule` sidecar in `~/.gemini/config/sidecars/<id>/sidecar.json`, which the built-in `/automation` skill writes; sidecars must be enabled in `~/.gemini/config/config.json`. [Slash commands](https://antigravity.google/docs/slash-commands), [hooks and tools](https://antigravity.google/docs/hooks), [sidecars](https://antigravity.google/docs/sidecars).
