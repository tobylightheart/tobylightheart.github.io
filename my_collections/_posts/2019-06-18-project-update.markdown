---
layout: post
title:  "Project Updates 2019-06-17"
date:   2019-06-18 17:32:00 +0930
categories: [Updates]
tags: [Data Collaboration, AUSRT, Constructive Algorithms]
---

## Week Summary

I have been writing weekly project updates over at my WordPress website for a few weeks now.
The content of these updates has become quite technical (engineering and machine learning), so I'm migrating that content over to this website.
I've done some restructuring of this website, and there may be more to do in future.
I don't suspect anyone has been linking to these pages, but I apologise if you have been affected.

I did some further work on the Adelaide University Solar Race Team software set up.
I added data logging to the start-up scripts; however, another python script was used to translate the logged data into CSV files.
There are still some visualisations to add to the GUI, but rather than learn how to do this in a JavaScript, I'm going to experiment with redeveloping the graphical user interface using PyQt.
I've made a start on this.
If this runs into too much trouble, I will come back to the current GUI.

I have written some constructive algorithm code for a NumPy-based neural network using Michael Nielsen's Neural Networks and Deep Learning code (updated for Python 3.5 by Michal Dobrzanski): https://github.com/MichalDanielDobrzanski/DeepLearningPython35.
This experimental code is about to ready for some testing.

I finished reinstalling Ubuntu on my desktop and I have CUDA and PyTorch running.
I have installed Minecraft and I'm ready to try setting up Malmo.
Once I have this working I may try registering for the MineRL competition.
I've had a better look at the NeurIPS competition track challenges this year, and there are a number that look interesting.
Depending on how things go, I might aim to make minimal working entries for a few of them for some extra study and practice.

I didn't make progress on the conference papers last week, but I had a conversation with my PhD supervisor and the possibility of conducting experiments with a rotating inverted pendulum machine was raised.
This could be a good option.
I'll try to catch up some work on these papers this week.


## Short-Term Tasks List

- AI Collaborative Network - Data Collaboration
  - Review and suggest questions for NfP meeting. **[Aim: 2019-06-19, Wednesday]**
- Adelaide University Solar Race Team
  - Data logging with separate rosbag to CSV conversion **[Complete]**
  - Recreate GUI and data visualisation using PyQt **[Aim: 2019-06-21, Friday]**
  - Add interface for projected battery charge and usage.
  - Create plan for code development and unit and integration tests.
- Literature and Study
  - Review literature on meta-learning and constructive neural networks. **[Due weekly: Wednesday]**
- Constructive Neural Networks
  - Test Dynamic Node Creation algorithm using NumPy. **[Aim: 2019-06-19, Wednesday]**
  - Add automatic neuron construction from error detection in PyTorch Blitz code. **[Aim: 2019-06-26, Wednesday]**
- Selective Neural Networks
  - Theory development: network structures to perform neuron selection rather than detection.
  - PyTorch methods for implementing neuron or module selection.
- Conference paper: Reinforcement learning with neural network construction for visual control
  - Literature survey
  - Theory development plan
  - Code development plan
  - Submission **[Deadline: 2019-09-23]**
- Conference paper: Self-supervised motion control learning with reinforcement-based target selection
  - Literature survey
  - Theory development plan
  - Code development plan
  - Submission **[Deadline: 2019-09-23]**
- NeurIPS competitions (https://nips.cc/Conferences/2019/CallForCompetitions)
  - Desktop OS installation **[Complete]**
  - Install and test Malmo (https://www.aicrowd.com/challenges/neurips-2019-minerl-competition) **[Aim: 2019-06-19, Wednesday]**
  - Register for MineRL Competition
  - MineRL first round submissions close **[2019-09-22]**
