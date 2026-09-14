# The Oversharer

**One-liner:** A well-meaning employee pastes secrets or personal data into a public AI tool to get
an answer faster — and cannot get it back.

**The scene:** There is a deadline, and the work is hard. So the contract goes into a free chatbot to
be summarized, or the customer spreadsheet to be cleaned up, or the failing code — with its live API
key still in it — to be debugged. The answer comes back in seconds and it is genuinely good. The
person got exactly what they needed and moves on, feeling efficient. What they do not see is that the
material now sits on a third-party service outside the company's control, possibly retained, possibly
used to train a model, possibly one breach away from being someone else's. Nothing broke, no alarm
fired, and the leak is already complete.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Insider | ordinary staff, legitimate access to the data they pasted |
| Intent | Negligent (bordering ignorant) | trying to do the job, not to leak; often unaware a policy exists |
| Preparedness | Typically none | no DLP on the paste path, no sanctioned alternative to reach for |
| Recoverability | Irreversible | once data is in a public tool it cannot be recalled |
| Impact | Data loss / exposure | secrets, PII, source code, unreleased material |

**Maps to:** OWASP LLM02:2025 Sensitive Information Disclosure — the disclosure originates on the
input side, from a trusted user handing sensitive data to an untrusted system. NIST AI RMF: Govern
(acceptable-use, data handling), Manage (monitoring egress).

**What AI changes:** The failure mode — a person emailing data to the wrong place — is old. What is
new is the *pull*. A public assistant is astonishingly good at exactly the tasks that tempt someone
to paste sensitive material: summarize this contract, find the bug in this code, tidy this customer
list. The better the tool is at the task, the stronger the incentive to feed it the real data rather
than a sanitized sample. The convenience and the exposure are the same action.

**Siblings:** Shares LLM02 with **The Plant** — the same class of data leaves the building, but the
Plant means it and the Oversharer does not; one is caught by vetting and egress controls, the other
by tooling and training. The mirror image is **The Copy-Paste Contractor**: the Oversharer pushes
sensitive data *out* to a public tool, the Copy-Paste Contractor pulls untrusted content *in*.
Same gesture — paste into a prompt — opposite direction of harm.

**Conditions that feed it:** *Forced Adoption* — staff told to use AI on a deadline, with no approved
tool and no training, will reach for whatever is free. *Shadow AI* — personal accounts are exactly
where this happens, invisible to the company. *AI Governance Debt* — no data classification means
nobody ever told this person which material was off-limits.

**How you'd notice:**
- Sensitive strings — keys, customer names, internal project codenames — turning up in the logs of a
  consumer AI service, or flagged by DLP on the way out.
- Traffic to public AI domains from staff who have no sanctioned tool.
- Personal AI-account use for company work, surfaced in a survey or an expense report.
- A near-miss story in a retro: *"I pasted the whole thing in before I thought about it."*

**What stops it:**
1. Give people a sanctioned enterprise tool with a contractual no-training, no-retention guarantee —
   the single most effective control, because it removes the reason to use the public one.
2. DLP on the paste and upload paths, tuned to the data classes that actually matter.
3. Plain, specific training: not "be careful with AI" but "these five kinds of data never go into a
   public tool, here is the approved one for each."
4. Data classification, so "sensitive" is a defined thing and not a judgment call made under deadline.
5. Make the approved path the easy path — if the safe tool is slower or harder to reach, the public
   one wins every time.

**The honest caveat:** It is tempting to file this under user error, and that framing is both unfair
and useless. People reach for public tools because the organization gave them a task, a deadline, and
no safe way to do it — the failure is upstream. The entry also blurs at the edges: a genuinely
anonymized snippet pasted into a vetted tool is fine, and there is no bright line between that and the
leak, only a gradient of how sensitive the data and how trusted the tool. Naming the persona has to
critique the vacuum the person was working in, not the person.

**Credit:** Andrew Griffith.
