---
type: source
source_url: "https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship?hide_intro_popup=true"
canonical_url: "https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship"
resource: "https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship"
title: "Inside OpenAI: How Does ChatGPT Ship So Quickly?"
author: Gergely Orosz, interviewing Evan Morikawa
date: 2023-11-14
timestamp: 2023-11-14
created_at: 2023-11-14
topics: [management]
tags: [organizational-design, product-engineering, research-engineering, team-autonomy, shipping-velocity, openai]
description: Publicly accessible preview text for Gergely Orosz's interview with Evan Morikawa about the early ChatGPT team's engineering culture.
content_hash: 57dba85407f15bfbc9ff018a164729858bfcf06f097bcad8164b1dab7568268c
extracted_at: "2026-08-12T21:53:02"
extractor: Jina Reader public article preview
---

# Raw content

Source: https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship


Title: Inside OpenAI: How does ChatGPT Ship So Quickly?

URL Source: http://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship?hide_intro_popup=true

Published Time: 2023-11-14T15:44:07+00:00

Markdown Content:
_👋 Hi, this is Gergely with a subscriber-only issue of the Pragmatic Engineer Newsletter. In every issue, I cover challenges at Big Tech and startups through the lens of engineering managers and senior engineers._

OpenAI might be the hottest company in tech right now. The company is behind the popular large language-based model, [ChatGPT](https://openai.com/chatgpt), and also built the GPT-3, GPT-3.5 and GPT-4 models which several AI coding assistants use, such as GitHub Copilot. The CEO of the company is Sam Altman, formerly president of Y Combinator.

ChatGPT launched in November 2022, and took the world by storm. It’s safe to say this product provided applied AI with its biggest “wow” moment, and has been the catalyst for a surge in AI investment, industry-wide. ChatGPT has passed 100M _weekly_ active users, as [announced](https://techcrunch.com/2023/11/06/openais-chatgpt-now-has-100-million-weekly-active-users/) by CEO Sam Altman on 6 November. Hitting this milestone in less than a year from launch is unprecedented.

Since it arrived last year, it seems ChatGPT has been shipping at breakneck speed:

*   Nov 2022: public launch (on 30 November 2022, to be exact)

*   Dec 2022: performance updates and conversation history

*   Jan 2023: the ability to stop generating, and factuality updates (this is when ChatGPT crosses 100M monthly users)

*   February: ChatGPT Plus, internationally

*   March: GPT-4 in ChatGPT. Shipping plugins.

*   May: web browsing and plugins rolled out in beta. Shared links plugin, and export data.

*   June: a “browsing” feature.

*   July: custom instructions and code interpreter rolled out in beta

*   August: ChatGPT Enterprise. Prompt examples, upload multiple files and custom instructions.

*   September: new voice and image capabilities. Language support for 10 languages in alpha

*   October: files such as PDFs can be uploaded to work “chat” with them. Browsing is out of beta.

*   6 November 2023: a flurry of announcements on [OpenAI’s first Developer Day](https://openai.com/blog/new-models-and-developer-products-announced-at-devday), including an Assitants API, new models, a GPT models store, and [dozens more](https://techcrunch.com/2023/11/06/everything-announced-at-openais-first-developer-event/)._We briefly covered Developer Day last week, [in The Pulse](https://newsletter.pragmaticengineer.com/i/138735980/openai-is-shipping-at-breakneck-speed-and-wants-to-become-a-platform)._

**So, what is the engineering culture that allows the ChatGPT team to iterate this fast?**Well, nobody outside of OpenAI really knows, as the company has never discussed its software engineering practices – until now.

In this exclusive interview with [Evan Morikawa](https://twitter.com/e0m), who heads up about half of the 130-person Applied engineering team that builds ChatGPT, we find out how the hottest player in tech gets things done, and builds a winning product at the cutting edge of innovation. _You can [follow Evan on Twitter](https://twitter.com/e0m)._

We cover:

1.   An introduction to ChatGPT, the Applied team, and Evan

2.   Operating like an independent startup

3.   Tight integration with Research

4.   Long-term Product and Research thinking

5.   Uncoupled and incremental releases

6.   High talent density

7.   Day-to-day habits that add up

8.   The road ahead

_This article is an engineering culture deep dive. [Read other deep dives we’ve previously covered](https://newsletter.pragmaticengineer.com/t/engineering-culture-deepdive) with companies like Figma, Linear, Amazon, Meta or Sourcegraph._

_For a follow-up on OpenAI with Evan, see the article [Scaling ChatGPT: Five Real-World Engineering Challenges](https://newsletter.pragmaticengineer.com/p/scaling-chatgpt)._

_With that, it’s over to Evan. My questions are in italic:_

_Evan, can you introduce OpenAI and yourself?_

OpenAI is the maker of ChatGPT. Hopefully you've used ChatGPT to learn something new, help you write, or just chat with it for fun. ChatGPT is just one of OpenAI's products – OpenAI also shipped things like [DALL·E 3](https://openai.com/dall-e-3) (image generation), [GPT-4](https://openai.com/gpt-4) (an advanced model) and the [OpenAI API](https://openai.com/product) (which developers and companies use to integrate AI into their businesses.) ChatGPT and the API each expose several classes of models named GPT-3, GPT-3.5, and GPT-4.

The engineering, product, and design organization that makes and scales these products is called "Applied". OpenAI is [charted](https://openai.com/charter) with building safe AGI that is useful for all of humanity. Applied is charted with building products that really make AI useful for all of humanity. Research trains big models, then Applied builds products like ChatGPT and the API on those models. In practice, it's a more tightly integrated back and forth which I'll talk more about later.

The Applied team is a fairly new addition within the company. OpenAI was founded in 2015, and Applied began in the summer of 2020. We formed this team because we wanted to build and scale an API around GPT-3, which was a model we had just finished training, back then.”

_How did you come to head up a large part of OpenAI’s Applied team?_

I joined OpenAI in October 2020. Back then, OpenAI had about 150 staff in total, and the Applied team was a handful of people. At the time, nearly everyone working at OpenAI was a researcher. I do not have a PhD in Machine Learning and was excited by the realization that OpenAI was building APIs and engineering teams.

At OpenAI, I started out writing code as an individual contributor for the GPT-3 API. In January 2021, a few months into my tenure, I transitioned into managing our Applied Engineering team. Back then my team consisted of about 6 people. Today, two and a half years later, the Applied Engineering team has grown to 130 engineers, of whom I manage about half. The full Applied group consists of about 150 people; the other 20 folks are PMs and designers.

Since October 2020, OpenAI has grown from around 150 to roughly 700 people, today. And we [keep on hiring](https://openai.com/careers).

_How does OpenAI ship as quickly as it does? I feel like there’s a major new feature launched every couple of months. As an outsider, it’s hard enough just to keep up!_

On one hand, this has definitely been the [highest velocity place](https://twitter.com/E0M/status/1707135602863534505) in my career; but on the other hand, it's not magic. I think the key has been:

*   Setting up ChatGPT to operate like a small independent startup

*   Tight integration with research

*   Long-term product & research thinking

*   Uncoupled, incremental releases

*   High talent density

*   Day-to-day habits that all add up

_You mentioned how ChatGPT operates independently. What’s the setup?_

ChatGPT looks, feels, and acts like a one-year-old startup, but OpenAI itself is nearly 8 years old. The Applied group within OpenAI was founded 3 years ago. ChatGPT is a product team within Applied that started about 1 year ago.

[![Image 1: The Applied group and ChatGPT, within OpenAI](https://substackcdn.com/image/fetch/$s_!8RFb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82bb5533-5b36-40e6-a4ad-e2fa74bc95ec_1448x766.png)](https://substackcdn.com/image/fetch/$s_!8RFb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82bb5533-5b36-40e6-a4ad-e2fa74bc95ec_1448x766.png)

The Applied group and ChatGPT, within OpenAI

I and the rest of Applied leadership wanted the ChatGPT team to feel like they are their own, independent startup. In practice this goal involved a lot of changes which evolved as the team grew.

In the summer of 2022, we began development of what would become ChatGPT. At that time, Applied had about 30 engineers, a handful of PMs and designers, and was running products like:

*   APIs for GPT-3 and Codex

*   Fine-tuning of models

*   Embedding APIs

*   DALL·E 2

All these products used the same codebase, ran in the same cluster, and used the same build pipelines. Within Applied, we were structured functionally; engineering was one unified team.

This changed with ChatGPT.

A few applied engineers, some designers, researchers, and Greg Brockman (OpenAI's president and co-founder) grabbed a room and started rapidly iterating product ideas.

We gave this nascent group its own code repository and a fresh cluster. The dev environment looked like the first days of a startup or a personal project.

**Our goal with this small ChatGPT subteam was to create the atmosphere of an early-stage startup iterating towards product-market fit (PMF.)**We wanted to foster the rhythm, pace, and autonomy to do this. Every member of the team was on-site, and we rearranged seating to put people next to each other.

As the ChatGPT team grew, we made sure to keep it vertically integrated. This meant engineering, product, design, and key researchers always worked closely together. We codified that pattern further in May 2023 when [Peter Deng](https://www.linkedin.com/in/peterxdeng/) joined to lead ChatGPT engineering, product, and design, as one cohesive group.

We knew to set ChatGPT up this way because we’d created a similar structure when the Applied team started work on the first version of the OpenAI API. Three years ago, we also started with a handful of engineers on a fresh repo, fresh cluster, and greenfield development. We also operated like an early-stage startup searching for PMF, and found it with the API product.

**This “fractal startup” approach feels like a good model for any new product category.**I expect we’ll continue applying this pattern to rapidly iterate new ideas which we consider pursuing.

_How important is tight integration with Research, and why does it matter?_

In most tech companies, the “classic” trio of teams that engineering works with tends to be referenced as “EPD”:

*   Engineering

*   Product

*   Design

These teams tend to collaborate heavily with one another, and cross-functional teams usually have members of engineering, product, and design within them.

**Research being integrated into product teams has been critical.**Instead of the classic “EPD,” I like to think of our unit that collaborated heavily as “DERP”:

*   Design

*   Engineering

*   Research

*   Product

At OpenAI, many product questions are _actually_ research ones. For example, take these questions, that could be seen as feature requests:

*   How can ChatGPT produce more concise outputs?

*   How can ChatGPT produce more accurate answers?

*   How can ChatGPT connect to additional data sources?

While these questions might feel like product questions, in reality they’re heavily dependent on research. How can underlying models be tweaked or fine-tuned for the desired goals, what other approaches could we take to achieve these outcomes?

**Researchers integrating with product engineering wasn’t always a given.**At OpenAI, Research and Applied are separate org structures. Within the Research organization, there are a variety of different research teams, such as:

*   Pre Training team: this team trains the GPT-4 model

*   Post Training team: they fine-tune GPT-4

*   [Superalignment team](https://openai.com/blog/introducing-superalignment): aligns GPT-4

*   Multimodal team: makes GPT-4 see, hear, and speak

*   … and several others!

Researchers tend to have significant academic or industry backgrounds. They read a lot of academic papers to stay up to date. They also take ideas and run lots of experiments to improve our models. They are all hands-on; researchers do a _lot_ of engineering and write a _ton_ of code!

**We could have chosen the approach where models are “thrown over the wall” to Applied.**This setup would have meant that Research trains a model, and then hands it over – aka throws it over the wall – for Applied to productize. However, we actively wanted to avoid a culture where Research is only focused on running experiments and Product just wants to commercialize and make money.

To prevent this, product teams like ChatGPT have software engineers, designers, product managers, and researchers working together. In the case of ChatGPT, most researchers came from a research team we call Post Training. These researchers are the masters of the latest fine-tuning techniques and [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) (RL) methods like [Proximal Policy Optimization](https://openai.com/research/openai-baselines-ppo) (PPO.) Those techniques are necessary to continuously improve the underlying models in ChatGPT. Thanks to these researchers being part of the product group, and running their own A/B experiments, the feedback loop between research and engineering is very tight.

**Tight coupling with Research is why we ship new ideas so quickly.**How did we ship features like browsing, code execution, plugins, and other ChatGPT features as quickly as we did? It’s because of tight integration! All these started as research ideas, and were deployed into production quickly because the teams doing the research are tightly integrated with engineering! Furthermore, there's a culture of tinkering and prototyping in both research and applied. A lot of those prototypes very quickly found their way to prod.

_How does thinking long-term help with execution?_

OpenAI's mission is to ensure that artificial general intelligence (AGI) benefits all of humanity. By AGI, we mean highly autonomous systems that outperform humans at most economically valuable work. This mission is captured within the [OpenAI Charter](https://openai.com/charter) document. The Charter document reflects the strategy of OpenAI in more detail; for example, detailing the focus on long-term safety.

Our Charter and Mission are referenced at almost every all-hands. We've tactically used the phrase "which of these options feels like it's getting us closer to AGI" – referring to our Mission – in product discussions. It not only helps decide what to build, but I’ve seen plenty of decisions to not build things, as a result of focusing on the mission.

Clear focus is always a driver of velocity. I’m convinced our broad mission has helped keep that focus and also pave the way for lots of new ideas.

Another thing that has helped us is how we organize research initiatives:
