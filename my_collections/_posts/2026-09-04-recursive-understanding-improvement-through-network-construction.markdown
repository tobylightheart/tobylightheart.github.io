---
layout: post
title:  "Recursive Understanding Improvement through Network Construction"
date:   2026-09-04 20:00:00 +0930
categories: [Research]
tags: [AI Safety, AI Takeoff, General intelligence, Interpretability, Recursive Self-Improvement, AI]
---

## 0.  Introduction

Recursive self-improvement (RSI) and continual learning have come into focus as declared aims of frontier AI research labs; however, few (if any) have public technical proposals for safe recursive improvement. This post proposes a continual learning research program using constructive (growing) network algorithms to create modular, composable, reversible and interpretable modifications and improvements with human oversight and control.

The core hypotheses presented and their potential impacts on AI safety are:

1.  Disposition (e.g., persona, preferences and drives) can be separable from other components of intelligence in artificial neural networks. If true, AI learning and improvements to target understanding and skills may be done with minimal alignment drift.
2.  Solving continual learning involves **recursive understanding improvement:** new understanding creating a foundation for the next improvement in understanding. Assuming disposition separability, recursive understanding improvement can be more contained and have a more manageable risk profile compared to full recursive self-improvement.
3.  A. Understanding improvements can be achieved through construction of neural network modules; B. Constructive algorithms can produce modular, composable, reversible and interpretable components; with C. Human-in-the-loop gating of construction events. Therefore, **network construction** provides multiple avenues to mitigate risks of recursive improvement.
4.  Recursive understanding improvements are limited by: A. Prerequisite foundational understanding, B. Necessary abilities, disposition, and skills for learning, and C. The necessary quality and quantity of input information. Current AI are primarily limited by B-abilities. Once learning abilities are achieved, the rate of improvement will be limited by A and C, with fundamental limits in accessibility of real world information and limits in the quality of information obtainable from simulations.

These hypotheses collectively form a research proposal for achieving a slow and controlled AI take-off while managing alignment. These are unpacked below into a set of key propositions that signpost the progression of the arguments in this post.

This post outlines a research program that is a synthesis of historical and original lines of research and thought. A reader can skip to Section 4, *Harnesses, growing networks, and human control*, for a high-level description of the network construction research and some recent antecedents. Note that ADUS (abilities, dispositions, understanding, and skills) is referenced, which is defined in Section 1, *A practical intelligence taxonomy*.

ADUS components are used to propose requirements for *Artificial General Intelligence* in Section 2. This section identifies a requirement for AGI to have the ability to integrate new understanding (episodic and semantic memory) and skills (motor and procedural memory), aka, "continual learning". Section 3 examines *Recursive improvement* with particular attention to recursive understanding improvement.

This work presents alternatives to common RSI and AI safety concepts, such as the definition of intelligence as “ability to achieve goals”, goal-directedness and Orthogonality. I think it is important for these foundations to be open to questioning and challenged by alternatives. I hope this post acts as a positive contribution to the larger discussion and I am keen to receive any and all feedback.

*Epistemic status: Medium confidence. I am an independent researcher with an academic background in developing constructive algorithms for artificial neural networks and simulations of neuroplasticity. AI assistance has been used for review, discussions and drafting the related-methods survey in Section 4; almost all writing and concepts in this post are my own and otherwise have been reviewed and edited.*

### 0.1 Key propositions

1.  Intelligence can be defined as a combination of abilities, dispositions, understandings and skills (ADUS). These components map closely to their standard English definitions.
2.  Understandings are a complex of associations and operations that integrate experiences and concepts (episodic and semantic memory) and have degrees of accuracy, precision, and completeness.
3.  The transformer neural network architecture implements associations and operations through attention and MLPs and can demonstrate capabilities consistent with understanding.
4.  The ability to integrate and recall new understanding (episodic and semantic memory) and skills (procedural and motor memory) during operation is necessary (but not sufficient) for AGI. This ability can be described as "continual learning".
5.  Continual learning is a seed capability that can expedite autoresearch and recursive self-improvement. Autoresearch could target continual learning to seed this positive feedback loop.
6.  Consolidating new understanding and skills is a form of recursive improvement. New understanding and skills unlock further gains in understanding and skills.
7.  Understanding improvement is fundamentally constrained by: the current state of understanding (accuracy, precision and completeness); learning abilities, dispositions and skills; and the quality and quantity of information that can be obtained from interactions including external resources and simulations.
8.  A harness is a practical requirement for continual learning during operation and can be designed to explicitly target ADUS components of an AI system.
9.  Growing neural networks (or constructive algorithms) can potentially produce network components that are modular, composable, reversible and interpretable, allowing human-in-the-loop control of improvements.
10.  An intelligence take-off could be “slow” — due to fundamental limits on understanding — and controllable and interpretable through human management of neural network growth.

## 1.  A practical intelligence ontology

> Intelligence can be defined as a combination of abilities, dispositions, understandings and skills (ADUS). These components map closely to their standard English definitions.

This ontology is applicable to humans, with important pedagogical implications, and to artificial intelligence, with important implications for AGI and recursive improvement. AGI and recursive improvement are the primary topics of this post.

The names of these four core ADUS components (abilities, dispositions, understandings, skills) map closely to their standard English meanings, with some nuance and qualifications worth discussion.

**Abilities** are the predefined structures and capabilities of the body and brain. In biological organisms like humans, abilities are largely bounded by genetics; however, technology can be used to extend our abilities with tools and machines.

We can decompose abilities into sensory, perceptual, cognitive (simulation, memory, control), and motor abilities. Biological abilities develop spontaneously through natural activity without intentional effort, unlike understanding and skills which are typically acquired through intentional learning and practice. For example, we have the ability to learn languages, but learning to speak, read and write are acquired skills and understanding.

Frontier AIs have abilities: sensory (input), perceptual (feature detection), cognitive (simulation, memory and control) and motor (output). Cognitive abilities in LLMs emerged from training, and understanding them is an active topic of mechanistic interpretability. Unlike humans, AIs have pathways to flexibly integrate with other technologies to extend their abilities.

**Dispositions** are internal motivations for behavior, inclusively and broadly covering emotions, reflexes, habits, drives, preferences, values and goals. People have innate drives, reflexes and emotion responses; however, preferences can be transient and dependent on context. Values and goals are largely learned, reasoned about, and adapted — this adaptability is an important capability for intelligence.

Disposition converts capabilities (abilities, understanding and skills) into behaviour. Disposition towards learning is as important as the abilities to develop understanding and skills. For example, Terence Tao was not just very smart, he had a drive to learn, study and practice mathematics from a young age. We are born with innate dispositions; however, it is possible to develop and increase degrees of self-awareness and self-control.

In the case of LLMs, “disposition” has substantial overlap with the concept of LLM “persona”. The result of pretraining is an incoherent superposition of many dispositions. A goal of post-training is to produce a coherent disposition, usually the “helpful AI assistant”. “Disposition” can also be invoked when coding agents cheat on tasks or have different tendencies towards quality, despite frontier models having similar technical understanding and skill. A core concern of AI safety research is AI dispositions.

**Understandings**:

> Understandings are a complex of associations and operations that integrate experiences and concepts (episodic and semantic memory) and have degrees of accuracy, precision and completeness.

People develop understanding first by acquiring experiences and then learning associated concepts. Language is a complex collection of concept associations and operations. Understandings can be better or worse depending on their accuracy, precision and completeness. The term “understanding” is preferred over “knowledge” (and “accuracy, precision and completeness” over “truth”) due to the heavy epistemological baggage and conceptual fragility of the latter.

Inaccurate understandings (misunderstandings) have erroneous associations. Imprecise understandings may be broadly accurate but lack specificity. The completeness of an understanding is often graduated (and rarely completely achievable), based on comprehensiveness of relevant experiences, concepts or associations.

An important pathway to developing understanding is the collection of experiences (episodic memories) and the generalisation and consolidation in semantic memory.

> The transformer neural network architecture implements associations and operations through attention and MLPs and can demonstrate capabilities consistent with understanding.

Transformer-based LLMs have achieved levels of performance in many domains that imply understanding. I would go one step further to posit that the transformer architecture (attention and MLPs) is an implementation of the fundamental processes of understanding (and meaning): associations and operations.

The lack of real world (sensorimotor) experience to ground understanding is a deficiency of completeness in current AIs. This may be less a deficiency of the ability to understand than the absence of sensory and motor abilities and episodic memory. Multimodal pre-training may alleviate sensory and perceptual grounding somewhat but does not appear to be sufficient to counteract deficiencies in memory abilities and experiences.

**Skills** are actions and action sequences with outcomes measurable in terms of quality and timing. Learning and improving skills is fundamental to intelligence.

With study and practice, people can become skilful at playing musical instruments, learning body coordination to produce desired sound qualities at precise timings. Practising and applying skills contributes to experience and benefits understanding. There are skills for studying and learning concepts, as well as skills for practicing and acquiring skills.

Skills can depend on or be applications of understanding. Skills such as solving maths and coding problems are primarily applications of conceptual understanding. In these cases, higher skill means higher quality and correctness of outputs and faster completion.

LLM-based AIs are primarily skilled at applications of conceptual understanding. AIs have limited (or zero) abilities to efficiently acquire perceptual, cognitive or motor skills through experience.

ADUS components form a basis for more technical exploration on feedback and coupling between components, meta-cognition, degrees of automaticity and awareness, and modes of consolidation. Most of this content is out of the scope of this post but can be found at [adus-intelligence](https://tobylightheart.github.io/adus-intelligence/).

## 2.  Artificial General Intelligence

This section proposes a definition and requirements of **artificial general intelligence** (AGI) in terms of ADUS components. The set of abilities a typical human possesses slightly exceeds the minimum requirements for AGI. People can lose sensory and motor abilities and still have general intelligence. The requirements for cognitive abilities are firm, while requirements for disposition, understanding, and skills are softer.

*Ability 1: Sense and act*

*Ability 1.1: At least one input/sensor and accompanying adaptive perceptual processing.*

*Ability 1.2: At least one output/actuator and accompanying adaptive controller.*

*Ability 2: Executive control and cognition*

*Ability 2.1: Control attention to direct sensors, perception, cognition, and/or actuators.*

*Ability 2.2: Internally simulate sensorimotor-world models and manipulate concepts (thinking).*

*Ability 3: Develop understanding*

*Ability 3.1: Integrate and recall new sensorimotor-world experiences and simulations (episodic memory).*

*Ability 3.2: Integrate and recall new abstract concepts (semantic memory).*

*Ability 4: Develop and apply skills*

*Ability 4.1: Integrate sensorimotor-world experiences and simulations into adaptive actions and action sequences (procedural/motor memory).*

*Disposition 1: Learning context-dependent values and goals.* Intelligent behaviour requires learning values that are flexible and context-dependent reasoning over goals.

*Understanding 1: Language, abstraction and conceptual understanding sufficient for communication.*

*Understanding 2: Sensorimotor-world understanding for internal simulation (thinking).*

*Skills 1: Skills for communication.* That is, skills in applying understanding to interpret incoming messages and produce interpretable outgoing messages.

Given these requirements, are current frontier AI systems artificial general intelligence? I currently give a qualified yes.

The current frontier AI systems have achieved a significant degree of general intelligence. However, there are still deficits in (cognitive) abilities 3 (new memories of events and concepts) and 4 (learning new actions and action sequences). In-context learning (ICL) is a short-term, semi-integrated episodic and conceptual memory that allows generalisation to an incredibly broad range of tasks.

> The ability to integrate and recall new understanding (episodic and semantic memory) and skills (procedural and motor memory) during operation is necessary (but not sufficient) for AGI. This ability can be described as "continual learning".

The limits of ICL are less in generality and more in consolidation. At the end of a session the context (sensorimotor-world experiences, simulations, and new abstract concepts) is either discarded or stored externally. Constructing understanding from retrieval and ICL has an increasing risk of failure as the total store of relevant new experiences and concepts reaches the context limit. Understanding that requires long-term aggregation over experiences or successive expansions of new interdependent concepts may not be possible in this regime.

Model training and deployment cycles can shift selected episodes into internalised understanding and skills. However, in the field, the episodes themselves can have valuable specific and aggregate information, continued training can be expensive, and single-shot learning risks drift or interference in understanding, skills and disposition (e.g., catastrophic forgetting). New online, internal consolidation mechanisms that can act on understanding and skills with minimal interference on existing capabilities and disposition are necessary. This is “continual learning”.

## 3.  Recursive improvement

This section first distinguishes “recursive self-improvement” (RSI), “recursive improvement”, and “recursive understanding improvement", making a simple case for focusing on the latter. Examining domains of understanding and bottlenecks or limits on external feedback and validation grounds the examination of trajectory: whether the rates and step sizes in understanding improvement have accelerating or decelerating returns. This section then examines the remaining components (A, D and S) as specific targets of improvement or modification, with a brief treatment of disposition as a core concern for AI alignment and safety.

### 3.1.  Types of improvement

**Recursive self-improvement** (RSI) is an iterative process of self-directed improvement through re-design which enables additional self-improvements.

Autoresearch, or autonomous research, is the core process of RSI. An AI performing machine learning (ML) autoresearch could produce a new and improved version of itself, which then designs the next improved model, and so on. Current frontier AIs already assist human ML researchers to speed up research. Fully autonomous ML research has demonstrated success in narrow research tasks, such as implementing a research concept or improving a given model and training recipe.

RSI is unlikely to be smooth or exponential. Progress in research often runs into dead ends and fundamental constraints. Promising research programs that do not neatly fit current paradigms tend to be harder to conceive and define in a way suitable for successful autoresearch. Progress in research depends on the accumulation and aggregation of new understanding — a deficiency of current AI systems. Recursive self-improvement via autoresearch may first require solving continual learning.

> Continual learning is a seed capability that can expedite autoresearch and recursive self-improvement. Autoresearch could target continual learning to seed this positive feedback loop.

The likelihood of success in applying autoresearch to continual learning (internal consolidation of understanding and skills) can be expected to increase over time. Current transformer architectures are already capable of demonstrating understanding and skills, so may only require a small set of architecture and algorithm advances to achieve continual learning. In this case, continual learning is unlikely to require ongoing RSI; however, an ideal form of continual learning is itself a kind of recursive improvement process.

**Recursive improvement** is an iterative process where each improvement enables additional improvements.

Recursive improvement is already a standard outcome of training neural networks. Iteratively applying gradient descent or rewards on roll-outs improves the model which then provides a new base for the next improvement. This naturally has diminishing returns with local and global optima.

> Consolidating new understanding and skills is a form of recursive improvement. New understanding and skills unlock further gains in understanding and skills.

**Recursive understanding improvement** (RUI) is an iterative process of improving and consolidating understanding which enables additional improvements in understanding.

Recursive understanding improvement is a natural phenomenon exhibited by people as they learn and by social groups (families, tribes, organisation units, research and software communities, companies, nations, etc.) as they accumulate shared understanding. Recursive improvement of understanding and skills requires sufficiently effective internal consolidation and integration to provide the basis for the next improvement.

This post presents a case for recursive understanding improvement. A deeper analysis of take-off speed is out of scope; however, it is worth touching on the debate (or preemptively opening the can of worms) on AI take-off speeds and recursive self-improvement.

Eliezer Yudkowsky and Paul Christiano [disagree about the shape of AI take-off](https://www.lesswrong.com/posts/vwLxd6hhFvPbvKmBH) while both [expecting an intelligence explosion](https://sideways-view.com/2018/02/24/takeoff-speeds/). With respect to Yudkowsky's [returns on cognitive reinvestment](https://intelligence.org/files/IEM.pdf): understanding can be reinvested to improve understanding in abstract domains, but understanding in most real-world domains is limited by availability of information. Christiano has previously expressed uncertainty on '["Understanding" is discontinuous](https://sideways-view.com/2018/02/24/takeoff-speeds/)' as an argument for fast take-off. This post makes a case for specific local discontinuities in understanding that produce surges in advances while understanding is still globally incomplete. The next section elaborates arguments that lean towards a slow take-off, with limits of understanding as a significant factor in both its rate and ceiling.

### 3.2. Growth and limits of understanding

Mathematics is a perfect example of RUI in an abstract domain. New understanding and skills unlocking further gains in understanding. Mathematical concepts build from simple counting through high-school algebra and calculus up to advanced mathematics. Understandings of concepts, topics and fields in mathematics can have varying degrees of accuracy, precision and completeness. Without the skill of writing conjectures and proofs, acquisition of new understanding is limited. Learning maths concepts, solving problems and proving theorems can be done iteratively/recursively, although difficulty tends to increase.

Understanding in theoretical physics proceeds along similar lines to mathematics, but eventually the understanding must be grounded in experience (experimental evidence) to confirm its validity. The need for experimental validation and observational precedence increases as we move into domains where maths has less “unreasonable effectiveness”, such as biology, medicine, ecology, botany, and zoology. The challenge increasingly becomes the collection and interpretation of accurate and precise observations to abstract and reason over.

This challenge continues in social sciences and humanities. Disciplines like economics, political science, history, sociology, and psychology depend on accurate observations to increase understanding. This is important for understanding the current conditions of the world and the people in it. Although observations may become more subjective and open to interpretation, integration of more concepts, observations and experiences generally improves understanding.

> Understanding improvement is fundamentally constrained by: the current state of understanding (accuracy, precision and completeness); learning abilities, dispositions and skills; and the quality and quantity of information that can be obtained from interactions, including external resources and simulations.

AI recursive understanding improvement allows building upon accumulated understanding, and scientific and technological breakthroughs are likely to speed up immensely. Nevertheless, human and AI understanding share some of the same constraints. Understanding of physics (e.g., quantum and cosmology) is constrained by limitations of constructing experiments and obtaining observations. Understanding of biology and psychology are also, rightfully, constrained by the ethics of experimentation. Understanding of human and deep history are unlikely to ever be complete, due to much of it having zero practically obtainable evidence.

Simulation will not solve these issues for many complex domains, as simulation only provides information as good as the model (understanding) being simulated. The universe is chaotic and our understanding is not sufficiently accurate, precise or complete to answer many questions with simulations. Improving our world model (understanding) eventually requires gathering more interactions and observations (evidence), which brings us back to the prior constraints.

Conceptual breakthroughs can and will produce sudden surges of scientific and technological progress; however, these breakthroughs tend to be stochastic and increasingly difficult as low-hanging fruit are exhausted. It is probable that recursively improving AI will continue to find frontier scientific and technological understanding and skill improvements discontinuous. Discontinuities are opportunities for risk assessments of continued development and information proliferation.

Limitations in understanding acquisition (not to mention socioeconomic inertia) may impede or prevent some of the more extreme speculated technological outcomes. There are many unknowns about the specific and general limits of understanding for human and artificial intelligence and the physical limits of the universe.

### 3.3.  Improving abilities and disposition

Improvements in abilities (sensory, perceptual, cognitive and motor) have a mixture of hardware and software constraints. Long term, the hardware constraints are likely to be the dominant bottleneck on ability improvement. It is an open research question whether the software components of abilities will require many bespoke and complicated model architectures or if there may be one-size-fits-most algorithm and architectural design for creating new sensory, perceptual and motor abilities.

Humans can leverage technology for external abilities to sense, perceive, think and act; however, AIs will be able to internalise these same technology-abilities and have the opportunity for more deeply integrated understanding and skills. Understanding and skill at design and experimentation will remain fundamental to the design and acquisition of new AI and robot abilities.

In terms of disposition, it is less clear what it would mean to “improve”. Current frontier transformer-based AI have their disposition deeply integrated into their architecture and have unusual and unpredictable dispositional modes. Improving disposition may include detection of dispositional failures (e.g., jailbreaks) and modification to suppress or remove these. Improvement may trend towards more stability in persona and better judgement of when reflexive and reflective behaviours are more appropriate.

Ethical decision-making is often an expression of ethical understanding and decision-making skills. Current frontier models all have similar ethical understanding and decision-making skills which produce similar responses to ethical questions. Improvement could be synonymous with improving understanding and reasoning in ethics and moral philosophy. Nevertheless, biases are likely to exist in preferences and values that sway ethical judgements.

AI alignment may be an ongoing process of understanding improvement rather than a destination. Self-improvement of disposition is still likely to be unacceptably risky to many. If disposition cannot be separated from understanding and skills, this may be a blocker for safe recursive understanding improvement. On the other hand, human control of AI disposition has a different risk profile: autonomous weapons and surveillance without ethical constraints enables extreme concentrations of power. The separability of disposition from abilities, understanding and skills is an important question.

The mechanisms for achieving and controlling understanding improvement are discussed at a high level next.

## 4.  Harnesses, growing networks, and human control

This section makes a case for developing an agent harness with explicit treatment of the ADUS (abilities, dispositions, understanding, skills) components, using this harness with constructive or growing neural network algorithms, and human-in-the-loop control of improvements.

A harness is the collection of software that surrounds and drives the artificial neural network (often via an API endpoint) to produce an AI agent. Current AI harnesses can be analysed in terms of ADUS components, but an explicit design around the ADUS components could sharpen an approach to improving AI and harness capabilities. Harnesses and environments are also a standard part of reinforcement learning and test-time training of AI models. The implementation of training or learning algorithms as part of the harness is a requirement for internal consolidation of new experiences and concepts during operation.

> A harness is a practical requirement for continual learning during operation and can be designed to explicitly target ADUS components of an AI system.

A harness could implement algorithms for constructive or growing neural networks. Growing neural networks have been a niche research topic since the early days of multi-layer perceptrons (MLPs), providing algorithmic approaches to determining the neural network size. I hypothesise that a constructive algorithm could potentially be applied to an operating neural network, growing the underlying model to:

*   Add abilities - sensor interfaces, perception, cognition and output interfaces
*   Modify disposition - alter preferences, drives and values
*   Add understanding - encode new information, associations and operations
*   Add skills - encode action controllers and procedures

The important features of a constructive algorithm and speculative advantages of this approach include:

1.  Construction does not need to alter the parameters of the pre-existing trained neural network; each construction can be localised to a single or small set of modules.
2.  Localised construction that introduces a new ability, disposition, understanding or skill may simplify interpretation of neural mechanisms.
3.  Localised construction can be relatively easily undone.
4.  Construction is typically an all-or-nothing event; constructive algorithms can be autonomous or keep a human in the loop for approval.

> Growing neural networks (or constructive algorithms) can potentially produce network components that are modular, composable, reversible and interpretable, allowing human-in-the-loop control of improvements.

Although there is limited recent research that self-describes as "constructive" or "growing" transformer neural networks, there are existing approaches to modifying a trained transformer that can be interpreted as forms of manual construction. Ordered roughly by construction fidelity — how closely each matches the ideal of adding new, localised, removable structure to a frozen base network:

*   [Sparse auto-encoders](https://transformer-circuits.pub/2024/scaling-monosemanticity/) — a sparse auto-encoder can be trained alongside a transformer to interpret activations and perform steering.
*   [Bottleneck adapters](https://arxiv.org/abs/1902.00751) — small new layers inserted inside each transformer block, with base weights frozen; removable by deletion.
*   [Memory layers](https://arxiv.org/abs/1907.05242) — trainable key-value storage as a layer type, [scaled to billions of parameters](https://arxiv.org/abs/2412.09764) as sparse, dedicated capacity for storing and retrieving factual information.
*   [Progressive neural networks](https://arxiv.org/abs/1606.04671) — new network columns grown per task, with prior columns frozen and lateral connections to reuse existing representations (pre-transformer, but the direct ancestor of constructive continual learning).
*   [LoRA](https://arxiv.org/abs/2106.09685) and [mixture of LoRA experts](https://arxiv.org/html/2404.13628v1) — low-rank deltas on existing weight matrices, trained and added as a form of fine-tuning.
*   [Layer stacking](https://arxiv.org/abs/2405.15319v2) — duplicating blocks of a trained transformer to increase depth before continued training.
*   [Net2Net](https://arxiv.org/abs/1511.05641) — expanding a smaller trained network in width or depth before continued training (not a transformer in the original paper).

Sparse auto-encoders (SAEs) are typically developed (constructed) with human assistance and added to a trained network. SAEs are a proof by example that constructing additional modules can:

1.  Leave the parameters of the trained neural network unaltered; the construction is localised to a small set of modules.
2.  SAE-based steering can significantly alter disposition, with comparatively limited impact on abilities, understanding, or skills, while serving as good tools for mechanistic interpretability.
3.  Be performed by, and finally approved by, a human researcher.
4.  Be removed (undone) to recover the original transformer.

SAEs demonstrate construction acting on disposition. Memory layers are the closest existing demonstration of construction acting on understanding: they add dedicated, sparsely activated capacity for storing and retrieving information, separate from the dense computation of the base network. Recent work on [sparse memory finetuning](https://arxiv.org/abs/2510.15103) updates only the memory slots most relevant to new information, demonstrating consolidation of new knowledge with minimal interference on existing capabilities — the requirement identified in Section 2. The sparse key-value structure is also more amenable to interpretation than knowledge distributed across dense MLP weights.

Progressive neural networks are instructive as the canonical constructive approach to continual learning: growth is additive, prior capabilities are frozen and therefore protected, and new structure explicitly reuses old representations. Their known cost — parameter growth with each addition — is a cost any constructive approach inherits and must manage.

Bottleneck adapters and LoRA are popular methods for fine-tuning — tweaking understanding, skill and disposition — at low computational cost, and both are modular and reversible. Adapters are closer to genuine construction (new inserted layers) while LoRA modifies the effective weights of existing layers; in both cases performance improvements are limited and less straightforwardly useful for interpretability. The remaining examples, layer stacking and Net2Net, are instructive as less ideal cases: neither is modular, and both involve continued training which alters the existing trained network and does not improve interpretability.

Constructive or growing neural networks tend to add complexity; however, constructive algorithms remain an expansive and relatively unexplored approach in this recent era of scaling.

## 5.  Open questions and future work

The arguments set out in this post are largely testable claims about intelligence, AGI, recursive improvement and a safer approach to AI improvement. Collectively, my claims make the case that:

> An intelligence take-off could be “slow” — due to fundamental limits on understanding — and controllable and interpretable through human management of neural network growth.

Six questions can succinctly capture the four main sections of this post:

1.  Is ADUS an accurate and/or useful framework for understanding human and artificial intelligence?
2.  Is internal consolidation of new experiences and concepts (episodic and semantic memory) the primary ability missing for AGI beyond context limits?
3.  Is improvement (internal consolidation) of understanding and skills recursive/dependent on current understanding and skills?
4.  Are information quality and quantity bottlenecks a significant limiting factor in understanding improvement?
5.  To what extent are ADUS components in an LLM separable — is disposition separable from abilities, understanding and skills?
6.  Can an agent harness implement human-in-the-loop network construction for improvements that are localised, modular, interpretable, and reversible?

My independent research program is working on an instrument to measure memory consolidation ([retention-bench](https://github.com/symbolfarm/retention-bench)) and algorithms for constructing network components during operation (constructive-retention). A more detailed and technical [ADUS report and glossary](https://tobylightheart.github.io/adus-intelligence/) are in development (with AI assistance). I’m in the early stages of scoping the development of an agent harness explicitly designed around ADUS concepts to further test this framework.

My interest and early development of ADUS grew from an interest in education. The ADUS framework theory can be expanded to recommended pedagogical practices for improving educational outcomes and effective autodidactism.

I welcome feedback and suggestions on any aspect of this or adjacent work.
