---
title: "Raw capture: fitting a logistic curve from early data"
date: 2026-09-19
type: source
topics:
  - system_thinking
tags:
  - logistic-curves
  - growth-curves
  - forecasting
resource: "https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/"
description: "Source capture of John D. Cook's logistic-fit sensitivity article and Constance Crozier's referenced X post."
sources:
  - id: cook-logistic-fit-sensitivity
    resource: "https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/"
  - id: crozier-x-post
    resource: "https://x.com/clcrozier/status/1251148890595708938"
---

# Raw source capture

## John D. Cook — “Why fitting a logistic is nearly impossible from early data”

- Source: https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/
- Retrieved through Jina Reader: https://r.jina.ai/http://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/
- Published time reported by the extractor: 2026-09-19T01:17:36+00:00

Nothing grows exponentially forever. What appears to be an exponential curve often turns out to be some sort of S curve, such as a logistic curve.

Suppose you’re collecting data on the left side of the curve. If there’s even a small amount of error in your data, you won’t be able to predict the asymptotic value with any accuracy. But if you have data on both sides of the inflection point, you can make a good prediction of the limiting value.

I’ve written about this [before](https://www.johndcook.com/blog/2025/12/20/fit-logistic-curve/), explaining that the problem is hard, but I didn’t say why it’s hard. Here I’d like to give an idea why it’s hard.

Suppose you want to fit a logistic equation

`y(t) = L / (1 + exp(-k(t - t0)))`

to three distinct values of `t` and the corresponding values of `y`. There is a unique solution, but in general you cannot find a solution in closed form. However, if the values of `t` are evenly spaced, there is a method [1] to solve for the parameters `L`, `k`, and `t0`. For this post we’re only interested in the limiting value `L`, and it can be found by

`L = [y1²(y0 + y2) - 2y0y1y2] / [y1² - y0y2]`

independent of the spacing `h`.

To find out how small changes in the `y's` change the estimate of `L`, we take the partial derivatives of `L` with respect to the `y's` and find:

`∂L/∂y0 = ∂L/∂y2 = y1² h² / (y1² - y0y2)²`

and

`∂L/∂y1 = -2 y0y2 h² / (y1² - y0y2)²`

All three derivatives have the same expression in the denominator: `y1² - y0y2`.

If the function `y(t)` were an exponential, this expression would be exactly zero [2]. The function `y(t)` is not exactly exponential, but it is approximately exponential when the `t`s are in the left or right tail of the logistic curve. The further out in either tail the `t`s are, the closer the expression is to zero.

So when all the `t`s come from the same side of the inflection point, `y(t)` is nearly exponential, the partial derivatives are huge, and the fitted value of `L` is extremely sensitive to changes in the `y's`.

### References in the article

[1] Raymond Pearl and Lowell J. Reed. [“On the Rate of Growth of the Population of the United States Since 1790 and its Mathematical Representation”](https://doi.org/10.1073/pnas.6.6.275). *Proceedings of the National Academy of Sciences of the United States of America*, Vol. 6, No. 6 (June 15, 1920), pp. 275–288.

[2] `exp(x + h)² = exp(x)² exp(h)² = exp(x) exp(x + 2h)`

### Article images

- https://www.johndcook.com/logistic_tangents.png
- https://www.johndcook.com/logistic_fit1.svg
- https://www.johndcook.com/logistic_fit2.svg
- https://www.johndcook.com/logistic_fit3.svg
- https://www.johndcook.com/logistic_fit4.svg
- https://www.johndcook.com/logistic_fit5.svg

## Constance Crozier — X post

- Source: https://x.com/clcrozier/status/1251148890595708938
- Author: Constance Crozier (@clcrozier)
- Published: 2020-04-17T14:01:55Z
- Linked article: https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/

> I spent a humiliating amount of time learning how to make animated graphs, just to illustrate a fairly obvious point.
>
> “Forecasting s-curves is hard”
>
> My views on why carefully following daily figures is unlikely to provide insight.
>
> https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/

The post included a 43.328-second, 900×600 video illustrating the point:

- Video: https://video.twimg.com/ext_tw_video/1251148822958338052/pu/vid/900x600/Lk8ddi4il_rAkXb3.mp4?tag=10
- Thumbnail: https://pbs.twimg.com/ext_tw_video_thumb/1251148822958338052/pu/img/YDK0Zq0dfZ6WqfPf.jpg

The Crozier article was retained as a linked reference from the post; this capture records the post text rather than claiming an independent retrieval of that page.
