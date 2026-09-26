# Grok Bot

Installation: [instructions](../install.md#grok-bot). Select this profile only in Grok Bot, not the [Grok Build CLI](grok.md) or another host using a Grok model.

| Reference | Grok Bot location |
| --- | --- |
| `<project-skills>` | `<project>/.agents/skills` (pstack filesystem convention) |
| `<user-skills>` | `/workspace/pstack/skills` (pstack filesystem convention) |
| `<model-config>` | None; Grok Bot has no model controls |
| Persistent instructions | Bot description; applicable team rules |
| Installed skills and tools | Settings → Plugins; private skills under Yours |

Resolve `<project>` from the active workspace. These filesystem conventions do not register native skills automatically. Native private skills are host-managed; use the installation steps to register a reference to a bundled skill. Installed plugins are account-wide and available to every Bot; only their individual tools can be switched on or off, and they may need authentication. Private skills are enabled per Bot. [Settings](https://cursor.com/docs/grok-bot/settings), [work with Grok Bot](https://cursor.com/docs/grok-bot/work).

## Agents and tools

Use available delegation tools or named Bots for pstack roles, supplying the bundled role prompt. Bots can also hand coding tasks to Cursor Cloud Agents when the team allows it; that is the real cloud-worker path. Bots share a computer and filesystem; separate conversations or screens do not isolate writes. Use separate worktrees for concurrent repository changes. Read-only intent still applies to shared tools. Discover browser, terminal, question and connector capabilities from the live catalogue; do not assume Cursor CLI tool names or local configuration paths. [Teams](https://cursor.com/docs/grok-bot/teams).

Keep durable files under `/workspace`. Conversations are stored outside the computer; use current conversation context rather than scanning `.cursor/projects`. Bot descriptions hold persistent role guidance. Team rules scoped to Grok Bot always apply.

## Continuation and models

Cursor picks the model for each task, and there is no model or reasoning picker. Skip `<model-config>` and `/setup-pstack`, and disclose that diverse-model review cannot be arranged. A Bot name is not a model ID, and separate Bots do not establish different model families. [FAQs](https://cursor.com/help/grok-bot/faqs).

Use native routines for supported schedules and events. Schedules must be at least five minutes apart, and a Bot can own up to 50 routines. Some Bots keep routines on the server, so ask the Bot in chat when the panel is locked. Approvals requested by unattended runs expire after about ten minutes. Verify the configured trigger, run history and a test run before reporting an automation active. Use only the actual returned webhook contract for `make-bot-ui`; installing pstack does not create a routine or endpoint. Goal, loop, plan and canvas references use the common fallbacks unless the runtime exposes native equivalents. [Routines](https://cursor.com/help/grok-bot/routines).
