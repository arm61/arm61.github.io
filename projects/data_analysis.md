---
layout: project
title: "Experimental Analysis"
description: "Harnessing data science to analyse experiments"
header-img: "img/banner.png"
category: analysis
posts: false
---

The analysis of experimental data is fundamental to the physical and chemical sciences. 
However, data analysis is rarely a trivial task, frequently being the most time-intensive part of a research project. 
The use of data science methods, such as Bayesian inference and machine learning, has the ability to increase experimental throughput, improve analytical reproducibility, enable greater integration of theory, and possibly a allow for more complete understanding of the experimental technique.

Currently this work is being applied to the technique of X-ray and neutron reflectometry; which is a technique to probe the nanoscale structure of an interface. 
These measurements are typically conducted at large scale facilities, such as Diamond Light Source ([Beamline I07](https://www.diamond.ac.uk/Instruments/Structures-and-Surfaces/I07.html)) or [ISIS Neutron and Muon Source](https://www.isis.stfc.ac.uk/Pages/Reflectometry.aspx).
This application involves using Bayesian inference and model selection to improve automation of analysis, allowing users to *hopefully* complete their beamtime with analysed data. 
This work is a collaborative effort between Diamond Light Source, ISIS Neutron and Muon Source, and the University of Oxford.

<center><img src="/img/reflectometry.png" width="80%"></center>

Alongside this work, we are investigating the use of convolutional neural networks to classify reflectometry profiles into given analytical model types. 
The belief is that this will allow for a suggested analytical model to be used, in effect automating the role of the data analysis as a service.
This work is being conducted in collaboration with ISIS Neutron and Muon Source and the SciML group of STFC. 

If you are using the large scale facilities and are interested in collaborating to make use of this "data analysis as a service"-like system, please [get in touch](mailto:andrew.mccluskey@diamond.ac.uk).

In addition to applying these methods in reflectometry, I am also working closely with researchers at the University of Bath to develop statistically informed methods for the quantification of diffusion in battery materials. 
This work involves the application of statistical techniques to accurately quantify the uncertainty in a given computational simulation. 