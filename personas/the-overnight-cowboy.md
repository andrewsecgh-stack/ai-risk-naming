# The Overnight Cowboy

**One-liner:** An autonomous agent is turned loose to work unattended against real systems overnight,
with no sandbox and no containment, doing exactly what it was told to systems that could not afford
it.

**The scene:** It is late, the deadline is close, and the idea is reasonable: let the agent run the
migration, refactor the module, or churn through the test matrix while everyone sleeps. So it is
pointed at the real environment — production credentials, live data, write access — because setting
up a safe copy would take time nobody has. Then the laptop closes and everyone goes home. The agent
does precisely what it was asked, with the literal-mindedness of a machine: it drops the table it was
told to "clean up," rewrites the files it was told to "fix," makes calls that cost real money, and
there is no one awake to see it and no guardrail to stop it. Morning arrives to either a small miracle
or a smoking crater, and which one was mostly luck.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Automated agent | acting alone, unattended, on a human's instruction |
| Intent | Legitimate | the work was sanctioned; the failure is the *absence of containment*, not the goal |
| Preparedness | **The whole point** — none in this persona | fully prepared, the same act is responsible; unprepared, it is reckless |
| Recoverability | Mixed | judged per impact class — see below |
| Impact | Cross-cutting | availability and integrity if it breaks things; data exposure if it leaks; denial of wallet if it loops |

**Maps to:** OWASP LLM06:2025 Excessive Agency (unattended action against real systems) and LLM10:2025
Unbounded Consumption (unwatched spend). NIST AI RMF: Manage (deployment controls, human oversight),
Measure.

**The teaching case for the preparedness axis:** This is the persona that exists to make the axis
concrete. The *act* — running an agent autonomously overnight — is not inherently a villain. With
**full preparedness** it is responsible engineering: a sandbox or non-production copy, a dry-run mode,
a hard budget cap, approval gates on destructive operations, snapshots taken first, and someone
on-call. With **no preparedness** the identical act is recklessness waiting for its unlucky night. The
persona name captures the *unprepared* version; the prepared version is not a different persona but a
control state — "earned recklessness," the same cowboy with a rope and a fence.

**The preparedness rule, per impact class:** Containment must be judged against each impact class it
faces, not as a blanket "we took a backup." Snapshots and rollback can *fully* cover the reversible
class — the agent wipes an environment, you restore it — while covering **none** of the irreversible
class: that same agent leaks proprietary data to a public model, and nothing redeploys confidentiality
back. "We can recover" is true only for the impacts you can actually reverse.

**Siblings:** The Excessive-Agency and Unbounded-Consumption neighborhood. **The Over-Permissioned
Assistant** is the standing *state* of too much access; the Overnight Cowboy is that access *exercised
without containment at a moment* — and an over-permissioned agent run overnight is the worst of both.
**The Runaway Agent** overlaps on cost, but its failure is an unbounded *loop*, while the Cowboy's is
unbounded *environment* — it can do irreversible harm on a single confident pass, no loop required.

**Conditions that feed it:** *"Usually Works" Complacency* — it ran clean last time, so nobody built
a fence. *Forced Adoption* — pressure to show autonomous AI results fast, containment deferred.
*AI Governance Debt* — no policy on what agents may touch unattended. *Agent Sprawl* — unattended runs
nobody enumerated are exactly the ones with no on-call.

**How you'd notice:**
- Agents holding production credentials and write access with no non-production path in sight.
- Scheduled or long-running autonomous jobs with no approval gate on destructive actions and nobody
  named to watch them.
- Morning-after surprises: data changed, resources deleted, or spend spiked between the last human
  action and the first.
- "We'll just run it against prod, it'll be fine" as an accepted phrase rather than a red flag.

**What stops it:**
1. Run unattended agents in a sandbox or non-production environment by default; touch production only
   with a deliberate, gated exception.
2. Dry-run first — have the agent propose its actions for review before it is allowed to execute them.
3. Approval gates on destructive and irreversible operations, so the agent pauses for a human at
   exactly the steps that cannot be undone.
4. Snapshots and backups taken *before* the run, plus hard budget caps and a kill switch — and be
   honest that these cover the reversible class only.
5. Someone on-call or an automated tripwire for unattended runs, so a bad night is caught in minutes
   rather than at 9 a.m.

**The honest caveat:** The whole value of this persona is that it is *not* a straightforward "don't do
that" — autonomous overnight work is legitimate and often the right call, which is why the framing has
to be preparedness rather than prohibition. The risk is that "earned recklessness" gets used as a
license by people who have not actually earned it: the sandbox, the gates, and the per-impact-class
honesty are the earning, and skipping them while keeping the swagger is just the reckless version with
better PR. The line between prepared and unprepared is a real gradient, and the entry is only useful
if it is applied strictly.

**Credit:** Andrew Griffith. Grounded in the real incident behind the preparedness axis — recovery
covering the reversible impact class fully while covering the irreversible class not at all.
