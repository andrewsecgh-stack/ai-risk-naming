# Contributing

Thank you for wanting to add to this. Please read the bar before proposing — it exists because the
fastest way to ruin a plain-language vocabulary is to let it grow into something nobody can hold in
their head.

## The governing principle

**Merging is a better outcome than adding.**

If your scenario can be absorbed into an existing entry, that is a success, not a rejection. The
project has already merged a contributed scenario into The Ghost Login rather than creating a new
persona, because the control set was identical — and that merge made both the entry and the framework
stronger. A catalog of twelve memorable names beats a catalog of forty forgettable ones.

## Gate tests

Every proposed **persona** must pass both:

1. **The retell test** — could a non-expert hear the name once and retell the scenario to a colleague?
   If it needs a diagram or a definition to survive one retelling, it is not a persona yet.
2. **The sorting test** — can you point at one person and one moment? If it is a slow organizational
   drift with no single culprit, it belongs on Side 2 as a **condition**, not Side 1 as a persona.

And one scope rule:

3. **The AI delta** — what does AI actually change here? Not "does this involve AI," but what is
   different *because* AI is in the picture: speed, autonomy, scale, irreversibility, a non-human
   actor. Many entries are old problems with a new surface, and that is fine — but where the delta
   is not self-evident, the entry must state it. Entries that cannot answer this belong in general
   security literature, not here.

## Naming rules

- **Six words maximum.** Shorter is better. "The Disgruntled Employee," not "The Retaliatory Insider
  Resource Exhaustion Scenario."
- **Actor plus action**, not mechanism. Personas name characters; OWASP already names mechanisms.
- **Exception — artifact personas.** Where the actor is an anonymous upstream stranger the victim
  will never meet, name the **artifact they actually encounter** instead. The test: *what does the
  person on the receiving end see?* Nobody meets the attacker who poisoned a repo; they meet the
  file. The Poisoned PDF and The Trojan Rulebook are named this way deliberately. This is a narrow
  exception, not licence to name mechanisms — if there is a human worth naming, name the human.
- **Adopt before you coin.** If the industry already has an accepted term — shadow AI, automation
  bias — use it and mark it *adopted*. Only coin where no agreed name exists, and mark it *coined*.
  This discipline is what makes the catalog citable rather than merely clever.
- **Sentence-level plainness.** If a CFO or an HR lead cannot follow the one-liner, rewrite it.

## Entry standards

Full persona entries follow [framework/entry-template.md](framework/entry-template.md) and must fill
every section, including:

- **The scene** — narrative, not findings. This is the part people retell.
- **The honest caveat** — every persona oversimplifies something. Name the oversimplification
  yourself so critics do not get to. Entries without a real caveat will be sent back.
- **Credit** — who shaped this entry.

An entry that cannot fill the template gets merged into one that can, or cut.

## How to propose

1. **Open an issue** using the persona or condition proposal template. Do not open a PR first — the
   discussion about whether something should merge or stand alone is the valuable part, and it is
   easier in an issue than in a diff.
2. If the issue concludes that a new entry is warranted, **open a PR** with the entry written to the
   template.
3. Contributions that change an axis, merge two entries, or correct a control are the most valuable
   kind. They will be credited as such.

## Credit

Contributors are named in [CONTRIBUTORS.md](CONTRIBUTORS.md) and inline in the entries they shaped.
If you would prefer not to be named, say so in the issue and your contribution will be recorded
without attribution.

## Private material

Some input arrives through private conversation. Do not add identifying details of a private source
to any tracked file. Anonymized scenarios are welcome; attributable ones require the person's
explicit agreement.
