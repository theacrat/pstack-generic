# OpenCode

Installation: [instructions](../install.md#opencode).

| Reference | OpenCode location |
| --- | --- |
| `<project-skills>` | `.opencode/skills` |
| `<user-skills>` | `~/.config/opencode/skills` |
| `<model-config>` | `~/.config/opencode/pstack-models.md` (pstack convention) |
| Project instructions | `AGENTS.md`; `CLAUDE.md` is a compatibility fallback |
| Agent definitions | `.opencode/agents/*.md`, `~/.config/opencode/agents/*.md` |
| Configuration | `opencode.json[c]`, `~/.config/opencode/opencode.json[c]` |

OpenCode also discovers skills from `.agents/skills`, `.claude/skills`, `~/.agents/skills` and `~/.claude/skills`. Prefer one native location to avoid duplicate names. Each skill needs a directory containing `SKILL.md` with `name` and `description` frontmatter; OpenCode advertises it and loads its body through the native `skill` tool. Keep pstack's whole resolved directory together so `docs/`, `agents/`, scripts and relative references remain available. OpenCode's `plugin` setting loads JavaScript or TypeScript modules; pstack is installed through native skill/config paths and its client-specific manifests are not OpenCode plugin manifests. [Skills](https://opencode.ai/docs/skills), [rules](https://opencode.ai/docs/rules/).

## Agents and tools

`Task` maps to OpenCode's `task` tool. `generalPurpose` maps to the built-in `general` subagent; custom pstack roles belong in `.opencode/agents/<name>.md` with `mode: subagent`, a description and a prompt body. If a named pstack role is unavailable, give `general` the corresponding `agents/*.md` file to read. Built-in `build` and `plan` are primary agents; `explore` and `general` are subagents. Use the tools exposed by the selected agent: `read`, `grep`, `glob`/`list`, `bash`, `question`, `todowrite`, `webfetch` and `websearch`. Permissions in `opencode.json[c]` or agent frontmatter can hide or deny them. [Agents](https://opencode.ai/docs/agents), [tools](https://opencode.ai/docs/tools/).

## Models and continuation

Run `opencode models` or `/models`; select the reported `provider/model` ID, with `--model` for one run. Variants such as `#low` or `#high` are model-specific. The installed CLI exposes `opencode run --variant <name>`; use that native flag for CLI runs, while `#variant` is the documented model-reference form where supported. Configure `model`, `small_model`, agent `model` and provider-specific `reasoningEffort` in native config or agent frontmatter. Do not invent IDs or treat a variant as a separate model family. [Models](https://opencode.ai/docs/models/).

Use `opencode session list --format json` to enumerate sessions. The installed CLI has no workspace filter flag, so select the current project by each entry's recorded project/directory metadata before reading or exporting it. Then use `opencode export <sessionID> --sanitize` when transcript data must be handed off. `opencode --continue` resumes the last session; `--session <id>` resumes a selected one and `--fork` creates a branch. The installed 1.18.30 CLI has no native durable goal, loop or scheduler command: `/continue` and session export are continuation aids, not a wake mechanism after the process exits. Treat bundled `/goal` and `/loop` workflows as session-scoped unless another scheduler is configured. [CLI](https://opencode.ai/docs/cli/).
