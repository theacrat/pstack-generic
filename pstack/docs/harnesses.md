# Harness mapping

Read this router and only the active profile: [Cursor](harnesses/cursor.md), [Codex](harnesses/codex.md), [Claude Code](harnesses/claude.md), [Gemini CLI](harnesses/gemini.md), [GitHub Copilot](harnesses/copilot.md), [Antigravity](harnesses/antigravity.md), [Grok Build](harnesses/grok.md), [Grok Bot](harnesses/grok-bot.md), or [OpenCode](harnesses/opencode.md). Identify the host from its system instructions and available tools, not the selected model. Cache the result for this session. Re-read after a host or capability change. For an unlisted host, resolve equivalent capabilities from its live tools and documented paths; never assume Cursor defaults.

Installation is in [install pstack](install.md); do not load it during ordinary workflow execution.

## Translation contract

Pstack retains Cursor reference notation in some workflows. This mapping overrides its paths, tool spelling, model identifiers and host features. It does not remove investigation, independence, ownership, verification, approval boundaries or completion criteria. Runtime tool schemas and higher-priority instructions always win.

The active profile defines `<project-skills>`, `<user-skills>` and `<model-config>`. Expand these before a filesystem operation. Read `<model-config>` if it exists before choosing models. It is an isolated pstack preference file, not permission to overwrite global instructions or host settings. Resolve bundled references from the installed pstack root, preserving `skills/`, `docs/`, `agents/` and referenced resources together. Treat retained `pstack/skills/...` paths as shorthand for this resolved plugin root. A `git show origin/main:pstack/...` example works only in the pstack source repository; in a consuming repository, re-read the corresponding installed plugin file. Quote resolved shell paths. Slash names such as `/how` mean the bundled workflow; use the host's namespaced invocation or read its `SKILL.md` explicitly.

- `Task` means the available delegation API; `generalPurpose` means its general-purpose worker. `subagent_type` selects a registered role. If a named pstack role is absent, give a general worker the corresponding `agents/*.md` path and require it to read that file first. Do not silently discard the role prompt.
- `run_in_background` means concurrent work where supported. `environment: cloud` and `cloud_base_branch` require a real remote execution service. Local worktrees preserve isolation but do not become cloud workers. If delegation is unavailable, perform separable steps serially and report the loss of independent review. A workflow whose acceptance requires another reviewer remains incomplete until one runs.
- `readonly` describes allowed actions. Preserve read-only intent and needed read tools; the Cursor claim that readonly strips MCP is not universal. Never broaden permissions just to imitate a flag.
- `AskQuestion` means the host's supported question UI, otherwise one concise chat question. Discover tools and MCP servers from the live tool catalogue or supported discovery API. Never assume Cursor's `mcps/` directory exists elsewhere.
- Resolve explicit model choices against the available catalogue. Preserve role difficulty and different model families for diverse review. An unavailable slug is not an alias for an invented model. Use an available suitable model, state the substitution, and state when family diversity is unavailable. `auto` and `inherit-parent` omit the override. Different prompts or reasoning settings on one model are not different model families. When effort is a separate native option, record it separately from the model ID in `<model-config>` and use only supported levels. If the spawn API cannot enforce that effort, say so rather than adding a suffix to the model ID.

## Capability gaps

Use native goal, loop, plan, browser, terminal and automation features only when exposed. A Markdown checklist records a goal; it does not enforce continuation. A sleep or polling process runs only while its host stays alive; it does not schedule a durable future session. For unattended work, verify the scheduler, wake mechanism, credentials and persisted state before claiming it is armed.

When a requested feature is missing, keep the workflow's useful local work and name the limitation. A local HTML preview can replace a canvas artifact, and a plan file can record a plan. Neither grants UI controls or changes host mode. Cursor cloud sleepers, Grok Bot webhooks and automation APIs need their actual service or a separately configured equivalent. Never invent their tool names, endpoints or parity.

Prefer installed browser/terminal tools, then the project's Playwright, HTTP, PTY or other verification scripts. `control-ui`, `control-cli`, `deslop`, `create-skill`, `verify-this`, `goal`, `loop` and `automate` are bundled skills, not required native tools. Read their bundled files even if absent from the live catalogue. Preserve their intended checks with available tools and report any check that could not run.

Transcript discovery is workspace-scoped. Use session metadata or a native export/list API to select the current project's sessions before reading message bodies. Do not search every project's private transcripts. Missing history is an evidence gap, never evidence that no work happened.

Profiles were checked against official documentation on 2026-09-15. Recheck version-sensitive setup against the installed CLI's help before changing configuration.
