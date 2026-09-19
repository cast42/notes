---
title: "Why fitting a logistic is nearly impossible from early data"
date: 2026-09-19
type: article
topics:
  - system_thinking
tags:
  - logistic-curves
  - growth-curves
  - forecasting
  - sensitivity-analysis
  - model-identification
resource: "https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/"
description: "John D. Cook derives why early-tail data makes the asymptote of a logistic growth curve numerically unstable and connects it to the practical difficulty of forecasting S-curves."
author: "John D. Cook"
source_url: "https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/"
canonical_url: "https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/"
sources:
  - id: cook-logistic-fit-sensitivity
    resource: "https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/"
  - id: crozier-x-post
    resource: "https://x.com/clcrozier/status/1251148890595708938"
---

# Why fitting a logistic is nearly impossible from early data

## TL;DR

An S-curve can look exponential for a long time, especially when observations all lie in one tail. In that regime, the eventual ceiling is weakly identified: tiny measurement errors can produce enormous changes in the fitted asymptote. Data spanning the inflection point is much more informative than simply collecting more observations from the early tail.

## Key takeaways

- A logistic curve has three parameters: its limiting value `L`, growth rate `k`, and midpoint `t0`.
- With three evenly spaced observations, the limiting value can be written as:

  `L = [y1²(y0 + y2) − 2 y0 y1 y2] / [y1² − y0 y2]`

- The sensitivity derivatives all contain `(y1² − y0 y2)²` in the denominator.
- For an exact exponential, `y1² = y0 y2`; a logistic tail is approximately exponential, so the denominator approaches zero in either tail.
- Therefore, a precise-looking logistic fit based only on early growth may have almost no predictive information about the eventual ceiling.

## The instability

Cook considers the logistic model:

`y(t) = L / (1 + exp(−k(t − t0)))`

For three equally spaced time points, the formula above estimates `L` independently of the spacing. But differentiating that estimate with respect to the observed values gives terms whose common denominator is `(y1² − y0 y2)²`. The closer the observations are to exponential behavior, the closer `y1² − y0 y2` is to zero and the larger the derivatives become.

This is an identification problem, not merely a problem of noisy arithmetic. Early-tail data does not contain enough curvature to distinguish among logistic curves with very different ceilings. More observations at the same stage can improve measurement of the local slope while leaving the long-run limit largely unconstrained.

## Practical forecasting lesson

The useful question is not only “How much data do we have?” but “Which part of the curve does the data cover?” Observations on both sides of the inflection point reveal the transition from acceleration to deceleration and constrain the limiting value. Observations confined to one tail should support humility about the ceiling and about any forecast of when saturation will arrive.

This complements Constance Crozier’s practical warning that **forecasting S-curves is hard**: following daily figures can create a strong feeling of insight while the underlying curve remains poorly identified. Her X post links to [“Forecasting S-curves is hard”](https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/).

## Related concepts

- [Growth: From Microorganisms to Megacities](2020-12-08_book_vaclav-smil_growth-from-microorganisms-to-megacities.md) — growth commonly follows S-curves that slow or stop; the forecasting problem is knowing where the system is on the curve.

## Sources

- John D. Cook, [“Why fitting a logistic is nearly impossible from early data”](https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/).
- Constance Crozier, [X post on why forecasting S-curves is hard](https://x.com/clcrozier/status/1251148890595708938), linking to [her accompanying article](https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/).
- [Raw source capture](raw/2026-09-19_article_why-fitting-a-logistic-curve-is-nearly-impossible-from-early-data.raw.md)
