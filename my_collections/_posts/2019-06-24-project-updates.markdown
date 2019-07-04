---
layout: post
title:  "Project Updates 2019-06-24"
date:   2019-06-24 12:00:00 +0930
categories: [Updates]
tags: [Data Collaboration, AUSRT, Constructive Algorithms]
---

## Progress Summary

Last week I had some trouble with storage and backup drives, which was a diversion from working on other projects.
I don't think I've lost any data, but I am going to spend some more time in the coming weeks ensuring that my important data is backed up.

I also allowed myself to be diverted looking into the recent microcontroller development boards.
In looking into these development boards, I also revisited getting a small drone, which can use the same microcontrollers.
The TurtleBot3 (Burger or Waffle) comes with the OpenCR board, which has a 32-bit ARM Cortex-M7 with FPU.
The OpenCR board is too heavy for small UAVs, but would still be fun to play with.
I may put together a post outlining some options and thoughts for buying a standalone development board, a drone kit, or TurtleBot3.

The AI Collaborative Network Data Collaboration is putting together some questions for a meeting with a Not-for-Profit organisation in a couple of weeks.
I'll try to check on this document and make some suggestions again this week.

I made some progress on recreating the GUI for the Adelaide University Solar Race Team using Qt Designer.
I'd like to try to get the GUI skeleton finished and make a start on getting the charts displaying simulated data.

I'm going to testing the constructive algorithm code I've written for a NumPy-based neural network using the MNIST dataset.
This should be possible make progress this week.

I need to make more progress on my proposed conference papers.
This means: 1) revisiting the literature survey, 2) writing an outline of the code development plan, 3) developing the theory and learning algorithms, and 4) implementation and testing.
I'll try to focus on completing 1 and 2 this week.

There may be some crossover in the algorithms and code I develop for the conference papers and the development of something for the MineRL competition.
At this stage, it is hard to decide what to prioritise, so I will try finish setting up Malmo and doing some preliminary tests this week.
I'll see what progress I make on the MineRL task before registering and exploring other NeurIPS competitions in more detail.

My projects related to learning techniques for people and other topics of writing will be discussed on my Wordpress site ([https://tobylightheart.wordpress.com](https://tobylightheart.wordpress.com)) on Tuesday.


## Updated Project and Task List

- AI Collaborative Network - Data Collaboration
  - Review and suggest questions for NfP meeting. **[Aim: 2019-06-25, Tuesday]**
- Adelaide University Solar Race Team
  - Create GUI skeleton in Qt Designer **[Aim: 2019-06-24, Monday]**
  - Add plots from simulated telemetry **[Aim: 2019-06-26, Wednesday]**
  - Add interface for projected battery charge and usage.
  - Create plan for code development and unit and integration tests.
- Literature and Study
  - Review literature on meta-learning and constructive neural networks. **[Due weekly: Wednesday]**
- Constructive Neural Networks
  - Test Dynamic Node Creation algorithm using NumPy. **[Aim: 2019-06-24, Monday]**
  - Add automatic neuron construction from error detection to PyTorch Blitz code. **[Aim: 2019-06-26, Thursday]**
- Selective Neural Networks
  - Theory development: network structures to perform neuron selection rather than detection.
  - PyTorch methods for implementing neuron or module selection.
- Conference paper: Reinforcement learning with neural network construction for visual control
  - Literature survey **[Aim: 2019-06-26, Wednesday]**
  - Theory development plan
  - Code development plan
  - Submission **[Deadline: 2019-09-23]**
- Conference paper: Self-supervised motion control learning with reinforcement-based target selection
  - Literature survey **[Aim: 2019-06-26, Wednesday]**
  - Theory development plan
  - Code development plan
  - Submission **[Deadline: 2019-09-23]**
- NeurIPS competitions (https://nips.cc/Conferences/2019/CallForCompetitions)
  - Install and test Malmo (https://www.aicrowd.com/challenges/neurips-2019-minerl-competition) **[Aim: 2019-06-27, Thursday]**
  - Register for MineRL Competition
  - MineRL first round submissions close **[2019-09-22]**


## Tasks This Week

1. Create GUI skeleton in Qt Designer **[Aim: 2019-06-24, Monday]**
2. Test Dynamic Node Creation algorithm using NumPy. **[Aim: 2019-06-24, Monday]**
3. Review and suggest questions for NfP meeting. **[Aim: 2019-06-25, Tuesday]**
4. Add plots from simulated telemetry **[Aim: 2019-06-26, Wednesday]**
5. Review literature on constructive neural networks and reinforcement learning. **[Due: 2019-06-26, Wednesday]**
    1. Conference paper: Reinforcement learning with neural network construction for visual control
    2. Conference paper: Self-supervised motion control learning with reinforcement-based target selection
6. Install and test Malmo (https://www.aicrowd.com/challenges/neurips-2019-minerl-competition) **[Aim: 2019-06-27, Thursday]**
