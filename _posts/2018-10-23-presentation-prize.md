---
layout: post
title: Presentation Prize
date: 2018-10-23
---
A few weeks ago, I was lucky enough to attend [SAS2018](https://sas2018.anl.gov/) conference in Michigan, USA.
This will be the last large, international conference of my PhD, so I decided to go all out with abstracts for talks, submitting two (one in the machine learning and one in the education session).
In the end, I got both...

I think that my getting of both talks can be put down to the fact that one of my talks was focused on the teaching of an aspect of small angle scattering (and was the only such talk at the conference).
This is the talk that I am going to write about here.

The education talk was focused on [pylj](https://pythoninchemistry.org/pylj), the 2D molecular dynamics engine that I have developed (and [published](https://jose.theoj.org/papers/58daa1a1a564dc8e0f99ffcdae20eb1d)) over the past year.
In particular, I was aiming to introduce the ability for pylj to introduce the interaction between molecular dynamics simulation and scattering/diffraction.

The use of classical simulation has become very popular in the analysis of small angle scattering, *Figure 1* shows the increase in publications that mention both.
However, the nature of the education of classical simulation (it isn't a particularly straight forward concept), leads the development and use of software packages to link the two that are essentially **black boxes**.
pylj is a tool that can be used in a wide range of teaching environments to introduce classical simulation.

![popularity](https://arm61.github.io/talks/sas2018-1/figures/chem_data_py.png)
*Figure 1*

This was the premise of the talk - however as I am able to explain this in 3 sentences, it won't exactly make a great fifteen minute talk.
Indeed, once I have written the [talk](/talks/sas2018-1) I had only six minutes of content.

Perfect, I could use the rest of my time to **show** people how simple pylj was to use and hopefully teach them something along the way.
And, that is just what I did.
For the final two-thirds I wrote, live, a molecular dynamics algorithm using pylj, indentifying the important stages to understand in classical simulation.

In the end the talk went quite well (despite the fact the live-coding makes my hands shake uncontrollably); my colleagues complimented it and I *somehow* won the prize for [Best Student Lecture](https://sas2018.anl.gov/awards/iucr-journals-prize/) from the [IUCr](https://www.iucr.org/).

Thanks to the people that voted for me (let's not mention the fact that having two talks gave me two chances to win...)
