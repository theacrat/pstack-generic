# Claude Code

Installation: [instructions](../install.md#claude-code).

| Reference | Claude Code location |
| --- | --- |
| `<project-skills>` | `.claude/skills` |
| `<user-skills>` | `~/.claude/skills` |
| `<model-config>` | `~/.claude/rules/pstack-models.md` |
| Project instructions | `CLAUDE.md`, `.claude/rules/*.md` |
| Agent definitions | `.claude/agents/*.md`, `~/.claude/agents/*.md`, plugin `agents/` |
| Settings | `.claude/settings.json`, `~/.claude/settings.json` |

Write model role lines as plain Markdown in `<model-config>`. No `alwaysApply` or `globs` frontmatter is needed. Leave unrelated `CLAUDE.md` and settings intact. [Memory and rules](https://code.claude.com/docs/en/memory), [settings](https://code.claude.com/docs/en/settings).

Prefer the runtime's `transcript_path` or session picker. Local transcripts live under `~/.claude/projects/<project>/<session>.jsonl`; identify the project from session metadata rather than assuming Cursor's slug format. [Local state](https://code.claude.com/docs/en/claude-directory).

## Agents and tools

Invoke bundled skills as `/pstack:<skill-name>`; `/how` means `/pstack:how`.

`Task` maps to Claude's exposed `Agent` tool, or the older `Task` tool when that is what the session supplies. `generalPurpose` maps to `general-purpose`. Registered plugin roles use `pstack:poteto-agent` and `pstack:comment-sicko`; `Comment Sicko` is the display name of the latter. Without registration, give a general worker the bundled role file to read.

Native agent names must be lowercase identifiers. Cursor fields such as `is_background` do not configure Claude scheduling. Use supported `background` frontmatter or runtime scheduling controls when needed. `mode`, `icon`, `color` and `reminder` are Cursor metadata, not Claude mode controls. Run `claude plugin validate`; `--strict` also rejects tolerated unknown metadata. Background execution and tool availability vary by release, so preserve required MCP access rather than blindly setting `run_in_background`. [Subagents](https://code.claude.com/docs/en/subagents).

Use `Read`, `Grep`/`Glob`, `Bash` and the exposed task/todo tools for file reads, search, terminal work and task tracking. Use `AskUserQuestion` when exposed. Discover MCPs through the active tool catalogue or `/mcp`. Bash or PowerShell supplies terminal execution; browser verification needs an available browser integration, MCP or project script. Do not pass Cursor cloud parameters to `Agent`. Separate worktrees provide local isolation.

## Continuation and models

Check `/goal` and `/loop` availability in the installed version. Claude has native goal and scheduled-task features, but they are not Cursor APIs. A scheduled task requires a live runtime to fire; fresh sessions, resumed sessions and self-paced loops have different restoration rules. Confirm state after resuming. [Goals](https://code.claude.com/docs/en/goal), [scheduling](https://code.claude.com/docs/en/scheduled-tasks).

Use native Plan Mode when available. Canvas, Cursor cloud sleepers and Grok Bot webhooks require another implementation. Use the common fallbacks. Select models from Claude's actual catalogue or configured provider. When only one model family is available, disclose that diverse-model review could not be reproduced.
