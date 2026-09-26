# Dependency sources

These are copies, not links to installed skills. Original pstack sources came from this repository at `be432a9`; no installed pstack skill was used as a source. Cursor built-ins came from the supplied `~/.cursor/skills-cursor` directory on 2026-09-15. `verify-this` is a transitive dependency of the control skills.

| Skill | Source | Source SHA-256 |
| --- | --- | --- |
| `automate` | Cursor built-in `skills-cursor/automate/SKILL.md` | `7dfe00c001ea24ac2ed7f6172a0d528718039c673d9382f39c36221d7f1ef4bf` |
| `create-skill` | Cursor built-in `skills-cursor/create-skill/SKILL.md` | `f3df382ea9cf2119ee8f121143b2ec0cacbd8bbc6dc3a15fd981ea547cef42f8` |
| `goal` | Cursor built-in `skills-cursor/goal/SKILL.md` | `95d2b1b1fbf9803f78b4d21e1b9ae4ed569f1581b7f07797f96aa751762b55a9` |
| `loop` | Cursor built-in `skills-cursor/loop/SKILL.md` | `fa195d01ca95def6f8e6ca1902d35470d153b49472ba4e60ea5224485f192a05` |
| `deslop` | `cursor-team-kit/skills/deslop/SKILL.md` at `be432a9` | `2f7b7def74af7ed11f5b44b4d32f0f91fca8c5d1f92bf2171e8d12fd33a0f810` |
| `control-cli` | `cursor-team-kit/skills/control-cli/SKILL.md` at `be432a9` | `13ac93e595bbda2000849bdb815d5f2ca03f7c2ca63788c8335f9212b9b422a2` |
| `control-ui` | `cursor-team-kit/skills/control-ui/SKILL.md` at `be432a9` | `410cae25bdb1e5d2323b126abc5047b0213be7fdb0195710213fa8de8a751871` |
| `verify-this` | `cursor-team-kit/skills/verify-this/SKILL.md` at `be432a9` | `c1c7b27c1133085bd3409c601ea12b6e6f61b4b23debcd52bc248fc01907e7de` |

The imported Cursor team kit files retain their [MIT notice](licenses/cursor-team-kit.txt). The supplied built-in skill directories contained no separate licence file; this records their provenance without assigning a new upstream licence.

## Updating

1. Compare the current upstream source with the source snapshot recorded above, then update the corresponding bundled directory, including any scripts and references.
2. Preserve only the harness-specific patch: the mapping link, native tool/path alternatives, and capability checks. Do not copy installed pstack skills back over these sources.
3. Update the source revision/hash here. Keep names and relative links stable.
4. Run `python3 pstack/scripts/check-portability.py` from the repository root, then the native plugin validators described in `harnesses.md`.

The workflows retain Cursor tool names and model IDs as notation where replacing every occurrence would make upstream updates noisy. `harnesses.md` resolves that notation once; only the active profile is loaded. Filesystem placeholders are resolved before executing commands, never passed literally to a shell. Native-only features remain conditional and have an explicit fallback.
