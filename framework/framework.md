# The Human AI-Risk Framework — working draft v0.2

A plain-language layer on top of the OWASP LLM Top 10 (2025). OWASP names the *risk* — the
mechanism inside the system. This framework names the *scenario* and the *conditions*: who trips
the wire, why, whether anyone was ready to catch it, and whether the damage can be undone.

Goal: give non-technical stakeholders (leadership, HR, finance, legal, everyday staff) memorable,
agreed-upon terms they can rely on — and dig deeper into only when they need to.

---

## The two sides

**Side 1 — Scenarios (acute).** A person, an action, a moment. "Someone did X." Named as short human
personas (≤6 words). These are the characters.

**Side 2 — Conditions (chronic).** No single actor, no single moment — a state the organization drifts
into. "The weather, not the event." Everyone has felt these; most have no agreed name.

**Sorting test:** *Can I point at one person and one moment?* Yes → Side 1. Slow drift, no single
culprit → Side 2.

**The interlock:** Side 2 conditions raise the odds and the cost of Side 1 events. The conditions are
the climate; the scenarios are the storms.

---

## The five axes

Every scenario is described on five axes. The first four say what happened; the fifth is the twist we
added last, and it changes everything.

**1. Actor — who.**
Insider · Outsider · Organization/leadership · Automated agent.

**2. Intent — why.**
Malicious (meant harm) · Negligent (knew better, cut a corner) · Ignorant (didn't know) ·
Legitimate (valid reason to act) · **None / unattributable** (no actor to assign — the thing simply
runs, unowned).

> The null case matters. Some of the most persistent AI risk has nobody behind it: an integration on
> a service account whose creator changed roles years ago. When it finally fails there is no one to
> place on this axis at all — which is precisely why it sits unfixed. A framework that assumes an
> actor will quietly skip the risks that have none.
> *(This axis value exists because Amanda Kollmorgan pointed out that it was missing.)*

**3. Preparedness — were the controls in place to contain it.**
None · Partial · Full. **Independent of intent.** Good intent with zero preparedness is still reckless;
a "risky" act with full preparedness can be responsible. Preparedness *is* the Side 2 conditions applied
to a Side 1 scenario.

**4. Recoverability — can the damage be undone.**
Reversible (operational/financial — restore from backup, absorb the cost) ·
Irreversible (confidentiality — once data is out of the box, it's out) · Mixed.

**5. Impact — what it costs.**
Denial of wallet · Data loss / exposure · Resilience & knowledge erosion · Integrity/poisoning ·
Availability / outage.

### The preparedness rule (from a real incident)
Preparedness must be judged **per impact class, not as a blanket "we're covered."** Recovery and rapid
redeployment can fully cover the *reversible* class (an agent wipes an environment — restore it) while
covering **none** of the *irreversible* class (that same agent leaks proprietary data to a public model —
nothing redeploys confidentiality back). "We can recover" is only true for the impacts you can actually
reverse.

---

## Side 1 — Scenario catalog (personas)

Intent key: M=malicious, N=negligent, I=ignorant, L=legitimate, none=unattributable. Prep = typical
preparedness when the scenario bites. Recov = recoverability of the usual impact.

| Persona | In one line | Actor | Intent | OWASP 2025 | Recov |
|---|---|---|---|---|---|
| The Disgruntled Employee | An angry insider loops costly calls or strips rate limits before access is cut. | Insider | M | LLM10 Unbounded Consumption | Reversible |
| The Plant | A hire who was never loyal — placed to exfiltrate or sabotage from day one. | Insider (infiltrator) | M | Cross-cutting (LLM02 / LLM04) | Irreversible |
| The Ghost Login | Access and agents still running under a name that no longer answers for them — whether the person left or simply moved on. | Ex-insider, or none | M / none | LLM10 / LLM02 / LLM06 | Mixed |
| The Oversharer | A well-meaning employee pastes secrets or PII into a public AI tool. | Insider | N | LLM02 Sensitive Info Disclosure | Irreversible |
| The Copy-Paste Contractor | Someone pastes untrusted outside content straight into a prompt. | Insider | I | LLM01 Prompt Injection | Mixed |
| The Poisoned PDF | Hidden instructions ride in on a shared document (indirect injection). | Outsider | M | LLM01 Prompt Injection | Mixed |
| The Over-Permissioned Assistant | An agent is granted more tools/scopes than its task needs. | Builder | N | LLM06 Excessive Agency | Mixed |
| The Runaway Agent | A well-intended agent loops unbounded and burns compute/budget. | Automated agent | N | LLM10 Unbounded Consumption | Reversible |
| The Overengineer | An unskilled user builds needlessly complex agent setups, burning many times the tokens for the same result. | Insider / builder | I | LLM10 Unbounded Consumption | Reversible |
| The Secondhand Executive | A senior decision-maker experiences the whole organization through agent summaries nobody audits. | Insider (senior) | L→N | LLM09 Misinformation / LLM06 | Mixed |
| The Overnight Cowboy | Unattended AI testing runs in production with no containment. | Automated agent | L | LLM06 / LLM10 | Mixed |

Notes:
- **The Overnight Cowboy** is the teaching case for the preparedness axis: same act, *full* preparedness →
  responsible; *no* preparedness → reckless. The persona name captures the unprepared version; the
  prepared version isn't a villain, it's a control state ("earned recklessness").
- **Denial of wallet spans three intents:** malicious (The Disgruntled Employee), negligent-config
  (The Runaway Agent), and ignorant self-inflicted waste (The Overengineer). Same OWASP risk, three
  different people and three different fixes.
- Personas are deliberately actor+action, not mechanism. That's what makes them stick for non-experts.

---

## Side 2 — Condition catalog (the add-ons)

Each condition notes whether we **ADOPT** an existing industry term or **COIN** a new one. Coining only
where the industry genuinely lacks a name is what keeps the catalog authoritative rather than just clever.

### Forced Adoption — *(coin)*
Leadership mandates AI use before the org is ready — no training, guardrails, or acceptable-use policy.
*You've felt this when:* a tool is pushed top-down with a deadline but no enablement.
*Why it's dangerous:* breeds corner-cutting and shadow workarounds. Feeds **The Oversharer** and **The
Copy-Paste Contractor**. *Control:* phased rollout, enablement, clear acceptable-use policy. *Maps to:*
NIST AI RMF — Govern.

### Premature Reviewer Cuts / Role Displacement — *(coin)*
Removing human reviewers, SMEs, or control steps too early because the AI "usually works."
*You've felt this when:* review headcount or sign-off steps are cut right after a successful pilot.
*Why it's dangerous:* erodes operational resilience, institutional knowledge, and the ability to recover
when automation fails. *Control:* define minimum human-control requirements, escalation paths, and
accountable decision owners *before* reducing oversight. *(Contributed by Purva Dublay.)*

### "Usually Works" Complacency — *(coin; kin to automation bias)*
Trust built from a good track record quietly turns into no verification at all.
*You've felt this when:* nobody checks the outputs anymore because they're "usually fine."
*Why it's dangerous:* a confident-but-wrong result sails into production unquestioned. *Control:* keep a
sampling/verification step proportional to stakes.

### Automation Bias / Over-Reliance — *(adopt)*
Humans defer to the AI even when it's wrong; the model is right about being wrong.
*You've felt this when:* a person overrides their own correct judgment to match the AI.
*Control:* keep a human accountable for high-stakes decisions; add friction where it counts.

### Shadow AI — *(adopt)*
Unsanctioned AI tools used for real work, outside any policy or visibility.
*You've felt this when:* staff quietly use personal AI accounts for company tasks.
*Control:* sanctioned tools, DLP, clear policy, an easy approved path.

### The Orphaned Model / Governance Failure — *(coin: "orphaned model")*
AI deployed with no inventory, owner, risk acceptance, auditability, or incident response.
*You've felt this when:* "whose model is this?" and nobody can answer.
*Why it's dangerous:* a technically secure model still creates org risk when no one owns its decisions,
data access, failures, or business impact. *Control:* AI inventory, a named accountable owner, documented
risk acceptance & appetite, IR plan, and DSPM/SPM coverage. *Maps to:* NIST AI RMF — Govern.
*(Contributed by Purva Dublay.)*

### Ownership Drift — *(coin; contributed by Amanda Kollmorgan)*
Ownership of a working AI integration silently evaporates through **role change rather than
departure**. Someone spins up an integration on a service account, it works, they move to a new
team — and two years later it is still running on valid credentials with nobody's name on it.
*You've felt this when:* an agent or integration breaks and the first question, unanswerable, is
"whose is this?" *Why it's dangerous:* it produces risk with **no attributable intent** — nothing to
investigate, nobody accountable, so it sits indefinitely. Especially common in vendor-managed and
third-party estates, where the drift happens outside your own org chart entirely.
*Distinct from The Ghost Login:* that is access surviving a **departure**; this is ownership dissolving
while the person is **still at the company**. Different trigger, different fix.
*Control:* the hard part is that **there is usually no trigger to hook into.** Offboarding has an
owner and a checklist; a lateral move has neither — nobody files a ticket when you change teams, so
the credential is never flagged. Departure is a process that failed; drift never had a process at all.
So: create a role-change trigger (don't just extend the exit checklist), tag every service account and
agent with a current human owner, run periodic ownership recertification, and extend all of it
contractually to vendor-managed environments.

### AI Governance Debt — *(coin; from "technical debt")*
Deferred governance that compounds — each ungoverned deployment raises the cost of ever getting control.
*You've felt this when:* the backlog of "we'll formalize this later" AI uses keeps growing.
*Control:* pay it down deliberately; gate new deployments on minimum governance.

### Needless Complexity — *(coin; credit: a Principal Engineer who named the pattern)*
Elaborate agent pipelines and setups that cost far more to accomplish the same job.
*You've felt this when:* a colleague's setup is many times more complex and burns many times the tokens
for the same output. *Why it's dangerous:* silent, self-inflicted denial of wallet at scale; also
harder to secure and maintain. Feeds **The Overengineer**. *Control:* cost-per-task baselines,
simplicity reviews, "does this need an agent?" gating.

### Model Overkill — *(coin)*
Defaulting to the most powerful (and most expensive) model when a lighter tier would do the job —
e.g., routing everything to a top-tier model "just in case."
*You've felt this when:* every task, trivial or not, hits the biggest model. *Why it's dangerous:*
straight-line cost inflation with no quality gain — an easy CFO conversation. *Control:* model
right-sizing / tiering policy, per-model cost dashboards, default to the cheapest model that passes.

### Agent Sprawl — *(coin)*
Sanctioned AI tools quietly spawning autonomous processes that nobody has enumerated. The tools are
approved and the accounts may even have owners — what is missing is any answer to *how many are
running, and what can they touch.*
*You've felt this when:* someone asks how many agents are operating against a system and the honest
answer is a shrug. *Why it's dangerous:* excessive agency at a scale nobody sized, cost accruing
across processes nobody totals, and no way to assess blast radius during an incident because the
inventory does not exist. Feeds **The Ghost Login** (unowned processes hide in the crowd) and
**The Secondhand Executive** (layers accumulate faster than anyone tracks them).
*Distinct from:* **Shadow AI** — there the tools are unsanctioned; here they are approved. And from
**Ownership Drift** — there the failure is ownership; here it is enumeration. An agent can be fully
sanctioned, correctly owned, and still be invisible.
*Control:* an agent registry with registration required before deployment; scoped, least-privilege
permissions per agent rather than per platform; periodic discovery to catch what never got
registered; per-agent budgets so cost surfaces the unregistered ones.
*Relationship to The Overengineer:* the same instinct at different altitudes — that persona is one
person building too much; this is an organization losing count of what got built.

### Agent Theater — *(coin; driver, not a control target)*
The human motive under Needless Complexity: ego-driven over-engineering — performing sophistication
("basically playing god") when a simple setup would do. Not something you patch; it's the *why* behind
the waste, and worth naming because the fix is cultural (norms, incentives), not technical.

---

## How to score a scenario

`(Actor · Intent · Preparedness · Recoverability · Impact)  ×  which Side 2 conditions are present`

The same scenario can be responsible or reckless depending on preparedness — and preparedness is only
real for the impact classes it actually covers. Read the climate (Side 2) to predict which storms
(Side 1) an organization is exposed to.

---

## Open questions / next
- Does "Actor: Organization/leadership" deserve its own persona set, or stay a Side 2 condition?
- Is "Legitimate" a fourth intent, or a separate "authorization" axis alongside preparedness?
- Priority personas to develop into their own posts: Disgruntled vs. Plant vs. Ghost Login (insider trilogy).
- Convert this matrix to a sortable spreadsheet once the vocabulary stabilizes.

*Contributors credited inline. Private/confidential input incorporated without attribution by request.*
