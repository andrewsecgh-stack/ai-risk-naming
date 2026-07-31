# Changelog

Notable changes to the framework. Entries that change an **axis**, **merge** two entries, or
**correct a control** are recorded here — those are the changes that affect anyone already using
the vocabulary.

Versioning is informal while the framework is a working draft.

## [Unreleased]

### Added
- Repository scaffolding: contribution bar, issue and PR templates, contributor credits, license.

## [0.3] — insider trilogy and the null intent case

### Changed — framework
- **Intent axis gained a null value** (`none / unattributable`). The axis previously assumed an actor;
  some of the most persistent AI risk has none — an integration running on a service account whose
  creator changed roles years ago. When it fails there is nobody to place on the axis at all, which is
  precisely why it goes unfixed. *(Amanda Kollmorgan)*

### Changed — entries
- **The Ghost Login widened** from "an offboarded person whose access was never cut" to "access and
  agents still running under a name that no longer answers for them — whether the person left or
  simply moved on." A proposed second persona was **merged** into it rather than added, because the
  control set is identical. *(Amanda Kollmorgan)*
- **Control corrected.** Ownership transfer cannot simply be "added to the offboarding checklist":
  departure has a trigger and an owner, a lateral move has neither. Departure is a process that
  failed; drift never had a process at all. The control is to *create* a role-change trigger, not
  extend an existing one. *(Amanda Kollmorgan)*

### Added — entries
- **The Plant** — an infiltrator who was never loyal; distinguished from The Disgruntled Employee by
  the absence of any behavioral change to detect. *(Johnny Xmas)*
- **The Ghost Login** — full entry.
- **Ownership Drift** condition — ownership evaporating through role change rather than departure,
  including vendor-managed estates. *(Amanda Kollmorgan)*
- Full entry template establishing the quality bar for all persona entries.

## [0.2] — the cost cluster

### Added
- **The Overengineer** persona — self-inflicted token waste through needless complexity, completing
  denial of wallet across all three intents: malicious (The Disgruntled Employee), negligent (The
  Runaway Agent), ignorant (The Overengineer).
- **Needless Complexity** and **Model Overkill** conditions; **Agent Theater** recorded as the
  cultural driver beneath them. *(a principal engineer, credit pending)*

## [0.1] — initial framework

### Added
- Two-sided structure: Side 1 scenarios (acute, actor-driven) and Side 2 conditions (chronic,
  organizational), with the sorting test and the interlock between them.
- Five axes: actor, intent, preparedness, recoverability, impact.
- **Preparedness axis** — independent of intent; the same action can be responsible or reckless
  depending on the controls around it. Includes the rule that preparedness must be judged per impact
  class, since recovery covers reversible damage and does nothing for irreversible disclosure.
  *(anonymous)*
- **Recoverability axis** — reversible operational damage versus irreversible loss of confidentiality.
- Nine seeded personas and seven conditions, with adopt-versus-coin discipline.
