---
layout: post
title:  "First Steps in Developing Selective Neural Networks"
date:   2018-11-12 15:50:30 +1030
categories: [Research]
tags: [Selective Neural Networks, Research, Theory]
---

# Neurons as Detectors and Selectors

A standard view of the function of neurons in an artificial neural networks is as feature detectors.
The neuron has input weights tuned to a particular feature (pattern of input activity) and the activation of the neuron is a representation of the presence of that feature.
Activities are calculated for each neuron for every input sample to determine what features are present.

An alternative perspective of the function of neurons is as selectors.
Rather than focusing on the neuron inputs, an alternative perspective is to focus on the neuron outputs: what does the neuron select.
An active neuron has connections (with high weight) that target other neurons for activation.
It may be possible to selectively calculate the activation of neurons and reduce the number of calculations required, particularly in neural networks that have sparse connections and low activity

<p align="center">
<img alt="Feature detection focuses on neuron input connections; neuron selection focuses on neuron output connections." src="/assets/network_detection_selection.svg"> <br />
<small>Feature detection focuses on neuron input connections; neuron selection focuses on neuron output connections.</small>
</p>


## Preliminary Theory

A standard model of a neuron $i$ that has input connections from neurons $j \in J$ with weights $w_{i,j}$.
The neuron $j \in J$ produces an input value, $x_{j}$, and the neuron $i$ also receives a trainable bias $b_{i}$.
The output $y_{i}$ of neuron $i$ is calculated using an activation function
<p align="center">
 $$\displaystyle y_{i}=f(b_{i} + \sum_{j \in J} w_{i,j} \cdot x_{j}).$$
 </p>
A high value of $y_{i}$  provides an indication of that the related feature is detected.
Each layer of neurons detects the activity neurons (the detection of features) in the previous layer.

<p align="center">
<img alt ="Standard model of a neuron with input connections." src="/assets/neuron_detector.svg"> <br />
<small>Standard model of a neuron with input connections.</small>
 </p>

Convolutional neural networks are a common approach to detecting features in images.
When applied to images, the weights of a neuron cover a small 2D patch of the image at a time.
This patch is shifted over the entire image with activation values at each location indicating the presence of the feature.
In the example below, the output of neuron $i$ is a result of a $3 \times 3$ patch of neurons,
<p align="center">
$$\displaystyle y_{i,j,k} = f(b_{i} + \sum_{a,b \in \{0,1,2\}} w_{i,j+a,k+b} \cdot x_{j+a,k+b}).$$ <br />
<img src="/assets/neuron_detect_convolution.svg" alt="Example of a neuron acting as a 2D feature detector."> <br />
<small>Example of a neuron acting as a 2D feature detector.</small>
 </p>

Neural networks may have many connections with low or zero weight and many neurons with low or zero activity.
Studies of neural network compression suggest that these connections can be ignored with little cost to the performance and large savings in the memory and computational expense of the neural network.


## Equivalent Algorithms for Calculating Neuron Output

The summation of inputs to the neurons, $i \in I$, can be presented as an algorithm:
1. **Given** $a_{I}, w_{I,J}, x_{J}$
2. **For each** neuron $i \in I$
3. &nbsp; **For each** neuron $j \in J$
3. &nbsp; &nbsp; $a_{i} \gets a_{i} + w_{i,j} \cdot x_{j}$
4. &nbsp; $y_{i} \gets f(a_{i})$

This algorithm can be rearranged to process the outputs of each neuron $j \in J$:
1. **Given** $a_{I}, w_{I, J}, x_{J}$
2. **For each** neuron $j \in J$
2. &nbsp; **For each** neuron $i \in I$
3. &nbsp; &nbsp; $a_{i} \gets a_{i} + w_{i,j} \cdot x_{j}$
4. &nbsp; $y_{i} \gets f(a_{i})$

The purpose of these algorithms is to find the outputs, $y_{i}$, of the neurons.
The end result of either of these algorithms is the same for the same given inputs and function $f(\cdot)$.

An aim of the work being described in this post is to reduce the amount of computation required to operate the neural networks that are not fully connected.
If input neurons are not connected to the full set of output neurons or there are connection weights that are approximately zero, then those connections can be skipped in calculations.
Networks may also have lots of neurons with low or zero output that may also be skipped in calculations with minimal effect on the overall network results.


## Representing Sparse Networks and Selective Neuron Activation

Alternative approaches to representing sparse neurons for neuron selection may be explored.
One approach to neuron selection is to store lists of neurons that the neurons selects.
An active neuron selects its associated list of neurons, those neurons become active and select their lists of neurons and so on.

This approach to neuron selection can be binary: a neuron is either selected or not selected for activation.
This is effectively an unweighted [directed graph](https://en.wikipedia.org/wiki/Directed_graph).
An extension could be to require neurons to be selected above a threshold number of times to become activated.
Neurons could be ranked by the number of times they are selected and processed in that order of rank.
Selection can also be performed with weighted connections to produce graded selection or activation of neurons.

Neuron activations could be calculated layer-by-layer (breadth first) or calculated to produce early predictions and updates on the deepest neuron activities (depth first).
If we are interested in reducing the number of calculations, the calculations of neuron output may only be performed for neurons that meet some criteria (for example, a threshold).
A neuron that only produces output under limited circumstances has parallels with the spiking activity of biological neurons.


## A Process for Sparse Neuron Selection

In sparsely connected networks, neurons only select a subset of the neurons in the network (or next layer).
When a neuron activates, the neurons that it selects should receive the weight of the now active connections to those neurons.
As we add the weights to neuron activation levels, we can decide which neuron to process next by ranking them by activation.

A high-level specification of the operation of a selective algorithm could be:

1. **Given** List of active (input) neurons, $A$
2. Find the neuron, $j \in A$, with the greatest activation level
3. Add connection weights, $w_{i,j}$, from $j$ to the set of neurons it connects to, $i \in I_{j}$
4. Add neurons $i \in I_{j}$ with activation above threshold to $A$
5. Reset the activation of neuron $j$
6. Repeat from 2.

Spiking neuron models often have a gradual drift or leak towards an equilibrium value of activation.
This can be modelled as an exponential decay in the activation potential.
This leak term adds computational expense to the operation that may be unnecessary if the network can adequately handle the occasional spontaneous activation of unrelated neurons.

Some approaches to training neural networks can result in sparse or bimodal connection weights and sparse neuron activity; therefore, it may be possible to develop processes for selectively calculating neuron activations and not have a significant reduction in performance.
This may be useful for reducing the expense of operating trained neural networks, although may not be any more effective than current compression techniques.

There is also an interest in reducing the cost of training the neural networks.


## Training Selective Neural Networks

A strength of artificial neural networks is that they can be trained with algorithms to perform tasks.
For a supervised learning task, inputs sample are paired with desired output values, and some set of neurons are specified as outputs.
Training algorithms for artificial neural networks typically make small adjustments to the weights over numerous iterations.

Stochastic gradient descent is a standard training method (a range of variants and extensions exist).
A mini-batch of samples is processed and the error of the network predictions are found.
The gradient, $\nabla$, of the error, $E_{d}$, for mini-batch $d$ is calculated with  respect to each connection weight and the weights are changed a small step according to the learning rate $\eta$ to reduce the error,
<p align="center"> $$\displaystyle w_{i,j} \gets w_{i,j} - \eta \nabla E_{d}(w_{i,j}).$$ </p>

A standard (non-selective) neural network will calculate the activation levels of all neurons in a forward pass to make an output prediction.
If the outputs use a one-hot encoding, the output neuron with the highest activation level will indicate the predicted output.
Updates are calculated for all connection weights and applied after processing a batch of input samples.  

Developing learning algorithms for selective neural networks could be an important step to produce applications in machine learning tasks.
Implementing stochastic gradient descent with selective neuron activation (that is, only updating active neurons) may add an additional degree of stochasticity to training updates.
This and similar training rules for adjusting connection weights can be tested for supervised learning and unsupervised learning.


## Planning Development and Experiments

There are a number of algorithms and processes that may benefit from simultaneous development.

* A high-level algorithm for operating a neural networks with selective neuron activations has been summarised.
This implementation of selective neuron activation can be viewed as a spiking neural network; therefore, attempts to implement other trained neural networks using this particular algorithm are unlikely to be successful.
This neural network implementation can be developed; however, tests of learning performance will require the additional implementation of a learning or training algorithm.

* Training algorithms for selective neuron activation could be developed to be applied to a randomly initialised network for standard machine learning tasks.
Methods of performing Hebbian and competitive Hebbian learning may be developed and tested first.
Implementations of stochastic gradient descent that only update active neurons can also be developed and tested.
Applications to reinforcement learning may also be investigated.

* Constructive algorithms can create neurons to learn new patterns and correct errors.
Neurons can be constructed for different tasks and can be expected to result in  sets of neurons that respond selectively to different inputs.
The presence or absence of active neurons can also be used as a condition to trigger neuron construction.

I plan to present details of these developments and test outcomes on this website.
