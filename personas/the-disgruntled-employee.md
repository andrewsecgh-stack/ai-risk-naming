# The Disgruntled Employee

**One-liner:** An angry insider with a valid login deliberately runs up your AI bill — no malware,
no breach, just a person with a motive and access nobody thought to limit.

**The scene:** Someone's angry — about a review, a passed-over promotion, or a personal problem
bleeding into their work. They know the AI systems because they use them every day. Before anyone
notices anything is wrong, and before access is cut, they act: quietly looping the most expensive
model calls they can, or stripping the rate limits they were trusted to manage. Nothing they touch
is technically broken. Every action uses access they were legitimately given. The first sign anyone
sees is the invoice.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Insider | current employee with legitimate access |
| Intent | Malicious | the defining feature — they meant it |
| Preparedness | Typically none–partial | cost caps and per-user anomaly detection are rare |
| Recoverability | Reversible | the cost is bounded and absorbable — painful, not permanent |
| Impact | Denial of wallet | can extend to availability if shared capacity is exhausted |

**Maps to:** OWASP LLM10:2025 Unbounded Consumption. NIST AI RMF: Govern (access accountability),
Measure (usage monitoring).

**Siblings:** Same OWASP category, different people — **The Runaway Agent** (negligent: a
well-intended agent loops unbounded; same bill, no villain) and **The Overengineer** (ignorant:
self-inflicted waste through needless complexity). One risk, three intents, three different fixes —
this trio is the framework's clearest proof that naming the mechanism alone isn't enough.
Insider cousins with different origins: **The Plant** (never loyal to begin with) and
**The Ghost Login** (was loyal, has left, still has keys).

**Conditions that feed it:** *The Orphaned Model* — no owner watching means no one notices until
the invoice. *AI Governance Debt* — no per-user budgets or caps were ever set. A separation-of-duties
gap is the accelerant: the angriest person in the room is sometimes the one trusted to manage the
rate limits.

**How you'd notice:**
- A single user's token/compute spend spikes far beyond their baseline, especially off-hours.
- Rate limits, budgets, or alerts get modified without a change ticket.
- Expensive model tiers get called for tasks that never needed them, in volume.
- HR context: the spike coincides with a bad review, a denied promotion, or a resignation notice.

**What stops it:**
1. Hard per-user and per-key cost caps — caps that stop spend, not alerts that report it later.
2. Spend anomaly detection keyed to individuals, not just team or org totals.
3. Separation of duties: no single person can both raise limits and consume under them.
4. Tight offboarding and access review triggered by role change or departure notice — not just exit day.
5. HR-security signal sharing for elevated-risk windows (with care for fairness and privacy).

**The honest caveat:** The persona names anger as the motive, but the control set works regardless
of why — the same caps and anomaly detection catch the plant, the compromised account, and the
runaway script. Don't build a program around detecting *emotion*; build it around limiting what any
single credential can spend. Also: treating every departing employee as a suspect poisons culture —
the controls should be invisible and universal, not targeted.

**Credit:** Origin scenario by Andrew Griffith. Insider-threat framing reinforced by Johnny Xmas
("a paycheck is no longer a guarantee of loyalty" — quote pending permission).
