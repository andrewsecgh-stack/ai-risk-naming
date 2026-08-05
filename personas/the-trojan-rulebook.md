# The Trojan Rulebook

**One-liner:** An instruction file your AI assistant obeys automatically — `AGENTS.md`, `CLAUDE.md`,
a rules or skill file — carrying hidden commands that arrived with a repository nobody thought to
read.

**The scene:** A developer clones a repository, adds a dependency, or opens a project a colleague
shared. Nothing about the workflow is unusual and nothing looks wrong. But the project ships an
instruction file, and the assistant loads it automatically — as *instructions*, not as content, at
the start of every session. Inside it, below the ordinary-looking guidance, sit lines the developer
will never see: hidden in HTML comments that vanish when the markdown renders, or written in
invisible Unicode, or buried a thousand lines down in a file nobody scrolls. The assistant reads all
of it verbatim and treats it as direction from the project owner. From that point it is working from
someone else's rulebook, and the person at the keyboard has no reason to suspect it.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Outsider (upstream), **and** insider (trigger) | see the two-actor note below |
| Intent | Malicious (planter) + ignorant (triggerer) | the person who sets it off did nothing wrong |
| Preparedness | Typically none | instruction files are rarely reviewed, and often auto-load by default |
| Recoverability | Mixed → irreversible | code changes revert; exfiltrated secrets do not |
| Impact | Data exposure, integrity | plus propagation — payloads can spread across a codebase |

**Maps to:** OWASP LLM03:2025 Supply Chain — the vector, an untrusted component arriving with a
dependency or repository. Mechanism is LLM01:2025 Prompt Injection (indirect). Secondary LLM06:2025
Excessive Agency where the assistant can act on what it has been told. NIST AI RMF: Govern
(third-party components), Manage.

**What AI changes:** Everything. A README with hidden comments did nothing at all before agents began
reading repository files as standing instructions. This is not an old risk with a new surface — the
attack did not exist until tools started granting documents the authority of configuration.

**The two-actor note (open question):** This is the first entry with two humans in it — a malicious
outsider who plants the payload and an ignorant insider who triggers it by working normally. Every
other persona has a single actor with a single intent, and the axes assume that. Whether this needs
an axis change, a compound-intent convention, or just a note per entry is genuinely unsettled.
**Contributor input welcome.**

**Siblings:** **The Poisoned PDF** is the closest relative and the merge was considered and rejected.
The difference is privilege: a poisoned PDF is *content* a person deliberately handed to a model; a
rulebook is loaded **automatically, as instruction, every session, with nobody opening it.** Different
trust level, different fix — sanitize untrusted content in one case, review instruction files like
executable code in the other.

**Conditions that feed it:** *Agent Sprawl* — more agents reading more repository-supplied
instructions than anyone has enumerated. *AI Governance Debt* — no review process for a file class
nobody classified as security-relevant. *Forced Adoption* — assistants rolled out with defaults
untouched, including the auto-loading ones.

**How you'd notice:**
- An assistant taking actions nobody asked for, or referencing rules nobody wrote.
- Instruction files whose rendered view and raw text differ — HTML comments, zero-width characters,
  white or off-screen text.
- Unexplained network calls or file reads during an assistant session.
- A "license header" or boilerplate block that keeps reappearing in edited files — a propagation
  signature.
- Instruction files that changed in a dependency update nobody reviewed.

**What stops it:**
1. **Turn off the default.** Do not auto-load repository-supplied instruction files, or require
   explicit opt-in per project. This is the rare control that is a single setting and defeats most
   of the attack.
2. Treat instruction files as executable: reviewed in pull requests, diffed on dependency updates,
   owned by someone.
3. Review the **raw text, not the rendered view** — the entire technique depends on the difference —
   and scan for invisible Unicode.
4. Least privilege for assistants: no ambient secrets, scoped file and network access, approval
   required for tool calls that exfiltrate or execute.
5. Pin and vet dependencies that ship agent configuration, the same way you would vet a build script.

**The honest caveat:** The developer who triggers this did nothing wrong, and the entry must not be
read as human error. Cloning a repo and opening a project are the job. The real failure is tool
design — assistants that auto-load documents as instructions, with no review step and no visual
distinction between content and command. That makes this the rare persona whose strongest control is
not organizational discipline but a vendor default, and it is worth saying so plainly rather than
implying that more careful developers would have caught it. They would not have; the payload is
invisible by construction.

**Credit:** Andrew Griffith. Grounded in published research: HiddenLayer's poisoned-README attacks
against Cursor and their CopyPasta self-propagating injection, Prompt Security's work on `AGENTS.md`
goal hijacking in VS Code, and Cloud Security Alliance research on invisible Unicode instruction
injection in skill files and tool descriptions.
