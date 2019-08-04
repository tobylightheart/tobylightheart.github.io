---
layout: post
title:  "[Update] AUSRT GUI; MNIST Data for Constructive Algorithms; Conferences and Competitions"
date:   2019-07-03 12:07:00 +0930
categories: [Updates]
tags: [Data Collaboration, AUSRT, Constructive Algorithms]
---

## Summary

There isn't much to report from last week.
I have received a new hard drive for creating local data backups; I'll be spending some time setting backups this week.

I'm ready to start working on importing some charts to a new GUI for the Adelaide University Solar Race Team.
The next steps are: 1) getting the GUI to display plots, 2) getting the plots to animate/update, 3) getting simulated data from ROS to the GUI, and 4) displaying the simulated data in the GUI.
If I get this working soon, I'll have a go at replacing the telemetry communication and logging in ROS with Python libraries.  

Testing my constructive algorithm code stalled momentarily while I was modifying scripts for downloading and unzipping the MNIST data set.
Now I'm working through some errors in the training and dynamic node creation.

Last week I listed conference paper tasks: 1) revisiting the literature survey, 2) writing an outline of the code development plan, 3) developing the theory and learning algorithms, and 4) implementation and testing.
I still have more work to do on the literature survey and algorithm outlines for my proposed conference papers.
I'm now aiming to get these near completion this week.

I still have some more work to do to finish setting up Malmo on my desktop.
I'll pencil this in for some more attention this week too.

I might also have some more work on the robot arm art display coming in the next week or two.

See my Wordpress site ([https://tobylightheart.wordpress.com](https://tobylightheart.wordpress.com)) for updates on my work on learning techniques for people and other topics of writing.


## Updated Project and Task List

- AI Collaborative Network - Data Collaboration
  - NfP meeting (unable to attend). **[2019-07-09, Tuesday]**
- Adelaide University Solar Race Team
  - Create GUI skeleton in Qt Designer. **[Complete]**
  - Add plots to GUI. **[Aim: 2019-07-04, Thursday]**
  - Display simulated telemetry.
  - Add plots of projected battery charge and usage.
  - Create plan for code development and unit and integration tests.
- Literature and Study
  - Review literature on meta-learning and constructive neural networks. **[Due weekly: Wednesday]**
- Constructive Neural Networks
  - Test Dynamic Node Creation algorithm using NumPy. **[Aim: 2019-07-04, Thursday]**
  - Add automatic neuron construction from error detection to PyTorch Blitz code.
- Selective Neural Networks
  - Theory development: network structures to perform neuron selection rather than detection.
  - PyTorch methods for implementing neuron or module selection.
- Conference paper: Reinforcement learning with neural network construction for visual control
  - Initial literature survey **[Aim: 2019-07-03, Wednesday]**
  - Theory development plan
  - Code development plan
  - Submission **[Deadline: 2019-09-23]**
- Conference paper: Self-supervised motion control learning with reinforcement-based target selection
  - Initial literature survey **[Aim: 2019-07-03, Wednesday]**
  - Theory development plan
  - Code development plan
  - Submission **[Deadline: 2019-09-23]**
- NeurIPS competitions (https://nips.cc/Conferences/2019/CallForCompetitions)
  - Install and test Malmo (https://www.aicrowd.com/challenges/neurips-2019-minerl-competition) **[Aim: 2019-06-03, Wednesday]**
  - Register for MineRL Competition
  - MineRL first round submissions close **[2019-09-22]**


## Tasks This Week

1. Survey recent literature on constructive neural networks and reinforcement learning for physics simulations/robotics. **[Due: 2019-07-03, Wednesday]**  
    1. Conference paper: Reinforcement learning with neural network construction for visual control
    2. Conference paper: Self-supervised motion control learning with reinforcement-based target selection
2. Install and test Malmo **[Aim: 2019-07-03, Wednesday]**
3. Test/Debug Dynamic Node Creation code (NumPy). **[Aim: 2019-07-04, Thursday]**
4. Adelaide University Solar Race Team  
    1. Add plots to new AUSRT GUI. **[Aim: 2019-07-04, Thursday]**
    2. Add plots from simulated telemetry **[Aim: 2019-07-04, Thursday]**
