The OWASP Top 10 for LLM Applications is one of the best things to happen to AI security. It tells you, precisely, what can go wrong inside the system.

What it doesn't tell you is who trips the wire, or why. Outside the AI security world, we're still missing the plain-language names that make these risks click.

Take LLM10: Unbounded Consumption — the risk that someone runs up uncontrolled requests and drives your compute bill through the roof. Accurate. But it describes a mechanism, not a moment.

Here's the moment: the disgruntled employee.

Someone's angry — about a review, a passed-over promotion, or a personal problem bleeding into their work. Whatever the reason, they act before anyone notices and before access is cut: quietly looping the most expensive model calls they can, or stripping the rate limits they were trusted to manage. No malware. No breach. Just a person, a valid login, and a motive. It's a "denial of wallet" attack with a face and a reason — and that face is exactly what makes it easy to explain to a CFO or an HR lead who will never read the OWASP doc.

But lean on that word — motive. It points only at the people who meant it, and that's not the whole story. Strip the motive away and the damage stays: the same bill lands when someone simply isn't thinking clearly — distracted, overwhelmed, cutting a corner they never clocked as one. No anger, no plan, same outcome.

I think the missing axis is intent:

- Malicious — they meant to hurt you (the disgruntled employee).
- Negligent — they knew better and cut the corner anyway (the engineer who ships an unbounded agent loop).
- Ignorant — they had no idea (the new hire who pastes source code into a public chatbot).

Same OWASP category. Three completely different people, controls, and conversations.

And some of the most common failures don't map onto the Top 10 at all — shadow AI, or over-reliance on an agent that's confidently wrong. Those are governance and human-trust gaps, not system flaws, and I want to name them the same way I have the disgruntled employee.

I'm going to keep working on this: mapping real human scenarios onto the OWASP risks, and naming the ones the framework doesn't quite reach.

So tell me: what's a scenario you've seen that the framework doesn't have a name for?

#AISecurity #OWASP #LLMSecurity #CyberSecurity #AIGovernance
