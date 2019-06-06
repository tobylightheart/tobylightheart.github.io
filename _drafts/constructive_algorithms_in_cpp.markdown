---
layout: post
title:  "Implementing constructive neural networks and neuron selection"
date:   2019-05-28 10:34:00 +0930
categories: [Research]
tags: [Constructive Algorithms]
---

## Computer memory: Neurons, connections and activity

Many modern neural network libraries represent neurons implicitly: an array stores the neuron activations, with array locations indicating which neuron has what activity.
Connection weights are organised in a similar array to line-up with this array of activities to indicate which neurons transmit to the next layer of neurons.
Arranging the activations and weights into multidimensional arrays also facilitates the use of parallel processing.

Pros of collected arrays:
- Does not require neuron explicit neuron addresses (memory efficient)
- Suitable for parallel processing

Cons of collected arrays:
- Changing array size is inefficient
- Additional apparatus required for neuron selection

Are there alternatives?

An alternative is to represent neurons explicitly in memory, giving each neuron an address.
This could be expected to increase the required memory if connections now need to indicate a neuron address as well a weight.
Having neurons stored individually and distributed across memory does not facilitate parallel computation.

Pros of individual representation:
- The number of neurons can be changed more efficiently
- Neuron selection can be performed with addresses

Cons of individual representation:
- The representation is memory inefficient
- Parallel processing may require substantial restructuring

Modern libraries for implementing artificial neural networks assume that the size of the network remains constant after initialisation.
Creating neural network classes that accommodate changing numbers of neurons is an important first step in creating constructive neural networks.
I'm aiming to create a set of neurons in memory that can increase in size.
This set of neurons will be selectively chosen for calculations.



Consider having a simulated/working set and swapping neuron weights in and out.




There is a range of possibilities for storing the network parameters.
It is common practice for neurons to be organised in layers and the parameters for each layer to be collected into a set of arrays.
Starting with this approach:
- A layer could be expanded be being re-instantiated as a larger size and the old parameters copied in.
- Another parallel layer could be created; the adjacent layers need their output or input parameters to be expanded as well.

## Selective neuron activity calculation

Modern neural network libraries usually have all neuron activations calculated for each input sample.
In the case of convolutional neural networks, there can be many calculations that return an approximately zero result.
An alternative that I have discussed on this blog is a selective approach to choosing neurons to calculate activations.

What might the process of selection entail?

First, some neurons need to be chosen as active, or calculated to be active using the standard "detection" approach (e.g., a convolutional filter).
These neurons (or convolutional filters) must be associated with a set or selection of neurons.
These neurons could be automatically deemed to be active or have their activations calculated taking the activity of other nearby filters.

How would this be represented in memory?

Assuming we are doing image processing.
We might start with a pass of a very simple convolutional filter to detect what parts of the image should be the focus of further processing.
These activation mark a location for further features/filters to be tested.
We still need the same number of weight parameters for the same number of neurons/convolutional filters, and these could be organised in the same way.

There is potentially a big difference in how layer activations are calculated.
Rather than calculate an activation for all filters at all input locations, we calculate the activation at one location through the full depth at a time.

If we have later layers in separate modules, can we train the early part of the network to predict which later module we need to select for the next part of the detection?
