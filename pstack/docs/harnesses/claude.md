# Claude Code

Installation: [instructions](../install.md#claude-code).

| Reference | Claude Code location |
| --- | --- |
| `<project-skills>` | `.claude/skills` |
| `<user-skills>` | `~/.claude/skills` |
| `<model-config>` | `~/.claude/rules/pstack-models.md` |
| Project instructions | `CLAUDE.md`, `.claude/rules/*.md`; `AGENTS.md` when no `CLAUDE.md` exists |
| Agent definitions | `.claude/agents/*.md`, `~/.claude/agents/*.md`, plugin `agents/` |
| Settings | `.claude/settings.json`, `~/.claude/settings.json` |

If `CLAUDE_CONFIG_DIR` is set, every `~/.claude` path moves under it. Write model role lines as plain Markdown in `<model-config>`. No `alwaysApply` or `globs` frontmatter is needed. Leave unrelated `CLAUDE.md` and settings intact. [Memory and rules](https://code.claude.com/docs/en/memory), [settings](https://code.claude.com/docs/en/settings).

Prefer the runtime's `transcript_path` or session picker. Local transcripts live under `~/.claude/projects/<project>/<session>.jsonl`, and subagent transcripts under `<session>/subagents/`; identify the project from session metadata rather than assuming Cursor's slug format. [Local state](https://code.claude.com/docs/en/claude-directory).

## Agents and tools

Invoke bundled skills as `/pstack:<skill-name>`; `/how` means `/pstack:how`.

`Task` maps to Claude's exposed `Agent` tool, or the older `Task` tool when that is what the session supplies. `generalPurpose` maps to `general-purpose`. Registered plugin roles use `pstack:poteto-agent` and `pstack:comment-sicko`; `Comment Sicko` is the display name of the latter. Without registration, give a general worker the bundled role file to read.

Agent names cannot start with `-` or contain `:`. Cursor fields such as `is_background`, `mode`, `icon` and `reminder` are ignored; `claude plugin validate --strict` does not flag them. Supported plugin agent fields include `background`, `isolation: worktree`, `effort`, `model`, `color`, `skills` and `maxTurns`. [Subagents](https://code.claude.com/docs/en/subagents), [plugin components](https://code.claude.com/docs/en/plugins/components).

Interactive sessions default to fork mode, which runs subagents in the background and removes the `Agent` tool's `run_in_background` parameter. Background subagents keep MCP tools but lose built-ins such as `AskUserQuestion`, `ScheduleWakeup` and the Cron tools, so keep work that needs those in the parent.

Use `Read`, `Grep`/`Glob` and `Bash` for file reads, search and terminal work. Task and todo tools are off by default on current models; use them only when exposed. Use `AskUserQuestion` when exposed. Discover MCPs through the active tool catalogue or `/mcp`. Browser verification needs an available browser integration, MCP or project script. Do not pass Cursor cloud parameters to `Agent`. Separate worktrees provide local isolation.

## Continuation and models

Claude has no goal tool the model can call. `/goal <condition>` is a command the user types (or passes to `claude -p`); a small model checks the condition at each stop until it is met. The agent cannot arm or complete a goal, so ask the user to run `/goal`. [Goals](https://code.claude.com/docs/en/goal).

For loops, `CronCreate`, `CronList` and `CronDelete` schedule prompts in the session: up to 50 tasks, recurring tasks expire after seven days, and they fire only while Claude Code runs and is idle. `ScheduleWakeup` paces a self-paced loop, and `Monitor` wakes the session on command output. Resumed sessions restore Cron tasks but not a self-paced `/loop`. Durable schedules are Routines (`/schedule`, minimum one hour), desktop scheduled tasks or GitHub Actions. [Scheduling](https://code.claude.com/docs/en/scheduled-tasks).

Use native Plan Mode when available. Canvas, Cursor cloud sleepers and Grok Bot webhooks require another implementation. Use the common fallbacks. Select models from Claude's actual catalogue or configured provider, and set effort with the `effort` agent field or `--effort` (`low` to `max`). When only one model family is available, disclose that diverse-model review could not be reproduced.
