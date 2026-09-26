# Cursor

Installation: [instructions](../install.md#cursor).

| Reference | Cursor location |
| --- | --- |
| `<project-skills>` | `.cursor/skills` |
| `<user-skills>` | `~/.cursor/skills` |
| `<model-config>` | `~/.cursor/rules/pstack-models.mdc` (pstack convention) |
| Project rules and agents | `.cursor/rules/**/*.mdc`, `.cursor/agents/*.md` |
| User agents | `~/.cursor/agents/*.md` |
| CLI settings | `~/.cursor/cli-config.json` |

Cursor does not auto-load `<model-config>`: project rules live in `.cursor/rules/`, and User Rules live in Customize → Rules, not on the filesystem. Pstack reads the file explicitly. Write it with `description: pstack model routing`, `alwaysApply: true` YAML frontmatter and the role lines below it. [Rules](https://cursor.com/docs/rules).

Cursor also loads skills from `.agents/skills`, `.claude/skills`, `.codex/skills` and their `~/` equivalents, including nested directories. A Claude Code or Codex install of pstack on the same machine creates duplicate skill names, so keep one installation. Cursor ships built-in `/loop`, `/automate` and `/create-skill` skills with the same names as pstack's bundled ones; check which one the session loaded. Only `~/.cursor/skills` syncs to cloud agents, through Settings → Agents → Sync Skills for Cloud Agents. [Skills](https://cursor.com/docs/skills).

For transcript-based work, first use the workspace transcript path provided by the runtime. A local layout used by Cursor is `~/.cursor/projects/<workspace-slug>/agent-transcripts/<session>/<session>.jsonl`. Treat it as a candidate to verify, not a stable export API. Do not derive a slug and search unrelated projects if the current session metadata supplies a path. For cloud runs, prefer the Cursor Cloud MCP's run transcripts.

## Tools and execution

Cursor reference tool names apply only when present in the current tool schema. `Task`, `generalPurpose`, `subagent_type`, `environment`, `cloud_base_branch` and `run_in_background` are not assumed CLI flags. Choose the registered `poteto-agent` or `comment-sicko` role when present. Retained `Comment Sicko` references mean that comment-review role. Subagents nest one level deep. Background subagent output is written to `~/.cursor/subagents/`, and a subagent can be resumed by agent ID.

Set effort inside the model ID with Cursor's parameter syntax, such as `claude-opus-5-5[effort=high]`; other parameters include `[context=300k]` and `[fast=false]`. Record the parameterised ID in `<model-config>`. [Subagents](https://cursor.com/docs/subagents).

Cloud workers need the repository, base branch, skills and credentials available remotely. Local MCP access is not proof of cloud MCP access; cloud agents use team MCP servers. Check worker capabilities before sending an MCP investigation. Asking for each subagent "in its own environment" gives each its own worktree or cloud VM, and `/in-cloud` sends the next task to a cloud subagent. Read-only investigation means no mutations, even when agent mode is needed for read access.

Use the exposed question tool for `AskQuestion`, tool discovery for MCPs, and native browser or terminal controls for live checks. The required control and cleanup skills from `cursor-team-kit` are bundled in pstack; no second plugin is required.

## Continuation and UI

Cursor's `/goal` keeps an active or paused goal across idle and headless runs; it is gated and rolling out, so check it is exposed. Cloud agent subscriptions wake an agent on timers, CI checks, GitHub PR activity, Slack messages and Linear events, for up to 180 days; they are cloud-only. Use Plan Mode, canvas and cloud automations only when the active client exposes them. Verify their actual persistence and wake behaviour before promising unattended work. A local loop needs a live session. Grok Bot webhook instructions require Grok Bot. CLI and editor support can differ. [Cloud agent capabilities](https://cursor.com/docs/cloud-agent/capabilities), [automations](https://cursor.com/docs/cloud-agent/automations), [CLI slash commands](https://cursor.com/docs/cli/reference/slash-commands).

Use the model catalogue in this session. Pstack's reference slugs can change or be unavailable under an account. Apply the router's role and diversity fallback rather than guessing replacements.
