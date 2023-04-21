---
layout: post
title: Why you might be fitting Arrhenius data badly
date: 2023-04-21
upstream: /blog/
tags: 
    - analysis
    - chemistry
    - data
    - science
---

The [Arrhenius equation](https://en.wikipedia.org/wiki/Arrhenius_equation) describes the behaviour of rate constants, $$k_r$$, as a function of temperature, $$T$$, 

$$
k_r = A \exp{\bigg(\frac{-E_a}{RT}\bigg)},
$$

where $$E_a$$ is the activation energy, $$R$$ is the ideal gas constant, and $$A$$ is a pre-exponential scaling factor. 
The Arrhenius equation is used widely in the chemical sciences and features prominiently in early undergraduate courses and textbooks[^1]. 
The Arrhenius equation can be used to describe the relationship between measured rate constants as a function of temperature and therefore provide estimates of activation energy and pre-exponential factor (the Arrhenius parameters). 
However, despite being more than 130 years old, the Arrhenius equation is still used in a way that distorts the estimates of these parameters. 

In particular, the problem comes from the "linearisation" of the Arrhenius equation. 
This is where the exponential problem above is manipluated to give a linear problem with the form

$$
\ln{(k_r)} = -\frac{E_a}{R}\frac{1}{T} + \ln{(A)}.
$$

Such that by plotting the natural logarithm of the rate constant against the reciprocal temperature, we can fit a straight line with gradient $$-E_a/R$$ and intercept $$\ln{(A)}$$.
The convinent reformulation is great for use in the classroom, where drawing a straight line through points is much easier than fitting an exponential relationship. 
**But it should not be used in formal analysis in academic publications** (yet, it is regularly -- I won't shame anyone in particular though).

<center>
    <img src="/assets/img/arr1.png" width="100%"><br>
    <small>
        The effect of linearisation of the Arrhenius equation.<br>
    </small>
</center><br>

Before we dive into **why** using the linearised Arrhenius equation is so problematic for data analysis there are some important aspects of uncertainties and data modelling to consider. 

<blockquote class="var">
    1. Generally speaking, the uncertainty in the measurement of a rate constant will be normally distributed.
</blockquote>

Let's think about the rate constant for some reaction. 
For a given temperature the true rate constant is single valued, there is only one value that quantifies the rate and direction of our chemical reaction. 
However, when we measure the rate constant some (random and systematic) uncertainty is introduced.
Even with a perfect measurement device (where there is no systematic uncertainty), there will always random uncertainties which we cannot control. 
These random uncertainties sum in the measurement of our physical quantity, meaning that repeated measurements of our rate constant will result in a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) of values, centred on the true rate constant with some variance.

<center>
    <img src="/assets/img/arr2.png" width="100%"><br>
    <small>
        A normally distributed rate constant.<br>
    </small>
</center><br>

<blockquote class="var">
    2. (Weighted) least squares assumes a normally distributed uncertainty. 
</blockquote>

 


[^1]: For example, there is a section on it in Atkins' Physical Chemistry (pages 799-803 in the ninth edition).