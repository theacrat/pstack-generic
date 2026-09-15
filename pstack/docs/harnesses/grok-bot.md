# Grok Bot

Installation: [instructions](../install.md#grok-bot). Select this profile only in Grok Bot, not the [Grok Build CLI](grok.md) or another host using a Grok model.

| Reference | Grok Bot location |
| --- | --- |
| `<project-skills>` | `<project>/.agents/skills` (pstack filesystem convention) |
| `<user-skills>` | `/workspace/pstack/skills` (pstack filesystem convention) |
| `<model-config>` | `/workspace/pstack-models.md` (explicitly read Markdown) |
| Persistent instructions | Bot description; applicable team rules |
| Installed skills and tools | Settings → Plugins → Yours |

Resolve `<project>` from the active workspace. These filesystem conventions do not register native skills automatically. Native private skills are host-managed; use the installation steps to register a reference to a bundled skill. Plugin tools may need enabling or authentication. [Settings](https://cursor.com/docs/grok-bot/settings).

## Agents and tools

Use available delegation tools or named Bots for pstack roles, supplying the bundled role prompt. Bots share a computer and filesystem; separate conversations or screens do not isolate writes. Use separate worktrees for concurrent repository changes. Read-only intent still applies to shared tools. Discover browser, terminal, question and connector capabilities from the live catalogue; do not assume Cursor CLI tool names or local configuration paths.

Keep durable files under `/workspace`. Conversations are stored outside the computer; use current conversation context or a host history/export facility rather than scanning `.cursor/projects`. Bot descriptions hold persistent role guidance. [Work with Grok Bot](https://cursor.com/docs/grok-bot/work).

## Continuation and models

Choose models and reasoning only through controls actually exposed for this Bot. A Bot name is not a model ID, and separate Bots do not establish different model families.

Use native routines for supported schedules and events. Verify the configured trigger, run history and a test run before reporting an automation active. Use only the actual returned webhook contract for `make-bot-ui`; installing pstack does not create a routine or endpoint. Goal, loop, plan and canvas references use the common fallbacks unless the runtime exposes native equivalents. [Routines](https://cursor.com/help/grok-bot/routines).
