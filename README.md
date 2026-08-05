# The AI Risk Naming Project

**OWASP tells you what breaks. Not who breaks it, or why.**

The OWASP Top 10 for LLM Applications describes risk mechanisms precisely — and says almost nothing
about the human scenarios in which those risks actually get triggered. This project adds that layer:
plain-language names for the people, situations, and organizational conditions behind AI risk, aimed
at the audiences who cause and absorb these incidents but will never read a security framework —
leadership, HR, finance, legal, and everyday staff.

Status: **working draft.** The vocabulary is still changing. Names, axes, and entries are subject to
revision, and several have already changed in response to contributor pushback.

---

## The two sides

**Side 1 — Scenarios (acute).** A person, an action, a moment. *"Someone did X."* Named as short
human personas (six words maximum). These are the characters: The Disgruntled Employee, The Plant,
The Ghost Login.

**Side 2 — Conditions (chronic).** No single actor, no single moment — a state an organization drifts
into. *"The weather, not the event."* Forced Adoption, Ownership Drift, Model Overkill.

**The interlock:** conditions raise both the odds and the cost of scenarios. The conditions are the
climate; the personas are the storms.

**Sorting test:** *Can you point at one person and one moment?* Yes → Side 1. Slow drift with no
single culprit → Side 2.

---

## The five axes

Every scenario is scored on five axes:

1. **Actor** — insider, outsider, organization/leadership, automated agent
2. **Intent** — malicious, negligent, ignorant, legitimate, or *none/unattributable*
3. **Preparedness** — none, partial, full (independent of intent)
4. **Recoverability** — reversible, irreversible, mixed
5. **Impact** — denial of wallet, data exposure, resilience erosion, integrity, availability

Two of these exist because practitioners pushed back on earlier drafts. Preparedness came from a real
incident; the null-intent value came from a contributor pointing out that the axis assumed an actor
when some of the most persistent AI risk has none.

---

## Repository layout

```
framework/
  framework.md        the matrix — axes, both catalogs, scoring
  entry-template.md   the quality bar every persona entry must meet
personas/             full worked entries, one file per persona
.github/              issue and PR templates encoding the contribution bar
```

Published writing (posts, slides, and their generators) is kept outside the repository — this is the
framework, not the publicity around it.

---

## Using and citing this work

Licensed under **CC BY 4.0** — use it, adapt it, build on it, including commercially. Attribution is
required. See [LICENSE](LICENSE).

If you use a name from this catalog in a talk, policy, or training, attribution back to the project
is what keeps the vocabulary coherent rather than fragmenting into a dozen private dialects.

---

## Contributing

The catalog is deliberately small and defended. New entries face a real bar, and **merging into an
existing entry is a better outcome than adding a new one.** See [CONTRIBUTING.md](CONTRIBUTING.md)
before proposing anything.

Contributors are credited by name in [CONTRIBUTORS.md](CONTRIBUTORS.md) and inline in the entries
they shaped.

---

## Origin

This began as a single observation — that "denial of wallet" describes a mechanism while "the
disgruntled employee" describes a moment — published as a LinkedIn article. Everything since has been
built in public, from practitioner input.
