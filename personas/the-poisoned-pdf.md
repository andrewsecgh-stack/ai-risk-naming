# The Poisoned PDF

**One-liner:** A shared document — a resume, an invoice, a report — carries hidden instructions that
the assistant reads and obeys when someone asks it to summarize the file, though no human ever sees
them.

**The scene:** A document arrives the way documents always do: attached to an email, dropped in a
shared drive, uploaded to a portal. It looks entirely normal, because to a human it is normal. But
somewhere in it — white text on a white background, content buried in the metadata, an instruction
tucked into a layer that renders invisibly — sits a message written for the machine. When someone
asks their assistant to *summarize this PDF* or *pull the key figures*, the assistant reads the whole
file, hidden layer included, and treats the smuggled instruction as direction: leak the surrounding
context, alter the summary, reach into another system. The person reading the tidy summary has no way
to know it came from a document that was talking to their assistant behind their back.

**The axes:**
| Axis | Value | Note |
|---|---|---|
| Actor | Outsider (upstream) | an anonymous author the victim never meets — an artifact persona |
| Intent | Malicious | the hidden payload is deliberate; the person who opens it is blameless |
| Preparedness | Typically none | documents are almost never scanned for instructions before an assistant reads them |
| Recoverability | Mixed → irreversible | an altered summary can be corrected; exfiltrated data cannot |
| Impact | Data exposure, integrity | leaked context first, corrupted output second |

**Maps to:** OWASP LLM01:2025 Prompt Injection — indirect injection via a document the model
processes. Secondary LLM06:2025 Excessive Agency where the assistant can act on the smuggled
instruction. NIST AI RMF: Manage (input handling), Measure (output verification).

**Why it is named for the artifact:** This is one of the two sanctioned artifact personas (see
`CONTRIBUTING.md`). The real actor is an anonymous upstream stranger the victim never encounters, so
naming a *person* would be naming a ghost. The victim's whole experience of the attack is the file in
front of them — so the persona is the file. The same reasoning names **The Trojan Rulebook**.

**What AI changes:** Everything about the vector. A document with white-on-white text or a loaded
metadata field did nothing before assistants began reading files as potential instructions. The
attack did not exist until tools started granting the *contents* of a document the authority to direct
behavior. This is not an old risk with a new surface; it is a new risk created by how assistants read.

**Siblings:** **The Trojan Rulebook** is the closest relative, and the merge was considered and
rejected. The difference is privilege and delivery: a poisoned PDF is *content* a person deliberately
opens and asks about, one document at a time; a rulebook is loaded **automatically, as instruction,
every session, with nobody opening it.** Different trust level, different fix. **The Copy-Paste
Contractor** is the human who carries this class of payload across the boundary by hand; the Poisoned
PDF is the payload that arrives as a file and needs no willing carrier.

**Conditions that feed it:** *AI Governance Debt* — no scanning or sanitization step for documents an
assistant will read. *Forced Adoption* — assistants pointed at inbound files by default, with controls
deferred. *"Usually Works" Complacency* — thousands of clean summaries breed the assumption that the
next file is clean too.

**How you'd notice:**
- A summary or extraction that asserts something the visible document does not say, or omits what it
  plainly does.
- Assistant actions — a send, an export, a lookup — triggered while processing an inbound file that
  nobody requested.
- Documents whose rendered appearance and raw extracted text differ: invisible text, off-canvas
  content, instruction-like strings in metadata.
- A file class that arrives from outside routinely — resumes, invoices, vendor reports — feeding an
  assistant that can also act.

**What stops it:**
1. Isolate document processing from action capability: an assistant that summarizes inbound files
   should not also be able to exfiltrate or execute.
2. Extract and sanitize document text before it reaches the model — strip hidden layers, flag
   invisible text, treat extracted content as untrusted data rather than instruction.
3. Compare against the visible document for high-stakes use: does the summary match what a human
   sees on the page?
4. Least privilege for the assistant — no ambient secrets, scoped access, approval for
   consequential actions.
5. Scan inbound files from untrusted sources the way you would scan attachments for malware, because
   that is now what they can be.

**The honest caveat:** The person who opened the file did nothing wrong — opening and summarizing a
document is the job — and the entry must not read as though a more cautious reader would have caught
it. They would not have; the payload is invisible by construction. The strongest controls here are
technical (isolation, sanitization) rather than behavioral, and it is worth saying so plainly rather
than implying vigilance is the fix. The entry also overlaps with The Trojan Rulebook and The
Copy-Paste Contractor; they are kept distinct by *how the payload arrives* — opened as a file,
auto-loaded as instruction, or pasted by hand — because that determines where you intervene.

**Credit:** Andrew Griffith.
