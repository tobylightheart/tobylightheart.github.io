---
layout: post
title:  "Incremental Logging of Research Developments and Results"
date:   2018-10-01 20:49:10 +0930
categories: [Research]
tags: [Research Topics, Research Tools, Workflow, Updates]
---
## Previous Research

My PhD study focused on constructive algorithms for spiking neural networks.
These algorithms produced some surprising results and have a lot of room for further development and experimenting with applications.
A more theoretical contribution of my thesis was related to interpreting artificial neural networks as existing within a larger neural system.
Although my research has previously focused on the construction of neurons, I think there could be value in having algorithms that predict and select neurons to simulate from a large neural network in memory.

## Current Research Topics

1. Experiment with applications and refinements of the constructive spiking neural networks that creates neurons with estimates of neuroplasticity convergence.
2. Develop theory and experiments to explore algorithms for the construction of neurons in memory and the subsequent selection of neurons in memory to simulate.

## Research Tools

I have been using Jupyter Notebooks recently to reproduce some of my PhD research on constructing neurons with estimates of STDP convergence (<https://github.com/tobylightheart/csnn-stdp>).
This has been a useful learning exercise, but I have come across the suggestion to produce code in a more reusable library-style format.
I have installed Atom and GitHub on my current work laptop and will use these for some more code development.
Atom has markdown editing and integration for commits to GitHub repositories, which will make adding to this website quick and easy.

## Other Updates

### LynxMotion ALD5 Robot Arms

I have had a few rounds of work programming the LynxMotion robot arms for an art display.
A generalised version of this code has been made available through GitHub (<https://github.com/tobylightheart/LynxMotion-Sequences>).
There may be another round or two of work on this, and the arms will need some ongoing maintenance.
Hopefully, I can pass on most of the necessary information to capable people at the venue.

### Neuron Construction using STDP Convergence

I have completed and uploaded a Jupyter Notebook that demonstrates the simulation of competitive spike-pattern detection using STDP and lateral inhibition and that neuron construction using a prediction of STDP convergence produces one-shot detection of the same repeating hidden pattern.
This doesn't show all of the results of the pre-print paper that I have uploaded to arXiv.
I will try to share the remaining Matlab code and upload simulation results to figshare to make them openly available soon.
