---
type: source
date: 2026-07-18
timestamp: 2026-07-18
source_url: "https://x.com/i/status/2078945495280427238"
canonical_url: "https://x.com/SebaTheOracle/status/2078382001820975452"
resource: "https://x.com/SebaTheOracle/status/2078382001820975452"
title: Anthropic's Superchicken Problem
author: Cody Peterson
handle: SebaTheOracle
created_at: 2026-07-18
topics: [organisation]
tags: [system-performance, organizational-incentives, product-reliability, customer-trust, group-selection]
description: "Raw X article capture arguing that whole-system customer outcomes matter more than isolated model or individual performance."
content_hash: 2e58e93a27a3b6b8c0a9b66fb2b93c57fbed84e85daf962c760c16155a085b04
extracted_at: "2026-07-20T08:32:32"
extractor: fxtwitter-article
---

# Raw content

Source: https://x.com/SebaTheOracle/status/2078382001820975452


Lucas Beyer post:
A bit long, but a nice read especially if like me you didn't know about the chicken individual vs coop selection experiment.

It's about organizations (here oai vs ant, but really more general) and how org of best individuals != best org.

Quoted post by Cody Peterson:
Anthropic’s Superchicken Problem

How the smartest lab in the world accidentally shipped the wrong product

I asked Anthropic’s most capable public model to edit an essay about Anthropic. It never got the chance. I attached this draft and typed seven harmless words: “Redraft make this POP. Format for Twitter.” The app automatically switched the task from Fable 5 to Opus 4.8. Its explanation was simple: “Fable’s safeguards flagged this message.”

To be precise, this was not ordinary rate limiting. Fable did not answer and refuse. Anthropic’s safeguard intercepted the request before the selected model could respond and routed it to another model instead. Anthropic has explained that this is exactly how the system works: when Fable’s classifier blocks a request, the request is sent to Opus 4.8. The company has also acknowledged that it deliberately enlarged the classifier’s safety margin, knowing that the result would be more false positives on benign work. (Anthropic)

I do not know why the safeguard fired, and I am not claiming Anthropic censored criticism. The verifiable—and sufficiently strange—fact is that a routine editing request was caught by a safeguard whose own warning discussed false positives in legitimate coding, cybersecurity, and biology work. It was an almost comically perfect opening to an essay about the team that made what many believe to be the most brilliant AI system on the planet.

This essay examines what happens when a system becomes so preoccupied with the performance of its individual parts that it loses sight of the outcome the whole system exists to produce.  The model can be brilliant, the safeguard can operate exactly as designed, and the pricing policy can make perfect sense to the people who created it. The user’s work can still remain unfinished.

Exhibit A:



The Chickens and Their Eggs

In 1982, Purdue geneticist William Muir began an unusual breeding experiment with egg-laying hens. Muir wanted to know what would happen if productivity were selected at the level of the group rather than the individual. Instead of breeding solely from the highest-producing individual birds—a measure of pure individual output—he housed related hens together and selected whole family groups according to their collective performance. The cage, rather than the isolated chicken, became the unit of selection. (PubMed)

Margaret Heffernan later turned Muir’s technical breeding program into the famous “superchicken” story. For managers, her tale became an ominous warning: hiring the strongest and the smartest does not always produce the best output. In her retelling, one flock of chickens was allowed to remain an ordinary flock—no superchickens allowed. A second group was repeatedly bred from the most productive individual chickens; she calls them “the all-star chickens.” (Purdue Alumnus)

The results were dramatic. Across six generations, annual mortality in Muir’s group-selected flock fell from 68 percent to 8.8 percent. Over the same period, production rose from 91 to 237 eggs per hen housed—2.6 times its original output. In a later head-to-head comparison conducted in groups of twelve, a commercial line bred for individual performance suffered 89 percent mortality by 58 weeks of age. Muir’s group-selected line suffered only 20 percent mortality, while the unselected control suffered 54 percent. In that same group environment, the group-selected flock outperformed the commercial all-stars in eggs per hen housed, egg mass, and eggs per hen per day. (PubMed)

Meanwhile, the flock of superchickens was ragged and worn down. In the version of the experiment that made the story famous, six of the nine all-star hens were dead and the remaining three had been pecked bare. The flock had, almost literally, pecked itself to death. (Purdue Alumnus)

The lesson was never that mediocrity beats talent. The real lesson is that your output will reflect what you reward. Select only for individual performance and you may accidentally build a weaker team, because the traits that allow one individual to dominate can reduce the productivity of everyone around them. Select individuals according to what they contribute to the group, and qualities that disappear inside an individual ranking—compatibility, restraint, reliability, and cooperation—suddenly become visible.

A chicken’s real contribution is not merely how many eggs she can squeeze out. It includes what her presence allows—or prevents—the other chickens from producing. Muir had not abandoned productivity in favor of harmony. He had discovered that, in a social system, harmony is part of productivity. The real unit of performance was never the chicken. It was the coop.

I learned a version of this hard-won lesson while running my own construction company. For years, dependable help was so difficult to find in our particular trade that an all-star felt like salvation. But the people who looked like all-stars too often came with a hidden tax: extra exceptions, extra management, damaged morale, and friction that the rest of the crew had to absorb.

Eventually, I stopped asking only, “How good is this person at their craft?” and started asking, “What happens to everyone else’s work when this person joins the team?” The person who looks strongest is not always the person who actually makes the company stronger. A master craftsperson who slows every adjacent trade, consumes the foreman’s attention, or drives dependable people away may be impressive in isolation and expensive in practice. A quieter worker who makes the entire crew more reliable may contribute far more than their individual output reveals.

The Supercoop

Anthropic really has assembled an extraordinary flock of really smart chickens. A 2025 SignalFire analysis, based on public employment data, estimated that engineers were eight times more likely to move from OpenAI to Anthropic than the reverse and nearly eleven times more likely to move there from DeepMind. It also estimated that 80 percent of Anthropic employees hired at least two years earlier remained through the end of their second year, compared with 78 percent at DeepMind and 67 percent at OpenAI. (SignalFire)

Those numbers do not describe a company struggling to attract or retain talent. They describe a magnet for all-stars.

That does not mean Anthropic’s employees are pecking one another to death. That would be a cheap analogy, and the talent numbers do not prove it. The more important danger is subtler. When a company can credibly point to exceptional researchers, unusually high retention, and frontier-leading models, it becomes easy to treat excellence in the individual parts as proof that the whole system is working.

Muir’s experiment demonstrates why that inference cannot be trusted. The danger is not brilliance itself. The danger is measuring performance one level too low.

The Model is Not The Product

The AI industry is built around superchickens: famous researchers, benchmark-leading models, enormous compensation packages, and launch pages covered in superlatives. Inside the lab, the pecking order is obvious. Outside it, we only see the eggs.

Silicon Valley has a clear blind spot: your team can be extraordinary while the product you've built remains frustrating, inaccessible, or unreliable.

Every day users don't judge a model by its team of talented chickens or its benchmarks. We only have the model, the app, the safeguards, the usage limits, the pricing, the customer support.



Two Companies, 74 Minutes Apart

On July 17, Anthropic responded to Fable’s overwhelming demand with a compromise. Beginning July 20, Max and Team Premium subscribers would receive Fable as part of their plans, but at half their normal limits. Pro and Team Standard users would continue accessing the model through usage credits and would receive a one-time $100 credit.



Seventy-four minutes later, OpenAI’s Thibault Sottiaux announced that usage limits had been reset for every paid Codex and ChatGPT Work user.

These were not economically identical offers. Anthropic was establishing an ongoing access policy for an unusually compute-intensive model, while OpenAI was granting a temporary reset after a difficult product launch. That caveat matters. The contrast in product posture was nevertheless difficult to miss.



OpenAI was not acting from a position of perfection. It had recently botched parts of its own desktop and ChatGPT Work rollout, and Sottiaux had admitted publicly that the company “didn’t get everything quite right.” Users had encountered confusing high-compute settings, opaque usage costs, and a redesign that disrupted familiar workflows. OpenAI responded by changing the defaults, promising to repair the interface, and repeatedly resetting usage so customers could continue working.

One organization was justifying scarcity.

The other was manufacturing goodwill.

OpenAI is not a flock of mediocre chickens. It is stacked with exceptional talent, too, and it has made serious cultural and product mistakes of its own. The meaningful difference in this moment is not intelligence, either in the models or in the coop. It is what the system appears to reward when pressure arrives.

At its best, OpenAI’s current product posture is relentlessly ordinary. It begins with the user’s task: What is this person trying to accomplish? What is preventing them from finishing? Where is the friction, and how quickly can we remove it? The resets do not prove that OpenAI has solved product culture, but it demonstrates to users an instinct to absorb some of the cost of its own mistakes rather than leaving them to carry all of it.

Anthropic’s product posture too often communicates something different: We have created extraordinary intelligence, and our principal responsibility is to determine how much of it you may safely access. That may be a coherent institutional posture, but it is not a customer-centered one. Golden eggs are impressive, but they do not feed the family when the coop will not let you collect them.

One company increasingly organizes itself around the user’s task. The other still organizes itself around systemic risk. Both companies must care about both questions, but the question they ask first shapes the product they eventually build. The difference does not appear only in mission statements. It appears in routing, limits, pricing, communication, and the willingness to repair trust when the system fails.



The whole coop

Culture is not what a company says about itself. Culture is what its systems repeatedly make easy—and what they repeatedly make difficult.

Anthropic does not need fewer brilliant people. It needs a broader definition of success, one that includes not only model intelligence and safeguard strength but also access, reliability, transparency, and trust. From the customer’s side, the final measure is surprisingly simple: Can I depend upon this entire system to finish the job?

Muir did not make his chickens less productive. He changed the level at which productivity was measured and discovered that collective performance contained information an individual egg count could not capture. The birds selected for group performance became healthier and more productive because destructive interaction was no longer invisible to the metric. Cooperation is not a sentimental alternative to output. It is one of the conditions that made greater output possible.

The frontier-model race is entering the same stage. When only one laboratory can produce extraordinary intelligence, the smartest model may look indistinguishable from the best product. Once several laboratories can produce extraordinary intelligence, the competitive advantage moves outward into the whole system.

The smartest model in the world is no longer automatically the best product or the best market fit. Claude may be the biggest and the smartest chicken in AI, but nobody outside the coop grades the chickens. We are only counting the eggs.

—

Sources

William M. Muir, “Group Selection for Adaptation to Multiple-Hen Cages,” Poultry Science (1996).
 https://pubmed.ncbi.nlm.nih.gov/8786932/

William M. Muir, “Incorporation of Competitive Effects in Breeding Programs,” Purdue University.
 https://web.ics.purdue.edu/~bmuir/papers/muir%20group%20selection%20genetics%20final%20v2.pdf

Margaret Heffernan, A Bigger Prize.
 https://www.hachettebookgroup.com/titles/margaret-heffernan/a-bigger-prize/9781610392914/

Margaret Heffernan, “Is the Professional Pecking Order Doing More Harm Than Good?,” NPR/TED Radio Hour.
 https://www.northcountrypublicradio.org/news/npr/443412777/is-the-professional-pecking-order-doing-more-harm-than-good

SignalFire, “The State of Tech Talent Report — 2025.”
 https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025

Anthropic, “Claude Fable 5 and Claude Mythos 5.”
 https://www.anthropic.com/news/claude-fable-5-mythos-5

—

AI disclosure: I developed the argument and wrote the original draft from my own experience, then used ChatGPT to help research, restructure, and redraft portions of the essay. I reviewed and revised the final text and take responsibility for its claims and conclusions.
