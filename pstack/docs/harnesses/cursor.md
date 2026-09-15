# Cursor

Installation: [instructions](../install.md#cursor).

| Reference | Cursor location |
| --- | --- |
| `<project-skills>` | `.cursor/skills` |
| `<user-skills>` | `~/.cursor/skills` |
| `<model-config>` | `~/.cursor/rules/pstack-models.mdc` |
| Project rules and agents | `.cursor/rules/*.mdc`, `.cursor/agents/*.md` |
| User agents | `~/.cursor/agents/*.md` |
| CLI settings | `~/.cursor/cli-config.json` |

Write the model preference file with `description: pstack model routing`, `alwaysApply: true` YAML frontmatter and the role lines below it. Read it explicitly when it exists even if rule auto-loading differs by client. `.agents/skills` is also supported; avoid installing duplicate copies with the same skill names. [Skills](https://cursor.com/docs/skills), [rules](https://cursor.com/docs/rules).

For transcript-based work, first use the workspace transcript path provided by the runtime. A local layout used by Cursor is `~/.cursor/projects/<workspace-slug>/agent-transcripts/<session>/<session>.jsonl`. Treat it as a candidate to verify, not a stable export API. Do not derive a slug and search unrelated projects if the current session metadata supplies a path.

## Tools and execution

Cursor reference tool names apply only when present in the current tool schema. `Task`, `generalPurpose`, `subagent_type`, `environment`, `cloud_base_branch` and `run_in_background` are not assumed CLI flags. Choose the registered `poteto-agent` or `comment-sicko` role when present. Retained `Comment Sicko` references mean that comment-review role.

Cloud workers need the repository, base branch, skills and credentials available remotely. Local MCP access is not proof of cloud MCP access; cloud agents use their own configured servers. Check worker capabilities before sending an MCP investigation. Read-only investigation means no mutations, even when agent mode is needed for read access. [Subagents](https://cursor.com/docs/subagents).

Use the exposed question tool for `AskQuestion`, tool discovery for MCPs, and native browser or terminal controls for live checks. The required control and cleanup skills from `cursor-team-kit` are bundled in pstack; no second plugin is required.

## Continuation and UI

Use `/goal`, `/loop`, Plan Mode, canvas and cloud automations only when the active Cursor client exposes them. Verify their actual persistence and wake behaviour before promising unattended work. A local loop needs a live session; a durable cloud routine needs an existing scheduler and credentials. Grok Bot webhook instructions require Grok Bot. CLI and editor support can differ. [Built-in skills](https://cursor.com/docs/skills), [automations](https://cursor.com/docs/cloud-agent/automations).

Use the model catalogue in this session. Pstack's reference slugs can change or be unavailable under an account. Apply the router's role and diversity fallback rather than guessing replacements.
