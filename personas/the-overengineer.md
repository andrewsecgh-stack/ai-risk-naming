# The Overengineer

**One-liner:** An unskilled but enthusiastic builder assembles a needlessly elaborate agent setup and
burns many times the tokens to get a result a single call would have produced.

**The scene:** The task is simple — answer a common question, tidy a list, route a request. The
solution is not. There is a multi-agent pipeline, a vector database, a planner that dispatches to a
critic that dispatches to a researcher, and three model calls where one would do. It works, more or
less, and the builder is proud of it — it looks like *real* engineering. What it actually is, is
thirty times the cost for the same output, harder to secure, harder to maintain, and slower. Nobody
questions it, because it produces the right answer and complexity reads as competence. The waste is
invisible precisely because the thing succeeds.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Insider (builder) | often a keen non-specialist, sometimes an over-eager specialist |
| Intent | Ignorant | genuinely does not know the simple path exists; not cutting a corner, over-building one |
| Preparedness | Typically none | no cost baseline to reveal that the setup is wildly over-scaled |
| Recoverability | Reversible | the harm is ongoing cost and drag; simplify and it stops |
| Impact | Denial of wallet | secondarily a wider attack surface and maintenance burden |

**Maps to:** OWASP LLM10:2025 Unbounded Consumption — self-inflicted, structural waste rather than a
runaway loop. NIST AI RMF: Manage (cost and complexity), Govern (standards).

**What AI changes:** Over-engineering predates AI, but two things make it worse here. First, cost is
metered per call, so needless indirection is not just inelegant — it is a recurring bill that scales
with usage. Second, the ecosystem actively encourages it: frameworks, tutorials, and hype present
elaborate multi-agent architectures as the default good practice, so a newcomer's honest attempt to
"do it right" lands on the expensive pattern. The ignorance is manufactured by the surrounding
culture, which is why the fix is partly cultural.

**Siblings:** The denial-of-wallet trio. **The Runaway Agent** is the *negligent* sibling — bounds
left off — and its fix (caps) does nothing here, because the Overengineer's cost is steady-state, not
a spike. **The Disgruntled Employee** is the *malicious* sibling. **The Secondhand Executive** shares
the over-automation instinct but not the harm: that persona degrades judgment, this one wastes money,
and no control is shared between them. The Overengineer is separated by intent — ignorance, not malice
or negligence — and by the tell that the system *works*, which is what hides the cost.

**Conditions that feed it:** This persona is the individual expression of **Needless Complexity** and
is driven by **Agent Theater** — the ego pull of performing sophistication, "basically playing god,"
when a simple setup would do. *Model Overkill* compounds it: every superfluous step also defaults to
the priciest model. *AI Governance Debt* — no simplicity or cost review to catch it.

**How you'd notice:**
- A cost-per-task far above peers for the same outcome — the clearest signal, if anyone measures it.
- Architecture diagrams with many components where the job is small; agents calling agents to do
  something linear.
- "It works, don't touch it" attached to a system nobody can fully explain.
- New builders replicating an elaborate template because it is what the tutorial showed, not because
  the task demanded it.

**What stops it:**
1. Cost-per-task baselines, so the 30x setup is *visible* — you cannot fix waste you never measured.
2. A "does this need an agent?" gate before building — the cheapest, most powerful step is often no
   agent at all.
3. Simplicity reviews that treat unnecessary complexity as a defect, not a flex.
4. Mentorship and good reference patterns for non-specialist builders, so "doing it right" points at
   the simple solution instead of the baroque one.
5. Default to the smallest model and fewest steps that pass; add complexity only when a measured need
   forces it.

**The honest caveat:** "Unskilled" is a blunt word for what is usually enthusiasm pointed at bad
defaults — the builder is often doing their sincere best with the patterns the ecosystem sold them,
and the persona must land on the pattern, not on mocking a person for trying. The boundary with
legitimately complex problems is also real: some tasks genuinely need multi-agent architectures, and
calling every elaborate system over-engineering would be its own error. The test is not complexity in
the abstract but complexity *relative to the task* — measured against cost-per-outcome, not taste.

**Credit:** Andrew Griffith. The underlying pattern was named by a principal engineer (credit
pending), whose observation also grounds the **Needless Complexity** condition.
