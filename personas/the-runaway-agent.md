# The Runaway Agent

**One-liner:** A well-intended agent falls into a loop it was never bounded against and burns through
compute and budget until someone notices the bill.

**The scene:** The agent was built to help, and it does — until the run where something goes sideways.
A task decomposes into subtasks that decompose into subtasks; a retry-on-failure hits a failure that
never clears and retries forever; two agents hand work back and forth in a cycle nobody drew on the
whiteboard. No cap stops it, because none was set. It runs overnight, over a weekend, calling the
model thousands of times, and every call is billed. Nobody meant any harm and nothing was attacked —
the agent is doing exactly what it was told, just without end. The damage is a number on an invoice,
and the only question is how large before someone happened to look.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Automated agent | no human in the moment; the loop runs itself |
| Intent | Negligent (config) | the builder omitted the bounds, not out of malice but oversight |
| Preparedness | Typically none | budgets, iteration caps, and timeouts are the missing controls |
| Recoverability | Reversible | the harm is financial and operational — absorb the cost, kill the run |
| Impact | Denial of wallet | secondarily availability, if the loop starves shared resources |

**Maps to:** OWASP LLM10:2025 Unbounded Consumption — the textbook case of resource use without a
ceiling. NIST AI RMF: Manage (operational limits, monitoring).

**What AI changes:** Runaway processes are not new — a bad `while` loop has always been able to spin
forever. What AI changes is the *cost per iteration* and the *plausibility of the loop*. Each turn of
an agent loop is a metered model call, not a free CPU cycle, so the bill climbs fast; and because the
agent's behavior is generated rather than fixed, loops appear in places no static code review would
have predicted — a retry strategy, a self-critique step, a multi-agent negotiation that never
converges.

**Siblings:** The denial-of-wallet trio, one OWASP risk across three intents. **The Disgruntled
Employee** drives the *malicious* version — deliberately looping costly calls; the Runaway Agent is
the *negligent-config* version — bounds simply left off; **The Overengineer** is the *ignorant*
version — needless complexity that costs many times what the job requires. Same LLM10, three
different people, three different fixes. The Runaway Agent's fix is the most mechanical of the three:
set the limits.

**Conditions that feed it:** *Needless Complexity* — elaborate pipelines have more places to loop.
*Model Overkill* — every runaway iteration costs more when it defaults to the priciest model. *Agent
Sprawl* — unenumerated agents run unbudgeted and unwatched. *"Usually Works" Complacency* — it has
never looped before, so nobody added a cap.

**How you'd notice:**
- A spend or token-usage graph with a sharp overnight or weekend spike and no matching business
  reason.
- Logs showing the same step, tool call, or agent-to-agent handoff repeating far beyond any sensible
  count.
- Cost alerts that fire (if they exist) — or, absent alerts, a surprise line on the monthly invoice.
- Latency or throughput problems in a shared system while one agent monopolizes capacity.

**What stops it:**
1. Hard budget and token caps per agent and per run, enforced by the platform — the run dies at the
   ceiling rather than at someone's attention.
2. Iteration, recursion-depth, and wall-clock limits on every loop and every agent-to-agent
   interaction.
3. Real-time spend alerting with a low threshold, so a runaway is caught in minutes, not on the
   invoice.
4. A kill switch — a fast, well-known way to stop a running agent — and someone with the authority to
   pull it.
5. Load-test the failure paths, not just the happy path: find the loops in staging where they cost
   nothing.

**The honest caveat:** This is the most fixable persona in the catalog, which is precisely why it
keeps happening — the controls are cheap and well understood, so the presence of a Runaway Agent is
really a signal about *process*, not about any hard technical problem. The line with The Overengineer
can blur: an over-built system that also loops is both at once, and that is fine — the personas name
intents, not mutually exclusive incidents. The entry should not be read as blaming the builder for a
single missed cap; the deeper failure is a platform that let an unbounded agent run at all.

**Credit:** Andrew Griffith.
