---
layout: post
title: Jupyter Notebooks in Tutorials
date: 2017-10-28
category: teaching
---

At bath, there has been a push for chemistry undergraduate students to get an introduction to programming at an early stage -- indeed there has been a push to this in many chemistry undergraduate course.
As a result we now have a computation lab exercise that involves the students gaining an introduction to Python coding, in a Jupyter notebook interface, in the first year and an advancement of this in second year.

As a result of this I am trying something new out in my first year tutorials.
Where I use a Python notebook to help the students with the visualisation of the mathematical aspects of the tutorial, such as plotting.
I am going to keep a bit of a diary as to how this is going.
All the notebooks are going in this [GitHub repo](https://github.com/bjmorgan/python_in_chemistry/tree/master/First_Year_Tutorials/).

So the first tutorial was yesterday, I was pretty exhausted having come off of a week long beamtime at Diamond.
This tutorial involved introducing them to the fact that I would be using the Jupyter notebooks to help with the mathematical stuff.
The tutorial had seven questions, only four of which had aspects that the notebook could be used for, and of these only one of which the students seemed to struggle with enough to desire it to be covered.

This was question 7 which was set to give the students an idea of the way that university level questions are set out and how they differ from those in school.
The aim was to use density and pressure data to calculate the molecular mass of a species.
The notebook was used for the plotting of the data and the calculation of the line of best fit.
The question was set up such that including all of the data points gave an incorrect answer due to a deviation from the ideal gas law.
Instead only the first point and the requirement that the line must pass through the origin should be used.
I felt that the students were able to engage will with the use of the notebook to draw the plots, even if the practicalities of the coding was lost on them.
The nice aspect of the notebook was it was possible to show the gradual deviation from the correct molecular mass that happened as the number of data-points included in the analysis was increase (and actually as a group we discovered that the best fit to the correct number is obtained when the first two data-points and the requirement to pass through the origin were used).

Anyway that is just my first thought on using the notebooks, I sent the students a pdf of the notebook and told them if they where interested in finding out more about Python coding I would be happy to help out.
The notebook provided a really nice way of quickly visualising the data in the final question.
Disappointingly I wasn't able to talk through the loops that are present in the notebooks...maybe next time.
