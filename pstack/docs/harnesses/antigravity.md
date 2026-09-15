# Antigravity

Installation: [instructions](../install.md#antigravity). Antigravity natively discovers Agent Skills and plugins; see [skills](https://antigravity.google/docs/skills), [plugins](https://antigravity.google/docs/cli/plugins), and [workflow migration](https://antigravity.google/docs/migration/workflows-to-skills).

| Reference | Antigravity location |
| --- | --- |
| `<project-skills>` | `.agents/skills` |
| `<user-skills>` | `~/.gemini/config/skills` (CLI versions may use `~/.gemini/antigravity-cli/skills`) |
| `<model-config>` | `~/.gemini/antigravity-cli/pstack-models.md` |
| Project rules | `.agents/rules`, with legacy `.agent/rules` support |
| User instructions | `~/.gemini/GEMINI.md` |
| Agent definitions | `.agents/agents/<name>.md` or `<name>/agent.md`; global `~/.gemini/config/agents/` |
| CLI configuration and plugins | `~/.gemini/antigravity-cli/settings.json`; workspace `.agents/plugins/`, global `~/.gemini/config/plugins/`, staged CLI `~/.gemini/antigravity-cli/plugins/` |

Antigravity now defaults to `.agents/skills` and `.agents/rules`, while retaining the legacy `.agent` aliases. Write model role lines as plain Markdown in `<model-config>` and read it explicitly; this is a pstack convention, not a native auto-loaded rule. Pstack supplies the required root `plugin.json`; installing it does not create a scheduler, cloud worker or other service. [Rules](https://antigravity.google/docs/rules-workflows)

## Agents and tools

`Task` maps to the exposed `invoke_subagent` capability. Built-ins include `research`, `browser`, and `self`; there is no portable `generalPurpose` identifier. Use a registered custom agent or suitable built-in, otherwise apply the router's serial fallback and retain any unmet independent-review requirement. Custom agents are Markdown files with YAML frontmatter; `tools`, `model` (`inherit`, `flash`, or `pro`), `subagent`, and `commandExecutionPolicy` are supported. Use exact names from the live catalogue: common built-ins include `view_file`, `grep_search`, `code_search`, file operations, and `run_command`. Use `/mcp` and the active tool list for MCPs. Async work uses `invoke_subagent`, `/agents`, `/tasks`, or `/btw`; do not pass Cursor-only `run_in_background`, `environment`, `cloud_base_branch`, or `readonly` fields. Preserve read-only work through allowed tools, permissions, and sandbox policy. [Subagents](https://antigravity.google/docs/subagents), [CLI tools and modes](https://www.antigravity.google/docs/cli/modes/)

## Continuation and models

Use `/resume`, `agy -c`/`agy --continue`, or `agy --conversation <id>` to select workspace-scoped history. A runtime hook may expose a transcript at `~/.gemini/antigravity/brain/<conversation-id>/.system_generated/logs/transcript.jsonl`; verify the current session metadata and path before reading it. Use `/model` or `--model` with an actually available model, and `/effort` or `--effort` with levels shown by the runtime; availability is plan- and version-dependent. Use native planning (`agy --mode=plan` or `/planning` where exposed). Pstack does not assume native `/goal` or `/loop`; use the router's session-only or local-artifact fallback. Disclose when the live catalogue cannot provide a separate model family for independent review. [Resume](https://antigravity.google/docs/cli/commands/resume), [models](https://antigravity.google/docs/models), [CLI reference](https://antigravity.google/docs/cli/reference/)
