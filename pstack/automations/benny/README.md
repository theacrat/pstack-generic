# benny

benny gives you two automations for slack issue reports. one triages each report. the other reproduces confirmed bugs and may prepare a small draft fix.

the files in this directory are dormant setup and automation sources. they do not appear as slash skills.

## set it up

1. point the active harness at [`FOR_AGENTS.md`](./FOR_AGENTS.md) and name the target repository.
2. let setup merge this whole directory into the target at `.agents/automations/benny/`. it must preserve destination-only files and review conflicts instead of overwriting local edits.
3. let setup enable shared pstack dependencies through the active harness's project configuration. Cursor uses `.cursor/settings.json`; other harnesses must use their own configuration. See the setup file for the capability checks.

4. keep user-owned configuration outside the copied pack, for example in `.agents/benny/`. adapt [`configuration.example.yaml`](./templates/configuration.example.yaml) and [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md).
5. commit the active harness project configuration, `.agents/automations/benny/`, and any secret-free configuration before enabling either automation.
6. review each new automation draft or update existing automations through the runner's supported tool or editor. then send a harmless test report and verify every source-channel post stays in the original thread.

Before setup, read pstack's [harness compatibility guide](../../docs/harnesses.md) and its active-harness reference. The default pack and config homes are `.agents/automations/benny/` and `.agents/benny/`. Existing native homes may be retained when every prompt and config reference uses the same committed paths. These directories store instructions and configuration; they do not register a scheduler.

Codex, Claude, Gemini, and Copilot setups need a verified automation tool or a configured CI runner. A time-based scheduler is not a Slack event trigger. If the runner cannot receive the report's original Slack coordinates, leave the automations disabled until an event adapter is configured and tested.
