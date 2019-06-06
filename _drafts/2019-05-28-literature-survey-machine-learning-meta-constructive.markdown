---
layout: post
title:  "Literature survey: Meta-learning and architecture search"
date:   2019-05-28 10:34:00 +0930
categories: [Research]
tags: [Literature, Meta-Learning, Constructive Algorithms]
---

## Starting with a website search

A lot of the most recent research is published as pre-prints at arXiv: [https://arxiv.org/](https://arxiv.org/).
I haven't looked into the research on meta-learning for a while, so I start with a search at arXiv for "meta-learning".
At 10:40 (+09:30), 2019-05-28, the search for " meta-learning" (without quotes) gave 664 results.
The first few results didn't grab me, so I scroll down to result 7:

Embedded Meta-Learning: Toward more flexible deep-learning models  
Andrew K. Lampinen, James L. McClelland  
(Submitted on 23 May 2019)  
[https://arxiv.org/abs/1905.09950](https://arxiv.org/abs/1905.09950)

This title suggests the work might be relevant to what I've been studying and researching.

## The authors and abstract

The authors of the paper are both at the Stanford University Department of Psychology.
They have some additional publications on arXiv, but right now I'll focus on this one.
This paper, _Embedded Meta-Learning: Toward more flexible deep-learning models_, has the abstract:

> How can deep learning systems flexibly reuse their knowledge? Toward this goal, we propose a new class of challenges, and a class of architectures that can solve them. The challenges are meta-mappings, which involve systematically transforming task behaviors to adapt to new tasks zero-shot. We suggest that the key to achieving these challenges is representing the task being performed along with the computations used to perform it. We therefore draw inspiration from meta-learning and functional programming to propose a class of Embedded Meta-Learning (EML) architectures that represent both data and tasks in a shared latent space. EML architectures are applicable to any type of machine learning task, including supervised learning and reinforcement learning. We demonstrate the flexibility of these architectures by showing that they can perform meta-mappings, i.e. that they can exhibit zero-shot remapping of behavior to adapt to new tasks.

## The embedded meta-learning architecture

The authors provide a nice diagram representing what parts of their proposed system is handled by trainable deep neural networks:
  - An output encoder
  - A target encoder
  - An input encoder
  - A "hyper network"
  - A meta network
