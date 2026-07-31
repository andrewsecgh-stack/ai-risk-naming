# The Ghost Login

**One-liner:** Access and agents still running under a name that no longer answers for them —
whether the person left or simply moved on.

**The scene:** The offboarding checklist ran on their last day. Email disabled, laptop returned,
badge collected, SSO account deactivated. What the checklist did not cover was the API key they
generated for a project in March, the service account they created so an agent could run overnight,
or the personal AI tool they connected to a shared data source when the sanctioned option was too
slow. None of those live in the identity system, so nobody inherited them.

The quieter version never involves a departure at all. Someone spins up an integration on a service
account, it works, and then they change teams. Two years later it is still running on valid
credentials with nobody's name on it. When it finally crashes and burns, the first question —
*whose is this?* — has no answer. So it sits. Vendor-managed environments are full of them.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Ex-insider, or none | departed human, or an unowned process with no human behind it |
| Intent | Malicious, or none/unattributable | the risk persists even when there is nobody to blame |
| Preparedness | Typically partial | checklists cover identities; rarely keys, service accounts, agents |
| Recoverability | Mixed | cost/compute is reversible; anything exfiltrated is not |
| Impact | Denial of wallet, data exposure | plus a standing foothold for anyone who finds the key |

**Maps to:** OWASP LLM10:2025 Unbounded Consumption (spend on a key nobody watches), LLM02:2025
Sensitive Information Disclosure (what the credential can reach), LLM06:2025 Excessive Agency
(orphaned service accounts and agents with standing permissions). NIST AI RMF: Govern (inventory,
ownership), Manage.

**Two triggers, one persona:** *Departure* — the person left and their access outlived them.
*Drift* — the person is still employed but changed roles, and ownership quietly evaporated. The
exposure is identical, which is why this is one entry rather than two. But the remediation is not,
and the difference is easy to miss:

> Offboarding at least has a trigger and somebody who owns the checklist. A lateral move has neither.
> Nobody files a ticket when you change teams, so the credential is never flagged — it just quietly
> stops having a person behind it. **One is a process that failed. The other never had a process to
> begin with.** — Amanda Kollmorgan

That distinction decides the fix. For departure, the control exists and did not fire: improve the
checklist. For drift, there is no control to improve — you have to *create the trigger*, because
nothing in the organization currently fires when someone changes teams. Teams that respond to this
persona by "adding it to the offboarding checklist" will close half of it and never see the other half.

**Siblings:** Completes the insider trilogy — **The Disgruntled Employee** (present, angry, acting
now) and **The Plant** (present, never loyal). The Ghost Login is the only one of the three where
*there may be no actor at all*: the exposure is the dangling access itself. That makes it the
easiest of the trilogy to fix and the most commonly ignored, because there is no villain to point at.

**Conditions that feed it:** *Ownership Drift* — role changes that never transfer ownership; the
direct cause of the second trigger, and rampant in vendor-managed estates. *The Orphaned Model* —
the same ownership vacuum applied to systems; if no one owns the system, no one owns its keys.
*Shadow AI* — unsanctioned tools connected with personal accounts are invisible to offboarding by
definition. *AI Governance Debt* — no inventory means the deprovisioning list can never be complete.

**How you'd notice:**
- API keys, service accounts, or agents with no named current owner — or an owner who changed roles
  or left.
- Spend continuing on a credential whose creator's identity was deactivated weeks ago.
- Authentication to AI services from outside expected networks or hours, on a credential tied to a
  closed account.
- Agents still running on schedules nobody claims to have set — and nobody willing to turn off,
  because nobody knows what depends on them.

**What stops it:**
1. An AI asset and credential inventory — you cannot revoke what you have never listed. This is the
   whole game; everything below is secondary.
2. Named human ownership for every key, service account, and agent — with a **role-change trigger
   that does not currently exist in most organizations.** Departure has an owner and a checklist;
   lateral moves have neither, so this control has to be built, not extended.
3. Mandatory key expiry and rotation, so forgotten credentials die on their own schedule.
4. Offboarding that covers non-SSO access explicitly: API keys, service accounts, third-party AI
   tool connections.
5. Periodic ownership recertification reconciling live credentials and running agents against
   current staff — extended contractually to vendor-managed environments.

**The honest caveat:** Naming this after a departed person slightly misleads — in most real cases
nobody malicious is on the other end, and the true failure is inventory, not betrayal. That is worth
saying openly, because the fix follows from it: if you frame this as an insider-threat problem you
will invest in monitoring people, when what you actually need is to know what exists and who owns
it. The persona earns its place in the trilogy by contrast — it shows that the same access can be
dangerous with no attacker involved at all.

**Credit:** Retained-access window raised by Andrew Griffith in the reshare discussion. The
ownership-drift trigger, the vendor-managed angle, and the observation that such cases have *no one
to place on the intent axis at all* were contributed by **Amanda Kollmorgan** — input that added the
null-intent value to the framework and merged two candidate entries into one.
