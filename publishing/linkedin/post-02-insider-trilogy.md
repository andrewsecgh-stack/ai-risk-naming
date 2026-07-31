A comment on my last post broke my framework. That's the best thing that could have happened to it.

I've been working on plain-language names for AI risks — the human scenarios that OWASP's LLM Top 10 describes precisely, but never staffs with actual people.

Then a security professional raised the one he had no name for: the agent nobody owns. Someone spins up an integration on a service account. It works. They change roles. Two years later it's still running on valid credentials with nobody's name on it. When it finally crashes and burns, there's no one to blame. So it sits.

That broke something. My model sorted risk by intent — malicious, negligent, ignorant. This has none of them. There's no actor at all. The axis assumed a person, and it turns out some of the most persistent AI risk doesn't have one.

So the framework now carries a null case: unattributable. And his scenario didn't become a new entry — it merged into an existing one, because the fix is the same either way. Inventory. Named ownership. Transfer on role change, not just on departure.

Here's the insider set as it stands:

The Disgruntled Employee — was loyal, then turned. There's a change to detect.

The Plant — never loyal. Nothing to detect, because nothing changed.

The Ghost Login — access and agents still running under a name that no longer answers for them.

Read in order, they aren't sorted by intent. They're sorted by how detectable they are: visible change, no change, no person. That progression is the part I didn't see until all three were written down.

The chart below is deliberately unfinished. Three entries are fully worked. Four are a name and a line. Several rows are empty, because I haven't seen the scenario clearly enough to name it honestly.

So — which of these have you actually watched happen, and what did you call it at the time?

#AISecurity #OWASP #LLMSecurity #InsiderThreat #AIGovernance
