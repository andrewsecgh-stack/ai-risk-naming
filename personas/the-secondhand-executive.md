# The Secondhand Executive

**One-liner:** A senior decision-maker who has delegated reading, summarizing, and replying to
agents — and now experiences their entire organization secondhand, through compressions nobody
audits.

**The scene:** It starts reasonably. There is too much email, so an agent summarizes it. The
summaries work, so an agent starts drafting the replies. Reports from direct reports get summarized
too, then the summaries of those get rolled up into a weekly digest. Each step is defensible on its
own and each one saves real time. A year in, the person at the top of this stack has not read an
original document in months. They are making decisions on compressions of compressions, replying in
a voice that is not quite theirs, to people who are increasingly aware that their carefully written
update was never actually read. Nothing has broken. Nobody has complained. And the first sign of
trouble will be a decision made confidently on a detail that was dropped three summaries ago.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Insider (senior decision-maker) | the decision authority is what makes it dangerous |
| Intent | Legitimate, drifting to negligent | they are trying to cope with real overload, not cut corners |
| Preparedness | Typically none | nobody designs a verification step into a convenience |
| Recoverability | Mixed | a bad call can be reversed; a missed signal usually cannot |
| Impact | Resilience & knowledge erosion | manifests as degraded decision quality and lost situational awareness |

**Maps to:** *(primary mapping open for review — see note.)* OWASP LLM09:2025 Misinformation, which
explicitly covers over-reliance on model output. Secondary: LLM06:2025 Excessive Agency, once the
agent is replying and acting rather than only summarizing. NIST AI RMF: Govern (human oversight),
Measure (output verification).

> **Open question for contributors:** which mapping should be primary? LLM09 fits the harm — decisions
> made on lossy, unverified output. LLM06 fits the mechanism — an agent granted authority to read,
> summarize, and reply on someone's behalf. The answer probably depends on whether you think the
> defining failure is the *compression* or the *delegation of authority*. Input welcome.

**What AI changes:** Executives have always worked from summaries — that is what chiefs of staff and
briefing notes are for. Three things are different when the summarizer is a model. A human
summarizer has **judgment and stake**: they notice when something is off and escalate it unprompted
— *"this one's strange, you should read it yourself."* An agent compresses faithfully and flags
nothing, because nothing in the chain knows what would alarm you. Second, the compression becomes
**recursive and invisible** — summaries of summaries of replies that were themselves agent-drafted,
with no way to see what was dropped at each layer. Third, when the agent also **replies**, the loop
closes: the person is no longer even seeing what their own organization believes they said.

**Siblings:** **The Overengineer** shares the over-automation instinct but not the harm — that
persona wastes money doing simple things elaborately; this one degrades judgment. Cost caps fix the
Overengineer and do nothing here. The organizational version of this same erosion is Purva Dublay's
**Premature Reviewer Cuts** condition: one is an individual losing contact with the source material,
the other is an institution removing the people who used to maintain that contact.

**Conditions that feed it:** *"Usually Works" Complacency* — the summaries have been fine for months,
so nobody checks. *Automation Bias / Over-Reliance* — deference to the digest over one's own reading.
*Forced Adoption* — pressure to demonstrate AI leadership from the top makes this look like modelling
good behavior. *Agent Sprawl* (candidate) — the coding and workflow agents nobody has inventoried,
doing more than anyone asked.

**How you'd notice:**
- Decisions that reference details which are subtly stale, wrong, or missing context.
- Surprise at things that were, in fact, communicated — in an email that got summarized away.
- Direct reports noticing that replies do not engage with what they actually wrote, and quietly
  adjusting how much effort they put into writing.
- The person can recall conclusions but not specifics, and cannot say where a number came from.
- Escalations that arrive late, because nothing in the chain knew the item was urgent.

**What stops it:**
1. Define categories that **bypass summarization entirely** — resignations, HR matters, legal,
   safety, anything from a skip-level. An agent cannot be told to "escalate anything unusual," so
   the exceptions have to be structural rather than judgment-based.
2. Keep summaries **linked to their originals** so the source is one click away, and make reading the
   original the norm for anything that will drive a decision.
3. No agent-authored replies to direct reports without review. This is the step that erodes trust
   fastest and is the easiest to stop.
4. Keep a human with stake in the chain for high-stakes flows — the chief-of-staff function exists
   precisely because judgment does not compress.
5. Periodically sample: take five summarized items, read the originals, and measure what was lost.
   This is the only control here that produces evidence rather than reassurance.

**The honest caveat:** Summarization is genuinely useful, and most people arrive at this pattern
through real overload rather than laziness — which is why naming it must critique the *pattern* and
not the person. There is no clean line where reasonable delegation becomes this persona; it is a
gradient, and everyone is somewhere on it. The entry is also unfalsifiable in the moment: the damage
shows up as decisions that were slightly worse than they would have been, which is almost impossible
to attribute after the fact. That weakness is real, and it argues for the sampling control above —
compare summaries against originals while you still can, rather than trying to prove harm later.

**Credit:** Andrew Griffith.
