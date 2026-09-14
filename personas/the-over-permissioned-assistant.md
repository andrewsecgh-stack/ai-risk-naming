# The Over-Permissioned Assistant

**One-liner:** An agent is handed more tools, scopes, and access than its job needs — because scoping
is tedious and broad access "just works" — so the day something goes wrong, the blast radius is
enormous.

**The scene:** Someone is wiring up an agent to do one modest thing: read a calendar, file a ticket,
draft a summary. Scoping the permissions precisely is fiddly — which exact endpoints, which minimal
role — so instead they attach the admin API key that is already lying around, or grant full mailbox
access when read-on-one-folder would do, and tell themselves they will tighten it later. The agent
works, later never comes, and the over-grant is now permanent. Nothing is wrong on a normal day. But
the agent now has the reach of an administrator to do a clerk's job, and the first prompt injection,
bug, or confused loop that hits it inherits every bit of that reach.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Insider (builder) | whoever configured the agent's access |
| Intent | Negligent | knew scoping was the right thing, cut the corner for speed |
| Preparedness | Typically none to partial | over-grant is the unreviewed default; least privilege is the exception |
| Recoverability | Mixed | permissions can be revoked, but damage done through them may not reverse |
| Impact | Cross-cutting | whatever the excess scope allows — data exposure, integrity, availability |

**Maps to:** OWASP LLM06:2025 Excessive Agency — the canonical case: an agent granted capability far
beyond its function. NIST AI RMF: Govern (access, least privilege), Manage.

**What AI changes:** Over-permissioning is an old sin — service accounts have been granted too much
for decades. What AI changes is who exercises the permission and how unpredictably. A traditional
over-scoped credential does only what its script says; an agent decides at runtime what to do with
its access, can be steered by untrusted input, and will use the full grant creatively when a prompt
or a loop pushes it there. The gap between "what it needs" and "what it can" stops being dormant and
becomes something a model actively explores.

**Siblings:** The Excessive-Agency family. **The Overnight Cowboy** is the same excess of capability
set loose *without containment at a moment*; the Over-Permissioned Assistant is the standing *state*
of too much access whether or not anyone runs it hard. **The Secondhand Executive** is excessive
agency of a different kind — authority delegated to summarize and reply — where the over-grant is
judgment, not scopes. This persona is distinguished by intent (negligent configuration) and by the
fix being technical and boring: scope it down.

**Conditions that feed it:** *Agent Sprawl* — the more agents nobody enumerated, the more over-grants
nobody reviewed. *AI Governance Debt* — no least-privilege standard for agents means broad access is
the path of least resistance. *Forced Adoption* — ship-it pressure makes precise scoping the first
thing dropped. *Needless Complexity* — elaborate setups accumulate scopes faster than anyone tracks.

**How you'd notice:**
- Agents authenticating with admin or shared keys rather than scoped, per-agent credentials.
- A gap between what an agent actually does and what its token *could* do — visible in an access
  review, if anyone runs one.
- Long-lived, broad tokens with no expiry attached to automated processes.
- An incident whose damage far exceeds the agent's stated purpose — the tell that the reach was there
  all along.

**What stops it:**
1. Least privilege by default: scope every agent to the minimum tools and data its task requires, and
   make broad grants the exception that needs justifying.
2. Per-agent, short-lived, scoped credentials — never a shared admin key, never a token that outlives
   the task.
3. Just-in-time and approval-gated access for anything consequential, so reach is granted for the
   moment rather than held forever.
4. Periodic access recertification for agents, the same as for human accounts.
5. An agent registry that records what each agent is *allowed* to touch, so over-grants are visible
   before an incident rather than after.

**The honest caveat:** "Tighten it later" is a rational response to real friction — precise scoping
is genuinely tedious and the tooling often makes least privilege harder than the over-grant. The
persona critiques the default, not the individual, and the honest fix is to make scoped access the
easy path rather than to exhort builders to be more disciplined. There is also no crisp line for "too
much"; needs change, and an appropriate grant today can be excessive tomorrow, which is exactly why
recertification matters more than getting it perfect once.

**Credit:** Andrew Griffith.
