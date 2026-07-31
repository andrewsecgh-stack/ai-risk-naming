# The Plant

**One-liner:** A hire who was never loyal — placed inside the company to take what they came for,
and handed AI tools that make the taking faster and quieter than any USB stick.

**The scene:** They pass the interview. They pass the background check, or the check was thin enough
not to matter. They show up, do adequate work, and are pleasant in meetings. Nothing about them
triggers suspicion, because there is nothing to trigger — they have not changed, become bitter, or
started acting strangely. They arrived this way. Within weeks they have normal access to the same
AI assistants and agents everyone else uses, and those tools will happily summarize, search,
aggregate, and export across systems on request. What used to take an infiltrator months of careful
manual collection now takes a well-phrased prompt and an afternoon.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Insider (infiltrator) | legitimate credentials, illegitimate person |
| Intent | Malicious | premeditated, from before day one |
| Preparedness | Typically none | most programs watch for *change* in behavior; there is no change |
| Recoverability | Irreversible | exfiltrated data cannot be un-exfiltrated |
| Impact | Data loss / exposure | secondarily integrity, if they poison as well as take |

**Maps to:** Cross-cutting — LLM02:2025 Sensitive Information Disclosure (what leaves), LLM06:2025
Excessive Agency (the tooling that accelerates it), LLM04:2025 Data and Model Poisoning if they
tamper as well as take. NIST AI RMF: Govern (access, personnel), Manage (monitoring).

**Siblings:** The insider trilogy, separated by origin rather than mechanism —
**The Disgruntled Employee** (was loyal, turned; motive is visible in hindsight) and
**The Ghost Login** (was loyal, has left, keys remain). The Plant is the hardest of the three
precisely because there is no turning point to detect: behavioral monitoring is built to spot a
delta, and there isn't one.

**Conditions that feed it:** *The Orphaned Model* — unowned AI systems mean nobody is reviewing who
queries what. *Forced Adoption* — rapid rollout grants broad access before access governance exists.
*AI Governance Debt* — no data classification or egress controls means the agent will retrieve
whatever it can reach.

**How you'd notice:**
- Broad, systematic querying that stays just inside normal volume but ranges far outside the person's
  actual job scope.
- AI-assisted aggregation across systems that were never meant to be joined — the value is in the
  combination, not any single document.
- Access requests that trend consistently wider over time, each individually reasonable.
- Employment context: short tenure, a role with unusual breadth of access, references that were never
  actually called.

**What stops it:**
1. Vetting proportional to access — the depth of the background check should match what the role can
   reach on day 30, not day 1.
2. Least privilege for humans *and* their agents: an assistant should not be able to retrieve what its
   operator could not retrieve manually.
3. Data classification plus egress controls, so the sensitive material an agent can reach is bounded
   regardless of who is asking.
4. Query and retrieval logging tied to identity, reviewed for scope rather than volume.
5. Onboarding-phase access staging — broad permissions earned over time rather than granted at start.

**The honest caveat:** This is the least AI-specific persona in the catalog — planted insiders long
predate LLMs, and a critic could fairly say this is a classic insider threat wearing new clothes.
That objection is worth conceding directly: what AI changes is not the existence of the threat but
its *speed and quietness*. An infiltrator with agent access can collect, summarize, and stage in
hours what once took months of conspicuous manual work, and does it using tooling that looks
identical to legitimate productivity. The threat is old; the acceleration is new. Also worth saying
plainly: this persona must not become a justification for suspicion of new hires or of any particular
group — the controls are structural (least privilege, egress limits), not intuitive.

**Credit:** Contributed by Johnny Xmas, whose reshare raised the planted-employee case from direct
professional experience — "a paycheck is no longer a guarantee of loyalty" (quote pending permission).
