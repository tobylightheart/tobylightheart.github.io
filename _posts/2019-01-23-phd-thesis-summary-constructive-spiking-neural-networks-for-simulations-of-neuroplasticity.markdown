---
layout: post
title:  "PhD Thesis Summary: Constructive Spiking Neural Networks for Simulations of Neuroplasticity"
date:   2019-01-23 19:52:30 +1030
categories: [Research]
tags: [PhD Thesis, Research, Constructive Algorithms, Spiking Neural Networks]
---

## Overview

My PhD thesis, titled _Constructive Spiking Neural Networks for Simulations of Neuroplasticity_, was accepted in 2018.
The thesis combined topics in machine learning and neuroscience, in particular:  
 - constructive algorithms, adding neurons to artificial neural networks (ANNs) during operation, and
 - spike-timing-dependent plasticity (STDP), a model of neuroplasticity based on the relative timing of neuron spikes.

A number of new concepts were developed to combine constructive algorithms, spiking neurons and STDP, and to develop constructive algorithms that could be implemented in simulations of biological networks.
This post will summarise the conceptual and theoretical developments and simulations presented in the thesis.

## Designing Constructive Neural Networks

Numerous constructive neural networks have been developed since multilayered perceptrons (artificial neural networks) grew in popularity in the 1980s.
I found no attempts to provide general guides for designing constructive neural networks prior to writing the thesis; therefore, the thesis provided a generalised description of the standard constructive neural network components and proposed standard questions in their design.

A constructive neural network is composed of an artificial neural network (ANN) and a constructive algorithm that creates neurons or connections.
There are no strict requirements for the ANN: any initial structure (or absence of structure) or neuron and connection models can potentially be used in a constructive neural network (whether they are effective is another matter).
Any algorithm that creates neurons or connections can be called a constructive algorithm.

<p align="center">
<img alt="Diagram of an artificial neural network with a neuron being constructed." src="/assets/neural_network_construction.svg"> <br />
<small>Diagram of an artificial neural network with a neuron being constructed. Circles represent neurons; lines represent connections. Most connections are omitted to simplify the diagram.</small>
</p>

The purpose (*Why*) of neuron and connection construction is to contribute to the ANN learning either indirectly, by increasing number of neurons and connections for training, or directly, by learning a sample or correcting an error.
The constructive algorithm may also be used to automate  the ANN structure design.
*How* neurons and connections are added is dependent on the implementation of the ANN (programming language and library) and requires decisions in the constructive algorithm.

The primary algorithm decisions necessary for adding neurons or connections to an ANN are:
- *When* will something be added to the network?
- *Where* will it be added to the network (the layer or connected neurons)?
- *What* parameters values to give the new components?

These decisions can be hard-coded into the constructive algorithm, for example:  
- When: A neuron and connections can be added every training sample, mini-batch, or batch.
- Where: New neurons can be added to a predefined layer with full connections to adjacent layers.
- What: The neuron parameters and connection weights can be set to predefined values.

Rather than being hard-coded, algorithm processes may be designed to make these decisions based on performance or events in the training or operation of the ANN.
Construction can be a binary event (construction occurs or does not occur), which can be triggered using a threshold on error, loss or activity.
Performance can be calculated locally (individual connections, neurons or layers) or globally (the overall network) and be calculated on a sample-by-sample basis or averaged over some period of training or operation.

In terms of construction decisions, examples that incorporate inputs or performance calculations include:
- When: The error/loss for a particular sample is above a threshold or no neuron is sufficiently correlated with the input.
- Where: Error/loss and activity levels may be localised to specific collections (or layers) of neurons, indicating the connections to give a new neuron.
- What: Parameters for new neurons and connections may be calculated from input samples, neuron activity, or error/loss values.  

The constructive algorithm processes must be integrated with the operation of the ANN.
Condition tests and parameter calculations can potentially be performed at any stage of the neural network operation: calculations of neuron activity, layer activity, sample class prediction, mini-batch or batch completion, or training convergence.
Constructive algorithms may also have variables that are maintained and updated over periods of the ANN operation.

A standard sequence of processes for a constructive algorithm is to:  
1. process an input sample with the ANN,
2. test performance conditions, and then
3. perform construction (calculate parameters and insert new network components).

An alternative sequence (e.g., evolving spiking neural networks) is to:
1. calculate parameters for a new neuron from an input sample,
2. test performance conditions to determine if the neuron should remain in the network, or
3. prune or merge the neuron with existing neurons.

### Neuron Pruning and Merging

Pruning is a standard term for removing neurons from an ANN.
The term 'synaptic pruning' is used in the context of biological neural networks to refer to the removal of connections (synapses) between neurons; however, pruning is not commonly used to refer to the loss of neurons in biological neural networks (cell death may be referred to as apoptosis or necrosis).

Similar to constructive algorithms, pruning algorithms in ANNs require decisions for when and where to remove connections or neurons.
This can benefit from calculations of local performance to identify specific connections or neurons with low "significance" or with a high contribution to error.
Pruning does not create new neurons or connections, so the calculation of new parameters (what) is unnecessary.

An alternative process that reduces the number of connections or neurons is merging.
Network components (one or more connections or neurons) are removed and some selection of remaining components have their parameters updated with reference to the removed component parameters.
Pruning and merging algorithms may operate alone or in combination with neuron construction.

### Spike-Timing-Dependent Construction

ANNs can make use of a variety of neuron models, including time-dependent models that approximate sharp spikes of neuron voltage or cell membrane potential seen in biological neurons.
Spiking neuron models are much more common in computational neuroscience and simulations of biological neural networks than in applications for machine learning; nevertheless, the intrinsic time-dependence of networks of spiking neurons make them a candidate for handling time-dependent tasks or predictions.

Construction of new neurons and synapses can be made dependent on the spike times of neurons.
In other words, one or more of the constructive algorithm processes (determining when, where and what to construct) take neuron spike times as a parameter.
Constructive algorithms that use neuron spike times in any process are performing spike-timing-dependent construction.

Note that the majority of constructive algorithms developed in the past have been applied to networks of non-spiking neurons.
There are constructive algorithm processes that do not depend on neuron spike times that can be applied to spiking neural networks; however, it would be inaccurate to describe these algorithms as performing spike-timing-dependent construction.

Past constructive algorithms have been developed that incorporate spike times in the calculation of synapse weights or the triggering of neuron construction (see the reference list at the end of this page).
Apart from the evolving spiking neural networks (Wysoski et al, 2010), the investigation of these constructive algorithms were often limited to a single study with limited applications.

The evolving spiking neural network has been designed for classification tasks with finite duration input samples.
This constructive algorithm requires modification to be applied to continuous simulations that do not have separable input samples, such as might be used in simulations of biological neural networks.

No past constructive spiking neural networks were found that were developed with an interest in being applied as the simulation of a biological neural network.
For constructive algorithms to be applied to simulations of biological neural networks, neuron construction first needs to be justified as biologically plausible.
The following developments build such a justification.

## Neuron Sets: Simulated, Surrounding, and Computer Memory

Simulations of biological neural networks often have many fewer neurons than related regions in a biological brain or neural system.
Therefore, a simulation with few neurons could be assumed to be surrounded by many neurons that are not simulated.
A neural system that has some neurons simulated can have two subsets of neurons defined:

> S1. Simulated neurons  
> S2. Surrounding neurons

Collectively, the (union of the) simulated neuron set and surrounding neuron set make up the entire brain or neural system.

<p align="center">
<img alt="Set diagram of a neural system ($N$) split into simulated neurons ($N_{sim}$) and surrounding neurons ($N_{sur}$)." src="/assets/neural_system_sim_sur_sets.svg"> <br />
<small>Set diagram of a neural system ($N$) split into simulated neurons ($N_{sim}$) and surrounding neurons ($N_{sur}$).</small>
</p>

For a neuron to be simulated (to be involved in calculations), it must have some representation in the computer memory.
This leads to an additional neuron set definition:

> S3. Neurons in computer memory

Not all neurons in memory need to be simulated; however to be simulated, a neuron must have some representation in memory.

<p align="center">
<img alt="Set diagram of a neural system ($N$) split into simulated neurons ($N_{sim}$), surrounding neurons ($N_{sur}$), and neurons in memory ($N_{mem}$)." src="/assets/neural_system_sim_sur_mem_sets.svg"> <br />
<small>Set diagram of a neural system ($N$) split into simulated neurons ($N_{sim}$), surrounding neurons ($N_{sur}$), and neurons in memory ($N_{mem}$).</small>
</p>

Another complementary neuron set can be explicitly defined:

> S4. Neurons that are not in computer memory

Neurons in the surrounding set that are not in computer memory can be theorised about to develop limits and predictions for neuron construction.
There are potentially interesting insights to be found in exploring the idea of there being infinite surrounding neurons and all possible combinations of parameters.
Sets of connections can also be defined, but for simplicity, this summary will focus on sets of neurons.

Assuming that these sets exist gives rise to alternative interpretations of changing the number of neurons in a simulation.

## Transferring Neurons Between Sets

Transfers of neurons between the sets can be used to define neuron construction, (simulation) expansion, pruning, and (simulation) contraction.

### Construction and Expansion

Neuron construction can be defined as adding a neuron to the computer memory.
This could be interpreted as a transfer from the set of neurons not in computer memory to the set of neurons in computer memory.
A constructed neuron could be simulated immediately; alternatively, the neuron could remain the surrounding set (to be simulated at a later time).

<p align="center">
<img alt="Set diagram of neuron construction: a neuron is transferred from surrounding neurons ($N_{sur}$) not in memory, to either simulated neurons ($N_{sim}$) or surrounding neurons ($N_{sur}$) in memory ($N_{mem}$)." src="/assets/neural_system_sets_construction.svg"> <br />
<small>Set diagram of neuron construction: a neuron is transferred from surrounding neurons ($N_{sur}$) not in memory, to either simulated neurons ($N_{sim}$) or surrounding neurons ($N_{sur}$) in memory ($N_{mem}$).</small>
</p>

The transfer of a neuron from the set of surrounding neurons to the set of simulated neurons can be described as (simulation) expansion, that is, the simulated neural network is expanding to include a surrounding neuron.
If this neuron is already in computer memory, then the expansion can be performed without neuron construction.

<p align="center">
<img alt="Set diagram of simulation expansion: a neuron is transferred from surrounding neurons ($N_{sur}$) to simulated neurons ($N_{sim}$)." src="/assets/neural_system_sets_expansion.svg"> <br />
<small>Set diagram of simulation expansion: a neuron is transferred from surrounding neurons ($N_{sur}$) to simulated neurons ($N_{sim}$). Expansion without construction occurs if the surrounding neuron is in memory ($N_{mem}$).</small>
</p>

Approaches to the selective simulation (activity calculation) of neurons in memory could be explored.
Neuron dropout (a technique for reducing overfitting from training) can be described as performing randomised selective simulation of neurons.
It may be possible to develop more complex techniques used during operation to reduce the number of neurons involved in calculations (and computational cost) for the present task or input.

### Pruning and Contraction

The reverse transfers can also be defined.
Pruning can be defined as the transfer of a neuron out of computer memory.
Pruned neurons can be assumed to continue to exist in the surrounding neuron set (but may now be disconnected from other simulated neurons).
An alternative term might be useful for neurons removed from the neural system completely; biological terms for cell death, apoptosis a necrosis, are candidates.

<p align="center">
<img alt="Set diagram of neuron pruning: a neuron is transferred out of the neurons in memory ($N_{mem}$)." src="/assets/neural_system_sets_pruning.svg"> <br />
<small>Set diagram of neuron pruning: a neuron is transferred out of the neurons in memory ($N_{mem}$). This transfer is pruning whether the neuron was in the simulation ($N_{sim}$) or surroundings ($N_{sur}$).</small>
</p>

Simulation contraction can be defined as the transfer of a neuron from the simulated set to the surrounding set.
Similar to construction, it is possible to transfer a neuron to the surrounding set without removing it from memory (contraction without pruning).

<p align="center">
<img alt="Set diagram of simulation contraction: a neuron is transferred from simulated neurons ($N_{sim}$) to the surrounding neurons ($N_{sur}$). The neuron may remain in memory ($N_{mem}$) or be pruned." src="/assets/neural_system_sets_contraction.svg"> <br />
<small>Set diagram of simulation contraction: a neuron is transferred from simulated neurons ($N_{sim}$) to the surrounding neurons <nobr>($N_{sur}$).</nobr> The neuron may remain in memory ($N_{mem}$) or be pruned.</small>
</p>

### Biologically Plausible Neuron Construction

Most biological neurons grow slowly during fetal development; new neurons do not appear instantaneously.
If neuron construction is interpreted as creating new neurons instantaneously, it is not biologically plausible.
The "transfer" of neurons that exist in the surrounding network into the simulation is an interpretation of neuron construction that can be biologically plausible.

Neurons added to the simulation are assumed to already exist in the surroundings, so their effects on the activity of simulated should already be present.
Changes to the activity of other simulated neurons need to be justified (e.g., it may be possible that the neurons were inhibited or otherwise inactive).
In other words, new neurons and connections should have a plausible effect on the simulation.
This can limit the probable characteristics of new neurons.

## Pre-Simulation History: Past Activity and Plasticity

Except when designed to model the growth and maturation of the network, simulations rarely explicitly state the level of maturity of the neural network.
We can assume that prior to the time being simulated, a mature neural network:
- has existed for a long time,
- has had patterns of input and activity that have repeated many times, and
- has connection weights the result of plasticity and past repetition of activity.

Assuming that there are surrounding neurons for which this is all true, we can make some predictions about plausible connection weights when constructing neurons.

### Spike-Timing-Dependent Plasticity

A voltage spike in the presynaptic neuron results in a transmission across the synapse to the postsynaptic neuron.
Spike-timing-dependent plasticity (STDP) models can be used to calculate adjustments in synapse weight (transmission strength) based on the relative timing of spikes of the presynaptic neuron and postsynaptic neuron.
An STDP function or curve can be defined to specify the change in synapse weight for a given relative timing of neuron spikes (see the figure below).

<p align="center">
<img alt="A common antisymmetric spike-timing-dependent plasticity curve." src="/assets/antisymmetric_stdp_curve.svg"> <br />
<small>A common antisymmetric spike-timing-dependent plasticity (STDP) curve. The change in synapse weight ($\Delta w_{\text{post},\text{pre}}$) is a function of the difference in presynaptic and postsynaptic spike times ($\Delta t_{\text{post},\text{pre}} = t^f_{\text{pre}} - t^f_{\text{post}}$).</small>
</p>

An additive model of STDP makes weight changes independent of the current weight.
This model typically enforces limits on connections weights with thresholds.
Computational studies have shown that additive models of STDP often result in bimodal distributions of synapse weights (clustering at the minimum and maximum values).
Other models of neuroplasticity can also be used (the thesis also examined outcomes of weight-dependent or multiplicative STDP).

Neuron construction can assume an initial weight and specific number of prior repetitions of an observed relative spike timing to calculate new connection weights.
Constructed connections weights can also be assumed to have converged bimodally.
All connections that have overall positive weight updates from the repeating pattern can be assigned the maximum weight (all other connections are assigned the minimum weight).
The number of synapses assigned the maximum weight can be restricted further, for example, with a minimum positive weight update, or a maximum number of synapses (starting with those with the most positive update).

The thesis formalised assumptions about the repetition of presynaptic spikes observed in the simulation to estimate prior plasticity and calculate synapse weights.
Given a predicted surrounding postsynaptic spike time, a window for eligible relative presynaptic spike times can be provided to limit calculations and the time to complete construction.
Next, methods for predicting the spike times of surrounding neurons are needed.

## Predicting Surrounding Neuron Spike Times

Neurons in the surrounding network are (by definition) not simulated, so their spike times are not directly provided by the simulation.
From a machine learning perspective, supervised learning can include target output values, such as surrounding neuron spike times, to perform learning calculations.
There may be circumstances where expected or desired postsynaptic spike times are available in simulations of biological networks.
Predictions of surrounding neuron spike times may still be possible even when target outputs have not been provided (performing unsupervised learning or reinforcement learning).

Many neurons spike in response to activity in a set of presynaptic neurons.
A set of neurons in the simulation can be taken to be presynaptic neurons with connections to surrounding postsynaptic neurons.
The activity in this set of simulated presynaptic neurons can be used to predict a postsynaptic spike time.
The prediction of a surrounding postsynaptic spike can also be used as a condition to trigger neuron construction.

### Presynaptic Set Spike-Rate Threshold

Spikes in a postsynaptic neuron can be correlated with high rates of activity in connected presynaptic neurons.
A postsynaptic neuron spike can be predicted to occur at times when the number of spikes from presynaptic neurons exceeds a given number within a short period of time.
This could be calculated as a threshold on the presynaptic neuron set spike rate.
A constructive algorithm could regularly calculate the spike rate of the presynaptic neuron set and trigger the construction of a postsynaptic neuron if the spike rate is above the threshold.

### Spike-Triggered Construction and Expansion

The distinction between surrounding neurons and simulated neurons can be blurred: a neuron can be simulated as a proxy for a subset of the surrounding neurons.
This proxy neuron does not represent any specific neuron, but has parameters set to approximately represent or predict activity in a subset of the surrounding neurons.
Spikes by this simulated proxy neuron can be used to trigger neuron construction (spike-triggered construction) and as a prediction of a surrounding neuron spike time for parameter calculations.

A related idea was proposed in the thesis as future work: use proxy neurons to predict the activity of specific subsets of surrounding neurons in memory.
Proxy neuron spikes could be used to trigger the expansion of the simulation to include that subset of surrounding neurons.
When the proxy neuron does not spike, it can be assumed that there is no significant activity in that subset of surrounding neurons and they can by excluded from calculations.
This could reduce the computational cost of the ANN; however, there may be a trade-off in the ANN prediction or model accuracy.

## Developed Algorithms for Spike-Triggered Construction

A range of basic constructive algorithms that use proxy neuron spikes to trigger neuron construction were specified in the thesis.
These algorithms were based on the following pattern:

**Algorithm: Proxy neuron spike-triggered construction with delay**  

1: &nbsp; **initialise** construction flag, $c \gets 0$; construction time, $t_{c} \gets - \infty$  
2: &nbsp; **for** neural network update steps, $t \gets 1, 2, 3, \dots, T$ **do**,  
3: &nbsp; &nbsp; &nbsp; Update the neural network  
4: &nbsp; &nbsp; &nbsp; **if** neuron construction flag is set, $c = 1$ **then**  
5: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **if** $t > t_{c}$ **then**  
6: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Calculate new neuron and synapse parameters  
7: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Add the new neuron and synapses to the network  
8: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Clear neuron construction flag: $c \gets 0$  
9: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **else**  
10: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Record eligible relative spike times, $\Delta t_{\text{proxy},j} \le T_{-}$  
11: &nbsp; &nbsp; &nbsp; &nbsp; **end if**  
12: &nbsp; &nbsp; **else**  
13: &nbsp; &nbsp; &nbsp; &nbsp; Update the proxy neuron  
14: &nbsp; &nbsp; &nbsp; &nbsp; **if** the proxy neuron spikes **then**  
15: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Record eligible relative spike times, $\Delta t_{\text{proxy},j} > T_{+}$  
16: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Set neuron construction time: $t_{c} \gets t + T_{-}$  
17: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Set neuron construction flag: $c \gets 1$  
18: &nbsp; &nbsp; &nbsp; &nbsp; **end if**  
19: &nbsp; &nbsp; **end if**  
20: **end for**

Note the algorithm uses a variable for the relative timing or difference in the proxy neuron spike time, $t_{\text{proxy}}$, and the presynaptic neuron spike time, $t_{j}$: $\Delta t_{\text{proxy},j} = t_{j} - t_{\text{proxy}}$.
Constants are also used to limit the duration of construction in the simulation to a window: $T_{+}$, time before the proxy neuron spike (presynaptic spikes in this time will provide a positive contribution to the constructed synapse weight); and $T_{-}$, time after the proxy neuron spike (presynaptic spikes in this time will provide a negative contribution to the constructed synapse weight).

Calculations that assign weights the maximum or minimum values (representing the convergence of additive STDP), may not need to consider presynaptic spikes after the proxy neuron triggers construction.
A number of presynaptic neurons that are the nearest before the proxy neuron are given the maximum synapse weight value and all others are given the minimum.

Algorithm processes can also be added to inhibit neuron construction or prune ineffective neurons.
This was necessary in simulations that were tested in the thesis that had consistently high presynaptic spike rates.
Activity in any simulated postsynaptic neuron would temporarily inhibit or cancel neuron construction (a postsynaptic neuron spike indicated that the present spike pattern is already detected).

To avoid missing patterns concealed in the presynaptic neuron activity, neurons were constructed frequently.
Neurons that had very low or no activity after construction were most likely not tuned to a repeating pattern.
If neurons failed to meet an activity threshold shortly after construction, they were pruned.

## Pattern Detection through STDP and STDC

Past simulated studies (Masquelier et al, 2008, 2009) showed that repeating patterns concealed in high levels of neural activity could be learned through additive spike-timing-dependent plasticity (neurons with tuned synapses would selectively respond to repetitions of that concealed pattern).
This learning model used high initial synapse weights that caused frequent indiscriminate postsynaptic spikes.
The STDP model gradually reduced the weights until the postsynaptic neuron would not respond to background activity but could remain responsive to activity in a subset of the presynaptic neurons.

The thesis presented experiments showing that neurons constructed with high initial synapse weights and modified using the STDP model underwent the same learning process with similar rates of learning success.
The calculation of synapse weights assuming small numbers of past pattern repetitions and STDP were found to slightly reduce learning success in these high-activity simulations.
Assigning weights assuming the convergence of STDP, however, was found to be able to result in neurons that immediately detect a repeating pattern and reject background activity.

A demonstration of this one-shot detection of concealed spike patterns is available at: [https://github.com/tobylightheart/csnn-stdp/blob/master/Jupyter-Notebooks/neuron_construction_stdp_convergence.ipynb](https://github.com/tobylightheart/csnn-stdp/blob/master/Jupyter-Notebooks/neuron_construction_stdp_convergence.ipynb)

The thesis also presented an extension to a past simulation of competitive pattern detection (Masquelier et al, 2009): introducing new concealed patterns at later times in the simulation.
Simulations without construction had postsynaptic neurons initialised with high total input weight.
A combination of lateral inhibition and additive STDP allowed neurons to tune to different sections of the patterns present at the start of the simulation.
However, once plasticity had depressed the synapses to the point of the neurons ignoring other activity, they were not capable of retuning to a new pattern (without intervention).

Neurons constructed in the simulation ("transferring" them from the surroundings) immediately detected new concealed patterns as they were introduced.
This produced a qualitative improvement in the simulation capabilities: construction allowed ongoing learning without overwriting the previously tuned connections.
The neurons added to the network could have feasibly existed in the surrounding neurons; no biologically implausible changes in the simulation were found resulting from neuron construction.

## Future Work

The thesis demonstrated success in developing constructive algorithms compatible with simulations of biological neural networks.
Future work could explore applications of constructive algorithms in developing models of biological learning and perception.
Biological vision has been extensively studied and may be a suitable target for the development and testing of biologically plausible constructive algorithms.

Machine learning has made rapid advances with deep neural networks.
Constructive algorithms could be explored for the potential to contribute to ANN design and learning capabilities (for deep and shallow networks).
Constructive algorithms may contribute to learning indirectly by adding neurons and connections to be trained or directly by selecting connection weights to detect a new sample or make an immediate correction (direct contributions may still be trained).
In either case, the constructive algorithm provides some automation of the design of the ANN structure.
Neuron construction may also be studied as an approach to adding new capabilities to a trained neural network without overwriting connections and avoiding "catastrophic forgetting".

Future work could also explore the dynamic selection of neurons in memory for simulation (expansion and contraction).
Biological brains have regions that specialise in certain kinds of perception, action selection and motor control.
A large artificial neural network that performs multiple tasks may similarly have specialised sets of neurons for separate tasks.
If the fraction of neurons required for the present task is low, methods for omitting insignificant neurons from calculations may substantially reduce the computational expense of the ANN operation.
It may be possible to develop and combine techniques for neuron construction and selective neuron simulation to produce agents capable of open-ended machine learning.


## References

### Publications

Lightheart, T., Grainger, S., & Lu, T.-F. (2013). Spike-timing-dependent construction. *Neural Computation*, *25*(10), 2611-2645. doi: 10.1162/NECO_a_00501

Lightheart, T., Grainger, S., & Lu, T.-F. (2010). A constructive spiking neural network for reinforcement learning in autonomous control. In G. Wyeth & B. Upcroft (Eds.), *Proceedings of the 2010 Australasian Conference on Robotics & Automation*. Retrieved from http://www.araa.asn.au/acra/acra2010/papers/pap155s1-file1.pdf

Lightheart, T., Grainger, S., & Lu, T.-F. (2011). Constructive network reinforcement learning for autonomous mobile robots. In *Proceedings of the 2011 International Conference on Mechatronics Technology [CD]*.

### Spike-Timing-Dependent Construction

- Refractoriness-based construction:
  - Takita, K., & Hagiwara, M. (2005). A pulse neural network reinforcement learning algorithm for partially observable Markov decision processes. *Systems and Computers in Japan*, *36*, 42-52. doi: 10.1002/scj.10645
- Evolving spiking neural networks (eSNNs) and related developments:
  - Wysoski, S. G., Benuskova, L., & Kasabov, N. (2010). Evolving spiking neural networks for audiovisual information processing. *Neural Networks*, *23*(7), 819-835. doi: 10.1016/j.neunet.2010.04.009
  - Schliebs, S., & Kasabov, N. (2013). Evolving spiking neural network{a survey. *Evolving Systems*, *4*(2), 87-98. doi: 10.1007/s12530-013-9074-9
  - Kasabov, N., Dhoble, K., Nuntalid, N., & Indiveri, G. (2013). Dynamic evolving spiking neural networks for on-line spatio- and spectro-temporal pattern recognition. *Neural Networks*, *41*, 188-201. doi: 10.1016/j.neunet.2012.11.014
  - Shirin, D., Savitha, R., & Suresh, S. (2013). A basis coupled evolving spiking neural network with afferent input neurons. In *The 2013 International Joint Conference on Neural Networks (IJCNN)*. doi: 10.1109/IJCNN.2013.6706964
  - Dora, S., Sundaram, S., & Sundararajan, N. (2015). A two stage learning algorithm for a Growing-Pruning Spiking Neural Network for pattern classification problems. In *2015 International Joint Conference on Neural Networks (IJCNN)*. doi: 10.1109/IJCNN.2015.7280592
  - Dora, S., Suresh, S., & Sundararajan, N. (2015). A sequential learning algorithm for a spiking neural classifier. *Applied Soft Computing*, *36*, 255-268. doi: 10.1016/j.asoc.2015.06.062
  - Dora, S., Subramanian, K., Suresh, S., & Sundararajan, N. (2016). Development of a self-regulating evolving spiking neural network for classification problem. *Neurocomputing*, *171*, 1216-1229. doi: 10.1016/j.neucom.2015.07.086
  - Wang, J., Belatreche, A., Maguire, L., & McGinnity, T. M. (2014). An online supervised learning method for spiking neural networks with adaptive structure. *Neurocomputing*, *144*, 526-536. doi: 10.1016/j.neucom.2014.04.017
  - Wang, J., Belatreche, A., Maguire, L., & McGinnity, T. (2015). Dynamically evolving spiking neural network for pattern recognition. In *2015 International Joint Conference on Neural Networks (IJCNN)*. doi: 10.1109/IJCNN.2015.7280649
  - Wang, J., Belatreche, A., Maguire, L. P., & McGinnity, T. M. (2015b). SpikeComp: An evolving spiking neural network with adaptive compact structure for pattern classication. In S. Arik, T. Huang, W. K. Lai, & Q. Liu (Eds.), *Neural Information Processing: 22nd International Conference, ICONIP 2015, Istanbul, Turkey, November 9-12, 2015, Proceedings, Part II* (pp. 259-267). doi: 10.1007/978-3-319-26535-3_30
  - Wang, J., Belatreche, A., Maguire, L. P., & McGinnity, T. M. (2017). SpikeTemp: An enhanced rank-order-based learning approach for spiking neural networks with adaptive structure. *IEEE Transactions on Neural Networks and Learning Systems*, *28*(1), 30-43. doi: 10.1109/TNNLS.2015.2501322
- Structural plasticity algorithms:
  - Roy, S., & Basu, A. (2016). An online structural plasticity rule for generating better reservoirs. *Neural Computation*, *28*(11), 2557-2584. doi: 10.1162/neco_a_00886
  - Roy, S., San, P. P., Hussain, S., Wei, L. W., & Basu, A. (2016). Learning spike time codes through morphological learning with binary synapses. *IEEE Transactions on Neural Networks and Learning Systems*, *27*(7), 1572-1577. doi: 10.1109/TNNLS.2015.2447011
  - Roy, S., & Basu, A. (2017). An online unsupervised structural plasticity algorithm for spiking neural networks. *IEEE Transactions on Neural Networks and Learning Systems*, *28*(4), 900-910. doi: 10.1109/TNNLS.2016.2582517

### Spike-Timing-Dependent Plasticity

Masquelier, T., Guyonneau, R., & Thorpe, S. J. (2008). Spike timing dependent plasticity finds the start of repeating patterns in continuous spike trains. *PLOS ONE*, *3*(1), e1377. doi: 10.1371/journal.pone.0001377

Masquelier, T., Guyonneau, R., & Thorpe, S. J. (2009). Competitive STDP-based spike pattern learning. *Neural Computation*, *21*(5), 1259{1276. doi: 10.1162/neco.2008.06-08-804
