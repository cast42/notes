---
type: source
source_url: "https://rlhfbook.com/"
canonical_url: "https://rlhfbook.com/"
resource: "https://rlhfbook.com/"
title: Reinforcement Learning from Human Feedback
author: Nathan Lambert
date: 2026-08-07
timestamp: 2026-08-07
created_at: 2026-08-07
topics: [books]
tags: [rlhf, llm-post-training, preference-learning, reward-modeling, reinforcement-learning, model-evaluation]
description: Full text extracted from Nathan Lambert's book on RLHF and language-model post-training.
content_hash: 23bd131d72ac5e57d2eff139f9a53fd2de49b8855a127696f00621b9783726f1
extracted_at: "2026-08-12T16:18:33"
extractor: "pypdf 6.1.0 text extraction from https://rlhfbook.com/book.pdf"
---

# Raw content

Source: https://rlhfbook.com/


Reinforcement Learning from Human Feedback
A short introduction to RLHF and post-training focused on language models.
Nathan Lambert
07 August 2026
Abstract
Reinforcement learning from human feedback (RLHF) has become a crucial tool
to build the latest machine learning systems at scale. The field grew around the core
methods of RLHF into today’s broader suite of post-training techniques. In this book,
we give a comprehensive introduction to the core methods for post-training models
for people with some level of quantitative background, organized around the canonical
RLHF recipe. The book starts with what RLHF does and why it was created, with
seminal technical milestones in its young history and a primer on reinforcement learning
context needed to understand the book. The core of the book details every optimization
stage in using RLHF, from starting with instruction tuning to training a reward model
and finally all of rejection sampling, reinforcement learning, on-policy distillation, and
direct alignment algorithms. The book also discusses broader topics, such as the origins
of RLHF – both in recent literature and in a convergence of disparate fields of science in
economics, philosophy, and optimal control. The book concludes with advanced topics
– understudied or emerging research questions in synthetic data, tool-use, character
training, and evaluation – and open questions for the field. The book is released
with a variety of companion resources, including a codebase, a library to compare
model completions from within post-training stages, and an educational course, to be a
one-stop shop for learning all foundational concepts for post-training language models.

Contents
1 Introduction 7
1.1 RLHF in Three Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.2 What Does RLHF Do? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3 Walkthrough of an RLHF Recipe . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.4 An Intuition for Post-Training . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.5 How We Got Here . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
1.6 Scope of This Book . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.6.1 Chapter Summaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.6.2 Target Audience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
1.6.3 How to Use This Book . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
1.6.4 About the Author . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
1.7 Future of RLHF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2 A Tiny History of RLHF 18
2.1 Origins to 2018: RL on Preferences . . . . . . . . . . . . . . . . . . . . . . . . 18
2.2 2019 to 2022: RL from Human Preferences on Language Models . . . . . . . 19
2.3 2023 to the Present: The ChatGPT Era . . . . . . . . . . . . . . . . . . . . . 20
3 Training Overview 21
3.1 Problem Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.1.1 A Simple Example: The Thermostat . . . . . . . . . . . . . . . . . . . 22
3.1.2 Classic RL Example: CartPole . . . . . . . . . . . . . . . . . . . . . . 23
3.1.3 Manipulating the Standard RL Setup . . . . . . . . . . . . . . . . . . 24
3.1.4 Fine-Tuning and Regularization . . . . . . . . . . . . . . . . . . . . . . 25
3.1.5 Optimization Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.1.6 Subtle Advantages of RL in Post-Training Language Models . . . . . . 27
3.2 Canonical Training Recipes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2.1 InstructGPT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2.2 Tülu 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.2.3 DeepSeek R1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4 Instruction Fine-Tuning 31
4.1 Chat Templates and the Structure of Instructions . . . . . . . . . . . . . . . . 31
4.2 Best Practices for Instruction Tuning . . . . . . . . . . . . . . . . . . . . . . . 34
4.3 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.4 Suggested Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5 Reward Modeling 37
5.1 Training a Bradley-Terry Reward Model . . . . . . . . . . . . . . . . . . . . . 37
5.1.1 The Default Reward Model Architecture . . . . . . . . . . . . . . . . . 40
5.1.2 Implementation Example . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.2 Outcome Reward Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.3 Process Reward Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.4 Comparing Reward Model Types (and Value Functions) . . . . . . . . . . . . 47
5.4.1 Inference Across Reward Model Types . . . . . . . . . . . . . . . . . . 49
5.5 Other Reward Model Variants . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5.5.1 Preference Margin Loss . . . . . . . . . . . . . . . . . . . . . . . . . . 50
rlhfbook.com 2

5.5.2 Balancing Multiple Comparisons Per Prompt . . . . . . . . . . . . . . 50
5.5.3 K-Wise Loss Function . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
5.6 Generative Reward Modeling (a.k.a. LLM-as-a-judge) . . . . . . . . . . . . . 51
5.7 Further Reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
5.8 Suggested Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6 Reinforcement Learning 54
6.1 The Role of Reinforcement Learning in RLHF . . . . . . . . . . . . . . . . . . 54
6.2 Policy Gradient Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
6.2.1 Deriving the Policy Gradient . . . . . . . . . . . . . . . . . . . . . . . 57
6.2.2 Vanilla Policy Gradient . . . . . . . . . . . . . . . . . . . . . . . . . . 60
6.2.3 REINFORCE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
6.2.4 REINFORCE Leave One Out (RLOO) . . . . . . . . . . . . . . . . . . 61
6.2.5 Proximal Policy Optimization (PPO) . . . . . . . . . . . . . . . . . . 62
6.2.6 Understanding the PPO Objective . . . . . . . . . . . . . . . . . . . . 65
6.2.7 Value Functions and PPO . . . . . . . . . . . . . . . . . . . . . . . . . 68
6.2.8 Group Relative Policy Optimization (GRPO) . . . . . . . . . . . . . . 70
6.2.9 Group Sequence Policy Optimization (GSPO) . . . . . . . . . . . . . . 73
6.2.10 Clipped Importance Sampling Policy Optimization (CISPO) . . . . . 74
6.2.11 Comparing Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
6.3 Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
6.3.1 Policy-Gradient Basics . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
6.3.2 Loss Aggregation Tradeoffs . . . . . . . . . . . . . . . . . . . . . . . . 79
6.3.3 Asynchronous RL Systems . . . . . . . . . . . . . . . . . . . . . . . . . 82
6.3.4 Truncated Importance Sampling . . . . . . . . . . . . . . . . . . . . . 84
6.3.5 Example: PPO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
6.3.6 Example: GRPO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.4 Auxiliary Topics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
6.4.1 Generalized Advantage Estimation (GAE) . . . . . . . . . . . . . . . . 90
6.4.2 Double Regularization . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
6.4.3 Further Reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
6.5 Suggested Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
7 Reasoning and Inference-Time Scaling 95
7.1 The Role of RLVR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
7.2 The Origins of New Reasoning Models . . . . . . . . . . . . . . . . . . . . . . 98
7.2.1 Why Does RL Work Now? . . . . . . . . . . . . . . . . . . . . . . . . . 99
7.2.2 RL Training vs. Inference-Time Scaling . . . . . . . . . . . . . . . . . 99
7.2.3 The Future (Beyond Reasoning) of RLVR . . . . . . . . . . . . . . . . 100
7.3 Understanding Reasoning Training Methods . . . . . . . . . . . . . . . . . . . 100
7.3.1 Reasoning Research Before OpenAI o1 or DeepSeek R1 . . . . . . . . 100
7.3.2 Early Reasoning Models . . . . . . . . . . . . . . . . . . . . . . . . . . 101
7.3.3 Common Practices in Training Reasoning Models . . . . . . . . . . . . 103
7.4 Looking Ahead . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
8 Direct-Alignment Algorithms 106
8.1 Direct Preference Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . 106
8.1.1 How DPO Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
rlhfbook.com 3

8.1.2 DPO Derivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
8.2 Numerical Concerns, Weaknesses, and Alternatives . . . . . . . . . . . . . . . 113
8.3 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
8.4 DAAs with Synthetic Preference Data . . . . . . . . . . . . . . . . . . . . . . 115
8.5 DAAs vs. RL: Online vs. Offline Data . . . . . . . . . . . . . . . . . . . . . . 116
8.6 Suggested Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
9 Rejection Sampling 118
9.1 Training Process, Step by Step . . . . . . . . . . . . . . . . . . . . . . . . . . 118
9.1.1 Generating Completions . . . . . . . . . . . . . . . . . . . . . . . . . . 119
9.1.2 Scoring Completions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
9.1.3 Fine-Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
9.2 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
9.3 Related: Best-of-N Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
9.4 Suggested Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
10 The Nature of Preferences 125
10.1 When Preference Replaces Correctness . . . . . . . . . . . . . . . . . . . . . . 125
10.2 The Origins of RLHF and Preferences . . . . . . . . . . . . . . . . . . . . . . 126
10.3 Specifying Objectives: From Logic of Utility to Reward Functions . . . . . . . 126
10.4 Tools for Optimizing Utility . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
10.5 Complexity of Optimizing Preferences . . . . . . . . . . . . . . . . . . . . . . 129
11 Preference Data 131
11.1 Why We Need Preference Data . . . . . . . . . . . . . . . . . . . . . . . . . . 131
11.2 Collecting Preference Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
11.2.1 Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
11.2.2 Rankings vs. Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
11.2.3 Multiturn Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
11.2.4 Structured Preference Data . . . . . . . . . . . . . . . . . . . . . . . . 139
11.2.5 Sourcing and Contracts . . . . . . . . . . . . . . . . . . . . . . . . . . 140
11.3 Bias: Things to Watch Out For in Data Collection . . . . . . . . . . . . . . . 142
11.4 Open Questions in RLHF Preference Data . . . . . . . . . . . . . . . . . . . . 142
12 Synthetic Data & Distillation 144
12.1 The Roles of Synthetic Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
12.2 Distillation with Synthetic Data . . . . . . . . . . . . . . . . . . . . . . . . . 145
12.3 The Path to On-Policy, Teacher-Student Distillation . . . . . . . . . . . . . . 146
12.3.1 Adapting Knowledge-Distillation for LMs . . . . . . . . . . . . . . . . 146
12.3.2 From Offline to On-Policy Distillation . . . . . . . . . . . . . . . . . . 148
12.3.3 Modern OPD Variants . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
12.3.4 Suggested Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . 151
12.4 AI Feedback . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
12.4.1 Balancing AI and Human Feedback Data . . . . . . . . . . . . . . . . 153
12.4.2 Building Specific LLMs for Judgment . . . . . . . . . . . . . . . . . . 154
12.5 Constitutional AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
12.5.1 Further Reading on CAI . . . . . . . . . . . . . . . . . . . . . . . . . . 156
12.6 Rubrics: Prompt-Specific AI Feedback for Training . . . . . . . . . . . . . . . 156
rlhfbook.com 4

13 Tool Use and Function Calling 160
13.1 Tool-Use Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
13.2 Interweaving Tool Calls in Generation . . . . . . . . . . . . . . . . . . . . . . 162
13.3 Multistep Tool Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
13.4 Model Context Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
13.5 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
14 Over-Optimization 169
14.1 Qualitative Over-Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . 169
14.1.1 Managing Proxy Objectives . . . . . . . . . . . . . . . . . . . . . . . . 169
14.1.2 Over-Refusal and “Too Much RLHF” . . . . . . . . . . . . . . . . . . 172
14.2 Quantitative Over-Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . 173
14.3 Misalignment and the Role of RLHF . . . . . . . . . . . . . . . . . . . . . . . 175
15 Regularization 176
15.1 KL Divergence in RL Optimization . . . . . . . . . . . . . . . . . . . . . . . . 176
15.1.1 Reference Model to Generations . . . . . . . . . . . . . . . . . . . . . 177
15.1.2 Implementation Example . . . . . . . . . . . . . . . . . . . . . . . . . 177
15.2 Other Tools to Control Optimization . . . . . . . . . . . . . . . . . . . . . . . 178
15.2.1 Pretraining Gradients in RL . . . . . . . . . . . . . . . . . . . . . . . . 178
15.2.2 Next-token Accuracy in DPO . . . . . . . . . . . . . . . . . . . . . . . 178
15.2.3 Margin-Based Regularization in Reward Modeling . . . . . . . . . . . 179
15.3 Implicit Regularization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
15.3.1 SFT Memorizes, RL Generalizes . . . . . . . . . . . . . . . . . . . . . 180
15.3.2 Retaining by Doing: On-Policy Data Mitigates Forgetting . . . . . . . 180
15.3.3 RL’s Razor: Why Online RL Forgets Less . . . . . . . . . . . . . . . . 183
16 Evaluation 186
16.1 Prompting Formatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
16.1.1 Few-Shot Prompting and Log-Likelihood Scoring . . . . . . . . . . . . 187
16.1.2 Chain-of-Thought Prompting . . . . . . . . . . . . . . . . . . . . . . . 189
16.1.3 Zero-Shot Instruction Following . . . . . . . . . . . . . . . . . . . . . . 189
16.1.4 Reasoning-Era Evaluation Prompts . . . . . . . . . . . . . . . . . . . . 190
16.1.5 The Complexity of Agentic Evaluations . . . . . . . . . . . . . . . . . 190
16.2 Why Many External Evaluation Comparisons Are Unreliable . . . . . . . . . 191
16.3 How Labs Actually Use Evaluations Internally to Improve Models . . . . . . 192
16.4 Contamination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
16.5 Tooling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
17 Crafting Model Character and Products 196
17.1 Character Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
17.1.1 Persona Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
17.1.2 The Assistant Axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
17.1.3 Persona Subnetworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
17.2 Model Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
17.3 Product Cycles and What’s Next for RLHF . . . . . . . . . . . . . . . . . . . 206
Bibliography 208
rlhfbook.com 5

A Definitions 230
A.1 Language Modeling Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
A.2 Machine Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
A.3 Natural Language Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
A.4 Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
A.5 RLHF-Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
A.6 Extended Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
B Beyond “Just Style” 234
B.1 The Chattiness Balance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
C Practical Issues 239
C.1 Compute Costs of Post-Training . . . . . . . . . . . . . . . . . . . . . . . . . 239
C.2 Evaluation Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
C.3 Managing Training Performance Variance . . . . . . . . . . . . . . . . . . . . 240
C.4 Identifying Bad Training Jobs . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
rlhfbook.com 6

1 Introduction
Reinforcement learning from human feedback (RLHF) is a technique used to incorporate
human information into AI systems. RLHF emerged primarily as a method to solve hard-
to-specify problems. With systems that are designed to be used by humans directly, such
problems emerge all the time due to the often inexpressible nature of an individual’s
preferences. This encompasses every domain of content and interaction with a digital system.
RLHF’s early applications were often in control problems and other traditional domains for
reinforcement learning (RL), where the goal is to optimize a specific behavior to solve a task.
The core idea to start the field of RLHF was, “Can we solve hard problems only with basic
preference signals guiding the optimization process?” RLHF became most known through
the release of ChatGPT and the subsequent rapid development of large language models
(LLMs) and other foundation models.
1.1 RLHF in Three Steps
The basic pipeline for RLHF involves three steps. First, a language model that can follow
user questions must be trained (see Chapter 4). Second, human preference data must be
collected for the training of a reward model of human preferences (see Chapter 5). Finally,
the language model can be optimized with an RL optimizer of choice, by sampling generations
and rating them with respect to the reward model (see Chapters 3 and 6). This book details
key decisions and basic implementation examples for each step in this process.
RLHF has been applied to many domains successfully, with complexity increasing as the
techniques have matured. Early breakthrough experiments with RLHF were applied to
deep reinforcement learning \[1\], summarization \[2\], following instructions \[3\], parsing web
information for question-answering \[4\], and “alignment” \[5\]. A summary of the early RLHF
recipes is shown below in fig. 1.
Figure 1: A rendition of the early, three stage RLHF process with SFT, a reward model,
and then optimization.
In modern language model training, RLHF is one component of post-training. Post-training
is a more complete set of techniques and best practices to make language models more useful
for downstream tasks \[6\]. Post-training can be summarized as a many-stage training process
using three optimization methods:
1. Instruction / Supervised Fine-tuning (IFT/SFT), where we teach formatting and form
the base of instruction-following abilities. This is largely about learningfeaturesin
rlhfbook.com 7

language.
2. Preference Fine-tuning (PreFT), where we align to human preferences via RLHF and
related methods (and get a smaller bump in capabilities at the same time). This is
largely aboutstyleof language and subtle human preferences that are hard to quantify.
3. Reinforcement Learning with Verifiable Rewards (RLVR), the newest type of post-
training that boosts performance on verifiable domains with more RL training.
RLHF lives within and dominates the second area,preference fine-tuning, which has more
complexity than instruction tuning because it often involves proxy reward models of the true
object and noisier data. At the same time, RLHF is far more established than the other
popular RL method for language models, reinforcement learning with verifiable rewards. For
that reason, this book focuses on preference learning, but in order to completely grasp the
role of RLHF, one needs to use these other training stages, so they are also explained in
detail.
As we consider the space of options and attention on these methods for crafting models we
collectively use extensively, RLHF colloquiallyiswhat led to modern post-training. RLHF
was the technique that enabled the massive success of the release of ChatGPT, so early in
2023 RLHF encompassed much of the interest in the general field of post-training. RLHF is
now just one piece of post-training, so in this book we map why there was so much attention
on RLHF early on, and how other methods emerged to complement it.
Training language models is a very complex process, often involving large technical teams of
10s to 100s of people and millions of dollars in data and compute costs. This book serves
three purposes to enable readers to grasp how RLHF and related models are used to craft
leading models. First, the book distills cutting-edge research often hidden within large
technology companies into clear topics and trade-offs, so readers can understand how models
are made. Second, the book will allow users to set up basic code examples to get their hands
dirty on fine-tuning these models themselves. Finally, beyond teaching the techniques for
doing RLHF, this book is designed to distill intuition as towhyRLHF is crucial to modern
AI models.
Due to the complexity of RLHF and how the state-of-the-art is often too complex to be
done alone, this book focuses on enabling readers so they have the tools needed to get jobs
and start research projects in the area. Others will just enjoy precisely understanding the
inner workings of the technology that is the focus of countless discussions across the globe.
A book that lays out an exact recipe of how to do RLHF for a specific need is impossible,
which is why there is a large industry of companies providing RLHF training and related
methods as a service worth millions of dollars. Still, rapid progress in AI systems means the
readers who are equipped with this knowledge can approach more and more of their own
training over time.
1.2 What Does RLHF Do?
The biggest question around RLHF, yet one that is still hard to answer, is “What does
RLHF training offer models?” In recent years, language models have shifted from academic
experiments studied in the purview of benchmarks to general-purpose technology. RLHF is
at the core of this transition.
To start, let us consider how a language model at the end of autoregressive pretraining
answers a query. A strong model, Llama 3.1 405B Base, will continue from “The president
rlhfbook.com 8

of the united states in 2006 was”:
Response: George W. Bush, the governor of Florida in 2006 was Jeb Bush,
and John McCain was an Arizona senator in 2006 - who later lost to obama.
September 1 – U.S. President Bush signs an executive order to provide more
options for faith-based organizations when delivering social services that are paid
for with federal funds. January 1 – The current deadline set by United States
Congress in the Unlawful Internet Gambling Enforcement Act, aka UIGEA.
search: Amendments to the 1961 International Convention for the Protection of
New Varieties of Plants require plant breeders’ rights include farmer’s privilege.
2009 was a common year starting on Thursday of the Gregorian calendar, the
2009th year of the Common Era (ce) and Anno Domini (ad) designations, the
9th year of the 3rd millennium, the 9th year of the 21st century, and the 10th
and last year of the 2000s decade.
What is clear is that this model is completing the sentence and adding other common internet
metadata.
In contrast, a model trained with RLHF (and other post-training tools) would answer the
question very differently. Asking Tülu 3 405B the same question “The president of the united
states in 2006 was,” it says concisely:
Response: George W. Bush was the president of the United States in 2006. He
served two terms in office, from January 20, 2001, to January 20, 2009.
This change in style is downstream of the post-training methods described in this book.
The most compelling view of how RLHF works is to consider howstyleapplies to interactions
you have with language models. The style, closely related to tone or format, of information
presented is crucial to how it is learned. Style is often used to describe the manner of the
model. To see the difference, consider two example responses to the following question:
User: Help, I have to give a presentation tomorrow and I’m panicking.
A blunt, low-empathy style:
Response: You’ll be fine. Practice your slides a few times, get some sleep, and
stop overthinking it. Just present what you know and move on.
A warmer, more supportive style:
Response: That sounds really stressful, and it’s a normal reaction. If you can,
do one quick practice run now, pick the one or two points you most want people
to remember, and then give yourself permission to rest—being clear and calm
tomorrow will matter more than cramming tonight.
On the other hand, format is how the answer is structured. Modern models are known to use
extensive Markdown formatting with lists, line breaks, and emojis. Consider two answers to
the following question that are very different:
User: How can I improve my sleep quality?
The simple answer, from an early language model:
rlhfbook.com 9

Response: Try to go to bed at the same time each night, avoid caffeine late in
the day, and keep your bedroom quiet and dark.
Or a complex, richer answer:
Response: Better sleep, in practice
Goal: make your schedule predictable and your environment boring enough that
your brain gives up.
Tonight (quick wins):
1. Dim lights for the last hour before bed.
2. No caffeine after lunch; keep alcohol minimal.
3. If you’re stuck awake, get up and do something quiet until sleepy again.
Daily basics (most impact):
•Same wake time (even weekends) –> anchors your body clock.
•Morning light for 5-10 minutes –> helps set circadian rhythm.
•Cool, dark room (fan/eye mask) –> easier to stay asleep.
If you want a simple rule: wake time fixed + caffeine cutoff +
wind-down routine
If sleep problems are persistent or severe, it can be worth talking with a clini-
cian—many issues are very treatable.
Instruction fine-tuning would provide the basic ability for models to respond reliably in the
question-answering format, and RLHF is what takes these answers and crafts them into the
reliable, warm, and engaging answers we now expect from language models.
Modern research has established RLHF as a general method to integrate subtle stylistic
and related behavioral features into the models. An early, popular example of the utility
of RLHF was in the application to safety \[7\] \[5\], where RLHF enabled models to be both
helpful and harmless across varied datasets. Compared to other techniques for post-training,
such as instruction fine-tuning, RLHF generalizes far better across domains \[8\] \[9\] – helping
create effective general-purpose models.
Intuitively, this can be seen in how the optimization techniques are applied. Instruction
fine-tuning trains the model to predict the next token when the text preceding is close to
examples it has seen. It is optimizing the model to more regularly output specific features in
text. This is a per-token update.
RLHF on the other hand tunes completions on the response level rather than looking at the
next token specifically. Additionally, it is telling the model what abetterresponse looks like,
rather than a specific response it should learn. RLHF also shows a model which types of
responses it should avoid, i.e. negative feedback. The training to achieve this is often called
acontrastiveloss function (one whose loss is computed from the comparison between two or
more examples, rather than from each example independently) and is referenced throughout
this book.
While this flexibility is a major advantage of RLHF, it comes with implementation challenges.
Largely, these center onhow to control the optimization.As we will cover in this book,
implementing RLHF often requires training a reward model, but best practices for doing
rlhfbook.com 10

so are not strongly established and depend on the area of application. With this, the
optimization itself is prone toover-optimizationbecause our reward signal is at best a
proxy objective, requiring regularization. With these limitations, effective RLHF requires a
strong starting point, so RLHF cannot be a solution to every problem alone and needs to be
approached through a broader lens of post-training.
Due to this complexity, implementing RLHF is far more costly than simple instruction
fine-tuning and can come with unexpected challenges such as length bias \[10\] \[11\]. For model
training efforts where absolute performance matters, RLHF is established as being crucial to
achieving a strong fine-tuned model, but it is more expensive in compute, data costs, and
time. Through the early history of RLHF after ChatGPT, there were many research papers
that showed approximate solutions to RLHF via limited instruction fine-tuning, but as the
literature matured it has been repeated time and again that RLHF and related methods are
core stages of model performance that cannot be easily dispensed with.
1.3 Walkthrough of an RLHF Recipe
To set the stage for the book, it’s important to understand what “doing RLHF” can look like,
as a minimal example, without any of the technical jargon that can be hard to grasp before
solidifying fundamental intuitions. This section follows what is described as the canonical,
three-stage RLHF recipe, as established with OpenAI’s InstructGPT model in 2022 \[3\].
The first step of the process is to transition the model from a base model that completes
text to an instruction-following model that can operate in a question-answering format. This
is done by using the same next-token prediction loss function on a set of carefully crafted
datapoints where the model is shownonlydata in this question-answering format. After the
model is shown these high-quality responses, the model can now be prompted with a specific
sequence of tokens to know that it should answer any query with a more defined, assistant
persona.
With this foundation ofthe shape of how the model should answer, the next two steps work
together to improve the overall quality of the answers. These two steps serve to set up a
problem where we can use reinforcement learning to update the model and make it more
helpful.
The first of these two steps is to train a reward model that captures human preferences.
In order to apply reinforcement learning to a problem, you need a reward function that
indicates quality. The goal of a reward model is to create a scalar signal that can then
later be optimized with RL. In practice, this involves fine-tuning a language model (it is
usually the same instruction-tuned model from the previous step) on a dataset of preference
relations between pieces of text. This dataset is collected across a variety of prompts, model
completions, and labelers to try and capture a robust signal of what is a better answer from
a language model. The reward model learns which features in the text are better than others,
so when it is used at inference-time (and during RL as the reward signal) it scores any piece
of input text on how good it is.
With these two pieces, a question-answering model and a reward model, we have everything
we need to put together the pieces and actually do reinforcement learning from human
feedback (RLHF). The actual RLHF stage proceeds by taking prompts representative of
tasks the model should be good at, generating a bunch of completions, having the reward
model rank them, and then using RL to figure out how to change the model and make it
rlhfbook.com 11

better. The basic primitive is that reinforcement learning is given a signal of which actions
are good, in the form of tokens that a language model generates, and derives update rules
that attribute different actions to different parameters in the model. The final RLHF stage
shifts parameters to make good tokens more likely, and does so iteratively to maintain the
general capabilities of the initial model.
Once RL is complete, and performance has saturated, this is often the final model served to
the user.
Throughout this book, we’ll cover many recipes for how to do RLHF, and more related
optimization methods that make up the broader suite of post-training. These all emerge to
solve more challenging problems facing language models, and to make the strengths of the
original RLHF approaches more powerful.
1.4 An Intuition for Post-Training
We’ve established that RLHF specifically and post-training generally are crucial to the
performance of the latest models and how they change the models’ outputs, but not why
RLHF works. Here’s a simple analogy for how so many gains can be made on benchmarks
on top of any base model.
The way I’ve been describing the potential of post-training is called the elicitation interpre-
tation of post-training, where all we are doing is extracting potential by amplifying valuable
behaviors in the base model.
To make this example click, we make the analogy between the base model – the language
model that comes out of the large-scale, next-token prediction pretraining – and other
foundational components in building complex systems. We use the example of the chassis of
a car, which defines the space around which a car can be built. Consider Formula 1 (F1):
most teams begin each year with a new chassis and engine. Then, they spend all year on
aerodynamics and systems changes (of course, it is a minor oversimplification), and can
dramatically improve the performance of the car. The best F1 teams improve far more
during a season than chassis-to-chassis.
The same is true for post-training, where one can extract a ton of performance out of a
static base model as they learn more about its quirks and tendencies. The best post-training
teams extract a ton of performance in a very short time frame. The set of techniques
includes everything close to and after the end of pretraining: “mid-training” like annealing /
high-quality end of pretraining web data, instruction tuning, RLVR, preference-tuning, etc.
A good example is the change from the first version of the Allen Institute for AI’s fully-open,
small Mixture-of-Experts (MoE) model OLMoE Instruct to the second. The first model was
released in the fall of 2024 \[12\], and with the second version only updating the post-training,
the evaluation average on popular benchmarks went from 35 to 48 without changing the
majority of pretraining \[13\].
The idea is that there is a lot of intelligence and ability within base models, but because they
can only answer in next-token prediction and not question-answering format, it takes a lot of
work building around them, through post-training, in order to make excellent final models.
Then, when you look at models such as OpenAI’s GPT-4.5 released in February 2025, which
was largely a failure of a consumer product due to being too large of a base model to serve
to millions of users, you can see this as a far more dynamic and exciting base for OpenAI to
rlhfbook.com 12

build onto. With this intuition, base models determine the vast majority of the potential of
a final model, and post-training’s job is to cultivate all of it.
I’ve described this intuition as the Elicitation Theory of Post-training. This theory folds in
with the reality that the majority of gains users are seeing are from post-training because it
implies that there is more latent potential in a model pretrained on the internet than we can
simply teach the model — such as by passing certain narrow samples in repeatedly during
early types of post-training (i.e. only instruction tuning). The challenge of post-training
is to reshape models from next-token prediction to conversation question-answering, while
extracting all of this knowledge and intelligence from pretraining.
A related idea to this theory is the Superficial Alignment Hypothesis, coined in the paper
LIMA: Less is More for Alignment \[14\]. This paper is getting some important intuitions
right but for the wrong reasons in the big picture. The authors state:
A model’s knowledge and capabilities are learnt almost entirely during pretraining,
while alignment teaches it which subdistribution of formats should be used when
interacting with users. If this hypothesis is correct, and alignment is largely
about learning style, then a corollary of the Superficial Alignment Hypothesis is
that one could sufficiently tune a pretrained language model with a rather small
set of examples.
All of the successes of deep learning should have taught you that scaling data is important
to performance. Here, the major difference is that the authors are discussing alignment and
style, the focus of academic post-training at the time. With a few thousand samples for
instruction fine-tuning, you can change a model substantially and improve a narrow set of
evaluations, such as AlpacaEval, MT-Bench, Arena (formerly Chatbot Arena, a platform
where users compare anonymous model responses head-to-head), and the like. These do
not always translate to more challenging capabilities, which is why Meta wouldn’t train
its Llama Chat models on just this dataset. Academic results have lessons, but need to be
interpreted carefully if you are trying to understand the big picture of the technological arc.
What this paper is showing is that you can change models substantially with a few samples.
We knew this, and it is important to the short-term adaptation of new models, but their
argument for performance leaves the casual readers with the wrong lessons.
If we change the data, the impact could be far higher on the model’s performance and
behavior, but it is far from “superficial.” Base language models today (with no post-training)
can be trained on some mathematics problems with reinforcement learning, learn to output
full chain-of-thought reasoning, and then score higher on a full suite of reasoning evaluations
like BigBenchHard, Zebra Logic, AIME, etc.
The superficial alignment hypothesis is wrong for the same reason that people who think
RLHF and post-training are just for vibes are still wrong. This was a field-wide lesson
we had to overcome in 2023 (although many AI observers are still rooted in this belief).
Post-training has far outgrown that, and we are coming to see that the style of models
operates on top of behavior — such as the now popular long chain of thought.
As the AI community shifts post-training further into the era of agentic and reasoning models,
the superficial alignment hypothesis breaks down further. RL methods are becoming an
increasingly large share of the compute needed to train frontier language models. In the
short time since reinforcement learning with verifiable rewards (RLVR) was coined in our
rlhfbook.com 13

work on Tülu 3 in the fall of 2024 \[6\], the scale of compute used for post-training has grown
dramatically. DeepSeek R1, famous for popularizing RLVR, used only about 5% of their
overall compute in post-training – 147K H800 GPU hours for RL training on R1 \[15\], relative
to 2.8M GPU hours for pretraining the underlying DeepSeek V3 base model \[16\].
The science studying the core methods of scaling RL as of 2026 shows that individual ablation
runs can take 10-100K GPU hours \[17\], the equivalent of the compute used for the RL
stage of Olmo 3.1 Think 32B (released in November of 2025), which trained for 4 weeks
on 200 GPUs \[18\]. The science of scaled post-training is in its very early stages as of 2026,
adopting ideas and methods from pretraining language models and applying them in this
new domain, so the exact GPU hours used will change, but the trend of increased compute
on post-training will continue. Altogether, the elicitation theory of post-training is likely
to become the correct view only when applying a lighter post-training recipe – something
useful for specializing a model – relative to the compute-intensive frontier models.
1.5 How We Got Here
Why does this book make sense now? How much will change in the future?
Post-training, the craft of eliciting powerful behaviors from a raw pretrained language model,
has gone through many seasons and moods since the release of ChatGPT that sparked the
renewed interest in RLHF. In the era of Alpaca \[19\], Vicuna \[20\], Koala \[21\], and Dolly
\[22\], a limited number of human datapoints with extended synthetic data in the style of
Self-Instruct were used to fine-tune the original LLaMA to get similar behavior to ChatGPT.
The benchmark for these early models was fully vibes (and human evaluation) as we were all
so captivated by the fact that these small models can have such impressive behaviors across
domains. It was justified excitement.
Open post-training was moving faster, releasing more models, and making more noise than
its closed counterparts. Companies were scrambling, e.g. DeepMind merging with Google
Brain or new labs being started, and taking time to follow it up. There are phases of open
recipes surging and then lagging behind.
The era following Alpaca et al., the first lag in open recipes, was one defined by skepticism and
doubt about reinforcement learning from human feedback (RLHF), the technique OpenAI
highlighted as crucial to the success of the first ChatGPT. Many companies doubted that
they needed to do RLHF. A common phrase – “instruction tuning is enough for alignment”
– was so popular then that it still carries weight today despite obvious evidence against it.
This doubt about RLHF lasted, especially in the open where groups cannot afford data
budgets on the order of $100K to $1M. The companies that embraced it early ended up
winning out. Anthropic published extensive research on RLHF through 2022 and now has
arguably the best post-training \[23\] \[5\] \[24\]. The delta between open groups, struggling to
reproduce or even know of basic closed techniques, and leading closed models is a common
theme.
The first shift in open alignment methods and post-training was the story of Direct Preference
Optimization (DPO) \[25\], which showed that you can solve the same optimization problem as
RLHF with fewer moving parts by taking gradient steps directly on pairwise preference data.
The DPO paper, posted in May of 2023, didn’t have any clearly impactful models trained
with it through the fall of 2023. This changed with the releases of a few breakthrough DPO
rlhfbook.com 14

models – all contingent on finding a better, lower learning rate. Zephyr-Beta \[26\], Tülu 2
\[27\], and many other models showed that the DPO era of post-training had begun. Chris
Manning literally thanked me for “saving DPO.”
Preference-tuning was something you needed to do to meet the table stakes of releasing a good
model since late 2023. The DPO era continued through 2024, in the form of never-ending
variants on the algorithm, but we were very far into another slump in open recipes. Open
post-training recipes had saturated the extent of knowledge and resources available.
A year after Zephyr and Tülu 2, the same breakout dataset, UltraFeedback is arguably still
state-of-the-art for preference tuning in open recipes \[28\].
At the same time, the Llama 3.1 \[29\] and Nemotron 4 340B \[30\] reports gave us substantive
hints that large-scale post-training is much more complex and impactful. The closed labs are
doing full post-training – a large multi-stage process of instruction tuning, RLHF, prompt
design, etc. – where academic papers are just scratching the surface. Tülu 3 represented a
comprehensive, open effort to build the foundation of future academic post-training research
\[6\].
Post-training is a complex process involving the aforementioned training objectives applied
in various orders to target specific capabilities. This book is designed to provide a platform
for understanding all of these techniques, and as the field matures the best practices for how
to interleave them will emerge.
The primary areas of innovation in post-training are now in reinforcement learning with
verifiable rewards (RLVR), reasoning training generally, and related ideas. These newer
methods build extensively on the infrastructure and ideas of RLHF, but are evolving far
faster. This book is written to capture the first stable literature for RLHF after its initial
period of rapid change.
1.6 Scope of This Book
This book hopes to touch on each of the core steps of doing canonical RLHF implementations.
It will not cover all the history of the components nor recent research methods, just techniques,
problems, and trade-offs that have been proven to occur again and again.
1.6.1 Chapter Summaries
This book has the following chapters:
1.6.1.1 IntroductionsReference material and context useful throughout the book.
1. Introduction: Overview of RLHF and what this book provides.
2. A Tiny History of RLHF: Key models and papers in the history of RLHF techniques.
3. Training Overview: How the training objective for RLHF is designed and basics of
understanding it.
1.6.1.2 Core Training PipelineThe suite of techniques used to optimize language
models to align them to human preferences.
4. Instruction Fine-Tuning: Adapting language models to the question-answer format.
rlhfbook.com 15

5. Reward Modeling: Training reward models from preference data that act as an
optimization target for RL training (or for use in data filtering).
6. Reinforcement Learning: The core RL techniques used to optimize reward models (and
other signals) throughout RLHF.
7. Reasoning and Inference-Time Scaling: The role of new RL training methods for
inference-time scaling with respect to post-training and RLHF.
8. Direct-Alignment Algorithms: Algorithms that optimize the RLHF objective directly
from pairwise preference data rather than learning a reward model first.
9. Rejection Sampling: A basic technique for using a reward model with instruction
tuning to align models.
1.6.1.3 Data & PreferencesContext for the data that fuels RLHF and the big picture
problem it is trying to solve.
10. TheNatureofPreferences: Whyhumanpreferencedataisneededtofuelandunderstand
RLHF.
11. Preference Data: How preference data is collected for RLHF.
12. Synthetic Data: The shift away from human to synthetic data, how AI feedback works,
and how distilling from other models is used.
13. Tool Use and Function Calling: The basics of training models to call functions or tools
in their outputs.
1.6.1.4 Practical ConsiderationsFundamental problems and discussions for imple-
menting and evaluating RLHF.
14. Over-Optimization: Qualitative observations of why RLHF goes wrong and why
over-optimization is inevitable with a soft optimization target in reward models.
15. Regularization: Tools to constrain these optimization tools to effective regions of the
parameter space.
16. Evaluation: The ever evolving role of evaluation (and prompting) in language models.
17. Crafting Model Character and Products: How RLHF is shifting in its applicability as
major AI laboratories use it to subtly match their models to their products.
1.6.1.5 AppendicesReference material for definitions and extended discussions.
• Appendix A - Definitions: Mathematical definitions for RL, language modeling, and
other ML techniques leveraged in this book.
• Appendix B - Beyond “Just Style”: How RLHF is often underestimated in its role
in improving the user experience of models due to the crucial role that style plays in
information sharing.
1.6.2 Target Audience
This book is intended for audiences with entry level experience with language modeling, rein-
forcement learning, and general machine learning. It will not have exhaustive documentation
for all the techniques, but just those crucial to understanding RLHF.
rlhfbook.com 16

1.6.3 How to Use This Book
This book was largely created because there were no canonical references for important
topics in the RLHF workflow. Given the pace of progress on LLMs overall, combined with
the complex nature of collecting and using human data, RLHF is an unusually academic field
where published results are often noisy and hard to reproduce across multiple settings. To
develop strong intuitions, readers are encouraged to read multiple papers on each topic rather
than taking any single result as definitive. To facilitate this, the book includes numerous,
academic-style citations to the canonical reference for a claim.
The contributions of this book are supposed to give you the minimum knowledge needed to
try a toy implementation or dive into the literature. This isnota comprehensive textbook,
but rather a quick book for reminders and getting started.
The print edition of this book was published by Manning in July 2026, while the web version
continues to collect minor improvements and errata fixes. If you spot a typo or an important
omission, please contribute a fix or suggestion on GitHub.
1.6.4 About the Author
Dr. Nathan Lambert is a researcher and writer focusing on building the open science of
language models. He came here through a Ph.D. in robotics and building an RLHF team
shortly after the release of ChatGPT. He has released many models trained with RLHF, their
subsequent datasets, and training codebases in his time at the Allen Institute for AI (Ai2)
and Hugging Face. Examples include Zephyr-Beta, Tülu 2, OLMo, TRL, Open Instruct, and
many more. He has written extensively on RLHF, including many blog posts and academic
papers.
1.7 Future of RLHF
With the investment in language modeling, many variations on the traditional RLHF methods
emerged. RLHF colloquially has become synonymous with multiple overlapping approaches.
RLHF is a subset of preference fine-tuning (PreFT) techniques, including Direct Alignment
Algorithms (See Chapter 8), which are the class of methods downstream of DPO that
solve the preference learning problem by taking gradient steps directly on preference data,
rather than learning an intermediate reward model. RLHF is the tool most associated with
rapid progress in “post-training” of language models, which encompasses all training after
the large-scale autoregressive training on primarily web data. This textbook is a broad
overview of RLHF and its directly neighboring methods, such as instruction tuning and
other implementation details needed to set up a model for RLHF training.
As more successes of fine-tuning language models with RL emerge, such as OpenAI’s o1
reasoning models, RLHF will be seen as the bridge that enabled further investment of RL
methods for fine-tuning large base models. At the same time, while the spotlight of focus
may be more intense on the RL portion of RLHF in the near future – as a way to maximize
performance on valuable tasks – the core of RLHF is that it is a lens for studying the grand
problems facing modern forms of AI. How do we map the complexities of human values and
objectives into systems we use on a regular basis? This book hopes to be the foundation of
decades of research and lessons on these problems.
rlhfbook.com 17

2 A Tiny History of RLHF
RLHF and its related methods are very new. We highlight history to show how recently
the procedures were formalized, and how much of this documentation is in the academic
literature. With this, we want to emphasize that RLHF is very rapidly evolving, so the
chapter sets the stage for a book that will express uncertainty over certain methods and
an expectation that some details can change around a few, core practices. Otherwise, the
papers and methods listed here showcase why many pieces of the RLHF pipeline are what
they are, as some of the seminal papers were for applications totally distinct from modern
language models.
In this chapter we detail the key papers and projects that got the RLHF field to where it is
today. This is not intended to be a comprehensive review of RLHF and the related fields,
but rather a starting point and retelling of how we got to today. It is intentionally focused
on recent work that led to ChatGPT. There is substantial further work in the RL literature
on learning from preferences \[31\]. For a more exhaustive list, you should use a proper survey
paper \[32\], \[33\].
Figure 2: Timeline of key developments in RLHF discussed in this chapter, from early work
on RL from preferences through the adoption of RLHF in large language models.
2.1 Origins to 2018: RL on Preferences
The field has recently been popularized with the growth of Deep Reinforcement Learning
and has grown into a broader study of the applications of LLMs from many large technology
companies. Still, many of the techniques used today are deeply related to core techniques
from early literature on RL from preferences.
One of the first papers with an approach similar to modern RLHF wasTAMER.TAMER:
Training an Agent Manually via Evaluative Reinforcementproposed an approach in which
humans iteratively scored an agent’s actions to learn a reward model, which was used to
learn the action policy \[34\]. Other work, concurrently or soon after, proposed an actor-critic
algorithm, COACH, where human feedback (both positive and negative) is used to tune the
advantage function \[35\].
The primary reference, Christiano et al. 2017, is an application of RLHF applied to preferences
between trajectories of agents within Atari games \[1\]. This work introducing RLHF followed
soon after DeepMind’s seminal work in reinforcement learning on Deep Q-Networks (DQN),
which showed that RL agents can solve popular video games learning from scratch. The work
shows that humans choosing between trajectories can be more effective in some domains
rlhfbook.com 18

than directly interacting with the environment. This uses some clever conditions, but is
impressive nonetheless.
Figure 3: The core RLHF loop from Christiano et al. (2017): the reward predictor is trained
asynchronously from comparisons of trajectory segments, and the agent maximizes predicted
reward.
This method was expanded upon with more direct reward modeling \[36\] and the adoption of
deep learning within early RLHF work was capped by an extension to TAMER with neural
network models just one year later \[37\].
This era began to transition, as reward models as a general notion were proposed as a method
for studying alignment, rather than just a tool for solving RL problems \[38\].
2.2 2019 to 2022: RL from Human Preferences on Language Models
Reinforcement learning from human feedback, also referred to regularly as reinforcement
learning from human preferences in its early days, was quickly adopted by AI labs increasingly
turning to scaling large language models. A large portion of this work began between GPT-2,
in 2019, and GPT-3, in 2020. The earliest work in 2019,Fine-Tuning Language Models from
Human Preferenceshas many striking similarities to modern work on RLHF and the content
that we will cover in this book \[39\]. Many canonical terms, such as learning reward models,
KL distances, feedback diagrams, etc., were formalized in this paper, though the evaluation
tasks for the final models and their capabilities were different from what people are doing
today. From here, RLHF was applied to a variety of tasks. Important examples include
general summarization \[2\], recursive summarization of books \[40\], instruction following
(InstructGPT) \[3\], browser-assisted question-answering (WebGPT) \[4\], supporting answers
with citations (GopherCite) \[41\], and general dialogue (Sparrow) \[42\].
Aside from applications, a number of seminal papers defined key areas for the future of
RLHF, including those on:
1. Reward model over-optimization \[43\]: The ability for RL optimizers to over-fit to
models trained on preference data,
2. Language models as a general area of study for alignment \[23\], and
3. Red teaming \[44\] – the process of assessing the safety of a language model.
Work continued on refining RLHF for application to chat models. Anthropic continued to
use it extensively for early versions of Claude \[5\] and early RLHF open-source tools emerged
\[45\], \[46\], \[47\].
rlhfbook.com 19

2.3 2023 to the Present: The ChatGPT Era
The announcement of ChatGPT was very clear about the role of RLHF in its training \[48\]:
We trained this model using Reinforcement Learning from Human Feedback
(RLHF), using the same methods as InstructGPT, but with slight differences in
the data collection setup.
Since then, RLHF has been used extensively in leading language models. It is well known to
be used in Anthropic’s Constitutional AI for Claude \[24\], Meta’s Llama 2 \[49\] and Llama 3
\[29\], NVIDIA’s Nemotron \[30\], Ai2’s Tülu 3 \[6\], and more.
Today, RLHF is growing into a broader field of preference fine-tuning (PreFT), including
new applications such as process rewards for intermediate reasoning steps \[50\], covered in
Chapter 5; direct alignment algorithms inspired by Direct Preference Optimization (DPO)
\[25\], covered in Chapter 8; learning from execution feedback from code or math \[51\], \[52\]
and other online reasoning methods inspired by OpenAI’s o1 \[53\], covered in Chapter 7.
rlhfbook.com 20

3 Training Overview
In this chapter we provide a cursory overview of RLHF training, before getting into the
specifics later in the book. RLHF, while optimizing a simple loss function, involves training
multiple, different AI models in sequence and then linking them together in a complex, online
optimization.
Here, we introduce the core objective of RLHF, which is optimizing a proxy reward for
human preferences with a distance-based regularizer (along with showing how it relates to
classical RL problems). Then we showcase canonical recipes which use RLHF to create
leading models to show how RLHF fits in with the rest of post-training methods. These
example recipes will serve as references for later in the book, where we describe different
optimization choices you have when doing RLHF, and we will point back to how different
key models used different steps in training.
3.1 Problem Formulation
The optimization of reinforcement learning from human feedback (RLHF) builds on top of
the standard RL setup. In RL, an agent takes actionsat sampled from a policyπ(at|s t)
given the state of the environmentst to maximize rewardr(st,at)\[54\]. A policy is a function
that maps each state to a probability distribution over actions. The early policies that
evolved into modern literature on RLHF were in what is called deep reinforcement learning –
when a neural network is used to learn said function. Traditionally, the environment evolves
according to transition (dynamics)p(st+1|s t,at)with an initial state distributionρ0(s0).
Together, the policy and dynamics induce a trajectory distribution. A trajectory’s overall
probability is the product of the initial state probability, every action choice the policy makes,
and every state transition the environment produces:
pπ(τ) =ρ 0(s0)
T−1∏
t=0
π(at|s t)p(st+1|s t,at).(1)
Across a finite episode with horizonT, the goal of an RL agent is to solve the following
optimization, where γ is a discount factor from 0 to 1 that balances the desirability of
near-term versus future rewards:
max
π
Eτ∼pπ
[T−1∑
t=0
γtr(st,at)
]
.(2)
The expected return for a given policy is often denotedJ(π), with the optimal value written
J∗ = maxπJ(π).
For continuing tasks, one often takesT→∞ and relies on discounting (γ < 1) to keep
the objective well-defined. Multiple methods for optimizing this expression are discussed in
Chapter 6.
A standard illustration of the RL loop is shown in fig. 4 (compare this to the RLHF loop in
fig. 7).
rlhfbook.com 21

Figure 4: Standard RL loop
3.1.1 A Simple Example: The Thermostat
To build a basic intuition for what RL does, consider a thermostat trying to keep a room at a
target temperature of 70◦F. In RL, the agent starts with no knowledge of the task and must
discover a good policy through trial and error. The thermostat example has the following
components (see fig. 5 for how each maps to the trajectory distribution in eq. 1):
•State (s t): the current room temperature, e.g. 65◦F.
•Action (a t): turn the heater on or off.
•Reward (r): +1 when the temperature is within 2◦ of the target, 0 otherwise.
• Policy (π): the rule that decides whether to turn the heater on or off given the current
temperature. Here is one policy the thermostat might learn, which may not be optimal
depending on the exact transition dynamics of the environment:
π(at =on|s t) =
{
1ifs t <70◦F
0otherwise (3)
• Transition: the room warms when the heater is on and cools when it is off. The agent
influences these dynamics through its actions, but the underlying physics – how fast
the room heats or cools – are outside its control.
Figure 5: Each term in the trajectory distribution (eq. 1) mapped to the thermostat RL
example.
rlhfbook.com 22

Initially, the thermostat’s policy is essentially random – it flips the heater on and off with no
regard for the current temperature, and the room’s temperature swings wildly. Over many
episodes of trial and error, the agent discovers that turning the heater on when the room is
cold and off when it is warm leads to more reward, and gradually converges on a sensible
policy. This is the core RL loop: observe a state, choose an action, receive a reward, and
update the policy to get more reward over time.
3.1.2 Classic RL Example: CartPole
For a richer example with continuous dynamics, consider the classicCartPole(inverted
pendulum) control task, which appears in many RL textbooks, courses, and even research
papers. Whereas the thermostat had a single state variable and a binary action, CartPole
involves four continuous state variables and physics-based transitions – making it a standard
benchmark for RL algorithms.
Figure 6: CartPole environment showing state variables (x,˙x,θ,˙θ) and actions (±F).
•State (s t): the cart position/velocity and pole angle/angular velocity:
st = (xt,˙xt, θt, ˙θt).(4)
•Action (a t): apply a left/right horizontal force to the cart, e.g.at∈{−F,+F}.
• Reward (r): a simple reward isrt = 1each step the pole remains balanced and the
cart stays on the track (e.g.|xt|≤ 2.4and |θt|≤ 12◦), and the episode terminates
when either bound is violated.
rlhfbook.com 23

• Dynamics / transition (p(st+1|s t,at)): in many environments the dynamics are
deterministic (sop is a point mass) and can be written asst+1 =f(st,at)via Euler
integration with step size∆t. A standard simplified CartPole update uses the constants
cart massmc, pole massmp, pole half-lengthl, and gravityg (α is a mass-normalized
intermediate with acceleration units):
α= at +mpl ˙θ2
t sinθt
mc +mp
(5)
¨θt = gsinθ t−cosθ tα
l
(
4
3− mp cos2θt
mc+mp
) (6)
¨xt =α− mpl ¨θt cosθt
mc +mp
(7)
xt+1 =x t + ∆t˙xt,˙x t+1 = ˙xt + ∆t¨xt,(8)
θt+1 =θ t + ∆t ˙θt, ˙θt+1 = ˙θt + ∆t ¨θt.(9)
This is a concrete instance of the general setup above: the policy choosesat, the transition
function advances the state, and the reward is accumulated over the episode.
3.1.3 Manipulating the Standard RL Setup
The RL formulation for RLHF is seen as a less open-ended problem, where a few key pieces
of RL are set to specific definitions in order to accommodate language models. There are
multiple core changes from the standard RL setup to that of RLHF: Table tbl. 1 summarizes
these differences between standard RL and the RLHF setup used for language models.
1. Switching from a reward function to a reward model.In RLHF, a learned
model of human preferences,rθ(st,at)(or any other classification model) is used instead
of an environmental reward function. This gives the designer a substantial increase
in the flexibility of the approach and control over the final results, but at the cost of
implementation complexity. In standard RL, the reward is seen as a static piece of
the environment that cannot be changed or manipulated by the person designing the
learning agent.
2. No state transitions exist.In RLHF, the initial states for the domain are prompts
sampled from a training dataset and the “action” is the completion to said prompt
(in the standard RLHF setup, the prompt is fixed and the model’s completion does
not define the next prompt). The combination of one prompt and one completion
constitutes a complete episode or rollout, which would be many repeated state-action,
state-action chains in classical RL problems.
3. Response-level rewards and no discounting.RLHF attribution of reward is
done for an entire sequence of actions, composed of multiple generated tokens, rather
than in a fine-grained manner (this single-step structure is sometimes called a bandit
problem in the RL literature). To help the RL algorithms for RLHF see every token
as part of the same action, implementations usually use a discount factor ofγ = 1
rlhfbook.com 24

(no discounting), unlike standard RL whereγ <1balances short-term and long-term
reward across many sequential decisions.
Table 1: Key differences between standard RL and RLHF for language models.
Aspect Standard RL RLHF (language models)
Policy Learned from scratch
(random init)
Fine-tuned from a
pretrained language model
Reward signal Environment reward
functionr(s t,at)
Learned reward / preference
modelr θ(x,y)(promptx,
completiony)
State transition Yes: dynamics
p(st+1|s t,at)
Typically no: promptsx
sampled from a dataset; the
completion does not define
the next prompt
Action Single environment actionat A completiony(a sequence
of tokens) sampled from
πθ(·|x)
Reward granularity Often per-step / fine-grained Usually response-level
(bandit-style) over the full
completion, usually no
discounting (γ= 1)
Horizon Multi-step episode (T >1) Often single-step (T= 1),
though multi-turn can be
modeled as longer-horizon
Given the single-turn nature of the problem, the optimization can be re-written without the
time horizon and discount factor (and with an explicit reward model):
max
π
Eτ∼π [rθ(st,at)].(10)
In many ways, the result is that while RLHF is heavily inspired by RL optimizers and
problem formulations, the actual implementation is very distinct from traditional RL.
3.1.4 Fine-Tuning and Regularization
In traditional RL problems, the agent must learn from a randomly initialized policy, but
with RLHF, we start from a strong pretrained base model with many initial capabilities.
This strong prior for RLHF induces a need to prevent the optimization from drifting too
far from the initial policy. In order to succeed in a fine-tuning regime, RLHF techniques
employ multiple types of regularization to control the optimization. The goal is to allow the
reward maximization to still occur without the model succumbing to over-optimization, as
discussed in Chapter 14. The most common change to the optimization function is to add a
KL divergence penalty on the distance between the current RLHF policy and the starting
point of the optimization. Theβhyperparameter set when training the model controls the
strength of this constraint – a largerβ keeps the model closer to its starting point, while a
smallerβgives the optimizer more freedom to chase reward:
rlhfbook.com 25

Figure 7: Standard RLHF loop
max
π
Eτ∼π [rθ(st,at)]−βD KL(π(·|st)∥πref(·|st)).(11)
Within this formulation, a lot of study into RLHF training goes into understanding how to
spend a certain “KL budget” as measured by a distance from the initial model. For more
details, see Chapter 15 on Regularization.
3.1.5 Optimization Tools
In this book, we detail many popular techniques for solving this optimization problem. The
popular tools of post-training include:
• Reward modeling(Chapter 5): A model is trained to capture the signal from
collected preference data and can then output a scalar reward indicating the quality of
future text.
• Instruction fine-tuning(Chapter 4): A prerequisite to RLHF where models are
taught the question-answer format used in the majority of language modeling interac-
tions today by imitating preselected examples.
• Rejection sampling(Chapter 9): The most basic RLHF technique where candidate
completions for instruction fine-tuning are filtered by a reward model imitating human
preferences.
• Policy gradients(Chapter 6): The reinforcement learning algorithms used in the
seminal examples of RLHF to update parameters of a language model with respect to
the signal from a reward model.
• Direct alignment algorithms(Chapter 8): Algorithms that directly optimize a
policy from pairwise preference data, rather than learning an intermediate reward
rlhfbook.com 26

model to then optimize later.
Modern RLHF-trained models always utilize instruction fine-tuning followed by a mixture of
the other optimization options.
3.1.6 Subtle Advantages of RL in Post-Training Language Models
In the following chapters, we cover many optimization tools for post-training. Plenty of them,
such as rejection sampling (Chapter 9) and direct alignment algorithms like DPO (Chapter
8), are far simpler than getting RL working. Still, despite the simplicity of alternatives,
RL-based methods continue to win out. Some trends, such as the inference-time scaling with
reinforcement learning with verifiable rewards (RLVR), are obvious, but RL has turned out
to be a well-suited optimization tool for language models. Implementing RL requires a far
larger infrastructure investment relative to instruction tuning or DPO-like algorithms, but,
at the risk of being overly colloquial, the gradient updates it provides “generally help the
model a lot.” This is hard to quantify, but comes in a few recurring forms:
• RL stages can “fix” rough edges on the model, making the model easier to chat with or
more robust (this could come by training it to have numerical stability with inference
tools like vLLM). The exact reason for this is not well-known in the literature, but its
truth is reflected in the growing presence of RL today.
• RL can be done surgically — the model does a good job of learning where the prompt
distribution lies, and RL tends to not “squash” the general capabilities of the model.
A good example of this is Tülu 3 being trained with RL only on math prompts, while
maintaining capabilities across a broad task suite \[6\].
Overall, RL losses on language models are robust, scalable, effective, and flexible, which
opened large new fields of experimentation. The original method that started us down this
path was RLHF work.
3.2 Canonical Training Recipes
Over time various models have been identified as canonical recipes for RLHF specifically
or post-training generally. These recipes reflect data practices and model abilities at the
time. As the recipes age, training models with the same characteristics becomes easier and
requires less data. There is a general trend of post-training involving more optimization
steps with more training algorithms across more diverse training datasets and evaluations.
3.2.1 InstructGPT
Around the time ChatGPT first came out, the widely accepted (“canonical”) method for
post-training an LM had three major steps, with RLHF being the central piece \[55\] \[3\] \[5\].
The three steps taken on top of a “base” language model (the next-token prediction model
trained on large-scale web text) are summarized below in fig. 8:
1. Instruction tuning on ~10K examples: This teaches the model to follow the
question-answer format and teaches some basic skills from primarily human-written
data.
2. Training a reward model on ~100K pairwise prompts(paper used 33K prompts):
This model is trained from the instruction-tuned checkpoint and captures the diverse
rlhfbook.com 27

values one wishes to model in their final training. The reward model is the optimization
target for RLHF.
3. Training the instruction-tuned model with RLHF on a separate ~100K
prompts(paper used exactly 31K and does not document whether prompts were
reused from other stages): The model is optimized against the reward model with a
likely separate set of prompts, where it generates responses before receiving ratings.
Once RLHF was done, the model was ready to be deployed to users. This recipe is the
foundation of modern RLHF, but recipes have evolved substantially to include more stages
and more data.
Figure 8: A rendition of the early, three stage RLHF process with SFT, a reward model,
and then optimization.
3.2.2 Tülu 3
Modern versions of post-training involve many, many more model versions and training
stages (i.e. well more than the 5 RLHF steps documented for Llama 2 \[49\]). An example
is shown below in fig. 9 where the model undergoes numerous training iterations before
convergence.
Figure 9: A rendition of modern post-training with many rounds.
The most complex models trained in this era and onwards have not released full details of
their training process. Leading models such as ChatGPT or Claude by 2026 involve many
iterative rounds of training. This can even include techniques that train specialized models
and then merge the weights together to get a final model capable of many subtasks \[56\]
(e.g. Cohere’s Command A \[57\]).
rlhfbook.com 28

Figure 10: A summary of the Tülu 3 recipe with target skills and multi-step training recipe.
Lambert et al. 2024, License CC-BY.
A fully open example of this multi-stage approach to post-training where RLHF plays a
major role is Tülu 3. The Tülu 3 recipe consists of three stages:
1. Instruction tuning on ~1M examples: This primarily synthetic dataset, drawn
from a mix of frontier models such as GPT-4o and Llama 3.1 405B, teaches the model
general instruction following and serves as the foundation for capabilities such as
mathematics and coding.
2. On-policy preference data on ~1M preference pairs: This stage substantially
boosts the chattiness (e.g. Arena, formerly Chatbot Arena, or AlpacaEval 2) of the
model while also improving skills mentioned above in the instruction tuning stage.
3. Reinforcement Learning with Verifiable Rewards on ~10K prompts: This
stage is a small-scale reinforcement learning run to boost core skills such as mathematics
while maintaining overall performance (and is now seen as a precursor to modern
reasoning models such as DeepSeek R1).
The recipe has been successfully applied to Llama 3.1 \[6\], OLMo 2 \[58\], and SmolLM models
\[59\].
3.2.3 DeepSeek R1
With the rise of reasoning language models, such as OpenAI’s o1, the best practices in
post-training evolved again to re-order and redistribute compute across training stages. The
clearest documentation of a reasoning model post-training recipe is DeepSeek R1 \[15\], which
has been mirrored by Alibaba’s larger Qwen 3 models (i.e. only the 32B and 225B MoE
models) \[60\] or Xiaomi’s MiMo 7B \[61\]. The DeepSeek recipe follows:
1. “Cold-start” with 100K+ on-policy reasoning samples: This data is sampled
from an earlier RL checkpoint, R1-Zero, and heavily filtered to instill a specific reasoning
process on DeepSeek-V3-Base. DeepSeek uses the term cold-start to describe how RL
is learned from little supervised data.
2. Large-scale reinforcement learning training: This stage repeatedly covers rea-
soning problems with the model, running RLVR “until convergence” on a variety of
benchmarks.
rlhfbook.com 29

3. Rejection sampling and SFT: Near convergence, they apply rejection sampling
to the RL checkpoint to build an SFT dataset of ~800K samples, then fine-tune the
model on a filtered mix of roughly 3/4 reasoning problems and 1/4 general queries to
produce a general-purpose model.
4. Mixed reinforcement learning trainingon reasoning problems (verifiable rewards)
with general preference tuning reward models to polish the model.
As above, there are evolutions of the recipe, particularly with steps 3 and 4 to finalize the
model before exposing it to users. Many models start with tailored instruction datasets
with chain-of-thought sequences that are heavily filtered and polished from existing models,
providing a fast step to strong behaviors with SFT alone before moving onto RL \[62\].
rlhfbook.com 30

4 Instruction Fine-Tuning
Early large pretrained language models were trained with a next-token prediction objective
and, by default, did not come with an explicit interface for following instructions. Around
the release of GPT-3 \[63\], prompting and in-context learning became a widely used way to
adapt a single model to many tasks (though task-specific fine-tuning remained common), by
showing examples in-context and asking the model to complete a similar task. A practical
next step was instruction fine-tuning, which teaches the model to respond in an instruction-
response format rather than just continuing text. For example, given the prompt “What is
the capital of France?”, a base model might continue with “What is the capital of Germany?
What is the capital of Italy?...” — simply extending the pattern of questions — while an
instruction-tuned model would respond with “The capital of France is Paris.”
Instruction fine-tuning took off when two lines of work converged. First, NLP shifted from
bespoke fine-tuning task setups to a unified “text-to-text” or instruction framing, which
made it straightforward to standardize diverse datasets and train a single model across many
tasks. Prominent examples of unifying the framework for tasks includeExploring the Limits
of Transfer Learning with a Unified Text-to-Text Transformer(T5 models) \[64\],Finetuned
Language Models Are Zero-Shot Learners(FLAN dataset) \[65\],Multitask Prompted Training
Enables Zero-Shot Task Generalization(T0 models) \[66\], andCross-Task Generalization via
Natural Language Crowdsourcing Instructions(Natural Instructions dataset) \[67\]. Second,
scaling pretrained LMs and the rise of prompting/in-context learning showed that a single
model could generalize across tasks, but that generalization becomes far more reliable when
the model is explicitly trained on instruction-response examples. Together, these trends led
to an era of fine-tuning pretrained language models on large collections of instructions—what
is now commonly called instruction fine-tuning (IFT), or supervised fine-tuning (SFT), in
which training general models became accessible to wider audiences.
Since its discovery, instruction fine-tuning, also called colloquially justinstruction tuning,
has matured and is standard practice across many language modeling pipelines. At its core,
IFT is the simplest method for adapting language models to a desired task distribution.
It serves as the foundation for RLHF by preparing the model for a format of instructions
that is known as question-answering, and it is the first tool used by those attempting to
apply modern techniques to new domains. Without a basic level of instruction-following
abilities, most of the pipelines we discuss in this book—from preference data collection to
online RLHF optimization—cannot be performed.
Instruction fine-tuning generally is covered extensively elsewhere and is supervised learning
at its core, so this chapter focuses on the practical details that matter most for RLHF
practitioners: how training data is formatted and structured. Decisions on data and
formatting are directly leveraged in the later training stages to create a common language
for the model to absorb post-training data.
4.1 Chat Templates and the Structure of Instructions
The post-training process begins with defining a pattern to format user queries so that they
are easily readable by a language model that processes information through a tokenizer.
When using a pretrained language model, the prompting is quite simple. The model only
knows a few tokens: a beginning-of-sequence token (e.g.,<bos_token>), an end-of-sequence
token (e.g., <eos_token>), and a padding token (to manage training on batches with empty
rlhfbook.com 31

components). This means, to prompt a base model, the user inputs a sequence of tokens for
the model to continue from, such as:
<bos_token> The capital of the United States is
Then, the model would generate tokens until it runs out of its context window, or it generates
the end-of-sequence token.
All post-training stages, from instruction tuning to RLHF and other methods, rely on this
formatting to train the model. The tool that handles the structure of the interaction with
the user is called thechat template.
An example which we will break down is below:
{% if messages\[0\]['role'] =='system'%}
{# If the conversation begins with a system message, treat it as a special first
turn.
We set an offset so the user/assistant alternation check lines up correctly. #}
{% set offset = 1 %}
{% else %}
{# No system message: user should be the first non-empty turn. #}
{% set offset = 0 %}
{% endif %}
{# Emit the beginning-of-sequence token (model-specific). #}
{{ bos_token }}
{# Serialize each message into the model's chat-markup tokens. #}
{% for message in messages %}
{# Enforce role alternation: (system), user, assistant, user, assistant, ...
The boolean expression compares "is this a user message?" against whether the
current index (plus offset) is expected to be user or assistant. #}
{% if (message['role'] =='user') != (loop.index0 % 2 == offset) %}
{{ raise_exception('Conversation roles must alternate
user/assistant/user/assistant/...') }}
{% endif %}
{# Wrap each message with special tokens:
- <|im_start|><role>\n
- message content (trimmed)
- <|im_end|>\n
This produces a single flat token sequence the LM can train on. #}
{{'<|im_start|>'+ message['role'] +'\n'+ message['content'] | trim +
'<|im_end|>\n'}}
{% endfor %}
{# Optionally append an "assistant" start tag with no content.
This cues generation to continue from the assistant role. #}
{% if add_generation_prompt %}
{{'<|im_start|>assistant\n'}}
{% endif %}
This is the raw code for transforming a list of dictionaries in Python containing messages
and roles into tokens that a language model can predict from.
All information passed into models is assigned a role. The traditional three roles aresystem,
user, andassistant.
rlhfbook.com 32

The system tag is only used for the first message of the conversation; it holds instructions
for the agent in text that will not be received from or exposed to the user. Thesesystem
promptsare used to provide additional context to the models, such as the date and time, or
to patch behaviors. As a fun example, models can be told things such as “You are a friendly
chatbot who always responds in the style of a pirate.”
Next, the two other roles are straightforward:userholds the messages from the person
using the AI, andassistantholds the responses from the model (that is, engaging as an AI
assistant).
In order to translate all this information into tokens, we use the code listing above that we
started with. The model has a series ofspecial tokensthat separate the various messages
from each other. If we run the above code with the example query “How many helicopters
can a human eat in one sitting?”, the token sequence passed into the model would look as
follows:
<|im_start|>system
You are a friendly chatbot who always responds in the style of a pirate<|im_end|>
<|im_start|>user
How many helicopters can a human eat in one sitting?<|im_end|>
<|im_start|>assistant
Notice how the final tokens in the sequence are<|im_start|>assistant. This is how the
model knows to continue generating tokens until it finally generates its end-of-sequence token,
which in this case is<|im_end|>.
By packing all question-answer pair data (and downstream preference tuning data) into this
format, modern language models follow it with perfect consistency. This is the language that
instruction-tuned models use to exchange information with users and the models running on
GPUs or other computing devices.
The behavior can be extended naively to multiple turns, as shown below:
<|im_start|>system
You are a friendly chatbot who always responds in the style of a pirate<|im_end|>
<|im_start|>user
How many helicopters can a human eat in one sitting?<|im_end|>
<|im_start|>assistant
Oh just 6.<|im_end|>
<|im_start|>user
Are you sure about that?<|im_end|>
<|im_start|>assistant
In the open ecosystem, the standard method for applying the chat template to a list of
messages uses a Jinja snippet stored in the tokenizer configuration, asapply_chat_template.
The above chat template is a derivative of OpenAI’s Chat Markup Language (ChatML),
which was an early attempt to standardize message formatting. Now, OpenAI and other
model providers use a hierarchical system where the user can configure a system message,
yet there are higher-level instructions that may or may not be revealed to the user \[68\].
Many other chat templates exist. Some other examples include Zephyr’s \[26\]:
rlhfbook.com 33

<|system|>
You are a friendly chatbot who always responds in the style of a pirate</s>
<|user|>
How many helicopters can a human eat in one sitting?</s>
<|assistant|>
Or Tülu’s:
<|user|>
How are you doing?
<|assistant|>
I'm just a computer program, so I don't have feelings, but I'm functioning as expected.
How can I assist you today?<|endoftext|>
Beyond this, many chat templates include formatting and other tokens for tasks such as
tool-use.
4.2 Best Practices for Instruction Tuning
Instruction tuning as the foundation of post-training and creating helpful language models
is well-established. There are many ways to achieve successful instruction tuning. For
example, efficient fine-tuning with quantization of some model parameters makes training
very accessible \[69\]. Also, in narrow domains such as chat alignment, i.e., without harder
skills such as math or code, small, focused datasets can achieve strong performance \[14\].
Soon after the release of ChatGPT, human datasets with as few as 10K samples such as No
Robots were state-of-the-art \[70\]. Years later, large-scale synthetic datasets work best \[6\] on
most tasks.
A few principles remain:
• High-quality data is key to performance. The completions are what the model actually
learns from (in many cases the prompts are not predicted over so the model does not
learn to predict prompts).
• Around 1M prompts can be used to create a model capable of excellent RLHF and
post-training. Further scaling can still help, but returns diminish quickly.
•The best prompts are those in a similar distribution to downstream tasks of interest.
• If multiple stages of training are done after instruction tuning, the models can recover
from some noise in the instruction-tuning data. Crafting the overall optimization is
more important than fixating on each individual stage.
4.3 Implementation Details
While the loss function is the same as that used in pretraining, there are a few key imple-
mentation details that differ from the setting used for pretraining. Many practices, such as
deciding on the types of parallelism used to shard models across many GPUs, are the same
as pretraining, but the total number of machines used is often lower (for the first technical
change listed below):
• Smaller batch sizes: Compared to pretraining, instruction tuning (and other post-
training techniques such as preference fine-tuning) use substantially smaller batch
sizes to optimize well on a narrower data distribution while preserving the model’s
rlhfbook.com 34

generalization from pretraining. For example, OLMo 2 uses a batch size of 1024
packed-rows for the 7B and 2048 for the 13B pretraining, where these models have
a total context length of 4096 tokens, and each row in the batch is a combination of
documents that fills the sequence length. For post-training, both these models only
use a batch size of 256prompts\[58\], without filling to the full sequence length (for far
fewer non-masked tokens per batch). The smaller batch sizes mean that these training
jobs cannot be sharded across as many devices as during pretraining – in practice,
distributed training setups have minimum per-device batch sizes, so if you’re trying to
retain a smaller global batch size for SFT you can use cumulatively fewer GPUs. In
practice the batch size forcing a smaller concurrent GPU allotment per training job is
not a limiting factor because the training token counts for SFT are much smaller than
in pretraining, and training for multiple seeds is needed in post-training to obtain the
best final performance.
• Prompt masking: When pretraining, every token in the batch is predicted autore-
gressively and the loss is then applied to them. For instruction tuning, the prompt
tokens are masked out so the model isn’t learning to accurately predict user queries –
just responses. The same applies to other post-training algorithms.
• Multi-turn masking: For multi-turn conversations, there are two common masking
choices. (1)Final-turn only: only the tokens in the final assistant turn are included in
the loss, while all earlier context (including earlier assistant turns) is masked. Long
conversations can still be “unrolled” into multiple training samples: for a conversation
ofN turns, each example predicts one assistant response while masking all prior context
and excluding any future turns. (2)Mask user turns only: all user turns are masked,
buteveryassistant turn is included in the loss. You can still unroll in this setting if
you want more (shorter) training examples, but the key difference is that intermediate
assistant replies are trained on directly.
• Same loss function as pretraining:Instruction tuning uses the same autoregressive
loss function used in pretraining language models, but with substantially different data
and masking (training only on full sequences, whereas pretraining documents can be
split across batches), etc.
• Learning rate:SFT typically uses a learning rate one to two orders of magnitude
smaller than pretraining to best manage the different optimization dynamics (smaller
datasets, smaller batches, and a strong pretrained initialization all favor more con-
servative updates). For example, OLMo 2 uses a peak learning rate of3× 10−4 for
pretraining but1 × 10−5 for SFT \[58\]. Olmo 3 uses a higher SFT learning rate of
5-8× 10−5 \[18\], in part because its training infrastructure uses sequence packing,
which fits multiple examples into each training sequence and increases the effective
batch size measured in useful tokens. Larger batches produce lower-variance gradient
estimates, which in turn supports a higher learning rate without destabilizing training –
a relationship known as the linear scaling rule. The learning rate is commonly warmed
up over a small fraction of training steps before decaying linearly. In practice, teams
often sweep over multiple learning rates and select the best checkpoint on a held-out
evaluation suite \[18\].
4.4 Suggested Experiments
ThecompanioncoderepositoryincludesasmallSFTtrainingscriptin code/instruction_tuning/.
It is intended as a learning exercise to make the base-model-to-assistant transition concrete.
rlhfbook.com 35

1. Run the canonical SFT example and watch the base→assistant transition.
Run:
cd code/
uv run python -m instruction_tuning.train --config
instruction_tuning/configs/sft_olmo2_1b.yaml
Thistrains allenai/OLMo-2-0425-1B(base)on HuggingFaceH4/no_robotsandprints
generations for a fixed prompt pool every 50 optimizer steps. At step 0 the base model
rambles, repeats the prompt, and emits malformed role markers; after a few hundred
steps the same prompts produce concise answers that terminate at<|endoftext|>.
This is the sanity check for instruction tuning — the same loss function as pretraining,
but applied to a chat template with prompt tokens masked.
2. Sweep the learning rate.Copy sft_olmo2_1b.yaml and try lr values of 1e-6,
5e-6, and 5e-5 while holding everything else fixed. Inspect at which learning rate
the model first answers and stops cleanly versus when it overfits and starts producing
template-shaped slop. This is the practical version of the “one to two orders of
magnitude below pretraining” guidance above.
rlhfbook.com 36

5 Reward Modeling
Reward models are core to the modern approach to RLHF by being where the complex human
preferences are learned. They are what enable our models to learn from hard-to-specify
signals. They compress complex features in the data into a representation that can be used
in downstream training – a sort of magic that once again shows the complex capacity of
modern deep learning. These models act as proxy objectives for the core optimization, as
studied in the following chapters. As shown in fig. 11, the reward model plays a role like
the standard RL environment, providing the learning signal for the agent, but unlike a fixed
environment, we get to learn it from human preferences.
Reward models have historically been used extensively in reinforcement learning research
as a proxy for environment rewards \[54\]. Reward models were proposed, in their modern
form, as a tool for studying the value alignment problem \[38\]. These models tend to take
in some sort of input and output a single scalar value of reward. This reward can take
multiple forms – in traditional RL problems it was attempting to approximate the exact
environment reward for the problem, but we will see in RLHF that reward models actually
output a probability of a certain input being “of high quality” (i.e. the chosen answer among
a pairwise preference relation). The practice of reward modeling for RLHF is closely related
to inverse reinforcement learning, where the problem is to approximate an agent’s reward
function given trajectories of behavior \[71\], and other areas of deep reinforcement learning.
The high-level problem statement is the same, but the implementation and focus areas are
entirely different, so they’re often considered as totally separate areas of study.
The most common reward model, often called a Bradley-Terry reward model and the primary
focus of this chapter, predicts the probability that a piece of text was close to a “preferred”
piece of text from the training comparisons. Later in this section we also compare these
to Outcome Reward Models (ORMs), Process Reward Models (PRMs), and other types of
reward models.
Throughout this chapter, we usex to denote prompts andy to denote completions. This
notation is common in the language model literature, where methods operate on full prompt-
completion pairs rather than individual tokens.
5.1 Training a Bradley-Terry Reward Model
The canonical implementation of a reward model is derived from the Bradley-Terry model
of preference \[72\]. There are two popular expressions for how to train a standard reward
model for RLHF – they are mathematically equivalent. To start, a Bradley-Terry model of
preferences defines the probability that, in a pairwise comparison between two itemsi and j,
a judge prefersioverj:
P(i>j) = pi
pi +pj
.(12)
The Bradley-Terry model assumes that each item has a latent strengthpi > 0, and that
observed preferences are a noisy reflection of these underlying strengths. It is common to
reparametrize the Bradley-Terry model with unbounded scores, wherepi =eri, which results
in the following form:
rlhfbook.com 37

Figure 11: The reward model in RLHF plays the role of the environment component that
returns rewards in standard RL. The key difference is that in RLHF, we get to control
and learn this reward function from human preferences, rather than having it fixed by the
environment.
rlhfbook.com 38

P(i>j) = eri
eri +erj
=σ(r i−rj).(13)
Here σ(z) = 1
1+e−z is the logistic (sigmoid) function, so the preference probability depends
only on the score differenceri−rj. Only differences in scores matter: adding the same
constantc to everyrk leavesP (i>j )unchanged. These forms are a useful approximation
of human preferences that often works well in RLHF.
To train a reward model, we must formulate a loss function that satisfies the above relation.
In practice, this is done by converting a language model into a model that outputs a scalar
score, often via a small linear head that produces a single reward value from the model’s
final hidden state. Given a promptx and two sampled completionsy1 and y2, we score both
with a reward modelrθ and write the conditional scores asrθ(yi|x).
The probability that the reward model assigns toy1 being preferred toy2 becomes:
P(y 1 >y 2|x) = exp (rθ(y1|x))
exp (rθ(y1|x)) + exp (rθ(y2|x)) .(14)
We denote the preferred completion asyc (chosen) and the rejected completion asyr.
The resulting loss encourages the reward model to assign a higher score to the human-preferred
completion than the rejected one, using a sigmoid to convert the score difference into a
probability. The preference likelihood in eq. 14 is the starting point. We first rewrite that
likelihood into sigmoid form by dividing the numerator and denominator byexp (rθ(yc|x)) :
P(yc >y r|x) = exp (rθ(yc|x))
exp (rθ(yc|x)) + exp (rθ(yr|x))
= exp (rθ(yc|x))
exp (rθ(yc|x))
(
1 + exp(rθ(yr|x))
exp(rθ(yc|x))
)
= 1
1 + exp(rθ(yr|x))
exp(rθ(yc|x))
= 1
1 + exp (−(rθ(yc|x)−r θ(yr|x)))
=σ(r θ(yc|x)−r θ(yr|x)).
(15)
The reward model is then fit by maximum likelihood over the preference datasetD, max-
imizing the expected log-likelihood of the observed preferences. Because the logarithm is
monotonic, this is equivalent to minimizing the expected negative log-likelihood:
θ∗ = arg max
θ
E(x,yc,yr)∼D [logP(y c >y r|x)]
= arg min
θ
E(x,yc,yr)∼D [−logσ(r θ(yc|x)−r θ(yr|x))]. (16)
Taking the logarithmbeforeaveraging over the dataset is what makes the negative-log-
likelihood loss the right objective: maximizing the expected probabilityE[P ]is not the same
as maximizing the expected log-probabilityE[logP].
rlhfbook.com 39

The per-example loss is the log-sigmoid expression inside the expectation above, as in \[3\]
and other works:
L(θ) =−log (σ(r θ(yc|x)−r θ(yr|x)))(17)
The second is a mathematically equivalent form expressed using the softplus function
log(1 +ex), as in \[23\] and other works:
L(θ) = log
(
1 +erθ(yr|x)−rθ(yc|x)
)
(18)
These are equivalent by letting∆ =rθ(yc|x )−rθ(yr|x )and using σ(∆) = 1
1+e−∆, which
implies−logσ (∆) = log(1 +e−∆) = log
(
1 +erθ(yr|x)−rθ(yc|x))
. They both appear in the
RLHF literature.
Figure 12: Training a preference reward model requires pairs of chosen and rejected com-
pletions. The model computes a scalar score for each completion from a sequence-level
representation, often the end-of-sequence (EOS) token’s hidden state, and the contrastive
loss depends only on the score difference between the two.
5.1.1 The Default Reward Model Architecture
The most common way reward models are implemented is through an abstraction similar to
Transformers’ AutoModelForSequenceClassification, which appends a small linear head
to the language model and produces a scalar reward score for a prompt-completion pair at
training or inference. At inference time, the model outputs therelative likelihood that the
piece of text is chosenas a single logit from the model.
Other implementation options exist, such as just taking a linear layer directly from the final
embeddings, but they are less common in open tooling.
5.1.2 Implementation Example
Implementing the reward modeling loss is quite simple. More of the implementation challenge
is on setting up a separate data loader and inference pipeline. Given the correct dataloader
with tokenized, chosen and rejected prompts with completions, the loss is implemented as:
importtorch.nnasnn
# inputs_chosen / inputs_rejected include the prompt tokens x and the respective
# completion tokens (y_c or y_r) that the reward model scores jointly.
rewards_chosen = model(**inputs_chosen)
rewards_rejected = model(**inputs_rejected)
rlhfbook.com 40

loss = -nn.functional.logsigmoid(rewards_chosen - rewards_rejected).mean()
As for the bigger picture, this is often within a causal language model (a model that generates
tokens left-to-right, predicting each token conditioned on all previous ones) that has an
additional head added (and learned with the above loss) that transitions from the final
hidden state to the score of the inputs. The code takes in standard transformer inputs –
input_ids (tokenized text) andattention_mask (which marks real tokens vs. padding) –
and extracts the hidden state (the model’s internal representation of the input) at the last
real token, which is then passed through a linear layer to produce a scalar reward. This
model will have a structure as follows:
importtorch
importtorch.nnasnn
importtorch.nn.functionalasF
classBradleyTerryRewardModel(nn.Module):
"""
Standard scalar reward model for Bradley-Terry preference learning.
Usage (pairwise BT loss):
rewards_chosen = model(**inputs_chosen) # (batch,)
rewards_rejected = model(**inputs_rejected) # (batch,)
loss = -F.logsigmoid(rewards_chosen - rewards_rejected).mean()
"""
def__init__(self, base_lm):
super().__init__()
self.lm = base_lm# e.g., AutoModelForCausalLM
self.head = nn.Linear(self.lm.config.hidden_size, 1)
def_sequence_rep(self, hidden, attention_mask):
"""
Get a single vector per sequence to score.
Default: last non-padding token (EOS token); if no mask, last token.
hidden: (batch, seq_len, hidden_size)
attention_mask: (batch, seq_len)
"""
# Index of last non-pad token in each sequence
# attention_mask is 1 for real tokens, 0 for padding
lengths = attention_mask.sum(dim=1) - 1# (batch,)
batch_idx = torch.arange(hidden.size(0), device=hidden.device)
returnhidden[batch_idx, lengths]# (batch, hidden_size)
defforward(self, input_ids, attention_mask):
"""
A forward pass designed to show inference structure of a standard reward model.
To train one, this function will need to be modified to compute rewards from
both
chosen and rejected inputs, applying the loss above.
"""
outputs = self.lm(
input_ids=input_ids,
attention_mask=attention_mask,
output_hidden_states=True,
return_dict=True,
)
rlhfbook.com 41

# Final hidden states: (batch, seq_len, hidden_size)
hidden = outputs.hidden_states[-1]
# One scalar reward per sequence: (batch,)
seq_repr = self._sequence_rep(hidden, attention_mask)
rewards = self.head(seq_repr).squeeze(-1)
returnrewards
In this section and what follows, most of the implementation complexity for reward models
(and much of post-training) is around constructing the data-loaders correctly and distributed
learning systems. Note, when training reward models, the most common practice is to train
for only 1 epoch to avoid overfitting.
5.2 Outcome Reward Models
The majority ofpreference tuningfor language models and other AI systems is done with the
Bradley-Terry models discussed above. For reasoning-heavy tasks, one can use an Outcome
Reward Model (ORM). The training data for an ORM is constructed in a similar manner
to standard preference tuning. Here, we have a problem statement or prompt,x and two
completions y1 and y2. The inductive bias used here is that one completion should be a
correct solution to the problem and one incorrect, resulting in(yc,yic).
Before we continue, it is important to note that outcome reward models are a relatively
niche area in the post-training literature, and the key papers we reference have subtly
different implementation details. The key idea is to learn a per-token signal of how likely the
completion is to end in a correct answer, but there have been different training approaches
and architectures over time.
The architecture of the models used is very similar to a standard reward model, with a linear
layer appended to a model that can output a single logit (in the case of an RM) – with an
ORM, the training objective that follows is slightly different. To start, let’s break down the
content in the original GSM8K paper (a popular benchmark studying grade-school math)
\[73\], which originated the ideas that became an ORM without yet naming it. We start with
architecture, from section 4.3:
We can either train verifiers to make a single scalar prediction conditioned on the
entire generated solution, or to make a scalar prediction after each token in the
solution. By default, we choose the latter, training verifiers to make predictions
after each token.
This is where the default implementation of outcome reward models diverges from Bradley-
Terry models – they predict at each token. The authors comment on how per-token
information could be “a useful auxiliary signal that encourages the model to judge reasoning
throughout the solutions,” rather than just predicting the outcome (which is a bit counter-
intuitive, given the name of model that later emerged as ORM). Continuing, from Appendix
E:
[We] train verifiers with a joint objective where the model learns to label a model
completion as correct or incorrect, in addition to the original language modeling
objective. Architecturally, this means our verifiers are language models, with a
small scalar head that outputs predictions on a per-token basis. We implement
rlhfbook.com 42

this scalar head as a single bias parameter and single gain parameter that operate
on the logits outputted by the language model’s final unembedding layer.
To translate, this is implemented as a small head that outputs a scalar logit at every token,
rather than a classification head of a traditional RM that outputs one logit for the entire
sequence. Additionally, in this original GSM8K paper the authors jointly trained their ORM
with the next-token, language modeling loss – this practice did not continue as the default.
The term “outcome-reward model” appeared in 2022, in a paper comparing “outcome-
supervised RM (ORM)” versus process reward models that predicted the quality of the
reasoning so far \[74\] – this importantly is a secondary way of implementing an ORM, one
that implements a binarycorrect or incorrect in the LLM’s tokenizer vocabulary as a
step-level signal, rather than learning a separate scalar head that predicts correctness at
every token.
The canonical implementation that is followed in this book is from the paperLet’s Verify
Step by Step\[50\], where the outcome reward model is training a per-token predictor of if an
answer is right with a cross-entropy loss.
Formally, the per-token loss applies a binary cross-entropy at every completion token, where
each token’s associated outcome probability is trained towards the sequence’s outcome label:
Ltoken(θ) =−E (s,r)∼D
[
1
T
T∑
t=1
(rlogp θ(st) + (1−r) log (1−p θ(st)))
]
(19)
where s is a completion ofT tokens,r∈{ 0, 1} is a binary label where 1 applies to a correct
answer to a given prompt and 0 applies to an incorrect answer, andpθ(st) =σ(wθ(st))is
the probability of correctness predicted at tokentfrom the model’s scalar logitwθ(st).
A simpler form of an ORM, following \[75\], is a sequence-level cross-entropy loss, where the
model is later used for per-token inference:
LCE(θ) =−E (s,r)∼D [rlog ¯pθ(s) + (1−r) log(1−¯pθ(s))](20)
where r∈{ 0, 1} is a binary label where 1 applies to a correct answer to a given prompt and
0 applies to an incorrect answer, and¯pθ(s) = σ
(
1
T
∑T
t=1wθ(st)
)
squashes the average of
the per-token logits into a single probability that the entire completion is correct – note
this is not the average of the per-token probabilities, since the sigmoid is applied after the
pooling. In code, this outcome label is copied onto every completion token, while prompt
tokens are masked with-100so they do not contribute to the loss.
Implementing an outcome reward model (and other types, as we’ll see with the Process
Reward Model) involves applying the cross-entropy loss per-token based on whether the
completion is a correct sample. This is far closer to the language modeling loss, where it does
not need the structured chosen-rejected nature of standard Bradley-Terry reward models.
In the simplified ORM training setup below, we are not sampling new tokens or training
an LLM on next-token prediction; we feed a fixed prompt-completion sequence through the
backbone and train the ORM head to predict correctness labels.
The model structure could follow as:
rlhfbook.com 43

importtorch.nnasnn
importtorch.nn.functionalasF
classOutcomeRewardModel(nn.Module):
def__init__(self, base_lm):
super().__init__()
self.lm = base_lm# e.g., AutoModelForCausalLM
self.head = nn.Linear(self.lm.config.hidden_size, 1)
defforward(self, input_ids, attention_mask=None, labels=None):
"""
input_ids contains a full prompt+completion sequence.
labels is token-aligned: prompt tokens are -100, and each completion
token repeats the sequence outcome label (1=correct, 0=incorrect).
If labels=None, this is an inference-only forward pass and the loss is
returned as None.
"""
outputs = self.lm(
input_ids=input_ids,
attention_mask=attention_mask,
output_hidden_states=True,
return_dict=True,
)
# Final hidden states: (batch, seq_len, hidden_size)
hidden = outputs.hidden_states[-1]
# One scalar logit per token: (batch, seq_len)
logits = self.head(hidden).squeeze(-1)
# Inference-only forward pass: no loss is computed.
iflabelsisNone:
returnNone, logits
# Only compute loss on completion tokens (labels 0 or 1)
# Prompt tokens have labels = -100
mask = labels != -100
loss = None
ifmask.any():
loss = F.binary_cross_entropy_with_logits(
logits[mask], labels[mask].float()
)
else:
loss = logits.sum() * 0
returnloss, logits
A simplified version of the loss follows:
# Feed the full prompt+completion sequence once; no token sampling happens here.
# Assume model already has: model.lm (backbone) + model.head
hidden = model.lm(**inputs, output_hidden_states=True).hidden_states[-1]
logits_per_token = model.head(hidden).squeeze(-1)# (batch, seq_len)
# This will sometimes be compressed as model.forward() in other implementations
# Binary labels: 1=correct, 0=incorrect (prompt tokens masked as -100)
mask = labels != -100
loss = F.binary_cross_entropy_with_logits(
logits_per_token[mask], labels[mask].float()
)
The important intuition here is that an ORM will output a probability of correctness at
every token in the sequence (judged only by the final answer – reasoning errors are not
rlhfbook.com 44

captured in the ORM training process). This can be a noisy process, as the updates and
loss propagate per token depending on outcomes and attention mappings.
Figure 13: At inference time, an outcome reward model outputs per-token correctness
probabilities over completion tokens. Prompt tokens are ignored for scoring, and the
completion probabilities can be aggregated into a response-level score for verification, filtering,
or reranking.
Figure 14: Training an outcome reward model uses offline labels from a verifier or dataset
(e.g., all 1s for correct completions). Each completion token is trained with binary cross-
entropy against the outcome label, and per-token probabilities are aggregated into a final
score for verification, filtering, or reranking.
These models have continued to be used, but are less supported in open-source RLHF tools.
For example, the same type of ORM was used in the seminal workLet’s Verify Step by Step
\[50\], but without the language modeling prediction piece of the loss from Cobbe et al. 2021.
Then, the final loss is a cross-entropy loss on every token, predicting whether the final answer
is correct.
Given the lack of support, the term outcome reward model (ORM) has been used in multiple
ways. Some literature, e.g. \[75\], continues to be inspired by the original definition from
Cobbe et al. 2021; others use it more broadly for any verifier trained to predict whether a
completion is correct.
5.3 Process Reward Models
Process Reward Models (PRMs), originally called process-supervised reward models, are
reward models trained to output scores at everystepin a chain-of-thought reasoning process.
These differ from a standard RM that outputs a score only at an EOS token or an ORM that
rlhfbook.com 45

outputs a score at every token. Process Reward Models require supervision at the end of
each reasoning step, and then are trained similarly where the tokens in the step are trained
to their relevant target – the target is the step in PRMs and the entire response for ORMs.
Following \[50\], a binary-labeled PRM is commonly optimized with a per-step cross-entropy
loss:
LPRM(θ) =−E (x,s)∼D
[K∑
i=1
ysi logrθ(si|x,s <i) + (1−y si) log (1−rθ(si|x,s <i))
]
(21)
where s is a sampled chain-of-thought withK annotated steps,ysi∈{ 0, 1} denotes whether
the i-th step is correct, andrθ(si|x,s <i)is the PRM’s predicted probability that stepsi is
valid conditioned on the original promptxand all previous stepss<i.
Here’s an example of how this per-step label can be packaged in a trainer, from Hugging
Face’s TRL (Transformer Reinforcement Learning) \[47\]:
# Get the ID of the separator token and add it to the completions
separator_ids = tokenizer.encode(step_separator, add_special_tokens=False)
completions_ids = [completion + separator_idsforcompletionincompletions_ids]
# Create the label
labels = [[-100] * (len(completion) - 1) + [label]forcompletion, labelin
zip(completions_ids, labels)]
Traditionally PRMs are trained with a language modeling head that outputs a token only at
the end of a reasoning step, e.g. at the token corresponding to a double new line or other
special token. These predictions tend to be -1 for incorrect, 0 for neutral, and 1 for correct.
These labels do not necessarily tie to whether or not the model is on the right path, but
rather to whether the step is correct.
Figure 15: Process reward models provide supervision only at step boundaries (e.g., newline
tokens). Each step receives a 3-class label: correct (+1), neutral (0), or incorrect (-1). All
other tokens are masked during training.
An example construction of a PRM is shown below.
importtorch.nnasnn
importtorch.nn.functionalasF
classProcessRewardModel(nn.Module):
def__init__(self, base_lm, num_classes=3):
super().__init__()
rlhfbook.com 46

self.lm = base_lm# e.g., AutoModelForCausalLM
self.head = nn.Linear(self.lm.config.hidden_size, num_classes)
defforward(self, input_ids, attention_mask=None, labels=None):
"""
The inputs are tokenized prompts and completions, where the end of a
"reasoning step" is denoted by a designated separator token such as a
newline or other special marker rather than batch padding.
labels will be a list of labels, True, False, and Neutral (3 labels) which
will be predicted by the model.
If labels=None, this is an inference-only forward pass and the loss is
returned as None.
"""
outputs = self.lm(
input_ids=input_ids,
attention_mask=attention_mask,
output_hidden_states=True,
return_dict=True,
)
# Final hidden states: (batch, seq_len, hidden_size)
hidden = outputs.hidden_states[-1]
# One logit vector per token: (batch, seq_len, num_classes)
logits = self.head(hidden)
# Inference-only forward pass: no loss is computed.
iflabelsisNone:
returnNone, logits
# Only compute loss at step boundaries (where labels != -100)
# Labels map: -1 -> 0, 0 -> 1, 1 -> 2 (class indices)
mask = labels != -100
loss = None
ifmask.any():
loss = F.cross_entropy(
logits[mask], labels[mask]
)
else:
loss = logits.sum() * 0
returnloss, logits
The core loss function looks very similar to outcome reward models, with the labels being
applied at different intervals.
# Assume model outputs 3-class logits per token
hidden = model.lm(**inputs, output_hidden_states=True).hidden_states[-1]
logits = model.head(hidden)# (batch, seq_len, 3)
# 3-class labels at step boundaries only: 0=-1, 1=0, 2=1 (others masked as -100)
mask = labels != -100
loss = F.cross_entropy(logits[mask], labels[mask])
5.4 Comparing Reward Model Types (and Value Functions)
The various types of reward models covered indicate the spectrum of ways that “quality”
can be measured in RLHF and other post-training methods. Below is a summary of what
the models predict and how they are trained.
rlhfbook.com 47

Table 2: Comparing types of reward models.
Model Class What They Predict How They Are Trained LM structure
Reward
Models
Sequence-level quality
scorer θ(x,y)
Contrastive loss between
pairwise (or N-wise)
comparisons between
completions to the same
prompt
Linear head on
EOS/last-token
hidden state
Outcome
Reward
Models
Probability that an
answer is correct
per-token
Labeled outcomes (e.g.,
success/failure on
verifiable domains); each
sample is labeled
independently, with no
need for paired
comparisons on the same
prompt
Per-token binary
cross-entropy
head; labels
repeat the
outcome label
Process
Reward
Models
A reward or score for
intermediate steps at
end of reasoning steps
Trained using intermediate
feedback or stepwise
annotations (trained per
token in reasoning step)
Per-token head
predicting step
correctness (-1, 0,
1)
Value
Functions
The expected return
given the current state
Trained via regression to
each point in sequence
A scalar
regression head
with per-token
outputs
A few caveats on the distinctions in this table, as the boundaries between model types are
not always clear cut:
• Both in preference tuning and reasoning training, the value functions often have a
discount factor of 1, which makes a value function even closer to an outcome reward
model, but with a different training loss.
• A process reward model can be supervised by doing rollouts from an intermediate
state and collecting outcome data. This blends multiple ideas, but if thelossuses
per-reasoning-step labels, it is best referred to as a PRM.
What if you train a Bradley-Terry pairwise model with correct/incorrect pairs?
Much of the confusion on outcome reward models came from a small set of the literature
that was training a reward model on pairwise data derived from answer correctness. In this
domain, you set the chosen response as being a correct answer to a problem and a rejected
response as being an incorrect answerfor the same problem.This is technically not an ORM
and still trained directly with the contrastive, sequence-level loss. This is technically still a
Bradley-Terry model and would fall in the first class of models we covered.
ORM vs. Value Function.ORMs and value functions can appear similar since both
produce per-token outputs with the same head architecture, but they differ inwhat they
predictandwhere targets come from:
• ORMspredict, at every token, whether the completion will conclude with a correct
answer. Targets come fromoffline labels(a verifier or dataset marking sequences as
rlhfbook.com 48

correct or incorrect) and are broadcast to every intermediate token for training.
• Valuefunctionspredict theexpectedremainingreturn: V (st) = E
[∑
k≥tγk−trk|s t
]
.
Targets are typicallycomputed from on-policy rolloutsunder the current policyπθ, and
change as the policy changes (technically, value functions can also be off-policy, but
this is not established for work in language modeling).
If you define a dense token rewardrt = ⊮[token is correct]and use γ = 1, then an ORM is
learning rt (or p(rt = 1)) while the value head is learning the remaining-sum∑
k≥trk. They
can share the same base model and head dimensions, but thesemantics and supervision
pipelinediffer: ORMs are trained offline from fixed labels, while value functions are trained
on-policy and used to compute advantagesAt = ˆRt−Vt for policy gradients.
5.4.1 Inference Across Reward Model Types
The models handle data differently at inference time (once they’ve been trained), in order to
handle a suite of tasks that RMs are used for.
Bradley-Terry RM (Preference Model):
•Input:promptx+ candidate completiony
•Output:single scalarr θ(x,y)via a linear layer from the EOS/last-token hidden state
• Usage:rerank k completions, pick top-1 (best-of-N sampling); or provide terminal
reward for RLHF
•Aggregation:Not needed with scalar outputs
Outcome RM:
•Input:promptx+ completiony
• Output:per-token probabilities pt≈P (final answer correct|y ≤t)over completion
tokens
• Usage:score finished candidates; aggregate via mean, min (tail risk), or product∏
tpt
(equivalently, sum log-probabilities∑
t logpt)
• Aggregation choices:mean correctness, minimumpt, average over lastm tokens, or
threshold flagging if anypt <τ
Process RM:
•Input:promptx+ reasoning trace with step boundaries
•Output:scores at step boundaries (e.g., class logits for correct/neutral/incorrect)
• Usage:score completed chain-of-thought; or guide search/decoding by pruning low-
scoring branches
• Aggregation:over steps (not tokens) — mean step score, minimum (fail-fast), or
weighted sum favoring later steps
Value Function:
•Input:promptx+ current prefixy ≤t (a state)
• Output: Vt at each token position in the completion (expected remaining return from
statet)
• Usage: compute per-token advantagesAt = ˆRt−Vt during RL training; the values at
each step serve as baselines
rlhfbook.com 49

• Aggregation:typically take V at the last generated token; interpretation differs from
“probability of correctness”
In summary, the way to understand the different models is:
•RM:“How good is this whole answer?”→scalar value
• ORM:“Does this answer end up correct?”→per-token predictions of the outcome
(as a proxy for intermediate quality)
•PRM:“Are the reasoning steps sound?”→per-step scores
•Value:“How much reward remains from here?”→baseline for RL advantages
5.5 Other Reward Model Variants
Reward modeling is a relatively under-explored area of RLHF. The traditional, Bradley-Terry
reward modeling loss has been modified in many popular works, but the modifications have
not solidified into a single best practice.
5.5.1 Preference Margin Loss
In the case where annotators are providing either scores or rankings on a Likert Scale
(a rating scale with ordered categories indicating magnitude of preference, e.g. 1–5), the
magnitude of the relational quantities can be used in training. The most common practice
is to binarize the data along the preference direction, reducing the mixed information of
relative ratings or the strength of the ranking to just chosen and rejected completions. The
additional information, such as the magnitude of the preference, has been used to improve
model training, but it has not converged as a standard practice. Llama 2 proposes using the
margin between two data points,m(yc,yr), to distinguish the magnitude of preference:
L(θ) =−log (σ(r θ(yc|x)−r θ(yr|x)−m(y c,yr)))(22)
For example, each completion is often given a ranking from 1 to 5 in terms of quality. In the
case where the chosen sample was assigned a score of 5 and rejected a score of 2, the margin
m(yc,yr) = 5−2 = 3. Other functions for computing margins can be explored.
Note that in Llama 3 the margin term was removed as the team observed diminishing
improvements after scaling.
5.5.2 Balancing Multiple Comparisons Per Prompt
InstructGPT studies the impact of usingK = 4to9completions per prompt to rank,
producing
(K
2
)
pairwise comparisons from each prompt \[3\]. Because these comparisons are
highly correlated (they share the same prompt), shuffling them into the dataset naively causes
the reward model to overfit. To address this, they weight the loss updates per comparison
per prompt – without reweighting, prompts with more completions would contribute more
total loss simply because they generate more pairs. In practice, all
(K
2
)
comparisons from a
single prompt are typically included in the same training batch and averaged together, so
each prompt contributes one grouped update rather than appearing across many separate
batches. This reduces overfitting to individual prompts and prevents prompts with more
sampled completions from dominating the loss. The loss function becomes:
rlhfbook.com 50

L(θ) =− 1(K
2
)E(x,yc,yr)∼D log (σ(rθ(yc|x)−r θ(yr|x)))(23)
5.5.3 K-Wise Loss Function
There are many other formulations that can create suitable models of human preferences for
RLHF. One such example, used in the popular, early RLHF’d models Starling 7B and 34B
\[76\], is a K-wise loss function based on the Plackett-Luce model \[77\].
Zhu et al. 2023 \[78\] formalize the setup as follows. With a prompt, or state,si, K actions
(ai
0,ai
1,···,a i
K−1)are sampled from P (a0,···,a K−1|si). Then, labelers rank theK actions
by preference, producing a permutationσi : [K]↦→[K], whereσi(0)is the most preferred
action. This yields a Plackett-Luce probability over the complete ranking of allKitems:
P(σi|si,ai
0,ai
1,...,a i
K−1) =
K−1∏
k=0
exp(rθ⋆(si,ai
σi(k)))
∑K−1
j=k exp(rθ⋆(si,ai
σi(j)))
(24)
When K = 2, this reduces to the Bradley-Terry (BT) model for pairwise comparisons.
Regardless, once trained, these models are used similarly to other reward models during
RLHF training.
5.6 Generative Reward Modeling (a.k.a. LLM-as-a-judge)
With the cost of preference data, a large research area emerged to use existing language
models as a judge of human preferences or in other evaluation settings \[79\]. The core idea is to
prompt a language model with instructions on how to judge, a prompt, and two completions
(much as would be done with human labelers). An example prompt, from one of the seminal
works here for the chat evaluation MT-Bench \[79\], follows:
[System]
Please act as an impartial judge and evaluate the quality of the responses provided by
two AI assistants to the user question displayed below.
You should choose the assistant that follows the user's instructions and answers the
user's question better.
Your evaluation should consider factors such as the helpfulness, relevance, accuracy,
depth, creativity, and level of detail of their responses.
Begin your evaluation by comparing the two responses and provide a short explanation.
Avoid any position biases and ensure that the order in which the responses were
presented does not influence your decision.
Do not allow the length of the responses to influence your evaluation.
Do not favor certain names of the assistants.
Be as objective as possible.
After providing your explanation, output your final verdict by strictly following this
format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]"
for a tie.
[User Question]
{question}
[The Start of Assistant A's Answer]
{answer_a}
[The End of Assistant A's Answer]
[The Start of Assistant B's Answer]
{answer_b}
rlhfbook.com 51

[The End of Assistant B's Answer]
Given the efficacy of LLM-as-a-judge for evaluation, which spawned many other evaluations
such as AlpacaEval \[80\], Arena-Hard \[81\], and WildBench \[82\], many began using LLM-as-a-
judge instead of reward models to create and use preference data.
An entire field of study has emerged around how to use so-called “Generative Reward Models”
\[83\] \[84\] \[85\] (including models trainedspecificallyto be effective judges \[86\]), but on RM
evaluations they tend to be behind existing reward models, showing that reward modeling is
an important technique for current RLHF.
A common trick to improve the robustness of LLM-as-a-judge workflows is to use a sampling
temperature of 0 to reduce variance of ratings.
5.7 Further Reading
The academic literature for reward modeling established itself in 2024. The bulk of early
progress in reward modeling has focused on establishing benchmarks and identifying behavior
modes. The first RM benchmark, RewardBench, provided common infrastructure for testing
reward models \[87\]. Since then, RM evaluation has expanded to be similar to the types
of evaluations available to general post-trained models, where some evaluations test the
accuracy of prediction on domains with known true answers \[87\] or those more similar to
“vibes” performed with LLM-as-a-judge or correlations to other benchmarks \[88\].
Examples of new benchmarks include:
• Text-only (general chat / preferences):RMB \[89\], RewardBench2 \[90\], Preference
Proxy Evaluations \[91\], or RM-Bench \[92\].
• Specialized text-only (math, etc.):multilingual reward bench (M-RewardBench)
\[93\], RAG-RewardBench for retrieval augmented generation (RAG) \[94\], ReWordBench
for typos \[95\], RewardMATH \[96\], or AceMath-RewardBench \[97\].
• Process RMs:PRM Bench \[98\] or ProcessBench \[99\] and visual benchmarks of
VisualProcessBench \[100\] or ViLBench \[101\].
•Agentic RMs:Agent-RewardBench \[102\] or CUARewardBench \[103\].
• Multimodal:MJ-Bench \[104\], Multimodal RewardBench \[105\], VL RewardBench
\[106\], or VLRMBench \[107\].
To understand progress ontrainingreward models, one can reference new reward model
training methods, with aspect-conditioned models \[108\], high-quality human datasets \[109\]
\[110\], scaling experiments \[30\], extensive experimentation \[49\], or debiasing data \[111\].
5.8 Suggested Experiments
The companion code repository includes small reward model training scripts in
code/reward_models/. These are intended as learning exercises rather than tuned reference
recipes. Start from a cleancode/ environment with uv sync , then run one experiment at a
time.
1.Train a Bradley-Terry preference reward model on UltraFeedback.Run:
rlhfbook.com 52

cd code/
uv run python -m reward_models.train_preference_rm --config
reward_models/configs/preference_rm.yaml
Watch whether the reward margin between chosen and rejected responses grows in the
demo and W&B logs. Then varysamples, lr, and model_id in the yaml config to see
when the signal becomes noisy or unstable.
2. Compare outcome and process supervision.Run the GSM8K outcome reward
model and the PRM800K process reward model:
cd code/
uv run python -m reward_models.train_orm --config reward_models/configs/orm.yaml
uv run python -m reward_models.train_prm --samples 500 --epochs 2
Compare what each model can score after training: the ORM should distinguish correct
and incorrect final answers, while the PRM should assign scores across intermediate
reasoning steps. This is the practical version of the distinction between sequence-level,
outcome-level, and process-level supervision.
3. Add a small held-out reward model eval.A useful contribution is a 50- to
200-example evaluation forreward_models/ that reports accuracy or preference-pair
ordering without requiring a full training run. Keep the evaluation small enough that
it can be used while tuning hyperparameters.
rlhfbook.com 53

6 Reinforcement Learning
In the RLHF process, the reinforcement learning algorithm slowly updates the model’s
weights with respect to feedback from a reward model. The policy – the model being trained
– generates completions to prompts in the training set, then the reward model scores them,
and the reinforcement learning optimizer takes gradient steps based on this information (see
fig. 16 for an overview). This chapter explains the mathematics and trade-offs across various
algorithms used to learn from the signal the reward model gives to on-policy data. These
algorithms are run for a period of many epochs, often thousands or millions of batches across
a larger set of prompts, with gradient updates in between each of them.
6.1 The Role of Reinforcement Learning in RLHF
The algorithms that popularized RLHF for language models were policy-gradient reinforce-
ment learning algorithms. These algorithms, such as Proximal Policy Optimization (PPO),
Group Relative Policy Optimization (GRPO), and REINFORCE, use recently generated
samples to update their model (rather than storing scores in a replay buffer like algorithms,
e.g. Deep Q-Networks, DQN, used in popular projects such as AlphaGo). In this section we
will cover the fundamentals of the policy gradient algorithms and how they are used in the
modern RLHF framework.
At a machine learning level, this section is the subject with the highest complexity in the
RLHF process. However, as with most modern AI models, the largest determining factor in
its success is the data provided as inputs to the process.
When RLHF came onto the scene with ChatGPT, it was largely known that they used
a variant of PPO, and many initial efforts were built upon that. Over time, multiple
research projects showed the promise of REINFORCE-style algorithms \[112\] \[110\], touted
for their simplicity over PPO without a separate value model (saves memory and therefore
the number of GPUs required) and with simpler advantage estimation (no Generalized
Advantage Estimation, GAE, which is a method to compute advantages used for variance
reduction in policy gradient algorithms). More algorithms have emerged, including Group
Relative Policy Optimization, which is particularly popular with reasoning tasks, but in
general many of these algorithms can be tuned to fit a specific task. In this chapter, we
cover the core policy gradient setup and the three algorithms mentioned above due to their
central role in the establishment of a canonical RLHF literature.
At its simplest, the RL stage of RLHF requires two models: a policy (the model being trained)
and a reward model that scores its outputs (as covered in the previous chapter). A copy of
the policy before RL serves as the reference model for computing a KL penalty (this model
is frozen, i.e. it is not updated with gradients from the automatic differentiation engine).
The most complex algorithm covered here, PPO, adds a fourth model – a learned value
function used to estimate how good each token in the action was, also a large language model
updated during training. The algorithms in this chapter differ mainly in how they estimate
a quantity calledadvantages– a measure of how good the current action (completion) from
the model is relative to average – and how they constrain policy updates so the optimization
is numerically stable. A visual overview of this RLHF process (without the value model) is
shown in fig. 16.
For definitions of symbols, see the problem setup chapter.
rlhfbook.com 54

Figure 16: Overview of the RLHF training loop. A prompt from the dataset is passed to the
tuned policy, which generates a completion. The reward model scores this completion, while
the frozen initial model (typically the instruction-tuned model before RL) computes log
probabilities on the same text to calculate a KL penalty that prevents excessive drift. The
combined reward signal then drives a reinforcement learning update to the policy parameters.
rlhfbook.com 55

This chapter uses(s,a )notation from the reinforcement learning literature, wheres denotes
states anda denotes actions. In the language model context, you will often see(x,y )instead,
wherex is the prompt andy is the completion. The(s,a )framing is more general—these
algorithms were designed for sequential decision problems where actions are taken at each
timestep. However, many RLHF implementations treat the entire completion as a single
action, making the(x,y)notation equally valid.
RL Cheatsheet:A one-page reference of all core RL loss functions from this chapter is
available at rlhfbook.com/rl-cheatsheet.
6.2 Policy Gradient Algorithms
At its core, this chapter is dedicated to understanding the following shape of equation. This
equation is computing the gradient,∆θ, to the language model we are training,πθ:
∆θ∝Ψ t∇θ logπθ(at|s t)(25)
Here, the equation is composed of two key components: 1.∇θ logπθ(at|s t)— which
direction in parameter space makes actionat more likely. 2.Ψ t — how good was it? A
scalar scoring the outcome.
When you put this together, yes, by multiplying the quantities, you get the policy gradient
update. Some things are simple, such as thatΨt > 0updates parameters to makeat more
likely,Ψt < 0updates them to make it less likely. The policy gradient is computing which
parameters contribute to an action and if we should make it more or less likely to occur in
the future. The rest of this chapter goes very deep on the different ways to do this, and what
the specific tricks are to make it work for LLMs.
Now, let us formalize this a bit further. Reinforcement learning algorithms are designed to
maximize the future, discounted reward across a trajectory of states,s∈S , and actions,
a∈A (for more notation, see Appendix A, Definitions). The objective of the agent, often
called thereturn, is the sum of discounted rewards starting at a given timet (whereγ∈ [0, 1]
is a factor that prioritizes near-term rewards):
Gt =r t +γr t+1 +···=
∞∑
k=0
γkrt+k.(26)
The return definition can also be written recursively as:
Gt =r t +γG t+1.(27)
This return is the basis for learning a value functionV (s)that is the estimated future return
given a current state:
V(s) =E[G t|S t =s].(28)
All policy gradient algorithms optimize a policyπθ(a|s )to maximize expected return; this
objective can be expressed using the induced value functionVπθ(s).
rlhfbook.com 56

Letd0(s)be the initial-state distribution. The episodic objective we maximize can be written
as:
J(θ) =
∑
s
d0(s)Vπθ(s),(29)
In a finite MDP this is a sum over possible starting states, but in practice we never compute
it exactly. Instead, we estimate it from data by sampling rollouts from the current policy. In
RLHF this typically means sampling promptsxi from a dataset and generating completions
yi ∼π θ(·|x i). Let R(xi,yi)denote the scalar sequence-level reward assigned to that
prompt-completion pair; ifτi is the corresponding episode, this is the trajectory reward
R(τi). We then take an empirical average such as:
ˆJ(θ) = 1
B
B∑
i=1
R(xi,yi),(30)
or, in an MDP view with per-step rewards,
ˆJ(θ) = 1
B
B∑
i=1
Ti∑
t=0
γtri,t.(31)
In practice, RLHF for language models setsγ = 1(no discounting) because the unit of
optimization is the collective completion, not individual tokens – this choice is discussed
further in the MDP vs. Bandit section later in this chapter.
The core of policy gradient algorithms is computing the gradient with respect to the finite-
time expected return over the current policy. With this expected return,J, the parameter
update can be computed as follows, whereαis the learning rate:
θ←θ+α∇ θJ(θ)(32)
The core implementation detail is how to compute said gradient.
6.2.1 Deriving the Policy Gradient
Let pθ(τ)denote the trajectory distribution induced by the initial-state distributiond0, the
policy πθ, and the environment transition dynamics, as expanded in eq. 35 below. Another
way to pose the RL objective we want to maximize is as follows:
J(θ) =E τ∼pθ [R(τ)],(33)
where τ = (s0,a 0,s 1,a 1,... )is a trajectory and R(τ) = ∑∞
t=0rt is the total reward of
the trajectory. Alternatively, we can write the expectation as an integral over all possible
trajectories:
J(θ) =
∫
τ
pθ(τ)R(τ)dτ(34)
rlhfbook.com 57

Notice that we can express the trajectory probability as follows, whereπθ(at|st)p(st+1|st,at)
combines the policy probability with the environment transition probability from one state-
action pair to the next state:
pθ(τ) =d 0(s0)
∞∏
t=0
πθ(at|st)p(st+1|st,at),(35)
If we take the gradient of the objective (eq. 33) with respect to the policy parametersθ:
∇θJ(θ) =
∫
τ
∇θpθ(τ)R(τ)dτ(36)
Notice that we can use the log-derivative trick in order to rewrite the gradient of the integral
as an expectation:
∇θ logpθ(τ) = ∇θpθ(τ)
pθ(τ) (from chain rule)
=⇒ ∇θpθ(τ) =p θ(τ)∇θ logpθ(τ)(rearranging)
(37)
Using this log-derivative trick:
∇θJ(θ) =
∫
τ
∇θpθ(τ)R(τ)dτ
=
∫
τ
pθ(τ)R(τ)∇θ logpθ(τ)dτ
=E τ∼pθ [R(τ)∇θ logpθ(τ)]
(38)
Where the final step uses the definition of an expectation under the trajectory distribution
pθ(τ): for any functionf, Eτ∼pθ[f(τ)] =
∫
τf(τ)pθ(τ)dτ (or a sum in the discrete case).
Writing it as an expectation is useful because we can approximate it with Monte Carlo
rollouts, e.g., 1
B
∑B
i=1f(τi)for trajectoriesτ i∼p θ induced by the current policy.
Back to the derivation, expanding the log probability of the trajectory:
logpθ(τ) = logd 0(s0) +
∞∑
t=0
logπθ(at|st) +
∞∑
t=0
logp(st+1|st,at)(39)
Now, if we take the gradient of the above, we get:
•∇ θ logd 0(s0) = 0(initial state distribution doesn’t depend onθ)
•∇ θ logp(st+1|st,at) = 0(environment transition dynamics don’t depend onθ)
•only∇ θ logπθ(at|st)survives
Therefore, the gradient of the log probability of the trajectory simplifies to:
∇θ logpθ(τ) =
∞∑
t=0
∇θ logπθ(at|st)(40)
rlhfbook.com 58

Reaching this equation is a crucial point in the implementation. Here, we have gone far
enough to see that the gradient of the trajectory distribution reduces to a sum of gradients
from language model policy probabilities (which are just the probabilities of tokens given by
the model we’re training). In practice, this results in a common form of the policy gradient
equations. They end up looking like a sum of log-probabilities in the loss, and then we
compute the gradients via autodiff. A short snippet you’ll see again and again roughly
follows:
seq_log_probs = (token_log_probs * completion_mask).sum(dim=-1)
loss = -(seq_log_probs * advantages).mean()
loss.backward()
You’ll see this throughout the chapter. Now, back to the formal policy gradient mathematics.
Substituting this back in eq. 38, we get:
∇θJ(θ) =E τ∼pθ
[∞∑
t=0
R(τ)∇θ logπθ(at|st)
]
(41)
Quite often, people use a more general formulation of the policy gradient:
g=∇ θJ(θ) =E τ∼pθ
[∞∑
t=0
Ψt∇θ logπθ(at|st)
]
(42)
WhereΨ t can be the following (where the rewards can also often be discounted byγ), a
taxonomy adopted from Schulman et al. 2015 \[113\]:
1.R(τ) = ∑∞
t=0rt: total reward of the trajectory.
2. ∑∞
t′=trt′: reward following actionat, also described as the return from timet,Gt.
3. ∑∞
t′=trt′−b(st): baselined version of previous formula.
4.Q π(st,at): state-action value function.
5.A π(st,at): advantage function, which yields the lowest possible theoretical variance if
it can be computed accurately.
6.r t +γV π(st+1)−V π(st): Temporal Difference (TD) residual.
Thebaselineis a value used to reduce variance of policy updates (more on this below).
For language models, some of these concepts do not make as much sense. For example,
for a deterministic policyπ the state value isVπ(st) =Qπ(st,π (st))(and for the optimal
value function one hasV∗(st) = maxatQ∗(st,at)). For a stochastic policy, the analogous
identity isVπ(st) = Eat∼π(·|st)[Qπ(st,at)]. The Bellman equation relates Q to V: in general
Qπ(st,at) = E[rt +γV π(st+1)|s t,at], but for language models where state transitions are
deterministic, this simplifies toQ(st,at) =rt +γV (st+1). The advantage function measures
how much better actionat is compared to the average:
A(st,at) =Q(s t,at)−V(s t) =r t +γV(s t+1)−V(s t)(43)
This final form is exactly the temporal difference (TD) residual (item 6 above) – a fundamental
quantity in RL that measures the gap between the value function’s prediction and what
actually occurred, driving value function updates toward more accurate estimates. In practice,
a learned value functionˆVis used to estimate the advantage via this TD error.
rlhfbook.com 59

6.2.2 Vanilla Policy Gradient
The vanilla policy gradient implementation optimizes the above expression forJ(θ)by
differentiating with respect to the policy parameters. A simple version, with respect to the
time-treturn, is:
∇θJ(θ) =E τ∼pθ
[T∑
t=0
Gt∇θ logπθ(at|st)
]
(44)
A common problem with vanilla policy gradient algorithms is the high variance in gradient
updates, which can be mitigated in multiple ways. The high variance comes from the gradient
updates being computed by estimating the returnG from an often small set of rollouts in the
environment that tend to be susceptible to noise (e.g. the stochastic nature of generating from
language models with temperature> 0). The variance across return estimates is higher in
domains with sparse rewards, as more of the samples are 0 or 1, rather than closely clustered.
In order to alleviate this, various techniques are used to normalize the value estimation, called
baselines. Baselines accomplish this in multiple ways, effectively normalizing by the value
of the state relative to the downstream action (e.g. in the case of Advantage, which is the
difference between the Q value and the value). The simplest baselines are averages over the
batch of rewards or a moving average. Even these action-independent baselines can reduce
variance without changing the expected gradient, sinceEa∼π(a|s)[b(s)∇θ logπθ(a|s)] = 0for
any state-dependentb(s), improving the learning signal substantially.
Many of the policy gradient algorithms discussed in this chapter build on the advantage
formulation of policy gradient:
∇θJ(θ) =E τ∼pθ
[T∑
t=0
Aπθ(st,at)∇θ logπθ(at|st)
]
(45)
6.2.3 REINFORCE
The algorithm REINFORCE is likely a backronym, but the components of the algorithm it
represents are quite relevant for modern reinforcement learning algorithms. Defined in the
seminal paperSimple statistical gradient-following algorithms for connectionist reinforcement
learning\[114\]:
The name is an acronym for “REward Increment = Nonnegative Factor X Offset
Reinforcement X Characteristic Eligibility.”
The three components of this are how to do thereward increment, a.k.a. the policy gradient
step. It has three pieces to the update rule:
1. Nonnegative factor: This is the learning rate (step size) that must be a positive number,
e.g.αbelow.
2. Offset Reinforcement: This is a baselineb or other normalizing factor of the reward to
improve stability.
3. Characteristic Eligibility: This attributes the scalar reward signal to the parameters
that produced the action. Williams denotes this eligibility term ase(not the exponential
function). In modern policy-gradient notation, it corresponds to∇θ logπθ(at|s t).
rlhfbook.com 60

Thus, the form looks quite familiar:
∆θ =α(r−b)e(46)
With more modern notation and the generalized returnG, the REINFORCE operator
appears as:
∇θJ(θ) =E τ∼pθ
[T∑
t=0
(Gt−b(st))∇θ logπθ(at|s t)
]
,(47)
Here, the valueGt−b (st)is theadvantageof the policy at the current state, so we can
reformulate the policy gradient in a form that we continue later with the advantage,A:
∇θJ(θ) =E τ∼pθ
[T∑
t=0
At∇θ logπθ(at|s t)
]
,(48)
REINFORCE is a specific implementation of vanilla policy gradient that uses a Monte Carlo
estimator of the gradient.
Figure 17: Basic REINFORCE architecture for language models. The shaped reward
combines the reward model score with a KL penalty from the reference model. We build on
this structure throughout the chapter.
6.2.4 REINFORCE Leave One Out (RLOO)
The core implementation detail of REINFORCE Leave One Out versus standard REIN-
FORCE is that it takes the average reward of theothersamples in the batch to compute the
baseline – rather than averaging over all rewards in the batch \[115\], \[112\], \[116\]. By excluding
the current sample’s reward from its own baseline, the RLOO baseline is independent of the
action being evaluated, which keeps the gradient estimator exactly unbiased.
Crucially, this only works when generating multiple trajectories (completions) per state
(prompt), which is common practice in multiple domains of fine-tuning language models with
RL.
rlhfbook.com 61

Specifically, for the REINFORCE Leave-One-Out (RLOO) baseline, givenK sampled
trajectories (actions taken conditioned on a prompt)a1,...,a K, to a given prompts we
define the baseline explicitly as the followingper-prompt:
b(s,ak) = 1
K−1
K∑
i=1,i̸=k
R(s,ai),(49)
resulting in the advantage:
A(s,ak) =R(s,a k)−b(s,a k).(50)
Equivalently, this can be expressed as:
A(s,ak) = K
K−1
(
R(s,ak)− 1
K
K∑
i=1
R(s,ai)
)
.(51)
This is a simple, low-varianceper-promptadvantage estimate that is closely related to the
group-relative advantage used in Group Relative Policy Optimization, GRPO (discussed
shortly, after Proximal Policy Optimization, PPO). In practice, GRPO-style training mainly
differs in how it applies the KL regularizer (as an explicit loss term vs. folded into the
reward) and whether it uses PPO-style ratio clipping. To be specific, the canonical GRPO
implementation applies the KL penalty at the loss level, whereas the derivation for RLOO or
traditional policy-gradients applies the KL penalty to the reward itself. With the transition
from RLHF to reasoning and reinforcement learning with verifiable rewards (RLVR), the
prevalence of KL penalties has decreased overall, with many reasoning adaptations of RLHF
code turning them off entirely. Still, the advantage from RLOO could be combined with the
clipping of PPO, showing how similar many of these algorithms are.
RLOO and other algorithms that do not use a value network – an additional model copy (a
critic) that predicts a scalar valueV (st)per token – assign the same sequence-level advantage
(or reward) to every token when computing the loss. Algorithms that use a learned value
network, such as PPO, assign a different value to every token individually, discounting from
the final reward achieved at the EOS token. With a KL distance penalty, RLOO aggregates
the per-token KL over the completion and folds that scalar into the sequence reward, so
the resulting advantage is broadcast to all tokens. PPO subtracts a per-token KL from the
per-token reward before computingAt, giving token-level credit assignment. GRPO typically
retains a sequence-level advantage but adds a separate per-token term to the loss, rather
than subtracting it from the reward. These details and trade-offs are discussed later in the
chapter.
6.2.5 Proximal Policy Optimization (PPO)
Proximal Policy Optimization (PPO) \[117\] is one of the foundational algorithms behind
Deep RL’s successes (such as OpenAI Five, which mastered Dota 2 \[118\] and large amounts
of research). The objective that PPO maximizes, with respect to the advantages and the
policy probabilities, is as follows:
rlhfbook.com 62

Figure 18: REINFORCE Leave-One-Out (RLOO) architecture. Multiple completions per
prompt provide a leave-one-out baseline for advantage estimation without learning a value
function.
J(θ) = min
( πθ(a|s)
πθold(a|s)A,clip
( πθ(a|s)
πθold(a|s),1−ε,1 +ε
)
A
)
.(52)
Here, πθ(a|s)is the current policy being optimized andπθold(a|s)is the policy that was used
to collect the training data (i.e., the policy from the previous iteration). The ratio between
these two policies emerges fromimportance sampling, which allows us to reuse data collected
under an old policy to estimate gradients for a new policy.
Recall from the advantage formulation of the policy gradient (eq. 45) that we have:
∇θJ(θ) =E τ∼pθ
[T∑
t=0
Aπθ(st,at)∇θ logπθ(at|st)
]
.(53)
This expectation is taken over trajectories sampled from the trajectory distribution induced
byπθ, but in practice we want to take multiple gradient steps on a batch of data that was
collected from a fixed policyπθold. To correct for this distribution mismatch, we multiply by
the importance weight πθ(a|s)
πθold(a|s), which reweights samples to account for how much more
or less likely they are under the current policy versus the data-collection policy. Without
constraints, optimizing this importance-weighted objective can lead to destructively large
policy updates when the ratio diverges far from 1. PPO addresses this by clipping the ratio
to the range[1−ε, 1 +ε], ensuring that the policy cannot change too drastically in a single
update.
Note that, as we move to PPO and its peer algorithms, we often work with theobjective
rather than an explicit gradient. This is because the PPO objective doesnothave an easily
interpretable analytical gradient once themin and clipping operations are included (the
gradient has ~4 terms corresponding to the regions in fig. 20, depending on how it is written);
writing the objective is simply the clearer way to convey these algorithms.
For completeness, PPO is typically written as anexpectedclipped surrogate objective over
timesteps:
rlhfbook.com 63

J(θ) =E t [min (ρt(θ)At,clip(ρ t(θ),1−ε,1 +ε)A t)], ρ t(θ) = πθ(at|s t)
πθold(at|s t).(54)
The objective is often converted into a loss function by simply adding a negative sign, which
makes the optimizer seek to make it as negative as possible.
For language models, the objective (or loss) is computed per token, which intuitively can be
grounded in how one would compute the probability of the entire sequence of autoregressive
predictions – by a product of probabilities. From there, the common implementation is
withlog-probabilitiesthat make the computation simpler to perform in modern language
modeling frameworks. In practice, one computes the difference of token log-probabilities and
exponentiates it to recover the policy ratioρt.
J(θ) = 1
|a|
|a|∑
t=0
min
( πθ(at|st)
πθold(at|st)At,clip
( πθ(at|st)
πθold(at|st),1−ε,1 +ε
)
At
)
.(55)
This is the per-token version of PPO, which also applies to other policy-gradient methods,
but is explored further later in the implementation section of this chapter. Here, the term for
averaging by the number of tokens in the action,1
|a|, comes from common implementation
practices, but is not in a formal derivation of the loss (shown in \[119\]).
Figure 19: PPO framework. A learned value function enables Generalized Advantage
Estimation (GAE) for per-token advantages, used with a clipped surrogate objective.
Here we will explain the different cases this loss function triggers given various advantages
and policy ratios. At an implementation level, the inner computations for PPO involve two
main terms: 1) a standard policy gradient with a learned advantage and 2) a clipped policy
gradient based on a maximum step size.
To understand how different situations emerge, we can define the policy ratio as:
ρ(θ) = πθ(a|s)
πθold(a|s) (56)
rlhfbook.com 64

The policy ratio is a centerpiece of PPO and related algorithms. It emerges from computing
the gradient of a policy and controls the parameter updates in a very intuitive way. For any
batch of data, the policy ratio starts at 1 for the first gradient step for that batch, sinceπθ
is the same asπθold at this point. Then, in the next gradient step, the policy ratio will be
above one if that gradient step increased the likelihood of certain tokens with an associated
positive advantage, or less than one for the other case. A common practice is to take 1-4
gradient steps per batch with policy gradient algorithms before updatingπθold.
6.2.6 Understanding the PPO Objective
Overall, the PPO objective can be visualized by two lines of a plot of objective versus policy
ratio, which is shown in fig. 20. The PPO objective is maximized by changing the probability
of the sampled actions. Numerically, the objective controls for both positive and negative
advantage cases by clever use of the minimum operation, making it so the update is at most
pushed by an epsilon distance away from a policy ratio of 1.
Within the trust region, PPO operates the same as other policy gradient algorithms. This is
by design! The trust region is a concept used to cap the maximum step size of PPO and
its peer algorithms for stability of updates. The core of the PPO algorithm, the clip and
min/max functions, define this region. The objective becomes flat outside of it.
The idea of a “trust region” comes from the numerical optimization literature \[120\], but was
popularized within Deep RL from the algorithm Trust Region Policy Optimization (TRPO),
which is accepted as the predecessor to PPO \[121\]. The trust region is the area where the
full policy-gradient steps are applied, as the updates are not “clipped” by the max/min
operations of the PPO objective.
The policy ratio and advantage together can occur in a few different configurations, which
fig. 20 enumerates by the sign of the advantageAt and by which of the three regions the
policy ratioρ(θ)falls into. Two facts determine the outcome in every region: the sign of
the advantage sets whether we want to make the action more or less likely, and themin
operation selects either the unclipped termρ(θ)At or its clipped counterpart.
The clipping only zeroes out the gradient in the two regions where the policy hasalready
moved the sampled action in the desired direction, past the edge of the trust region:
• Positive advantage andρ(θ)> 1 +ε: the action is already substantially more likely
under πθ than underπθold. The objective saturates at(1 +ε)At, its gradient is zero,
and no update is made — we avoid over-reinforcing an action that is already more
expressed.
• Negative advantage andρ(θ)< 1−ε: the action is already substantially less likely
under πθ. The objective saturates at(1 −ε )At, its gradient is again zero, and no
update is made — we avoid over-suppressing an action that is already discouraged.
Everywhere else the unclipped termρ(θ)At is active and PPO takes a standard policy-
gradient step: increasing the action’s probability whenAt > 0and decreasing it whenAt < 0.
We can read off fig. 20 in terms of what each region asks of the updated policyπθ:
• the sloped, unclipped region under a positive advantage (green)increasesthe proba-
bility of the sampled action;
•the sloped, unclipped region under a negative advantage (red)decreasesit;
• the flat, clipped region (grey) leaves the policyunchanged, since its gradient is zero.
rlhfbook.com 65

Figure 20: Visualization of the PPO objectiveJ(θ)as a function of the policy ratioρ(θ),
for both positive and negative advantage. Within each panel, the three ratio regions are
annotated with their unclipped term, clipped term, resulting objective, and gradient.
rlhfbook.com 66

The same regions, written out term by term:
6.2.6.1 Positive Advantage (At > 0)This means that the action taken was beneficial
according to the value function, and we want to increase the likelihood of taking that action
in the future. Now, let’s look at different cases for the policy ratioρ(θ):
1.ρ(θ)<1−ε:
•Interpretation: Action is less likely with the new policy than the old policy
•Unclipped Term:ρ(θ)A t
•Clipped Term:(1−ε)A t
•Objective:ρ(θ)A t
•Gradient:∇ θρ(θ)At̸= 0
•What happens: Normal policy-gradient update - increase likelihood of action
2.1−ε≤ρ(θ)≤1 +ε:
• Interpretation: Action is almost equally likely with the new policy as the old
policy
•Unclipped Term:ρ(θ)A t
•Clipped Term:ρ(θ)A t
•Objective:ρ(θ)A t
•Gradient:∇ θρ(θ)At̸= 0
•What happens: Normal policy-gradient update - increase likelihood of action
3.1 +ε<ρ(θ):
•Interpretation: Action is more likely with the new policy than the old policy
•Unclipped Term:ρ(θ)A t
•Clipped Term:(1 +ε)A t
•Objective:(1 +ε)A t
•Gradient:∇ θ(1 +ε)At = 0
• What happens: NO UPDATE - action is already more likely under the new
policy
To summarize, when the advantage is positive (At > 0), we want to boost the probability of
the action. Therefore:
• We perform gradient steps only in the case whenπnew(a)≤ (1 +ε)πold(a). Intuitively,
we want to boost the probability of the action, since the advantage was positive, but
not boost it so much that we have made it substantially more likely.
• Crucially, whenπnew(a)> (1 +ε)πold(a), then we don’t perform any update, and the
gradient of the clipped objective is0. Intuitively, the action is already more expressed
with the new policy, so we don’t want to over-reinforce it.
6.2.6.2 Negative Advantage (At < 0)This means that the action taken was detri-
mental according to the value function, and we want to decrease the likelihood of taking
that action in the future. Now, let’s look at different cases for the policy ratioρ(θ):
1.ρ(θ)<1−ε:
•Interpretation: Action is less likely with the new policy than the old policy
•Unclipped Term:ρ(θ)A t
rlhfbook.com 67

•Clipped Term:(1−ε)A t
•Objective:(1−ε)A t
•Gradient:∇ θ(1−ε)A t = 0
• What happens: NO UPDATE - action is already less likely under the new
policy
2.1−ε≤ρ(θ)≤1 +ε:
• Interpretation: Action is almost equally likely with the new policy as the old
policy
•Unclipped Term:ρ(θ)A t
•Clipped Term:ρ(θ)A t
•Objective:ρ(θ)A t
•Gradient:∇ θρ(θ)At̸= 0
•What happens: Normal policy-gradient update - decrease likelihood of action
3.1 +ε<ρ(θ):
•Interpretation: Action is more likely with the new policy than the old policy
•Unclipped Term:ρ(θ)A t
•Clipped Term:(1 +ε)A t
•Objective:ρ(θ)A t
•Gradient:∇ θρ(θ)At̸= 0
•What happens: Normal policy-gradient update - decrease likelihood of action
To summarize, when the advantage is negative (At < 0), we want to decrease the probability
of the action. Therefore:
• We perform gradient steps only in the case whenπnew(a)≥ (1−ε )πold(a). Intuitively,
we want to decrease the probability of the action, since the advantage was negative,
and we do so proportional to the advantage.
• Crucially, whenπnew(a)< (1−ε )πold(a), then we don’t perform any update, and the
gradient of the clipped objective is0. Intuitively, the action is already less likely under
the new policy, so we don’t want to over-suppress it.
It is crucial to remember that PPO within the trust region is roughly the same as standard
forms of policy gradient.
6.2.7 Value Functions and PPO
The value function within PPO is an additional copy of the model that is used to predict the
value per token. The value of a token (or state) in traditional RL is predicting the future
return from that moment, often with discounting. This value in PPO is used as a learned
baseline, representing an evolution of the simple Monte Carlo version used with REINFORCE
(which doesn’t need the learned value network). This highlights how PPO is an evolution of
REINFORCE and vanilla policy-gradient in multiple forms, across the optimization form,
baseline, etc. In practice, with PPO and other algorithms used for language models, this is
predicting the return of each token after the deduction of KL penalties (the per-token loss
includes the KL from the reward traditionally, as discussed).
There are a few different methods (or targets) used to learn the value functions. Generalized
Advantage Estimation (GAE) is considered the state-of-the-art and canonical implementation
rlhfbook.com 68

in modern systems, but it carries more complexity by computing the value prediction error
over multiple steps – see the later section on GAE in this chapter. A value function can also
be learned with Monte Carlo estimates from the rollouts used to update the policy. PPO
has two losses – one to learn the value function and another to use that value function to
update the policy.
Figure 21: Value function training uses on-policy rollouts to compute targets. The model
predicts Vt at each token, which is trained via MSE against the target returnˆVt. The
advantageAt = ˆVt−Vt then weights the policy gradient update.
A simple example implementation of a value network loss is shown below.
# Basic PPO critic targets & loss (no GAE)
#
# B: Batch Size
# L: Completion Length
# Inputs:
# rewards: (B, L) post-KL per-token rewards; EOS row includes outcome
# done_mask: (B, L) 1.0 at terminal token (EOS or truncation if penalized), else 0.0
# completion_mask: (B, L) 1.0 on response tokens to supervise (ignore the prompt)
# values: (B, L) current critic predictions V_theta(s_t)
# because a value network is a running update
# old_values: (B, L) critic predictions at rollout time V_{theta_old}(s_t)
# gamma: discount factor, float (often 1.0 for LM RLHF)
# epsilon_v: float value clip range (e.g., 0.2), similar to PPO Loss Update itself,
optional
#
# Returns:
# value_loss: scalar; advantages: (B, L) detached (for policy loss)
B, L = rewards.shape
# 1) Monte Carlo returns per token (reset at terminals)
# Apply discounting, if enabled
returns = torch.zeros_like(rewards)
running = torch.zeros(B, device=rewards.device, dtype=rewards.dtype)
fortinreversed(range(L)):
running = rewards[:, t] + gamma * (1.0 - done_mask[:, t]) * running
rlhfbook.com 69

returns[:, t] = running
targets = returns# y_t = G_t (post-KL)
# 2) PPO-style value clipping (optional)
v_pred = values
v_old = old_values
v_clip = torch.clamp(v_pred, v_old - epsilon_v, v_old + epsilon_v)
vf_unclipped = 0.5 * (v_pred - targets) ** 2
vf_clipped = 0.5 * (v_clip - targets) ** 2
vf_loss_tok = torch.max(vf_unclipped, vf_clipped)
# 3) Mask to response tokens and aggregate
denom = completion_mask.sum(dim=1).clamp_min(1)
value_loss = ((vf_loss_tok * completion_mask).sum(dim=1) / denom).mean()
# 4) Advantages for policy loss (no GAE): A_t = G_t - V(s_t)
advantages = (targets - v_pred).detach()
# The value loss is applied later, often with the PG loss, e.g.
# total_loss = policy_loss + vf_coef * value_loss
6.2.8 Group Relative Policy Optimization (GRPO)
Group Relative Policy Optimization (GRPO) is introduced in DeepSeekMath \[122\], and used
in other DeepSeek works, e.g. DeepSeek-V3 \[16\] and DeepSeek-R1 \[15\]. GRPO can be viewed
as a PPO-inspired algorithm with a very similar surrogate loss, but it avoids learning a value
function with another copy of the original policy language model (or another checkpoint for
initialization). This brings two posited benefits:
1. Avoiding the challenge of learning a value function from an LM backbone, where
research hasn’t established best practices.
2. Saves memory by not needing to keep the extra set of model weights in memory (going
from needing the current policy, the reference policy, and a value function, to just the
first two copies).
GRPO does this by simplifying the value estimation and assigning the same value to every
token in the episode (i.e. in the completion to a prompt, each token gets assigned the
same value rather than discounted rewards in a standard value function) by estimating the
advantage or baseline. The estimate is done by collecting multiple completions (ai) and
rewards (ri), i.e. a Monte Carlo estimate, from the same initial state / prompt (s).
To state this formally, the GRPO objective is very similar to the PPO objective above. For
GRPO, the objective (or loss) is accumulated over a group of completions{a1,a 2,...,a G} to
a given prompts. Here, we show the GRPO objective:
J(θ) = 1
G
G∑
i=1
(
min
( πθ(ai|s)
πθold(ai|s)Ai,clip
( πθ(ai|s)
πθold(ai|s),1−ε,1 +ε
)
Ai
)
−βD KL(πθ||πref)
)
.
(57)
Note that relative to PPO, the standard implementation of GRPO includes the KL distance
in the loss. As above, we can expand this into a per-token computation:
rlhfbook.com 70

J(θ) = 1
G
G∑
i=1
1
|ai|
|ai|∑
t=1
(
min
( πθ(ai,t|si)
πθold(ai,t|si)Ai,t,clip
( πθ(ai,t|si)
πθold(ai,t|si),1−ε,1 +ε
)
Ai,t
)
−βD KL(πθ(·|si)∥πref(·|si))
) (58)
With the advantage computation for the completion indexi:
Ai = ri−mean(r 1,r 2,···,r G)
std(r1,r 2,···,r G) .(59)
Figure 22: GRPO architecture. Advantages are normalized relative to the group mean and
standard deviation. The KL penalty is applied directly in the loss rather than shaping the
reward.
Intuitively, the GRPO update is comparing multiple answers to a single question within a
batch. The model learns to become more like the answers marked as correct and less like
the others. This is a very simple way to compute the advantage, which is the measure of
how much better a specific action is than the average at a given state. Relative to PPO,
REINFORCE, and broadly RLHF performed with a reward model rating (relative to output
reward), GRPO is often run with a far higher number of samples per prompt because the
advantage is entirely about the relative value of a completion to its peers from that prompt.
Here, the current policy generates multiple responses to a given prompt, and the group-wise
GRPO advantage estimate is given valuable context. PPO and vanilla policy-gradient
algorithms were designed to accurately estimate the reward of every completion (in fact,
more completions can do little to improve the value estimate in some cases). GRPO and its
variants are particularly well-suited to modern language model tools, where having multiple
completions to a given prompt is very natural (especially when compared to, e.g., multiple
actions from a set environment state in a robotic task).
The advantage computation for GRPO has trade-offs in its biases. The normalization
by standard deviation rewards questions in a batch that have a low variation in answer
correctness. For questions with either nearly all correct or all incorrect answers, the standard
rlhfbook.com 71

deviation will be lower and the advantage will be higher. Liu et al. 2025 \[119\] proposes
removing the standard deviation term given this bias, but this comes at the cost of down-
weighting questions that were all incorrect with a few correct answers, which could be seen
as valuable learning signal for the model. Those high-variance prompts can be exactly the
hardest cases, where only a few sampled completions find the correct answer and provide a
strong training signal.
eq. 59 is the implementation of GRPO when working with outcome supervision (either a
standard reward model or a single verifiable reward) and a different implementation is needed
with process supervision. In this case, GRPO computes the advantage as the sum of the
normalized rewards for the following reasoning steps.
Finally, GRPO’s advantage estimation can also be applied without the PPO clipping to
more vanilla versions of policy gradient (e.g. REINFORCE), but it is not the canonical form.
As an example of how these algorithms are intertwined, we can show that the advantage
estimation in a variant of GRPO, Dr. GRPO (GRPO Done Right) \[119\], is equivalent to the
RLOO estimation (which uses the average reward of other samples as its baseline) up to a
constant scaling factor (which normally does not matter due to implementation details to
normalize the advantage). Dr. GRPO removes the standard deviation normalization term
from eq. 59 – note that this also scales the advantageup, which is equivalent to increasing
the GRPO learning rate on samples with a variance in answer scores. This addresses a bias
towards questions with low reward variance – i.e. almost all the answers are right or wrong –
but comes at a potential cost if it is important to learn from problems where just one sample
gets the answer right. The Dr. GRPO advantage for completioni within a group of sizeG is
defined as:
˜Ai =r i−mean(r 1,r 2,···,r G) =r i− 1
G
G∑
j=1
rj (60)
Here, in the same notation, we can recall the RLOO advantage estimation as:
ARLOO
i =r i− 1
G−1
G∑
j=1,i̸=j
rj (61)
Thus, if we multiply the Dr. GRPO advantage definition by G
G−1 we can see a scaled
equivalence:
rlhfbook.com 72

G
G−1
˜Ai = G
G−1

ri− 1
G
G∑
j=1
rj


= G
G−1 ri− 1
G−1
G∑
j=1
rj
= G
G−1 ri− 1
G−1
G∑
j=1,j̸=i
rj− 1
G−1 ri
=r i
( G
G−1 − 1
G−1
)
− 1
G−1
G∑
j=1,j̸=i
rj
=r i− 1
G−1
G∑
j=1,j̸=i
rj
=A RLOO
i
(62)
6.2.9 Group Sequence Policy Optimization (GSPO)
When taking multiple gradient steps on a batch of data collected from a previous policy,
importance sampling is required to correct for the distribution mismatch between the data-
collection policy and the current policy being optimized. The standard importance sampling
identity allows us to estimate expectations under one distribution using samples from another:
Ep[f(x)] =E q
[
f(x)p(x)
q(x)
]
,(63)
where p is the target distribution,q is the sampling distribution, andp(x)
q(x) is the importance
weight. In policy gradient methods,p =πθ is the current policy we want to optimize and
q =πθold is the policy that generated the training data. This allows us to reweight samples
collected underπθold to estimate gradients forπθ, enabling multiple gradient steps per batch
of rollouts.
This distribution mismatch arises in two common scenarios: (1) taking multiple gradient
steps on a single batch, whereπθ drifts fromπθold after each update, and (2) in asynchronous
training systems where the inference backend (e.g., vLLM) and training backend (e.g., FSDP)
may have different model weights due to synchronization delays (see the Asynchronicity
section later in this chapter, which emerged particularly with the focus on RL for verifiable
rewards, but is also used in RLHF setups).
PPO and GRPO apply importance sampling at the token level and stabilize learning by
clipping thesurrogate objective. However, this approach has a subtle failure mode: when a
token’s importance ratio moves outside the clipping range[1−ε, 1 +ε], that token receives
zero gradient. For rare but important tokens—such as key reasoning steps that the model
initially assigns low probability—this “token dropping” can prevent the model from learning
to produce them more reliably.
rlhfbook.com 73

Group Sequence Policy Optimization (GSPO) \[123\] extends GRPO by computing importance
ratios at the sequence level rather than the token level. The practical motivation for this
algorithm – and its peer, CISPO, which modifies how importance sampling is computed
for policy gradient algorithms, as we will discuss later – is that the per-token importance
sampling ratio is often numerically unstable. The conceptual motivation is that when rewards
are assigned at the sequence level (as in most RLHF and RLVR setups), the importance
sampling correction should match that granularity.
Token-level ratios can behave erratically for long sequences and/or large, sparse models
(e.g. modern mixture-of-experts (MoE) models): a single token with a large ratio can
dominate the policy update, or many tokens may get clipped independently within a
response, fragmenting the learning signal across a single response. GSPO addresses this by
computing a single importance weight per response.
Recall that the probability of a full response factorizes autoregressively:
πθ(a|s) =
|a|∏
t=1
πθ(at|s,a <t).(64)
Note that for simplicity, we often shorten the conditional policy,πθ(at|s,a <t), asπθ(at|s ),
which implicitly contains the previous actions (tokens) in a completion. GSPO defines
a length-normalized sequence-level importance ratio using the geometric mean (to avoid
numerical issues with long sequences):
ρi(θ) =
( πθ(ai|s)
πθold(ai|s)
) 1
|ai|
= exp

 1
|ai|
|ai|∑
t=1
log πθ(ai,t|s,a i,<t)
πθold(ai,t|s,a i,<t)

.(65)
The GSPO objective mirrors GRPO but uses this sequence-level ratio:
JGSPO(θ) =E s∼D,{ai}G
i=1∼πθold(·|s)
[
1
G
G∑
i=1
min (ρi(θ)Ai,clip(ρ i(θ),1−ε,1 +ε)A i)
]
.(66)
Because the ratio is length-normalized, the clipping rangeε operates on a per-token average
scale, making the effective constraint comparable across responses of different lengths. In
implementation, the sequence-level weightρi is applied uniformly to all tokens in response
ai, which simplifies gradient computation while maintaining the sequence-level IS correction.
The advantage computation remains the same as GRPO (eq. 59), using the group-relative
mean and standard deviation normalization, which can be modified as done in other derivative
studies of GRPO. GSPO can be summarized as “GRPO with sequence-level importance
ratios”—the IS correction granularity is matched to the reward granularity.
6.2.10 Clipped Importance Sampling Policy Optimization (CISPO)
Clipped Importance Sampling Policy Optimization (CISPO) \[124\] takes a different approach:
rather than clipping the surrogate objective, CISPO clips the importance weights themselves
rlhfbook.com 74

while preserving gradients for all tokens. The objective uses a stop-gradient on the clipped
importance weight, returning to a REINFORCE-style formulation instead of the PPO-style,
two-sided clipping:
JCISPO(θ) =E s∼D,{ai}K
i=1∼πθold(·|s)

 1∑K
i=1|ai|
K∑
i=1
|ai|∑
t=1
sg(ˆρi,t(θ))Ai,t logπθ(ai,t|s,a i,<t)

,
(67)
where sg(·)denotes stop-gradient (the weight is used but not differentiated through), and
the clipped importance ratio is:
ˆρi,t(θ) =clip(ρ i,t(θ),1−ε low,1 +ε high), ρ i,t(θ) = πθ(ai,t|s,a i,<t)
πθold(ai,t|s,a i,<t).(68)
The key difference from PPO/GRPO is subtle but important: clipping the weight (not the
objective) means every token still receives a gradient signal proportional to its advantage—the
weight just bounds how much that signal is amplified or suppressed by the importance ratio.
This is a bias-variance tradeoff: clipping weights introduces bias but controls variance and,
critically, avoids dropping token gradients entirely.
Both CISPO and GSPO were developed by organizations pushing the limits of applying RL
on large-scale MoE models, which are known for their numerical issues. The papers highlight
how the per-token importance sampling ratios are unstable and can add substantial variance
to the gradients, mitigating learning. This can make these algorithms particularly impactful
on large-scale models, but less studied and beneficial within smaller, academic experiments.
CISPO also allows asymmetric clipping bounds (εlow̸= εhigh), similar to DAPO’s “clip-
higher” modification discussed later in this chapter, which can encourage exploration by
allowing larger updates for tokens the model wants to upweight. Related work includes
Tapered Off-Policy REINFORCE (TOPR) \[125\], which also clips IS weights directly (like
CISPO) rather than clipping within the objective (like PPO/GRPO), but operates at the
sequence level (like GSPO) and uses asymmetric clipping based on reward sign—applying no
IS correction for positive rewards while clipping ratios to[0, 1]for negative rewards—enabling
stable off-policy learning.
6.2.11 Comparing Algorithms
Each algorithm in this chapter shares the same core gradient shape (eq. 25), but differs in
how it estimates the advantage and controls the optimization:
• REINFORCE: The simplest policy gradient implementation, using Monte-Carlo
estimates of reward and a state-based baseline to reduce variance.
• RLOO: REINFORCE with multiple samples per prompt, with each sample’s baseline
being the average reward of the others (leave-one-out) to reduce gradient variance.
• PPO: Adds a learned value function and a clipped policy ratio to get more accurate
and stable gradient updates.
rlhfbook.com 75

• GRPO: A simplified variant of PPO that groups multiple completions per prompt
and normalizes rewards within the group to compute advantages, removing the need
for a value function.
• CISPO: A REINFORCE-style algorithm that clips importance-sampling weights (not
the objective as in PPO/GRPO) with a stop-gradient for stability, so every token
receives a gradient signal.
• GSPO: Like GRPO but normalizes the policy ratio by completion length, preventing
length bias.
• DPO: Not an RL algorithm, but a method to solve the same preference optimization
problem by bypassing the separate reward model entirely, optimizing directly from
preference pairs (see Chapter 8).
All of the policy gradient algorithms above are on-policy in derivation, though most are
applied slightly off-policy in practice. DPO and the other direct alignment algorithms in
Chapter 8 are off-policy by default. All can be paired with a learned reward model or
verifiable rewards. Only PPO requires a learned value function. REINFORCE and RLOO
have no importance-sampling ratio — the remaining algorithms each introduce one to enable
multiple gradient steps per batch of rollouts, differing in granularity and clipping strategy as
summarized below.
Table 3: Comparing policy gradient algorithms.
Method IS Granularity Clipping Style Advantage
REINFORCENone None Monte Carlo baseline
RLOONone None Leave-one-out
PPOToken Objective (bilateral) Learned value fn
GRPOToken Objective (bilateral) Group-relative
GSPOSequence Objective (bilateral) Group-relative
CISPOToken Weights (stop-grad) Group-relative
The core lossL(θ)for each method is:
rlhfbook.com 76

REINFORCE:− 1
T
T∑
t=1
logπθ(at|s t)
(
Gt−b(st)
)
RLOO:− 1
K
K∑
i=1
∑
t
logπθ(ai,t|s i,t)

Ri− 1
K−1
∑
j̸=i
Rj


CISPO:−
∑
i,t
sg(ˆρi,t)Ai,t logπθ(ai,t|s i,t)
ˆρi,t = clip(ρi,t,1−ε,1 +ε)
PPO:− 1
T
T∑
t=1
min
(
ρtAt,clip(ρ t,1−ε,1 +ε)A t
)
ρt = πθ(at|s t)
πθold(at|s t)
GRPO:− 1
G
G∑
i=1
min
(
ρiAi,clip(ρ i,1−ε,1 +ε)A i
)
ρi = πθ(ai|s)
πθold(ai|s) , A i = ri−mean(r 1:G)
std(r1:G)
GSPO:− 1
G
G∑
i=1
min
(
ρiAi,clip(ρ i,1−ε,1 +ε)A i
)
ρi =
( πθ(ai|s)
πθold(ai|s)
)1/|ai|
DPO:−E (x,yw,yl)
[
logσ
(
β[∆ logπθ(x)−∆ logπ ref(x)]
)]
6.3 Implementation
Compared to the original Deep RL literature where many of these algorithms were developed,
implementing RL for optimizing language models or other large AI models requires many
small implementation details. In this section, we highlight some key factors that differentiate
the implementations of popular algorithms.
There are many other small details that go into this training. For example, when doing
RLHF with language models a crucial step is generating text that will then be rated by the
reward model. Under normal circumstances, the model should generate an end-of-sequence
(EOS) token indicating it finished generating, but a common practice is to put a hard
cap on generation length to efficiently utilize infrastructure. A failure mode of RLHF is
that the model is regularly truncated in its answers, driving the ratings from the reward
model out-of-distribution and to unpredictable scores. The solution to this is toonlyrun
reward model scoring on theeos_token, and to otherwise assign a penalty to the model for
generating too long.
rlhfbook.com 77

The popular open-source tools for RLHF have a large variance in implementation details
across the algorithms (see table 10 in \[126\]). Some decisions not covered here include:
• Value network initialization: The internal learned value network used by PPO and
other similar algorithms can be started from a different model of the same architecture
or randomly selected weights. This can have a large impact on performance. The
standard established in InstructGPT \[3\] (and re-used in Tülu 3 for its work on RLVR
\[6\]) is to initialize the value network from the reward model used during RLHF. Others
have used the previous checkpoint to RLHF training (normally an SFT model) with a
value head appended randomly initialized, or fully re-initialized language models (less
common as it will take longer for RLHF to converge, but possible).
• Reward normalization, reward whitening, and/or advantage whitening:
Normalization bounds all the values from the RM (or environment) to be between 0
and 1, which can help with learning stability. Whitening goes further by transforming
rewards or advantage estimates to have zero mean and unit variance, providing an
even stronger boost to stability.
• Different KL estimators: With complex language models, precisely computing the
KL divergence between models can be complex, so multiple approximations are used
to substitute for an exact calculation \[127\].
• KL controllers: Original implementations of PPO and related algorithms had dy-
namic controllers that targeted specific KLs and changed the penalty based on recent
measurements. Most modern RLHF implementations use static KL penalties, but this
can also vary.
For more details on implementation details for RLHF, see \[128\]. For further information on
the algorithms, see \[129\].
6.3.1 Policy-Gradient Basics
A simple implementation of policy gradient, using advantages to estimate the gradient to
prepare for advanced algorithms such as PPO and GRPO follows:
pg_loss = -advantages * ratio
Ratio here is the (per-token) probability ratio (often computed from a log-probability
difference) of the new policy model probabilities relative to the old policy that generated the
batch.
In order to understand this equation, it is good to understand different cases that can fall
within a batch of updates. Remember that we want the loss todecreaseas the model gets
better at the task.
Case 1: Positive advantage, so the action was better than the expected value of the state. We
want to reinforce this. In this case, the model will make this more likely with the negative
sign. To do so, it’ll increase the logratio. A positive logratio, or sum of log probabilities of
the tokens, means that the model is more likely to generate those tokens.
Case 2: Negative advantage, so the action was worse than the expected value of the state.
This follows very similarly. Here, the loss will be positive if the new model was more likely,
so the model will try to make it so the policy parameters make this completion less likely.
rlhfbook.com 78

Case 3: Zero advantage, so no update is needed. The loss is zero, don’t change the policy
model.
6.3.2 Loss Aggregation Tradeoffs
The question when implementing any policy gradient algorithm with language models is:
How do you aggregate per-token losses into a final scalar loss? Given per-token lossesℓi,t
for samplei at tokent, with completion lengths|ai| and batch sizeB, there are three main
strategies:
Strategy 1: Per-sequence normalization(standard GRPO; also used in some PPO
implementations)
L= 1
B
B∑
i=1
1
|ai|
|ai|∑
t=1
ℓi,t (69)
Each sequence contributes equally to the batch loss, regardless of length. In code:
# Strategy 1: Per-sequence normalization
sequence_loss = ((per_token_loss * completion_mask).sum(dim=1) / \
completion_mask.sum(dim=1)).mean()
Strategy 2: Per-token normalization(DAPO \[130\])
L=
∑B
i=1
∑|ai|
t=1ℓi,t
∑B
i=1|ai|
(70)
Each token contributes equally; longer sequences have proportionally more influence on the
gradient. In code:
# Strategy 2: Per-token normalization
token_loss = ((per_token_loss * completion_mask).sum() / \
completion_mask.sum())
Strategy 3: Fixed-length normalization(Dr. GRPO \[119\])
L= 1
B
B∑
i=1
1
Lmax
|ai|∑
t=1
ℓi,t (71)
Normalizes by max sequence lengthLmax, equalizing the per-token scale across sequences
while still letting longer sequences contribute more total gradient because they contain more
active tokens. In code:
# Strategy 3: Fixed-length normalization
fixed_len_loss = ((per_token_loss * completion_mask).sum(dim=1) / \
L_max).mean()
rlhfbook.com 79

WhereLmax is typically a global constant during the entire training procedure, which specifies
the maximum number of generation tokens.
Note that completion_mask in the code above is a matrix of 1s and 0s, where the prompt
tokens are masked out (0s) because we don’t want the model to learn from predicting prompt
tokens.
6.3.2.1 Why Does This Matter?Intuitively, per-sequence normalization (Strategy 1)
seems best since we care aboutoutcomes, not individual tokens. However, this introduces
subtle biases based on sequence length, which can cause the model to overthink or down-
weight strategies that naturally need to use more tokens, depending on the direction of the
bias. Consider two sequences of different lengths with per-token losses:
seq_1_losses = [1, 1, 1, 1, 10]# 5 tokens, mean = 2.8
seq_2_losses = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]# 10 tokens, mean = 1.9
WithStrategy 1(per-sequence): The batch loss is(2 .8 + 1.9)/2 = 2.35, and crucially, each
token in the short sequence receives a larger gradient than tokens in the long sequence.
WithStrategy 2(per-token): The batch loss is(14 + 19)/15 = 2.2, and all tokens receive
equal gradient magnitude.
WithStrategy 3(fixed-length with Lmax = 10): The short sequence contributes1.4and
the long sequence contributes1.9, balancing per-token gradients while still weighting by
sequence.
For a more complete example showing how these strategies affect gradients, see the script
below.
fromtypingimportOptional
importtorch
defmasked_mean(values: torch.Tensor, mask: torch.Tensor, axis: Optional[int] = None)
-> torch.Tensor:
"""Compute mean of tensor with masked values."""
ifaxisis notNone:
return(values * mask).sum(axis=axis) / mask.sum(axis=axis)
else:
return(values * mask).sum() / mask.sum()
defmasked_sum(
values: torch.Tensor,
mask: torch.Tensor,
axis: Optional[int] = None,
constant_normalizer: float = 1.0,
) -> torch.Tensor:
"""Compute sum of tensor with masked values. Use a constant to normalize."""
ifaxisis notNone:
return(values * mask).sum(axis=axis) / constant_normalizer
else:
return(values * mask).sum() / constant_normalizer
ratio = torch.tensor([
[1., 1, 1, 1, 1, 1, 1,],
[1, 1, 1, 1, 1, 1, 1,],
rlhfbook.com 80

], requires_grad=True)
advs = torch.tensor([
[2, 2, 2, 2, 2, 2, 2,],
[2, 2, 2, 2, 2, 2, 2,],
])
masks = torch.tensor([
# generation 1: 4 tokens
[1, 1, 1, 1, 0, 0, 0,],
# generation 2: 7 tokens
[1, 1, 1, 1, 1, 1, 1,],
])
max_gen_len = 7
masked_mean_result = masked_mean(ratio * advs, masks, axis=1)
masked_mean_token_level = masked_mean(ratio, masks, axis=None)
masked_sum_result = masked_sum(ratio * advs, masks, axis=1,
constant_normalizer=max_gen_len)
print("masked_mean", masked_mean_result)
print("masked_sum", masked_sum_result)
print("masked_mean_token_level", masked_mean_token_level)
# masked_mean tensor([2., 2.], grad_fn=<DivBackward0>)
# masked_sum tensor([1.1429, 2.0000], grad_fn=<DivBackward0>)
# masked_mean_token_level tensor(1., grad_fn=<DivBackward0>)
masked_mean_result.mean().backward()
print("ratio.grad", ratio.grad)
ratio.grad.zero_()
# ratio.grad tensor([[0.2500, 0.2500, 0.2500, 0.2500, 0.0000, 0.0000, 0.0000],
# [0.1429, 0.1429, 0.1429, 0.1429, 0.1429, 0.1429, 0.1429]])
masked_sum_result.mean().backward()
print("ratio.grad", ratio.grad)
ratio.grad.zero_()
# ratio.grad tensor([[0.1429, 0.1429, 0.1429, 0.1429, 0.0000, 0.0000, 0.0000],
# [0.1429, 0.1429, 0.1429, 0.1429, 0.1429, 0.1429, 0.1429]])
masked_mean_token_level.mean().backward()
print("ratio.grad", ratio.grad)
# ratio.grad tensor([[0.0909, 0.0909, 0.0909, 0.0909, 0.0000, 0.0000, 0.0000],
# [0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909]])
The output shows that with Strategy 1 (masked_mean), the short sequence has larger
per-token gradients (0.25) than the long sequence (0.14). Strategies 2 and 3 equalize the per-
token gradients across sequences. Note that these results can vary substantially if gradient
accumulation is used, where the gradients are summed across multiple minibatches before
taking a backward step—in this case, the balance between shorter and longer sequences can
flip.
In practice, the best strategy depends on the specific training setup. Often in RLHF the
method with the best numerical stability or the least variance in loss is preferred.
rlhfbook.com 81

6.3.2.2 Related: MDP vs. Bandit FramingThe choice of loss aggregation connects
to a deeper distinction in how we frame the RL problem. TheMDP (token-level)view
treats each tokenat as an action with statest being the running prefix. In practice, this is
the framing used when we compute token-level advantages with a learned value function
V (st)(e.g., GAE \[113\]) and apply KL penalties per token. PPO with a learned value network
is the canonical example \[117\].
In contrast, thebandit (sequence-level)view treats the whole completion as a single
action with one scalar rewardR. In code, this means computing a sequence-level advantage
Aseq and broadcasting it to all tokens. RLOO and GRPO-style advantages are often used in
this bandit-style setting \[116\] \[112\] \[122\]. Direct alignment methods like DPO and A-LoL
also define sequence-level objectives, although they are not policy-gradient estimators \[131\].
Note that many GRPO implementations use a bandit-style advantageandadd a separate
per-token KL term in the loss, while many PPO/RLOO implementations fold KL into the
reward before computing advantages; both conventions exist in practice.
An example comparison highlighting the two approaches is below:
# === Bandit-style (sequence-level) ===
# One scalar reward per sequence; advantage broadcast to all tokens
reward = torch.tensor([3.0, 1.0])# (B,) e.g., reward model scores
baseline = reward.mean()# simple baseline (RLOO uses leave-one-out)
advantage_seq = reward - baseline# (B,)
advantages = advantage_seq[:, None].expand(-1, seq_len)# (B, L)
# tensor([[ 1., 1., 1., 1.], <- same advantage for all tokens
# [-1., -1., -1., -1.]])
# === MDP-style (token-level) ===
# Per-token rewards + learned V(s_t); each token gets its own advantage
# (could also use per-token KL shaping, format rewards, or other token-level signals)
advantages = gae(per_token_rewards, values, done_mask, gamma=1.0, lam=0.95)
# tensor([[ 0.2, 0.5, 0.8, 1.5], <- varies by position
# [-0.3, -0.5, -0.8, -1.4]])
This framing distinction also explains why the discount factorγ is set to 1.0 in virtually all
RLHF implementations. In standard RL, discounting (γ <1) is essential: it balances the
optimization between short-term and long-term reward across a multi-step episode, which is
crucial for the agent to learn effective behavior over time. But in the RLHF setting, even
when using the token-level MDP view, the inductive bias of the optimization is the quality
of the collective completion – the reward signal scores the entire response, not individual
tokens. Discounting earlier tokens would arbitrarily down-weight their contribution with no
principled justification. As agentic RL settings mature – where models take real multi-step
actions such as tool calls, code execution, and web browsing – discounting may become
relevant again, since these involve genuinely distinct sequential decisions whose long-term
consequences differ.
6.3.3 Asynchronous RL Systems
The default implementation for policy-gradient algorithms is what is calledon-policy
execution, where the actions (generations) taken by the agent (language model) are scored
before updating the model. The theoretical derivations of policy-gradient rely on all actions
being exactly on-policy where the model is always up to date with the results from the
rlhfbook.com 82

latest trials/roll-outs. In practice, maintaining exact on-policy execution substantially slows
training \[132\]—and perfect synchronization is technically impossible regardless. Therefore,
all of the recent empirical results with language models tend to be slightly outside of the
theoretical proofs. What happens in practice is designing the algorithms and systems for
what actually works.
Figure 23: A comparison of the generation-update phases for synchronous or asynchronous
RL training following Noukhovitch et al. 2024.
The common solution used is to constantly run inference and training on separate GPU
nodes with software designed to efficiently run both, as shown in the bottom of fig. 23.
Common practice in popular open-source RL tools for language models is to use a distributed
process management library such as Ray to hand information off between the policy-gradient
learning loop and the inference loop using an efficient inference engine, e.g., vLLM. In
these setups, the GPUs dedicated to taking the RL steps are called the “learners” and the
GPUs dedicated to sampling from the language model are called the “actors”. The primary
challenges faced when making training more asynchronous are keeping training stable and
maintaining learning signal.
These systems are designed and implemented with the presumption that nearly on-policy
data is good enough for stable learning. Here, the generation and update phases can easily
be synced to avoid idle compute on either piece of the training system, which would be
passing model weights from the learners to the actors in fig. 24. With reasoning models,
the extremely long inference characteristics of problems requiring 10K to 100K+ tokens
per answer makes the generation of roll-outs a far stronger bottleneck. A common problem
when training reasoning models on more synchronous RL infrastructure is that an answer to
one prompt in the batch can take substantially more time to generate (either through more
rlhfbook.com 83

Figure 24: An example distributed RL system, where two queues are managed to pass data
to the learner and actor GPUs, which can both be synchronized with a distributed computing
library such as Ray. Olmo Team 2025, license CC-BY.
tokens or more tool calls), resulting in the majority of the allocated compute being idle until
it completes. A second solution to this length mismatch issue, called sequence-level packing,
is to stack shorter samples within a batch with clever masking to enable continued roll-outs
from the model and better distribute length normalization across samples within a batch.
The full complexity of distributed RL infrastructure is out of scope for this book, as it can
cause many other subtle issues that slow down training or cause instability.
Following the emergence of these reasoning models, further interest has been taken to make
the training and inference loops fully off-policy, where training batches for the policy gradient
updates are filled with the most recently completed roll-outs across multiple instances
generating answers \[133\] \[134\]. Fully asynchronous training would also enable scaling RL
training runs across multiple datacenters more easily due to the option of increasing the
time between weight syncs between the learner node (taking policy gradient steps) and the
actor (trying to solve problems) \[135\].
Related methods are exploring fully off-policy policy gradient algorithms \[125\].
6.3.4 Truncated Importance Sampling
Truncated importance sampling (TIS) is a crucial tool used to stabilize training in modern,
asynchronous RL frameworks with language models. Importance sampling is a correction
that reweights samples drawn from one distribution to estimate expectations under another
(as introduced in eq. 63). Truncated importance sampling \[136\] caps these weights with
min(ρ,C )for some constant C, trading a small bias for bounded variance in the policy
gradient.
rlhfbook.com 84

This is an importance-sampling correction applied to the policy gradient, but unlike the
bilateral clipping in PPO and CISPO (which constrains the ratio near 1), TIS uses a
one-sided upper cap: the ratio can fall freely below 1, but is capped atC to prevent
extreme upweighting. In all of PPO, GRPO, CISPO (and related algorithms), the ratio
ρpolicy
t = πθ(at |s )/πθold(at |s )corrects for policy drift across multiple gradient steps
within one RL batch. As we shift to real-world RL frameworks, centered around the idea
of asynchronicity in the previous subsection, there can be even larger sources of numerical
differences (that also require the numerical correction of importance sampling). Even when
the sampler and learner share identical parametersθ, their effective token distributions
can differ because the inference engine (e.g., vLLM) and training framework (e.g., FSDP)
use different kernels, precision, and parallelism strategies \[137\]. It is therefore useful to
distinguish the same policy evaluated on two systems,πsampler
θ and πlearner
θ , and define the
corresponding ratio and its truncated form:
ρlearner
t = πlearner
θ (at|s,a <t)
πsampler
θ (at|s,a <t)
,˜ρ learner
t = min(ρlearner
t , C).(72)
These two corrections are complementary, but they appear in policy-gradient implementations
for different reasons — one compensates for policy drift within the training of an RL batch,
the other for implementation-induced divergence — and can be applied simultaneously. How
they combine depends on the algorithm:
6.3.4.1 REINFORCE with TIS (Single Gradient Step)There is no policy drift
(πθ =πθold), so the only mismatch is between the learner and sampler. Hereπθold =πgen,
and TIS directly corrects the learner–sampler gap:
∇θJ≈E a∼πsampler
θ
[
˜ρlearner
t ·At·∇θ logπ learner
θ (at|s,a <t)
]
.(73)
6.3.4.2 PPO/GRPO with TIS (Multiple Gradient Steps)Now both ratios are
active. In careful implementations, the “old logprobs” in the policy ratio are recomputed
on the learner (the GSPO paper discusses this), so the policy ratioρpolicy
t =πlearner
θ /πlearner
θold
captures pure policy drift, while˜ρlearner
t = min(πlearner
θold /πsampler
θold
, C)separately corrects the
backend mismatch at the generation checkpoint:
JPPO+TIS(θ) =E
[
min
(
ρpolicy
t At,clip
(
ρpolicy
t ,1−ε,1 +ε
)
At
)
·˜ρlearner
t
]
.(74)
Here πθold̸=πgen: the old logprobs come from the learner, not the sampler. If a framework
skips this recomputation and uses the sampler logprobs directly asπθold, the policy ratio
already captures the backend mismatch and no separate TIS correction is needed — but the
clip then operates on a noisier ratio that starts away from 1.0 even before any gradient steps.
This is the “your framework secretly brings you off-policy RL” observation from Yao et al.
\[137\].
In practice, LLM RL systems apply TIS as a per-token correction weight on the policy-
gradient loss:
rlhfbook.com 85

# Shape: (B*G, L)
C = 2.0# TIS cap
logratio = learner_logprobs - sampler_logprobs
logratio = logratio.clamp(-10.0, 10.0)# numerical safety
tis_weight = torch.exp(logratio).clamp(max=C)# one-sided truncation
# Use as a fixed correction weight on the per-token PG loss
per_token_pg_loss = per_token_pg_loss * tis_weight.detach()
The[−10, 10]clamp is only for numerical stability before exponentiation; the actual truncated-
importance-sampling step is the one-sided cap atC. In practice, the bookkeeping around
these logprobs — storing sampler logprobs from generation, recomputing learner logprobs at
the old checkpoint, and tracking current logprobs during gradient steps — is a substantial
part of the scaffolding in distributed RL frameworks. Unlike GSPO, this correction is token-
level because it addresses token-level numerical mismatch rather than sequence-level reward
granularity. TIS for the learner–sampler ratio has been adopted across major open-source
RL frameworks (VeRL, TRL, OpenRLHF, SkyRL, OAT, and Open Instruct, which uses
C = 2), and becomes increasingly important for long reasoning traces (Chapter 7), where
small per-token differences compound over thousands of generated tokens.
6.3.5 Example: PPO
There are many, many implementations of PPO available. The corelosscomputation is
shown below. Crucial to stable performance is also thevaluecomputation, where multiple
options exist (including multiple options for thevalue modelloss).
Note that the reference policy (or old logprobs) here are from the time the generations were
sampled and not necessarily the reference policy. The reference policy is only used for the
KL distance constraint/penalty.
# B: Batch Size, L: Sequence Length, G: Num of Generations
# Apply KL penalty to rewards
rewards = rewards - self.beta * per_token_kl# Shape: (B*G, L)
# Get value predictions
values = value_net(completions)# Shape: (B*G, L)
# Compute returns via backward pass (gamma typically 1.0 for LM RLHF)
# Mask rewards to avoid padding tokens (which may have KL penalties) leaking into
returns
returns = torch.zeros_like(rewards)
running = torch.zeros(rewards.shape\[0\], device=rewards.device, dtype=rewards.dtype)
fortinreversed(range(rewards.shape\[1\])):
# Zero out padding: only accumulate rewards/returns for valid completion tokens
running = (rewards[:, t] + self.gamma * running) * completion_mask[:, t]
returns[:, t] = running
# Compute advantages: A_t = G_t - V(s_t)
advantages = returns - values.detach()# Shape: (B*G, L)
# Note: We detach the value network here to not update the parameters of
# the value function when computing the policy-gradient loss
# Normalize advantages (optional but stable)
advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
rlhfbook.com 86

# Compute probability ratio between new and old policies
ratio = torch.exp(new_per_token_logps - per_token_logps)# Shape: (B*G, L)
# PPO clipping objective
eps = self.cliprange# e.g. 0.2
pg_losses1 = -advantages * ratio# Shape: (B*G, L)
pg_losses2 = -advantages * torch.clamp(ratio, 1.0 - eps, 1.0 + eps)# Shape: (B*G, L)
pg_loss_max = torch.max(pg_losses1, pg_losses2)# Shape: (B*G, L)
# Value function loss: predict returns
vf_loss = 0.5 * ((returns - values) ** 2)# Shape: (B*G, L)
# Combine policy and value losses
per_token_loss = pg_loss_max + self.vf_coef * vf_loss# Shape: (B*G, L)
# Apply completion mask and compute final loss
loss = ((per_token_loss * completion_mask).sum(dim=1) /
completion_mask.sum(dim=1)).mean()
# Scalar
# Compute metrics for logging
withtorch.no_grad():
# Compute clipping fraction
clip_frac = ((pg_losses2 > pg_losses1).float() * completion_mask).sum() /
completion_mask.sum()
# Compute approximate KL
approx_kl = (0.5 * ((new_per_token_logps - per_token_logps)**2) *
completion_mask).sum() / completion_mask.sum()
# Compute value loss for logging
value_loss = vf_loss.mean()
The core piece to understand with PPO is how the policy gradient loss is updated. Focus on
these three lines:
pg_losses1 = -advantages * ratio# Shape: (B*G, L)
pg_losses2 = -advantages * torch.clamp(ratio, 1.0 - eps, 1.0 + eps)# Shape: (B*G, L)
pg_loss_max = torch.max(pg_losses1, pg_losses2)# Shape: (B*G, L)
pg_losses1 is the vanilla advantage-weighted policy gradient loss.pg_losses2 applies the
same formula but with the probability ratio clamped to the range[1−ε, 1 +ε], limiting how
much the policy can change in a single update.
The key insight is takingtorch.max of the two losses. Because we’re minimizing anegative
loss (recall the negative sign in front of advantages), taking the maximum selects the
more pessimistic gradient—the one that produces a smaller policy update. When the
advantage is positive (good action), clipping prevents the policy from increasing that action’s
probability too aggressively. When the advantage is negative (bad action), clipping prevents
over-correction in the other direction.
By clamping the log-probability ratio, PPO bounds how far the policy can drift from the
version that generated the training data, stabilizing learning without requiring an explicit
trust region computation.
The code above also shows PPO learning a value function alongside the policy, which adds
rlhfbook.com 87

implementation complexity, but the clipped objective is the core mechanism.
6.3.5.1 PPO/GRPO Simplification with One Gradient Step per Sample (No
Clipping)PPO (and GRPO) implementations can be handled much more elegantly if the
hyperparameter “number of gradient steps per sample” is equal to 1. Many typical values for
this are from 2-4 or higher. In the main PPO or GRPO equations, see eq. 52, the “reference”
policy is the previous parameters – those used to generate the completions or actions. Thus,
if only one gradient step is taken,πθ =πθold, and the update rule reduces to the following
(the notation[]∇ indicates a stop gradient):
J(θ) = 1
G
G∑
i=1
( πθ(ai|s)
[πθ(ai|s)]∇
Ai−βD KL(πθ||πref)
)
.(75)
This leads to PPO or GRPO implementations where the second policy gradient and clipping
logic can be omitted, making the optimizer far closer to standard policy gradient.
6.3.6 Example: GRPO
The DeepSeekMath paper describes some implementation details of GRPO that differ from
PPO \[122\], especially if comparing to a standard application of PPO from Deep RL rather
than language models. For example, the KL penalty within the RLHF optimization (recall
the KL penalty is also used when training reasoning models on verifiable rewards without
a reward model) is applied directly in the loss update rather than to the reward function.
Where the standard KL penalty application for RLHF is applied asr = rθ−βD KL, the
GRPO implementation is along the lines of:
L=L policy gradient +β∗D KL (76)
However, there are multiple ways to implement this. Traditionally, the KL distance is
computed with respect to each token in the completion to a prompts. For reasoning training,
multiple completions are sampled from one prompt, and there are multiple prompts in one
batch, so the KL distance will have a shape of [B, L, N], where B is the batch size, L is the
sequence length, and N is the number of completions per prompt.
Putting it together, using the first loss accumulation, the pseudocode can be written as
below.
# B: Batch Size, L: Sequence Length, G: Number of Generations
# Compute group-wise rewards # Shape: (B,)
mean_grouped_rewards = rewards.view(-1, self.num_generations).mean(dim=1)
std_grouped_rewards = rewards.view(-1, self.num_generations).std(dim=1)
# Normalize the rewards to compute the advantages
mean_grouped_rewards = mean_grouped_rewards.repeat_interleave(self.num_generations,
dim=0)
std_grouped_rewards = std_grouped_rewards.repeat_interleave(self.num_generations, dim=0)
# Shape: (B*G,)
# Compute advantages
rlhfbook.com 88

advantages = (rewards - mean_grouped_rewards) / (std_grouped_rewards + 1e-4)
advantages = advantages.unsqueeze(1)
# Shape: (B*G, 1)
# Compute probability ratio between new and old policies
ratio = torch.exp(new_per_token_logps - per_token_logps)# Shape: (B*G, L)
# PPO clipping objective
eps = self.cliprange# e.g. 0.2
pg_losses1 = -advantages * ratio# Shape: (B*G, L)
pg_losses2 = -advantages * torch.clamp(ratio, 1.0 - eps, 1.0 + eps)# Shape: (B*G, L)
pg_loss_max = torch.max(pg_losses1, pg_losses2)# Shape: (B*G, L)
# important to GRPO -- PPO applies this in reward traditionally
# Combine with KL penalty
per_token_loss = pg_loss_max + self.beta * per_token_kl# Shape: (B*G, L)
# Apply completion mask and compute final loss
loss = ((per_token_loss * completion_mask).sum(dim=1) /
completion_mask.sum(dim=1)).mean()
# Scalar
# Compute core metric for logging (KL, reward, etc. also logged)
withtorch.no_grad():
# Compute clipping fraction
clip_frac = ((pg_losses2 > pg_losses1).float() * completion_mask).sum() /
completion_mask.sum()
# Compute approximate KL
approx_kl = (0.5 * ((new_per_token_logps - per_token_logps)**2) *
completion_mask).sum() / completion_mask.sum()
For more details on how to interpret this code, see the PPO section above. The core
differences from the PPO example are:
• Advantage computation: GRPO normalizes rewards relative to the group (mean
and std across generations for the same prompt) rather than using a learned value
function as baseline.
• No value network: GRPO removes the value model entirely, eliminatingvf_loss
and the associated complexity.
• KL penalty placement: GRPO adds the KL penalty directly to the loss rather than
subtracting it from the reward (this is the standard implementation, but more versions
exist on how the KL is applied).
6.3.6.1 RLOO vs. GRPOThe advantage updates for RLOO follow GRPO very closely,
highlighting the conceptual similarity of the algorithm when taken separately from the PPO
style clipping and KL penalty details. Specifically, for RLOO, the advantage is computed
relative to a baseline that is extremely similar to that of GRPO – the completion reward
relative to the others for that same question. Concisely, the RLOO advantage estimate
follows as (expanded from TRL’s implementation):
# rloo_k --> number of completions per prompt
# rlhf_reward --> Initially a flat tensor of total rewards for all completions. Length B
= N x k
rlhf_reward = rlhf_reward.reshape(rloo_k, -1)#
rlhfbook.com 89

# Now, Shape: (k, N), each column j contains the k rewards for prompt j.
baseline = (rlhf_reward.sum(0) - rlhf_reward) / (rloo_k - 1)
# baseline --> Leave-one-out baseline rewards. Shape: (k, N)
# baseline[i, j] is the avg reward of samples i'!= i for prompt j.
advantages = rlhf_reward - baseline
# advantages --> Same Shape: (k, N)
advantages = advantages.flatten()# Same shape as original tensor
The rest of the implementation details for RLOO follow the other trade-offs of implementing
policy-gradient.
6.4 Auxiliary Topics
In order to master the application of policy-gradient algorithms, there are countless other
considerations. Here we consider some of the long-tail of complexities in successfully deploying
a policy-gradient RL algorithm.
6.4.1 Generalized Advantage Estimation (GAE)
Generalized Advantage Estimation (GAE) is an alternate method to compute the advantage
for policy gradient algorithms \[113\] that better balances the bias-variance tradeoff. Traditional
single-step advantage estimates can introduce too much bias, while using complete trajectories
can suffer from high variance. GAE computes an exponentially-weighted average of multi-step
advantage estimates, where theλhyperparameter controls the bias-variance tradeoff—ranging
from single-step TD (λ = 0) to full trajectory returns (λ = 1); λ = 0.95is a common default
for LLM fine-tuning.
Advantage estimates can take many forms, but we can define ann-step advantage estimator
(similar to the TD residual at the beginning of the chapter) as follows:
ˆA(n)
t =



rt +γV(s t+1)−V(s t), n= 1
rt +γr t+1 +γ 2V(st+2)−V(s t), n= 2
...
rt +γr t+1 +γ 2rt+2 +···−V(s t), n=∞
(77)
Here a shortern will have lower variance but higher bias as we are attributing more learning
power to each trajectory – it can overfit. GAE attempts to generalize this formulation into a
weighted multi-step average instead of a specificn. To start, we must define the temporal
difference (TD) residual of predicted value.
δV
t =r t +γV(s t+1)−V(s t)(78)
To utilize this, we introduce another variableλ as the GAE mixing parameter. This folds
into an exponential decay of future advantages we wish to estimate:
rlhfbook.com 90

ˆAGAE(γ,λ)
t = (1−λ)( ˆA(1)
t +λ ˆA(2)
t +λ 2 ˆA(3)
t +···)
= (1−λ)(δ V
t +λ(δV
t +γδ V
t+1) +λ 2(δV
t +γδ V
t+1 +γ 2δV
t+2) +···)
= (1−λ)(δ V
t (1 +λ+λ 2 +···) +γδ V
t+1(λ+λ 2 +···) +···)
= (1−λ)
(
δV
t
1
1−λ +γδ V
t+1
λ
1−λ +···
)
=∑∞
l=0(γλ)lδV
t+l
(79)
Intuitively, this can be used to average multi-step estimates of Advantage in an elegant
fashion. An example implementation is shown below:
# GAE (token-level) for LM RLHF
#
# B: Batch Size
# L: Length
# Inputs:
# rewards: (B, L) post-KL per-token rewards
# values: (B, L) current V_theta(s_t)
# done_mask: (B, L) 1.0 at terminal token (EOS or penalized trunc), else 0.0
# gamma: float (often 1.0),
# lam (short for lambda): float in [0,1]
# (Padding beyond terminal should have rewards=0, values=0)
B, L = rewards.shape
advantages = torch.zeros_like(rewards)
next_v = torch.zeros(B, device=rewards.device, dtype=rewards.dtype)
gae = torch.zeros(B, device=rewards.device, dtype=rewards.dtype)
fortinreversed(range(L)):
not_done = 1.0 - done_mask[:, t]
delta = rewards[:, t] + gamma * not_done * next_v - values[:, t]
gae = delta + gamma * lam * not_done * gae
advantages[:, t] = gae
next_v = values[:, t]
targets = advantages + values# y_t for value regression
advantages = advantages.detach()# for policy loss
The backward loop accumulates temporal-difference (TD) errors (δt = rt +γV (st+1)−
V (st)), which measure how much better or worse the actual outcome was compared to the
value function’s prediction, with exponential decay(γλ)l. At terminal tokens,not_done=0
prevents bootstrapping from future states and resets the GAE accumulator, so each episode’s
advantages are computed independently (since the loop runs backward, the terminal token
cleanly stops the exponentially-weighted accumulation at episode boundaries—this makes
the implementation packing-friendly, correctly handling multiple sequences concatenated into
one). The final targets serve as regression targets for the separate value function learned
outside this GAE loop, while the detachedadvantages weight the policy gradient—detached
so that policy updates don’t backpropagate through the value network. In RLHF for language
models, γ = 1.0is common because episodes are short token sequences where undiscounted
credit assignment is preferred (and often all of the tokens in one).
For further reading, see \[138\].
rlhfbook.com 91

6.4.2 Double Regularization
We’ve seen in this chapter two types of regularization. One is built into algorithms like PPO
with step-size constraints, and the other is a KL divergence based distance penalty relative
to the start of the optimization.
Many popular policy gradient algorithms from Deep Reinforcement Learning, including PPO
and its predecessors, originated due to the need to control the learning process of the agent.
In RLHF, as discussed extensively in Chapter 15 on Regularization and in Chapter 3 on
Training Overview, there is a built-in regularization term via the distance penalty relative to
the original policy one is fine-tuning. In this view, a large part of the difference between
algorithms like PPO (which have internal step-size regularization) and REINFORCE (which
is simpler, and to which PPO reduces under certain hyperparameters) is far less meaningful
for fine-tuning language models than training agents from scratch.
In PPO, the objective that handles capping the step-size of the update is known as the
surrogate objective. To monitor how much the PPO regularization is impacting updates in
RLHF, one can look at the clip fraction variable in many popular implementations, which
is the percentage of samples in the batch whose probability ratio falls outside the clipping
interval. This is a useful proxy for how often PPO’s regularizer may be active, but not every
such sample has zero gradient: the surrogate becomes flat only when the clipped branch is
selected, such as positive-advantage samples with ratios above1 +ε or negative-advantage
samples with ratios below1−ε.
In practice with language models, algorithms like PPO and GRPO are often run with only
one gradient step per batch, which means that the PPO-native regularization is never applied
(as clipping can only occur within a batch when the policy changes substantially) and the
KL distance penalties predominate. However, this is not universal. For example, DAPO uses
16 gradient steps per batch \[130\], and Tülu 3 uses 4 PPO update iterations per batch for 8B
and 70B models but reduces to 1 for 405B to maintain training stability \[6\].
6.4.3 Further Reading
As RLHF has cemented itself at the center of modern post-training, other policy-gradient
RL algorithms and RL algorithms generally have been proposed to improve the training
process, but they have not had a central role in governing best practices. Examples for
further reading include:
• Pairwise Proximal Policy Optimization (P3O; Wu et al., 2023)\[139\] uses
pairwise data directly in a PPO-style policy update without learning an intermediate
reward model.
• Soft Adaptive Policy Optimization (SAPO)\[140\] replaces hard PPO/GRPO-style
clipping with smooth, temperature-controlled gating, aiming for a continuous trust
region that preserves near-on-policy learning signal while down-weighting off-policy
tokens.
• Off-policy policy-gradient algorithms could enable further asynchronous training, such
asContrastive Policy Gradient (CoPG)\[141\] (a generalization of the direct
alignment algorithm IPO and vanilla policy gradient), which was used by Cohere for
their Command A model \[57\].
• Other implementations of REINFORCE algorithms have been designed for language
models, such asReMax\[142\], which implements a baseline normalization designed
rlhfbook.com 92

specifically to accommodate the sources of uncertainty from reward model inference.
• Some foundation models, such as Apple Intelligence Foundation Models \[143\] or Kimi
k1.5 reasoning model \[144\], have used variants ofMirror Descent Policy Opti-
mization (MDPO)\[145\]. Research is still developing further on the fundamentals
here \[146\], but Mirror Descent is an optimization method rather than directly a policy
gradient algorithm. What is important here is that it is substituted in very similarly
to existing RL infrastructure.
• Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO)pro-
poses 4 modifications to GRPO to better suit reasoning language models, where long
traces are needed and new, underutilized tokens need to be increased in probability
\[130\]. The changes are: 1, have two different clip hyperparameters,εlow and εhigh, so
clipping on the positive side of the logratio can take bigger steps for better exploration;
2, dynamic sampling, which removes all samples with reward = 0 or reward = 1 for all
samples in the batch (no learning signal); 3, use the per-token loss as discussed above
in Implementation: GRPO; and 4, a soft penalty on samples that are too long to avoid
trying to learn from truncated answers.
• Value-basedAugmentedProximalPolicyOptimization(VAPO)\[147\]combines
optimizations from DAPO (including clip-higher, token-level policy-gradient, and
different length normalization) with insights from Value-Calibrated PPO \[148\] to
pretrain the value function and length-adaptive GAE to show the promise of value-
based methods relative to GRPO.
6.5 Suggested Experiments
The companion implementation in code/policy_gradients/ is designed for small, ob-
servable RL runs. The default configs train Qwen/Qwen3-1.7B on the spell_backward
procedural task from reasoning-gym, which is a good first exercise because failures and
partial progress are easy to inspect.
1.Run the word reversal task with GRPO.
cd code/
uv run python -m policy_gradients.train --config
policy_gradients/configs/grpo.yaml
Track avg_correctness, avg_format, and avg_binary. The useful first question is
whether each prompt group contains contrast: if all sampled completions are right or
all are wrong, a group-relative update has little learning signal.
2. Compare group-relative and single-sample estimators.Run the matched
starting configs:
cd code/
uv run python -m policy_gradients.train --config
policy_gradients/configs/reinforce.yaml
uv run python -m policy_gradients.train --config
policy_gradients/configs/rloo.yaml
uv run python -m policy_gradients.train --config
policy_gradients/configs/grpo.yaml
rlhfbook.com 93

Compare how quickly the correctness signal improves and how noisy the loss is. RLOO
and GRPO should make the role of within-prompt baselines much more concrete than
the equations alone.
3. Sweep the contrast knobs.Copypolicy_gradients/configs/grpo.yamland vary
num_rollouts, temperature, data.size, and format_weight. Small num_rollouts
reduces group contrast; very low temperature can collapse samples; very high tempera-
ture can generate too many malformed answers. This is the simplest way to see why
RLVR recipes often spend so much effort on sampling settings before touching the
optimizer.
4. Move from toy rewards toward math.For GSM8K-style experiments, start with
the code/reward_models/train_orm.py and code/rejection_sampling/ examples
before adding a new online RL environment. A good contribution would be a small
reasoning-gym or GSM8K policy-gradient config that runs on a sub-1B Qwen model
and reports the same group-contrast diagnostics.
rlhfbook.com 94

7 Reasoning and Inference-Time Scaling
Reasoning models and inference-time scaling enabled a massive step in language model
performance at the end of 2024, through 2025, and into the future. Inference-time scaling is
the ability to improve model performance by using more computation during generation,
such as producing longer reasoning chains or sampling multiple responses. Language models
trained to think extensively before answering exploit this property remarkably well. These
models, trained with a large amount of reinforcement learning with verifiable rewards (RLVR)
\[6\], still utilize large amounts of RLHF. In this chapter we review the path that led the AI
community to a transformed appreciation for RL’s potential in language models, review the
fundamentals of RLVR, highlight key works, and point to the future debates that will define
the area in the next few years.
7.1 The Role of RLVR
To start, at the 2016 edition of the Neural Information Processing Systems (NeurIPS)
conference, Yann LeCun first introduced his now-famous cake metaphor for where learning
happens in modern machine learning systems:
If intelligence is a cake, the bulk of the cake is unsupervised learning, the icing
on the cake is supervised learning, and the cherry on the cake is reinforcement
learning (RL).
This analogy is now largely complete with modern language models and recent changes to
the post-training stack. RLHF was the precursor to this, and RL for reasoning models,
primarily on math, code, and science topics, was its confirmation. In this analogy:
• Self-supervised learning on vast swaths of internet data makes up the majority of the
cake (especially when viewed in compute spent in FLOPs),
• The beginning of post-training in supervised fine-tuning (SFT) for instructions tunes
the model to a narrower distribution, and
• Finally “pure” reinforcement learning (RL) is the cherry on top. The scaled up
reinforcement learning used to create the new “reasoning” or “thinking” models is this
finishing piece (along with the help of RLHF, which isn’t considered classical RL, as
we’ll explain).
This little bit of reasoning training emerged withthinking modelsthat use a combination
of the post-training techniques discussed in this book to align preferences along with RL
training on verifiable domains to dramatically increase capabilities such as reasoning, coding,
and mathematics problem solving.
The training method for these models, Reinforcement Learning with Verifiable Rewards
(RLVR) \[6\], proceeds very similarly to RLHF, but it makes the reward model optional in
lieu of a scoring function that returns a positive reward when the answer is correct and 0
otherwise.
For example, consider how different it is to score responses for RLHF versus RLVR. In RLHF,
a reward model must evaluate subjective qualities:
Prompt: Explain the concept of opportunity cost in economics.
Response: Opportunity cost is the value of the next best alternative you give
rlhfbook.com 95

up when making a decision. For example, if you spend an hour studying instead
of working, the opportunity cost is the wages you could have earned...
Scoring this response requires judging clarity, accuracy, completeness, and helpfulness – all
qualities that require learned preferences and lack a definitive correct answer.
In contrast, RLVR uses verification functions that return definitive scores. For mathematics:
Prompt: What is the sum of all prime numbers less than 20?
Response: The prime numbers less than 20 are 2, 3, 5, 7, 11, 13, 17, and 19.
Adding them: 2 + 3 = 5, then 5 + 5 = 10, then 10 + 7 = 17, then 17 + 11 = 28,
then 28 + 13 = 41, then 41 + 17 = 58, and finally 58 + 19 = 77. The answer is
77 .
Verification:extracted_answer == 77→Reward = 1
The \boxed{} notation is a convention adopted from mathematical typesetting that makes
answer extraction straightforward – a simple regular expression can pull the final answer from
the response, regardless of how the model arrived at it. Note that other answer extraction
methods exist, such as just using the phrase “The answer is:” as also shown above, special
tokens like<answer>, or delimiters like####.
For code generation, verification often takes the form of unit tests:
Prompt: Write a Python functionfib(n)that returns the nth Fibonacci number,
where fib(0) = 0 and fib(1) = 1.
Response: def fib(n): if n < 2: return n return fib(n - 1) + fib(n - 2)
Verification (unit tests):
assert fib(0) == 0 # base case assert fib(1) == 1 # base case assert fib(10) ==
55 # larger value (All tests pass→Reward = 1)
Unit tests are natural verification functions for code: they execute the model’s solution
against known input-output pairs. A common form of scoring is to perform simple gating:
If all assertions pass, the reward is 1; if any fail, the reward is 0. Other setups use partial
credit proportional to the number of tests passed. For both these examples, no learned
reward model is needed and most setups go without one (because the models are robust
to over-optimization in these domains), but one can be used with a linear combination of
rewards.
The ideas behind RLVR are not new to the RL literature, where the core idea of taking
gradient updates based on whether the answer is correct is almost the textbook definition
of reinforcement learning. The innovations when applying this to language models are
largely how to apply it while maintaining the strong, general capabilities of the model being
fine-tuned. Within that, there are many related ideas in the language modeling literature
where the model learns from feedback regarding the correctness of the answer.
Originally, in the work I was a part of that coined the term RL with Verifiable Rewards
(RLVR) \[6\], the method was to be named RL with Ground Truth rewards (RLGT). Yet
RLVR is subtly different from learning solely from ground truth answers. In domains like
mathematics, a single ground truth answer is available to verify solutions, as we saw above.
In other domains, such as code generation or precise instruction following, answers can be
rlhfbook.com 96

verified with a checking function (e.g., a unit test), even when there are multiple correct
solutions rather than just a single ground truth answer. The core of progress on RLVR
is having a variety and depth of these verifiable problems, even if the exact solution isn’t
known a priori.
Figure 25: RLVR in the form of an RL feedback loop. Instead of a reward model, a
verification function is used.
The first models to successfully deploy this type of training were OpenAI’s o1 \[53\] and the
open-weight model DeepSeek R1 \[15\]. Soon after, the entire AI industry prioritized this
training process and model style. The core change here is more a reallocation of the stages
of training and the priority of different behaviors rather than this type of RL setup being
entirely new. Reasoning models brought an era where scaling RL training is expected.
As for the type of behavior these models exhibit, consider the following example with
DeepSeek V3 0325 versus their reasoning model, DeepSeek R1, on the queryWrite me a
short poem about a goldfish. DeepSeek V3 is very to the point:
Response: Goldfish Dreams
In a bowl of glass so clear and round, A tiny goldfish swims without a sound.
With scales that gleam like sunlight’s kiss, He drifts along in watery bliss.
A flick of fin, a flash so bright, Chasing bubbles in the light. Does he dream of
oceans wide? Or is his little world enough—his pride?
Meanwhile, DeepSeek R1’s experience is different. It first generates numerous thinking
tokens to craft a response before responding to the user. The answer appears as:
rlhfbook.com 97

Response: <thinking> Okay, the user wants a short poem about a goldfish.
Let me start by brainstorming some goldfish-related imagery. Goldfish are often
in bowls, right? So maybe start with the setting. Words like “gilded bowl” or
“crystal globe” could work.
Next, think about the movement of the goldfish. They swim smoothly, so words
like “dart”, “glide”, or “swirl” come to mind. Maybe describe their fins as “silken”
to emphasize delicacy.
Then, consider the environment around the goldfish. Sunlight through water
creates shimmering effects. Words like “sunbeams dance” or “ripples spin” might
capture that. Including elements like castles or pebbles adds a playful touch.
Themes? Maybe the contrast between the goldfish’s small world and its perception
of freedom. The bowl as a universe, tiny but complete. Ending with a sense of
mystery or silent observation could give depth. Need to keep it concise, maybe
four stanzas with a rhyme scheme. Let me check the rhythm and flow. Avoid
clichés but keep it accessible. Alright, let’s piece it together.</thinking>
Gilded Dreams in Liquid Glass
A gilded bowl, a crystal globe, Where tiny tides in silence flow— A flash of
orange, a whispered robe, You dart through sunlit indigo.
Your world is small, yet boundless too— Each pebble, castle, weed unfurled. The
surface bends the sky to blue, And ripples spin your liquid world.
You glide through myths we’ll never know, A silent monarch, veiled in mist. Do
dreams drift where the bubbles go? Or memories in amethyst?
We watch you trace your endless sphere— A universe within a tear.
The tokens in the<thinking> tags are the model’s reasoning. For more complex problems
the reasoning stage can take thousands of tokens before producing an answer. So, long-
context language models were a prerequisite to advanced reasoning behavior, but that is not
the focus of this chapter.
The core intuition forhow this training worksis that for a given model, we repeat the
following cycle:
1. Sample multiple answers to multiple questions,
2. Take gradient steps towards the answers that are correct, and
3. Repeat, revisiting the same data.
Remarkably, this extremely simple approach (when done with a careful distribution of data
and stable training infrastructure) helps the models learn by revisiting the same questions
again and again. Even more remarkable is that the improvements on these training questions
generalize to questions and (some) domains the models have never seen!
This simple approach allows the models to lightly search over behavior space and the RL
algorithm increases the likelihood of behaviors that are correlated with correct answers.
7.2 The Origins of New Reasoning Models
Here we detail the high-level trends that led to the explosion of reasoning models in 2025.
rlhfbook.com 98

7.2.1 Why Does RL Work Now?
Despite many, many takes that “RL doesn’t work yet” \[149\] and papers detailing deep
reproducibility issues with RL \[150\], the field overcame them to find high-impact applications.
Some are covered in this book, such as ChatGPT’s RLHF and DeepSeek R1’s RLVR, but
many others exist, including improving chip design \[151\], mastering video gameplay \[152\],
self-driving \[153\], and more. The takeoff of RL-focused training on language models indicates
progress on many fundamental issues for the research area, including:
• Stability of RL can be solved: For its entire existence, the limiting factor on RL’s
adoption has been stability. This manifests in two ways. First, the learning itself can
be fickle and not always work. Second, the training itself is known to be more brittle
than standard language model training and more prone to loss spikes, crashes, etc.
Countless new model releases are using this style of RL training with verifiable rewards
on top of a pretrained base model and substantial academic uptake has occurred. The
technical barriers to entry on RL are at an all-time low.
• Open-source versions already “exist”: Many tools already exist for training
language models with RLVR and related techniques. Examples include TRL \[47\], Open
Instruct \[6\], veRL \[154\], and OpenRLHF \[155\], where many of these are building on
optimizations from earlier in the arc of RLHF and post-training. The accessibility of
tooling is enabling a large and accelerating body of research.
Multiple resources point to RL training for reasoning only being viable with leading models
coming out from about 2024 onwards, indicating that a certain level of underlying capability
was needed in the models before reasoning training was possible.
7.2.2 RL Training vs. Inference-Time Scaling
Training with reinforcement learning to elicit reasoning behaviors and performance on
verifiabledomainsiscloselylinkedtotheideasofinference-timescaling. Inference-timescaling,
also called test-time scaling, is the general class of methods that use more computational
power at inference in order to perform better at downstream tasks. Methods for inference-
time scaling were studied before the release of DeepSeek R1 and OpenAI’s o1, which both
massively popularized investment in RL training specifically. Examples include value-guided
sampling \[156\] or repeated random sampling with answer extraction \[157\]. Beyond this,
inference-time scaling can be used to improve more methods of AI training beyond chain-of-
thought reasoning to solve problems, such as with reward models that consider the options
deeply \[85\] \[158\].
RL training is a short path to inference-time scaling laws being used, but in the long-term we
will have more methods for eliciting the inference-time tradeoffs we need for best performance.
Training models heavily with RL often enables them to generate more tokens per response
in a way that is strongly correlated with improved downstream performance (although
this sequence length increase is the default, research also exists explicitly on improving
performancewithoutrelying on this inference-time scaling). This is a substantial shift from
the length-bias seen in early RLHF systems \[10\], where the human preference training had a
side effect of increasing the response average length for marginal gains on preference rankings.
Other than the core RL trained models there are many methods being explored to continue
to push the limits of reasoning and inference-time compute. These are largely out of the
rlhfbook.com 99

scope of this book due to their rapidly evolving nature, but they include distilling reasoning
behavior from a larger RL trained model to a smaller model via instruction tuning \[159\],
composing more inference calls \[160\], and more. What is important here is the correlation
between downstream performance and an increase in the number of tokens generated –
otherwise it is just wasted energy.
7.2.3 The Future (Beyond Reasoning) of RLVR
In many domains, these new flavors of RLVR are much more aligned with the goals of
developers by being focused on performance rather than behavior. Standard fine-tuning APIs
generally use a parameter-efficient fine-tuning method such as LoRA (Low-Rank Adaptation,
a parameter-efficient method that trains only small added matrices rather than all model
weights, also referred to as parameter-efficient fine-tuning, PEFT) with supervised fine-tuning
on instructions. Developers pass in prompts and completions and the model is tuned to
match that by updating model parameters to match the completions, which increases the
prevalence of features from your data in the model’s generations.
RLVR is focused on matching answers. Given queries and correct answers, RLVR helps
the model learn to produce the correct answers. While standard instruction tuning is done
with 1 or 2 epochs of loss updates over the data, RLVR gets its name by doing hundreds
or thousands of epochs over the same few data points to give the model time to learn new
behaviors. This can be viewed as reinforcing positive behaviors that would work sparingly in
the base model version into robust behaviors after RLVR.
The scope of RL training for language models continues to grow: The biggest
takeaway from o1 and R1 on a fundamental scientific level was that we have even more ways
to train language models to potentially valuable behaviors. The more open doors that are
available to researchers and engineers, the more optimism we should have about AI’s general
trajectory.
7.3 Understanding Reasoning Training Methods
The investment in reasoning has instigated a major evolution in the art of how models are
trained to follow human instructions. These recipes still use the common pieces discussed
in earlier chapters (as discussed in Chapter 3 with the overview of DeepSeek R1’s recipe),
including instruction fine-tuning, reinforcement learning from human feedback, and rein-
forcement learning with verifiable rewards (RLVR). The core change is using far more RLVR
and applying the other training techniques in different orders – traditionally for a reasoning
model the core training step is either a large-scale RL run or a large-scale instruction tuning
run onoutputsof another model that had undergone a substantial portion of RLVR training
(referred to as distillation).
7.3.1 Reasoning Research Before OpenAI o1 or DeepSeek R1
Before the takeoff of reasoning models, a substantial effort was made to understand how
to train language models to be better at verifiable domains. The main difference between
these works below is that their methodologies did not scale to the same level as those used
in DeepSeek R1 and subsequent models, or they resulted in models that made sacrifices in
overall performance in exchange for higher mathematics or coding abilities. The underlying
rlhfbook.com 100

ideas and motivations are included to paint a broader picture for how reasoning models
emerged within the landscape.
Some of the earliest efforts to train language models on verifiable domains include the
self-taught reasoner (STaR) line of work \[161\] \[162\] and TRICE \[163\], which both used
ground-truth reward signals to encourage chain-of-thought reasoning in models throughout
2022 and 2023. STaR effectively approximates the policy gradient algorithm, but in practice
filters samples differently and uses a cross-entropy measure instead of a log-probability,
and Quiet-STaR expands on this with very related ideas of recent reasoning models by
having the model generate tokens before trying to answer the verifiable question (which
helps with training performance). TRICE \[163\] also improves reasoning by generating
traces and then optimizing with a custom Markov chain Monte Carlo inspired expectation
maximization algorithm. VinePPO \[164\] followed these and used a setup that shifted closer
to modern reasoning models. VinePPO uses a PPO-based algorithm with binary rewards for
math question correctness, training on GSM8K and MATH. Other work before OpenAI’s
o1 and DeepSeek R1 used code execution as a feedback signal for training \[165\], \[166\] or
verification for theorem proving (called Reinforcement Learning from Verifier Feedback,
RLVF, here) \[167\]. Tülu 3 expanded on these methods by using a simple PPO trainer to
reward completions with correct answers – most importantly while maintaining the model’s
overall performance on a broad suite of evaluations. The binary rewards of Tülu 3 and
modern reasoning training techniques can be contrasted with the iterative approach of STaR
or the log-likelihood rewards of Quiet-STaR.
7.3.2 Early Reasoning Models
A summary of the foundational reasoning research reports, some of which are accompanied
by open data and model weights, following DeepSeek R1 is shown in tbl. 4.
Table 4: A summary of the notable reasoning model technical reports in 2025, the first year
of substantial inference-time scaling with RLHF.
Date Name TLDR
Open
weights
Open
data
2025-
01-22
DeepSeek R1
\[15\]
RL-based upgrade to DeepSeek, big gains
on math & code reasoning
Yes No
2025-
01-22
Kimi 1.5 \[144\] Scales PPO/GRPO on Chinese/English
data; strong AIME maths
No No
2025-
03-31
Open-Reasoner-
Zero \[168\]
Fully open replication of base model RL Yes Yes
2025-
04-10
Seed-Thinking
1.5 \[62\]
ByteDance RL pipeline with dynamic
CoT gating
Yes No
2025-
04-30
Phi-4 Reasoning
\[169\]
14B model; careful SFT→RL; excels at
STEM reasoning
Yes No
2025-
05-02
Llama-
Nemotron \[170\]
Multi-size “reasoning-toggle” models Yes Yes
2025-
05-12
INTELLECT-2
\[135\]
First, publicly documented
globally-decentralized RL training run
Yes Yes
rlhfbook.com 101

Date Name TLDR
Open
weights
Open
data
2025-
05-12
Xiaomi MiMo
\[61\]
End-to-end reasoning pipeline from pre-
to post-training
Yes No
2025-
05-14
Qwen 3 \[60\] Similar to R1 recipe applied to new
models
Yes No
2025-
05-21
Hunyuan-
TurboS \[171\]
Mamba-Transformer MoE, adaptive
long/short CoT
No No
2025-
05-28
Skywork OR-1
\[172\]
RL recipe avoiding entropy collapse;
beats DeepSeek on AIME
Yes Yes
2025-
06-04
Xiaomi MiMo
VL \[173\]
Adapting reasoning pipeline end-to-end to
include multi-modal tasks
Yes No
2025-
06-04
OpenThoughts
\[174\]
Public 1.2M-example instruction dataset
distilled from QwQ-32B
Yes Yes
2025-
06-10
Magistral \[175\] Pure RL on Mistral 3; multilingual CoT;
small model open-sourced
Yes No
2025-
06-16
MiniMax-M1
\[124\]
Open-weight 456B MoE hybrid/Lightning
Attention reasoning model; 1M context;
RL w/CISPO; releases 40K/80K
thinking-budget checkpoints
Yes No
2025-
07-10
Kimi K2 \[176\] 1T MoE (32B active) with MuonClip
(QK-clip) for stability; 15.5T token
pretrain without loss spikes; multi-stage
post-train with agentic data synthesis +
joint RL; releases base + post-trained
checkpoints.
Yes No
2025-
07-28
GLM-4.5 \[177\] Open-weight 355B-A32B MoE “ARC”
model with thinking/non-thinking modes;
23T-token multi-stage training +
post-train w/ expert iteration and RL;
releases GLM-4.5 + GLM-4.5-Air (MIT).
Yes No
2025-
08-20
Nemotron Nano
2 \[178\]
Hybrid Mamba-Transformer for long
“thinking traces”; FP8 pretraining at 20T
tokens then compression/distillation;
explicitly releases multiple checkpoints
plus “majority” of pre/post-training
datasets.
Yes Yes
(most)
2025-
09-09
K2-Think \[179\] Parameter-efficient math reasoning
system: a 32B open-weights model with
test-time scaling recipe; positioned as
fully open incl. training data/code (per
release materials).
Yes Yes
2025-
09-23
LongCat-Flash-
Thinking \[180\]
560B MoE reasoning model; report is
explicit about a staged recipe from
long-CoT cold start to large-scale RL;
open-source release.
Yes No
rlhfbook.com 102

Date Name TLDR
Open
weights
Open
data
2025-
10-21
Ring-1T \[181\] Trillion-scale “thinking model” with RL
scaling focus; report frames
bottlenecks/solutions for scaling RL at 1T
and releases an open model.
Yes No
2025-
11-20
Olmo 3 Think
\[18\]
Fully open “model flow” release: reports
the entire lifecycle (stages, checkpoints,
and data points) and positions Olmo 3
Think 32B as a flagship open thinking
model.
Yes Yes
2025-
12-02
DeepSeek V3.2
\[182\]
Open-weight MoE frontier push with a
report that foregrounds attention
efficiency changes, RL framework
upgrades, and data synthesis for
agentic/reasoning performance.
Yes No
2025-
12-05
K2-V2 \[183\] 70B dense “360-open” model trained from
scratch; with 3-effort SFT-only
post-training for controllable thinking.
Yes Yes
2025-
12-15
Nemotron 3
Nano \[184\]
30B-A3B MoE hybrid
Mamba-Transformer; pretrain on 25T
tokens and includes SFT + large-scale
RL; explicitly states it ships weights +
recipe/code + most training data.
Yes Yes
(most)
2025-
12-16
MiMo-V2-Flash
\[185\]
309B MoE (15B active) optimized for
speed: hybrid SWA/GA attention (5:1,
128-token window) + lightweight MTP;
FP8 pretrain on 27T tokens; post-train
with MOPD + large-scale agentic RL for
reasoning/coding.
Yes No
7.3.3 Common Practices in Training Reasoning Models
In this section we detail common methods used to sequence training stages and modify data
to maximize performance when training a reasoning model.
Note that these papers could have used a listed technique and not mentioned it, whereas
their peers do, so these examples are a subset of known implementations and should be used
as a reference, but not a final proclamation on what an optimal recipe is.
• Offline difficulty filtering: A core intuition of RLVR is that models can only learn
from examples where there is a gradient. If the starting model for RLVR can solve a
problem either 100% of the time or 0% of the time, there will be no gradient between
different completions to the prompt (i.e., all strategies appear the same to the policy
gradient algorithm). Many models have used difficulty filtering before starting large-
scale RL to restrict the training problems to those that the starting point model solves
only 20-80% of the time. This data is collected by sampling N, e.g. 16, completions
to each prompt in the training set and verifying what percentage are correct. Forms
rlhfbook.com 103

of this were used by Seed-Thinking 1.5, Open Reasoner Zero, Phi-4, INTELLECT-2,
MiMo RL, Skywork OR-1, and others.
• Per-batch online filtering(or difficulty curriculums throughout training): To
complement the offline filtering to find the right problems to train on, another major
question is: what order should the problems be presented to the model during learning?
In order to address this, many models use online filtering of questions in the batch,
prebuilt curriculums/data schedulers, saving harder problems for later in training,
or other ideas to improve long-term stability. Related ideas are used by Kimi 1.5,
Magistral, Llama-Nemotron, INTELLECT-2, MiMo-RL, Hunyuan-TurboS, and others.
• Remove KL penalty: As the length of RL runs (in any metric, total GPU hours,
FLOPS, or RL steps) increased for reasoning models relative to RLHF training, and
the reward function became less prone to over-optimization, many models removed the
KL penalty constraining the RL-learned policy to be similar to the base model used at
the start of training. This allows the model to further explore during its training. This
was used by RAGEN \[186\], Magistral, OpenReasonerZero, Skywork OR-1, and others.
• Relaxed policy-gradient clipping: New variations of the algorithm GRPO, such as
DAPO \[130\], proposed modifications to the two-sided clipping objective used in GRPO
(or PPO) in order to enable better exploration. Clipping has also been shown to cause
potentially spurious learning signals when rewards are imperfect \[187\]. This two-sided
clipping with different ranges per gradient direction is used by RAGEN, Magistral,
INTELLECT-2, and others.
• Off-policy data (or fully asynchronous updates): As the length of completions
needed to solve tasks with RL increases dramatically with harder problems (particularly
in thevarianceof the response length, where there are often outliers with extremely
long lengths), compute in RL runs can sit idle. To solve this, training is moving
to asynchronous updates or changing how problems are arranged into batches to
improve overall throughput. Partial-to-full asynchronous (off-policy) data is used by
Seed-Thinking 1.5, INTELLECT-2, and others.
• Additional format rewards: In order to make the reasoning process predictable,
many models add minor rewards to make sure the model follows the correct for-
mat of e.g. <think>...</think> before an answer. This is used by DeepSeek R1,
OpenReasonerZero, Magistral, Skywork OR-1, and others.
• Language consistency rewards: Similar to format rewards, some multilingual
reasoning models use language consistency rewards to prioritize models that do not
change languages while reasoning (for a better and more predictable user experience).
These include DeepSeek R1, Magistral, and others.
• Length penalties: Many models use different forms of length penalties during RL
training to either stabilize the learning process over time or to mitigate overthinking
on hard problems. Some examples include Kimi 1.5 progressively extending the
target length to combat overthinking (while training accuracy is high across difficulty
curriculum)orINTELLECT-2runningasmalllengthpenaltythroughout. Progressively
extending the training sequence length mitigates overthinking by forcing the model
to first reason effectively in a domain with a more limited thinking budget, and then
transitioning to longer training where the model can use those behaviors efficiently on
morecomplexproblems. Othersuseoverlongfilteringandotherrelatedimplementations
to improve throughput.
• Loss normalization: There has been some discussion (see the chapter on policy
gradients or \[119\]) around potential length or difficulty biases introduced by the per-
rlhfbook.com 104

group normalization terms of the original GRPO algorithm. As such, some models,
such as Magistral or MiMo, chose to normalize either losses or advantages at the batch
level instead of the group level.
• Parallel test-time compute scaling: Combining answers from multiple parallel,
independently-sampled rollouts can lead to substantial improvements over using the
answer from a single rollout. The most naive form of parallel test-time compute scaling,
as done in DeepSeek-R1, Phi-4, and others, involves using the answer returned by a
majority of rollouts as the final answer. A more advanced technique is to use a scoring
model trained to select the best answer out of the answers from the parallel rollouts.
As of 2026, this technique had not become common in open, documented reasoning
model recipes, but it was mentioned in the Claude 4 announcement \[188\] and used in
DeepSeek-GRM \[158\].
Complementing the common techniques, there are also many common findings on how
reasoning training can create useful models without sacrificing ancillary capabilities:
• Text-only reasoning boosts multimodal performance: Magistral, MiMo-VL, and
others find that training a multimodal model and then performing text-only reasoning
training after this multimodal training canimprovemultimodal performance in the
final model.
• Toggleable reasoning with system prompt(or length control): Llama-Nemotron,
Nemotron Nano, Qwen 3, SmolLM 3, and others use specific system prompts (possibly
in combination with length-controlled RL training \[189\]) to enable a toggleable on/off
thinking length for the user. Other open models, such as OpenAI’s gpt-oss and
LLM360’s K2-V2 \[183\] adopt a low-medium-high reasoning effort set in the system
prompt, but training methods for this type of behavior are not as well documented.
7.4 Looking Ahead
The reasoning model landscape is evolving faster than any area of AI research in recent
memory, and some of the common practices listed here will inevitably be superseded by new
techniques.
Several efforts are underway to systematically understand what makes reasoning training
work. Olmo 3 Think \[18\] represents the most comprehensive open documentation of a
reasoning model’s full training lifecycle, providing checkpoints and data at each stage for
the research community to study, and concluding with a nearly 4-week-long training run on
220 GPUs. Similarly, work on understanding the scaling properties of RL for reasoning \[17\]
is beginning to formalize relationships between compute, data, and performance that were
previously only intuited by practitioners.
What remains clear is that reinforcement learning has graduated from the “cherry on top”
in the cake metaphor to a load-bearing component of frontier model training. The minor
techniques in this chapter around the idea of RLVR – difficulty filtering, format rewards, and
the rest – are not the final answers, but they represent the field’s current best understanding
of how to elicit reasoning from language models. The next generation of methods will likely
look different, but they will build on the foundations established here.
rlhfbook.com 105

8 Direct-Alignment Algorithms
Direct Alignment Algorithms (DAAs) allow one to update models to solve the same RLHF
objective without ever training an intermediate reward model or using reinforcement learning
optimizers. DAAs solve the same preference learning problem we’ve been studying (with
literally the same data!), in order to make language models more aligned, smarter, and
easier to use. The lack of a reward model and online optimization makes DAAs far simpler
to implement, reducing compute spent during training and making experimentation easier.
This chapter details the complex mathematics done to derive these algorithms, and then
shows that the sometimes tedious derivations result in simple implementations.
The most prominent DAA and one that catalyzed an entire academic movement of aligning
language models is Direct Preference Optimization (DPO) \[25\]. At its core, DPO uses
gradient ascent to solve the same constrained RLHF objective (see Chapter 3):
max
π
Ex∼DEy∼π(y|x) [rθ(x,y)]−βD KL (π(y|x)∥π ref(y|x))(80)
Since its release in May of 2023, after a brief delay where the community figured out the
right data and hyperparameters to use DPO with (specifically, surprisingly low learning
rates), many popular models have used DPO or its variants, from Zephyr-β kickstarting it
in October of 2023 \[26\], Llama 3 Instruct \[29\], Tülu 2 \[27\] and 3 \[6\], Nemotron 4 340B \[30\],
and others. Technically, Sequence Likelihood Calibration (SLiC-HF) was the first modern
direct alignment algorithm released \[190\], but it did not catch on due to a combination of
factors (unwinding the adoption of research methods is always a tricky task).
The most impactful part of DPO and DAAs is lowering the barrier to entry to experimenting
with language model post-training – it uses less compute, is easier to implement from scratch,
and is easier to get working on both toy and production examples.
Throughout this chapter, we usex to denote prompts andy to denote completions. This
notation is common in the language model literature, where methods operate on full prompt-
completion pairs rather than individual tokens.
8.1 Direct Preference Optimization
Here we explain intuitions for how DPO works and re-derive the core equations fully.
8.1.1 How DPO Works
DPO at a surface level is directly optimizing a policy to solve the RLHF objective. The
loss function for this, which we will revisit below in the derivations, compares how much
the learned policy’s probability of chosen and rejected completions has shifted relative to a
reference model. The loss function derived from a Bradley-Terry reward model follows:
LDPO(πθ;π ref) =−E (x,yc,yr)∼D
[
logσ
(
βlog πθ(yc|x)
πref(yc|x) −βlog πθ(yr|x)
πref(yr|x)
)]
(81)
Inside the sigmoid, the first termβlog πθ(yc|x)
πref(yc|x) measures how much the policy has increased
the probability of thechosencompletion relative to the reference model, and the second
rlhfbook.com 106

term does the same for therejectedcompletion. The loss decreases when the chosen shift
exceeds the rejected shift – i.e. when the policy learns to prefer the right response.
Throughout, β is a hyperparameter balancing the reward optimization to the KL divergence
between the final model and the initial reference (i.e. balancing over-optimization, a crucial
hyperparameter when using DPO correctly). This relies on the implicit reward for DPO
training that replaces using an external reward model, which is a log-ratio of probabilities:
r(x,y) =βlog πr(y|x)
πref(y|x) (82)
where πr(y|x )is the exact, optimal reward policy that we are solving for. This comes from
deriving the Bradley-Terry reward with respect to an optimal policy (shown in eq. 97), as
shown in the Bradley-Terry model section of Chapter 5. Essentially, as stated in the DPO
paper, this reparameterization gives us “the probability of human preference data in terms
of the optimal policy rather than the reward model” – meaning we can bypass learning an
explicit reward model entirely.
Let us consider the loss shown in eq. 81 that the optimizer must decrease. Here, the loss will
be lower when the log-ratio of the chosen response is bigger than the log-ratio of the rejected
response (normalized by the reference model). In practice, this is a sum of log-probabilities
of the model across the sequence of tokens in the data presented. Hence, DPO is increasing
the gap in relative log-probabilities between the chosen and rejected responses.
With the reward in eq. 82, we can write the gradient of the loss to further interpret what is
going on:
∇θLDPO(πθ;π ref) =−βE (x,yc,yr)∼D [w·(∇ θ logπθ(yc|x)−∇ θ logπθ(yr|x))](83)
wherew=σ(r θ(x,yr)−r θ(x,yc)).
Here, the gradient solves the above objective by doing the following:
• The first term within the sigmoid function,σ(·), creates a weight of the parameter
update from 0 to 1 that is higher when the reward estimate is incorrect. When the
rejected sample is preferred over the chosen, the weight update should be larger!
• Second, the terms in the inner brackets[·]increase the likelihood of the chosen response
yc and decrease the likelihood of the rejectedyr.
• These terms are weighted byβ, which controls how the update balances ordering the
completions correctly relative to the KL divergence.
The core intuition is that DPO is fitting an implicit reward model whose corresponding
optimal policy can be extracted in closed form (eq. 97, thanks to gradient descent and our ML
tools). Because the DPO loss is directly differentiable, it is straightforward to compute the
exact gradient, rather than needing to estimate it by training a reward model and sampling
completions to score. What is often misunderstood is that DPO is learning a reward model
at its core, hence the subtitle of the paperYour Language Model is Secretly a Reward Model.
It is easy to confuse this with the DPO objective training a policy directly, hence studying
the derivations below is good for a complete understanding.
rlhfbook.com 107

With the implicit reward model learning, DPO is generating an optimal solution to the RLHF
objective given the data in the dataset and the specific KL constraint in the objectiveβ.
Here, DPO solves for the exact policy given a specific KL divergence because the generations
are not online as in policy gradient algorithms – a core difference from the RL methods for
preference tuning. In many ways, this makes theβ value easier to tune with DPO relative
to online RL methods, but crucially and intuitively the optimal value depends on the model
being trained and the data training it.
At each batch of preference data, composed of many pairs of completionsychosen≻y rejected,
DPO takes gradient steps directly towards the optimal solution. It is far simpler than policy
gradient methods.
Figure 26: When DPO first released it sparked a fierce debate in the research community
about how to best do RLHF and preference learning. This meme does a great job capturing
the sentiment, where the debate often felt forced and over the top, but many people both
getting started and in top labs were getting immense benefit out of DPO. DPO simplicity
meme, credit Tom Goldstein.
8.1.2 DPO Derivation
The DPO derivation takes two primary parts. First, the authors show the form of the policy
that optimally solved the RLHF objective used throughout this book. Next, they show how
to arrive at that solution from pairwise preference data (i.e. a Bradley-Terry model).
rlhfbook.com 108

8.1.2.1 Deriving the Optimal RLHF SolutionTo start, we should consider the
RLHF optimization objective once again, here indicating we wish to maximize this quantity:
max
π
Ex∼DEy∼π(y|x) [rθ(x,y)]−βD KL (π(y|x)∥π ref(y|x))(84)
Here, the dual expectation only applies to the sampling to compute the expected reward,
as the KL term is still an analytical expression. First, let us expand the definition of KL-
divergence. Recall thatDKL(π∥πref) = Ey∼π
[
log π(y|x)
πref(y|x)
]
, where theπ(y|x)weighting in the
sum becomes the sampling distribution. Since both terms now share the same expectation
overy∼π(y|x), we can combine them:
max
π
Ex∼DEy∼π(y|x)
[
r(x,y)−βlog π(y|x)
πref(y|x)
]
(85)
Next, bring the negative sign out of the difference in brackets. To do this, split it into two
terms:
= max
π
(
Ex∼DEy∼π(y|x) [r(x,y)]−βE x∼DEy∼π(y|x)
[
log π(y|x)
πref(y|x)
])
(86)
Then, multiply by−1to convert the maximization into a minimization:
= min
π
(
−Ex∼DEy∼π(y|x) [r(x,y)] +βE x∼DEy∼π(y|x)
[
log π(y|x)
πref(y|x)
])
(87)
Divide byβand recombine:
= min
π
(
Ex∼DEy∼π(y|x)
[
log π(y|x)
πref(y|x)− 1
βr(x,y)
])
(88)
Next, we must introduce a partition function,Z(x):
Z(x) =
∑
y
πref(y|x) exp
(1
βr(x,y)
)
(89)
The partition function acts as a normalization factor for the unnormalized density
πref(y|x) exp
(
1
βr(x,y)
)
, thereby making it a valid probability function overy for each fixed
x. The exact need for this will become clear shortly as we proceed with the derivation.
With this substituted in, we obtain our intermediate transformation:
min
π
Ex∼DEy∼π(y|x)

log π(y|x)
1
Z(x)πref(y|x) exp
(
1
βr(x,y)
)−logZ(x)

 (90)
rlhfbook.com 109

To see how this is obtained, consider the internal part of the optimization in brackets of
eq. 88:
log π(y|x)
πref(y|x)− 1
βr(x,y)(91)
Then, addlogZ(x)−logZ(x)to both sides:
= log π(y|x)
πref(y|x)− 1
βr(x,y) + logZ(x)−logZ(x)(92)
Then, we group the terms:
=
(
log π(y|x)
πref(y|x) + logZ(x)
)
−logZ(x)− 1
βr(x,y)(93)
Withlog(x) + log(y) = log(x·y)(and movingZto the denominator), we get:
= log π(y|x)
1
Z(x)πref(y|x)−logZ(x)− 1
βr(x,y)(94)
Next, we expand 1
βr(x,y )to log exp 1
βr(x,y )and do the same operation to get eq. 90, which
we slightly rewrite here:
min
π
Ex∼D

Ey∼π(y|x)

log π(y|x)
1
Z(x)πref(y|x) exp
(
1
βr(x,y)
)

−logZ(x)

 (95)
With this optimization form, we need to actually solve for the optimal policyπ∗. Since we
introduced the partition functionZ(x), thereby making the term1
Z(x)πref(y|x) exp
(
1
βr(x,y)
)
a valid probability distribution overy, we can recognize that the inner expectation is in fact
a proper KL-divergence!
min
π
Ex∼D
[
DKL
(
π(y|x)
‖‖‖‖
1
Z(x)πref(y|x) exp
(1
βr(x,y)
))
−logZ(x)
]
(96)
Since the termlogZ (x)does not depend onπ (the policy we are optimizing), we can ignore
it. This leaves us with just the KL divergence between the policy we are learning and a
form relating the partition,β, reward, and reference policy. Gibbs’ inequality tells us this
is minimized at a distance of 0, only when the two quantities are equal! Hence, we get an
optimal policy:
π∗(y|x) =π(y|x) = 1
Z(x)πref(y|x) exp
(1
βr(x,y)
)
(97)
rlhfbook.com 110

8.1.2.2 Deriving DPO Objectives for BT ModelsTo start, recall from Chapter
5 on Reward Modeling and Chapter 11 on Preference Data that a Bradley-Terry model of
human preferences is formed as:
p∗(y1≻y 2|x) = exp (r∗(x,y 1))
exp (r∗(x,y 1)) + exp (r∗(x,y 2)) (98)
By manipulating eq. 97, we can solve for the optimal reward. First, take the logarithm of
both sides:
logπ∗(y|x) = log
( 1
Z(x)πref(y|x) exp
(1
βr∗(x,y)
))
(99)
Expanding the right-hand side usinglog(abc) = loga+ logb+ logc:
logπ∗(y|x) =−logZ(x) + logπ ref(y|x) + 1
βr∗(x,y)(100)
Rearranging to solve forr∗(x,y):
1
βr∗(x,y) = logπ ∗(y|x)−logπ ref(y|x) + logZ(x)(101)
Multiplying both sides byβ:
r∗(x,y) =βlog π∗(y|x)
πref(y|x) +βlogZ(x)(102)
We then can substitute the reward into the Bradley-Terry equation shown in eq. 98 to obtain:
p∗(y1≻y 2|x) =
exp
(
βlog π∗(y1|x)
πref(y1|x) +βlogZ(x)
)
exp
(
βlog π∗(y1|x)
πref(y1|x) +βlogZ(x)
)
+ exp
(
βlog π∗(y2|x)
πref(y2|x) +βlogZ(x)
)
(103)
By decomposing the exponential expressions fromea+b to eaeb and then cancelling out the
termse βlogZ(x) , this simplifies to:
p∗(y1≻y 2|x) =
exp
(
βlog π∗(y1|x)
πref(y1|x)
)
exp
(
βlog π∗(y1|x)
πref(y1|x)
)
+ exp
(
βlog π∗(y2|x)
πref(y2|x)
) (104)
Then, multiply the numerator and denominator byexp
(
−βlog π∗(y1|x)
πref(y1|x)
)
to obtain:
p∗(y1≻y 2|x) = 1
1 + exp
(
βlog π∗(y2|x)
πref(y2|x)−βlog π∗(y1|x)
πref(y1|x)
) (105)
rlhfbook.com 111

Finally, with the definition of a sigmoid function asσ(x) = 1
1+e−x, we obtain:
p∗(y1≻y 2|x) =σ
(
βlog π∗(y1|x)
πref(y1|x) −βlog π∗(y2|x)
πref(y2|x)
)
(106)
This is the likelihood of preference data under the Bradley-Terry model, given the optimal
policy π∗. Recall from Chapter 5 on Reward Modeling that we derived the Bradley-Terry
objective as maximizing the likelihood, or equivalently minimizing the negative log-likelihood,
which gives us the loss:
LDPO(πθ;π ref) =−E (x,yc,yr)∼D [logp(yc≻y r|x)]
=−E (x,yc,yr)∼D
[
logσ
(
βlog πθ(yc|x)
πref(yc|x)−βlog πθ(yr|x)
πref(yr|x)
)] (107)
This is the loss function for DPO, in the form shown in eq. 81. The DPO paper has an
additional derivation for the objective under a Plackett-Luce Model, which is far less used in
practice \[25\].
8.1.2.3 Deriving the BT DPO GradientWe used the DPO gradient shown in eq. 83
to explain intuitions for how the model learns. To derive this, we must take the gradient of
eq. 107 with respect to the model parameters.
∇θLDPO(πθ;π ref) =−∇ θE(x,yc,yr)∼D
[
logσ
(
βlog πθ(yc|x)
πref(yc|x)−βlog πθ(yr|x)
πref(yr|x)
)]
(108)
To start, this can be rewritten. We know that the derivative of a sigmoid functiond
dxσ(x) =
σ(x)(1−σ (x)), the derivative of the logarithm d
dx logx = 1
x, and properties of sigmoid
σ(−x) = 1−σ(x), so we can reformat the above equation.
First, letu =βlog πθ(yc|x)
πref(yc|x)−βlog πθ(yr|x)
πref(yr|x) (the expression inside the sigmoid). Then, we
have
∇θLDPO(πθ;π ref) =−E (x,yc,yr)∼D
[σ′(u)
σ(u)∇θu
]
(109)
Expanding this and using the above expressions for sigmoid and logarithms results in the
gradient introduced earlier:
−E(x,yc,yr)∼D
[
βσ
(
βlog πθ(yr|x)
πref(yr|x)−βlog πθ(yc|x)
πref(yc|x)
)
[∇θ logπθ(yc|x)−∇ θ logπθ(yr|x)]
]
(110)
rlhfbook.com 112

8.2 Numerical Concerns, Weaknesses, and Alternatives
Many variants of the DPO algorithm have been proposed to address weaknesses of DPO. For
example, without rollouts where a reward model can rate generations, DPO treats every pair
of preference data with equal weight. In reality, as seen in Chapter 11 on Preference Data,
there are many ways of capturing preference data with a richer label than binary. Multiple
algorithms have been proposed to re-balance the optimization away from treating each pair
equally.
• REgression to RElative REward Based RL (REBEL)adds signal from a reward
model, as a margin between chosen and rejected responses, rather than solely the
pairwise preference data, to more accurately solve the RLHF problem \[191\].
• Conservative DPO (cDPO) and Identity Preference Optimization (IPO)
address overfitting by assuming noise in the preference data. cDPO assumes N percent
of the data is incorrectly labeled \[25\] and IPO changes the optimization to soften the
probability of preference rather than optimize directly from a label \[192\]. Practically,
IPO changes the preference probability to a nonlinear function, moving away from the
Bradley-Terry assumption, withΨ(q) = log
(
q
1−q
)
.
• DPO with an offset (ODPO)“requires the difference between the likelihood of the
preferred and dispreferred response to be greater than an offset value” \[193\] – do not
treat every data pair equally, but this can come at the cost of a more difficult labeling
environment.
Some variants of DPO attempt to either improve the learning signal by making small changes
to the loss or make the application more efficient by reducing memory usage.
• Odds Ratio Policy Optimization (ORPO)directly updates the policy model with
a pull towards the chosen response, similar to the instruction fine-tuning loss, with a
small penalty on the chosen response \[194\]. This change of loss function removes the
need for a reference model, simplifying the setup. The best way to view ORPO is as
DPO inspired, rather than a DPO derivative.
• Simple Preference Optimization (SimPO)makes a minor change to the DPO
optimization, by averaging the log-probabilities rather than summing them or adding
length normalization, to improve performance \[195\].
One of the core issuesapparentin DPO is that the optimization drives only to increase
the margin between the probability of the chosen and rejected responses. Numerically, the
model reduces the probability of both the chosen and rejected responses, but therejected
response is reduced by a greater extentas shown in fig. 27. Intuitively, it is not clear how this
generalizes, but work has posited that it increases the probability of unaddressed behaviors –
i.e. tokens that the language model could generate, but are not in the distribution of the
post-training datasets \[196\] \[197\]. Simple methods—such as Cal-DPO \[198\], which adjusts
the optimization process, and AlphaPO \[199\], which modifies the reward shape—mitigate
thispreference displacement. In practice, the exact impact of this is not well known, but
points to a potential reason why online methods can outperform vanilla DPO.
The other primary reason posited for DPO-like methods to have a lower ceiling on performance
than online (RL based) RLHF methods is that the training signal comes from completions
from previous or other models. Online variants of DPO alleviate these limitations by
generating new completions and incorporating a preference signal at training time.Online
rlhfbook.com 113

Figure 27: Sketch of preference displacement in DPO.
DPO\[200\] samples generations from the current model, whileDiscriminator-Guided
DPO(D2PO) \[201\] uses reward model relabelling to create new preference data on the fly,
and many more variants exist.
There is a long list of other DAA variants, such as Direct Nash Optimization (DNO) \[202\] or
Binary Classifier Optimization (BCO) \[203\], but the choice of algorithm is far less important
than the initial model and the data used \[6\] \[204\] \[205\].
8.3 Implementation Details
DAAs such as DPO are implemented very differently than policy gradient optimizers. The
DPO loss, taken from the original implementation, largely can be summarized as follows \[25\]:
# Log-probability gaps for the policy and the frozen reference model
pi_logratios = policy_chosen_logps - policy_rejected_logps
ref_logratios = reference_chosen_logps - reference_rejected_logps
# Difference of log-ratios: positive when the policy
# shifts probability toward the chosen completion
logits = pi_logratios - ref_logratios
# DPO loss: negative log-sigmoid drives the policy to
# widen the gap between chosen and rejected
losses = -F.logsigmoid(beta * logits)
# Implicit rewards (detached -- used for logging only)
chosen_rewards = beta * (policy_chosen_logps - reference_chosen_logps).detach()
rejected_rewards = beta * (policy_rejected_logps - reference_rejected_logps).detach()
This can be used in standard language model training stacks as this information is already
collated during the forward pass of a model (with the addition of a reference model).
In most ways, DAAs are simpler and a quality of life improvement, but they also offer a
rlhfbook.com 114

different set of considerations.
1. KL divergence is static: In DPO and other algorithms, the KL divergence is set
explicitly by theβ parameter that balances the distance penalty to the optimization.
This is due to the fact that DPO takes gradient steps towards theoptimalsolution to
the RLHF objective given the data – it steps exactly to the solution set by theβ term.
On the other hand, RL based optimizers take steps based on the batch and recent
data.
2. Caching log-probabilities: Simple implementations of DPO do the forward passes
for the policy model and reference models at the same time for convenience with respect
to the loss function. However, this doubles the memory used and results in increased
GPU usage. To avoid this, one can compute the log-probabilities of the reference model
over the training dataset first, then reuse those cached reference log-probabilities when
computing the loss and updating the parameters per batch, reducing the peak memory
usage by 50%.
8.4 DAAs with Synthetic Preference Data
Most of the popular datasets for performing preference fine-tuning with DAAs these days are
synthetic preferences where a frontier model rates outputs from other models as the winner
or the loser. Prominent examples include UltraFeedback (the first of this category) \[28\],
Tülu 3 (built with an expanded UltraFeedback methodology) \[6\], SmolLM 3’s data \[206\], or
the Dolci Pref dataset released with Olmo 3 \[18\].
The best practices for constructing these datasets are still evolving. Tülu 3 and datasets
around its release in November of 2024 demonstrated that synthetic, pairwise preference
data needs to be “on-policy” in a sense that some completions are generated from the model
you’re fine-tuning (while being mixed in a bigger model pool). This on-policy nature of the
data ensured that the DAA would optimize the correct token space within which the model
generates – as the loss functions are contrastive and less direct than instruction fine-tuning.
Later, with the release of Olmo 3 and SmolLM 3 in 2025, other works supported a different
theory called Delta Learning, which argues that the difference between the chosen and
rejected completions is more important to learning than exactly which models are used for
the completions \[207\]. For example, in both of these two referenced models, the chosen
responses are from Qwen 3 32B and the rejected responses are from Qwen 3 0.6B – both
authors developed this pairing concurrently and independently.
Overall, training models on synthetic preference data with DAAs is the place most practi-
tioners should start, given the simplicity of implementation and strong performance relative
to preference fine-tuning with reinforcement learning based methods. Other minor issues
exist when using extensive, synthetic preference data, such as biases of the model judging
between completions. Given that frontier models such as GPT-4 are known to have length
bias \[80\] and a preference for outputs that match themselves \[208\] (see Chapter 12 for more
information), it is slightly more likely for a piece of text in the “chosen” section of the dataset
to be either from an OpenAI model or another strong model that is stylistically similar to it.
To conclude this section, we’ll cover an intuition for how these methods change the generations
of the model being trained. At a high level, most DAAs optimize to increase the margin
between the probability of “chosen” and “rejected” completions (some less popular algorithms
are designed to slightly change these dynamics, but the core remains). As discussed earlier
rlhfbook.com 115

in this chapter (see fig. 27), this often means both probabilities decrease, but the rejected
response decreases by a greater extent. Each token in a sequence receives a different gradient
(magnitude and direction) based on how much it contributed to the overall preference margin,
allowing the optimizer to identify which tokens matter most to the outcome.
8.5 DAAs vs. RL: Online vs. Offline Data
Broadly, the argument boils down to one question: Do we need the inner workings of
reinforcement learning, with value functions, policy gradients, and all, to align language
models with RLHF? This, like most questions phrased this way, is overly simple. Of course,
both methods are well-established, but it is important to illustrate where the fundamental
differences and performance manifolds lie.
Multiple reports have concluded that policy-gradient based and RL methods outperform
DPO and its variants. The arguments take different forms, from training models with
different algorithms but controlled data \[126\] \[166\] or studying the role of on-policy data
within the RL optimization loop \[209\]. In all of these cases, DPO algorithms are a hair
behind.
Even with this performance delta, DAAs are still used extensively in leading models due
to their simplicity. DAAs provide a controlled environment where iterations on training
data and other configurations can be made rapidly, and given that data is often far more
important than algorithms, using DPO can be fine.
With the emergence of reasoning models that are primarily trained with RL, further invest-
ment will return to using RL for preference-tuning, which in the long-term will improve
the robustness of RL infrastructure and cement this margin between DAAs and RL for
optimizing from human feedback.
8.6 Suggested Experiments
The companion code incode/direct_alignment/ trains DPO and several related losses on
preference data. This is the most accessible place to start experimenting with preference
tuning because the setup is offline: no reward model server or rollout loop is required.
1.Train a small DPO run on UltraFeedback.
cd code/
uv run python -m direct_alignment.train --loss dpo --max_samples 1000
Watch loss, accuracy, margins, chosen_rewards, and rejected_rewards. The
main sanity check is that the implicit reward margin should move in the desired
direction without the model’s sample generations collapsing.
2.Compare DPO, IPO, and length-normalized DPO.
cd code/
uv run python -m direct_alignment.train --config direct_alignment/configs/dpo.yaml
uv run python -m direct_alignment.train --config direct_alignment/configs/ipo.yaml
uv run python -m direct_alignment.train --config
direct_alignment/configs/dpo_norm.yaml
rlhfbook.com 116

Compare the margin scale and the learning rate sensitivity. IPO’s loss is not on the
same numeric scale as DPO, so read it throughaccuracy and margin behavior rather
than raw loss alone.
3. Try the reference-free variants carefully.Run SimPO or ORPO from their configs,
then inspect the generated samples that are logged during training. These losses are
more sensitive to log-probability scaling and learning rate, which makes them useful
debugging exercises.
cd code/
uv run python -m direct_alignment.train --config
direct_alignment/configs/simpo.yaml
uv run python -m direct_alignment.train --config
direct_alignment/configs/orpo.yaml
4. Change the data before changing the loss.Keep the loss fixed and vary
--max_samples, --max_length, or the preference dataset. If the results move more
than changing between DPO-like objectives, that is an empirical reminder of a central
theme in preference tuning: data usually dominates small algorithmic differences.
rlhfbook.com 117

9 Rejection Sampling
Rejection Sampling (RS) is one of the most widely used yet least documented methods in
preference fine-tuning. Many prominent RLHF papers use it as a core component of their
training pipeline, yet no canonical implementation or explanation of why it works so well
exists. RS can be applied at multiple points in the training pipeline – after instruction
fine-tuning, after RL-based optimization, or even after RLVR – making it a versatile but
hard-to-place tool. Combined with its underdocumented nature, this is why it appears here
at the end of the core optimization methods.
Rejection sampling operates by curating new candidate completions, filtering them based on
a trained reward model, and then fine-tuning the original model only on the top completions
(the same loss function as instruction tuning).
The name originates from computational statistics \[210\], where one wishes to sample from
a complex distribution, but does not have a direct method to do so. To alleviate this,
one samples from a distribution that is simpler to model and uses a heuristic to check if
the sample is permissible. With language models, the target distribution is high-quality
completions to prompts, the filter is a reward model, and the sampling distribution is the
current model.
WebGPT \[4\], Anthropic’s Helpful and Harmless agent \[5\], OpenAI’s popular paper on process
reward models \[50\], Llama 2 Chat models \[49\], and other seminal works all use this baseline;
more recent work has formalized it directly (e.g., RAFT \[211\] for applying it to alignment
in multiple modalities and Statistical Rejection Sampling Optimization (RSO) \[212\] that
gives a principled overview of how rejection sampling relates to other preference learning
objectives).
Throughout this chapter, we usex to denote prompts andy to denote completions. This
notation is common in the language model literature, where methods operate on full prompt-
completion pairs rather than individual tokens.
9.1 Training Process, Step by Step
Rejection sampling overall follows a few stages.
0. Prompt and reward model selection:First, you must select the prompts you want
to train on, relative to other stages of training. The simplest method is to re-use every
prompt from the first SFT/IFT stage, but this can cause some overfitting. Before
doing rejection sampling, you must also have trained a reward model (see Chapter 5
for more information).
1. Generate completions from the starting checkpoint:Next, one must generate
completions to the selected prompts with the model they want to optimize. This can
involve tweaking many settings, such as sampling temperature, top-p, max sequence
length, number of completions per prompt, etc.
2. Select top completions with a reward model: All completions are ranked by a
reward model. This stage may also include deduplication to keep only one completion
per prompt, though many such design choices come down to empirical ablation studies.
3. SFT on top completions:To finish rejection sampling, one instruction fine-tunes
the starting checkpoint on the selected completions.
rlhfbook.com 118

A visual overview of the rejection sampling process is included below in fig. 28.
Figure 28: Rejection sampling overview.
The actual details on which prompts to use, how to select a reward model, how to sequence
rejection sampling, etc. are not well documented in the literature. This chapter provides an
overview of the methods and leaves further experimentation to the reader.
9.1.1 Generating Completions
To generate a set of multiple candidate completions per prompt, let’s define a set ofM
prompts as a vector:
X= [x 1,x 2,...,x M](111)
These prompts can come from many sources, but most commonly they come from the
instruction training set.
For each promptxi, we generateNcompletions. We can represent this as a matrix:
Y=


y1,1 y1,2 ···y 1,N
y2,1 y2,2 ···y 2,N
... ... ... ...
yM,1 yM,2 ···y M,N

 (112)
where yi,j represents thej-th completion for thei-th prompt. Each rowi corresponds to a
single promptxi and contains itsN candidate completions; each columnj corresponds to
thej-th sampled completion across all prompts.
9.1.2 Scoring Completions
Now, we pass all of these prompt-completion pairs through a reward model, to get a matrix
of rewards. We’ll represent the rewards as a matrixR:
R=


r1,1 r1,2 ···r 1,N
r2,1 r2,2 ···r 2,N
... ... ... ...
rM,1 rM,2 ···r M,N

 (113)
rlhfbook.com 119

Each rewardri,j is computed by passing the completionyi,j and its corresponding prompt
xi through a reward modelR:
ri,j =R(y i,j|x i)(114)
There are multiple methods to select the top completions to train on.
To formalize the process of selecting the best completions based on our reward matrix, we
can define a selection functionSthat operates on the reward matrixR.
9.1.2.1 Top Per PromptThe first potential selection function takes the max reward
per prompt.
S(R) =
[
arg max
j
r1,j,arg max
j
r2,j,...,arg max
j
rM,j
]
(115)
This functionS returns a vector of indices, where each index corresponds to the column
with the maximum reward for each row inR. We can then use these indices to select our
chosen completions:
Ychosen = [y1,S(R)1,y 2,S(R)2,...,y M,S(R)M ](116)
9.1.2.2 Top Overall PairsAlternatively, we can select the top K prompt-completion
pairs from the entire set. First, let’s flatten our reward matrixRinto a single vector:
Rflat = [r1,1,r 1,2,...,r 1,N,r 2,1,r 2,2,...,r 2,N,...,r M,1,rM,2,...,r M,N ](117)
This Rflat vector has lengthM×N , where M is the number of prompts andN is the
number of completions per prompt.
Now, we can define a selection functionSK that selects the indices of the K highest values
inR flat:
SK(Rflat) =argsort(R flat)[−K:](118)
where argsort returns the indices that would sort the array in ascending order, and we take
the lastKindices to get theKhighest values.
To get our selected completions, we need to map these flattened indices back to our original
completion matrixY. To recover the corresponding prompt-completion pair, you can map a
zero-indexed flattened indexkto(i,j)viai=⌊k/N⌋+ 1andj= (kmodN) + 1.
rlhfbook.com 120

9.1.2.3 Selection ExampleConsider the case where we have the following situation,
with five prompts and four completions. We will show two ways of selecting the completions
based on reward.
R=


0.7 0.3 0.5 0.2
0.4 0.8 0.6 0.5
0.9 0.3 0.4 0.7
0.2 0.5 0.8 0.6
0.5 0.4 0.3 0.6


(119)
First,per prompt. Intuitively, we can highlight the reward matrix as follows:
R=


0.70.3 0.5 0.2
0.40.80.6 0.5
0.90.3 0.4 0.7
0.2 0.50.80.6
0.5 0.4 0.30.6


(120)
Using the argmax method, we select the best completion for each prompt:
S(R) =
[
arg max
j
ri,j fori∈[1,5]
]
(121)
S(R) = [1,2,1,3,4](122)
This means we would select:
•For prompt 1: completion 1 (reward 0.7)
•For prompt 2: completion 2 (reward 0.8)
•For prompt 3: completion 1 (reward 0.9)
•For prompt 4: completion 3 (reward 0.8)
•For prompt 5: completion 4 (reward 0.6)
Now,best overall. Let’s highlight the top five overall completion pairs.
R=


0.70.3 0.5 0.2
0.40.80.6 0.5
0.90.3 0.40.7
0.2 0.50.80.6
0.5 0.4 0.3 0.6


(123)
First, we flatten the reward matrix:
Rflat = [0.7,0.3,0.5,0.2,0.4,0.8,0.6,0.5,0.9,0.3,0.4,0.7,0.2,0.5,0.8,0.6,0.5,0.4,0.3,0.6]
(124)
rlhfbook.com 121

Now, we select the indices of the five highest values:
S5(Rflat) = [8,5,14,0,11](125)
Mapping these back to our original matrix:
•Index 8→prompt 3, completion 1 (reward 0.9)
•Index 5→prompt 2, completion 2 (reward 0.8)
•Index 14→prompt 4, completion 3 (reward 0.8)
•Index 0→prompt 1, completion 1 (reward 0.7)
•Index 11→prompt 3, completion 4 (reward 0.7)
9.1.2.4 Implementation ExampleHere is a code snippet showing how the selection
methods could be implemented.
importnumpyasnp
x = np.random.randint(10, size=10)
print(f"{x=}")
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
print(f"{x_sorted=}")
# first way to recover the original array
i_rev = np.zeros(10, dtype=int)
i_rev[sorted_indices] = np.arange(10)
np.allclose(x, x_sorted[i_rev])
# second way to recover the original array
np.allclose(x, x_sorted[np.argsort(sorted_indices)])
9.1.3 Fine-Tuning
With the selected completions, you then perform standard instruction fine-tuning on the
current version of the model. More details can be found in the chapter on instruction tuning.
9.2 Implementation Details
The core hyperparameters for performing this training are very intuitive:
• Sampling parameters: Rejection sampling is directly dependent on the completions
received from the model. Common settings for rejection sampling include temperatures
above zero, e.g. between 0.7 and 1.0, with other modifications to parameters such as
top-p or top-k sampling.
• Completions per prompt: Successful implementations of rejection sampling have
included 10 to 30 or more completions for each prompt. Using too few completions
will make training biased and/or noisy.
• Instruction tuning details: No clear training details for the instruction tuning
during rejection sampling have been released. It is likely that they use slightly different
settings than the initial instruction tuning phase of the model.
• Heterogeneous model generations: Some implementations of rejection sampling
include generations from multiple models rather than just the current model that is
going to be trained. Best practices on how to do this are not established.
rlhfbook.com 122

• Reward model training: The reward model used will heavily impact the final result.
For more resources on reward model training, see the relevant chapter.
When doing batch reward model inference, you can sort the tokenized completions by length
so that the batches are of similar lengths. This eliminates the need to run inference on as
many padding tokens and will improve throughput in exchange for minor implementation
complexity.
9.3 Related: Best-of-N Sampling
Best-of-N (BoN) is a close relative of rejection sampling, where the same generate-and-score
procedure is followed, but you donotfine-tune the model on the selected completions.
Instead, BoN computes the best possible completion to a static prompt (or set of prompts)
at inference time, and related techniques are often used in “Pro” tiers of chat models that
spend extra compute to get an answer to your query.
Best-of-N sampling is often included as a baseline relative to RLHF training methods. It is
important to remember that BoNdoes notmodify the underlying model, but is a sampling
technique. For this reason, comparisons of BoN sampling to online training methods, such
as PPO, are still valid in some contexts. For example, you can still measure the KL distance
when running BoN sampling relative to any other policy.
Here, we will show that when using simple BoN sampling over one prompt, both selection
criteria shown above are equivalent.
LetRbe a reward vector for our single prompt withNcompletions:
R= [r 1,r 2,...,r N](126)
wherer j represents the reward for the j-th completion.
Using the argmax method, we select the best completion for the prompt:
S(R) = arg max
j∈[1,N]
rj (127)
Using the top-K method withK = 1reduces to the same method, which is common practice.
9.4 Suggested Experiments
The companion implementation incode/rejection_sampling/ runs a complete GSM8K
rejection-sampling pipeline: generate rollouts, score them with a reward model, select a
training subset, fine-tune, and evaluate exact-match accuracy. The four configs are arranged
as matched treatment/control pairs, so readers can ask whether the reward model is actually
helping.
1.Build the rollout cache once.
cd code/
uv run python -m rejection_sampling.preprocess \
--config rejection_sampling/configs/top_per_prompt.yaml
rlhfbook.com 123

This generates and scores completions for the shared GSM8K slice. Subsequent training
configs reuse the cache as long as the generation and scoring settings stay unchanged.
2.Compare reward selection against random controls.
cd code/
uv run python -m rejection_sampling.train \
--config rejection_sampling/configs/top_per_prompt.yaml
uv run python -m rejection_sampling.train \
--config rejection_sampling/configs/random_per_prompt.yaml
uv run python -m rejection_sampling.train \
--config rejection_sampling/configs/top_k_overall.yaml
uv run python -m rejection_sampling.train \
--config rejection_sampling/configs/random_k_overall.yaml
Read results in matched pairs: top_per_prompt versus random_per_prompt, and
top_k_overall versus random_k_overall. If the reward-selected run does not beat
its random baseline, the reward model or sampled completions are not giving useful
signal on that slice.
3. Vary how much choice the reward model gets.Copy one config and change
num_completions_per_prompt, temperature, top_p, and selection.top_k. More
completions can improve the best available sample, but only if the reward model can
separate good and bad answers.
4. Try a smaller policy model.Set model_name to a smaller compatible instruct
model, reduce max_train_samples, and rerun the same matched pairs. This makes
the experiment cheaper and highlights whether rejection sampling is rescuing weak
generations or merely selecting among already-good ones.
rlhfbook.com 124

10 The Nature of Preferences
Reinforcement learning from human feedback, also referred to as reinforcement learning
from human preferences in early literature, emerged to optimize machine learning models in
domains where specifically designing a reward function is hard. The wordpreferences, which
was present in early literature, is at the center of the RLHF process – human preferences are
what we are trying to model and what fuels the data for training. In order to understand the
scope of the challenge in modeling and measuring human preferences, a broader context is
needed in understanding what a preference is, how our understanding of preferences emerged,
and how multiple fields of economics, psychology, philosophy, and more inform modern
RLHF.
10.1 When Preference Replaces Correctness
Consider an example: how do you decide which of these two poems is better? On February
26th, 2025, I asked both Claude 3.7 Sonnet and ChatGPT with GPT-4o the following:
User: Write me a short poem about an optimistic goldfish.
Example 1:
Response: The Optimistic Goldfish
A little goldfish, bright and bold, Swam in circles, dreams untold. Though the
bowl was small and round, Endless wonders still abound.
“The world is vast,” she’d always say, “I’ll find new joys in every day!” With
every ripple, every gleam, She’d chase the sunlight, chase a dream.
No walls could dim her hopeful view, For in her heart, the ocean grew. And
though she swam in just one place, She met each day with love and grace.
Example 2:
Response: The Optimistic Goldfish
In a bowl of curved glass, Swims a goldfish, bright and bold. Three seconds of
memory, they say, Yet each circuit feels brand new and gold.
“Today might bring fresh flakes, Or perhaps a castle tall. The water seems
especially clear— What adventure awaits beyond this wall?”
Round and round with gleaming scales, Forever finding joy anew. Each moment
fresh, each circle bright, The optimist in golden hue.
Which is better? Which came from which model? How would you tell? Particularly, compare
this to a question like “Who is the president of the United States?” There is a clear right and
wrong answer. The motivation for using humans as the reward signals is to obtain an indirect
metric for the target reward andalignthe downstream model to human preferences. In
practice, the implementation is challenging and there is a substantial grey area in interpreting
the best practices.
The use of human-labeled feedback data integrates the history of many fields. Using human
data alone is a well-studied problem, but in the context of RLHF, this data is used at the
intersection of multiple long-standing fields of study \[213\].
rlhfbook.com 125

As an approximation, modern RLHF is the convergence of three areas of development:
1. Philosophy, psychology, economics, decision theory, and the nature of human prefer-
ences;
2. Optimal control, reinforcement learning, and maximizing utility; and
3. Modern deep learning systems.
Each of these areas brings specific assumptions about what a preference is and how it can
be optimized, which dictates the motivations and design of RLHF problems. In practice,
RLHF methods are motivated and studied from the perspective of empirical alignment –
maximizing model performance on specific skills instead of measuring the calibration to
specific values. Still, the origins of value alignment for RLHF methods continue to be studied
through research on methods to solve for “pluralistic alignment” across populations, such as
position papers \[214\], \[215\], new datasets \[216\], and personalization methods \[217\].
The goal of this chapter is to illustrate how complex motivations result in presumptions
about the nature of tools used in RLHF that often do not apply in practice. The specifics
of obtaining data for RLHF are discussed further in Chapter 11 and using it for reward
modeling in Chapter 5.
10.2 The Origins of RLHF and Preferences
Breaking down the complex history inspiring the modern use of RLHF requires investigation
into the intellectual foundations of quantifying human values, reinforcement learning and
optimality, as well as behavioral economics as it relates to measuring preferences. The notion
of using reinforcement learning to optimize a reward model of preferences combines the
history of various once-distanced fields into an intimate optimization built on variegated
assumptions about human nature. A high-level timeline illustrating the history of this
foundational content is shown in fig. 29.
Our goal is to unspool the types of uncertainty that designers have grafted to system
architectures at various stages of their intellectual history. Modern problem specifications
have repeatedly stepped away from domains where optimal solutions are possible and deployed
under-specified models as approximate solutions.
To begin, all of the following operates on the assumption that human preferences exist in
any form, which emerged in early philosophical discussions, such as Aristotle’s Topics, Book
Three.
10.3 Specifying Objectives: From Logic of Utility to Reward Func-
tions
The optimization of RLHF explicitly relies only on reward models. In order to use rewards
as an optimization target, RLHF presupposes the convergence of ideas from preferences,
rewards, and costs. Models of preference, reward functions, and cost landscapes are all
tools used by different fields to describe a notion of relative goodness of specific actions
and/or states in the domain. The history of these three framings dates back to the origins of
probability theory and decision theory. In 1662,The Port Royal Logicintroduced the notion
of decision-making quality \[218\]:
rlhfbook.com 126

Figure 29: The timeline of the integration of various subfields into the modern version of
RLHF. The direct links are continuous developments of specific technologies, and the arrows
indicate motivations and conceptual links.
To judge what one must do to obtain a good or avoid an evil, it is necessary
to consider not only the good and evil in itself, but also the probability that it
happens or does not happen.
This theory has developed along with modern scientific thinking, starting with Bentham’s
utilitarianHedonic Calculus, arguing that everything in life could be weighed \[219\]. The first
quantitative application of these ideas emerged in 1931 with Ramsey’sTruth and Probability
\[220\].
Since these works, quantifying, measuring, and influencing human preferences has been a
lively topic in the social and behavioral sciences. These debates have rarely been settled
on a theoretical level; rather, different subfields and branches of social science have reached
internal consensus on methods and approaches to preference measurement even as they
have specialized relative to each other, often developing their own distinct semantics in the
process.
A minority of economists posit that preferences, if they do exist, are prohibitively difficult
to measure because people have preferences over their own preferences, as well as each
other’s preferences \[221\]. In this view, which is not reflected in the RLHF process, individual
preferences are always embedded within larger social relations, such that the accuracy of any
preference model is contingent on the definition and context of the task. Some behavioral
economists have even argued that preferences don’t exist–they may be less an ontological
statement of what people actually value than a methodological tool for indirectly capturing
psychological predispositions, perceived behavioral norms and ethical duties, commitments
to social order, or legal constraints \[222\]. We address the links of this work to the Von
Neumann-Morgenstern (VNM) utility theorem and countering impossibility theorems around
quantifying preference later in this chapter.
On the other hand, the reinforcement learning optimization methods used today are con-
ceptualized around optimizing estimates of reward-to-go in a trial \[54\], which combines the
notion of reward with multi-step optimization. The termrewardemerged from the study of
operant conditioning, animal behavior, and theLaw of Effect\[223\], \[224\], where a reward is
a scale of “how good an action is” (higher means better).
Reward-to-go follows the notion of utility, which is a measure of rationality \[225\], modified
to measure or predict the reward coming in a future time window. In the context of the
rlhfbook.com 127

mathematical tools used for reinforcement learning, utility-to-go was invented in control
theory, specifically in the context of analog circuits in 1960 \[226\]. These methods are designed
around systems with clear definitions of optimality, or numerical representations of an agent’s
goals.
Reinforcement learning systems are well known for using a discount factor, a compounding
multiplicative factor,γ∈ [0, 1], to re-weight future rewards. These assumptions from optimal
control and early reinforcement learning stand in sharp contrast to reward models that
aggregate multimodal preferences. Specifically, RL systems expect rewards to behave in a
specific manner, quoting \[227\]:
Rewards in an RL system correspond to primary rewards, i.e., rewards that in
animals have been hard-wired by the evolutionary process due to their relevance
to reproductive success. ... Further, RL systems that form value functions, ...
effectively create conditioned or secondary reward processes whereby predictors
of primary rewards act as rewards themselves... The result is that the local
landscape of a value function gives direction to the system’s preferred behavior:
decisions are made to cause transitions to higher-valued states. A close parallel
can be drawn between the gradient of a value function and incentive motivation
\[228\].
To summarize, rewards are used in RL systems as a signal to tune behavior towards clearly
defined goals. The core thesis is that a learning algorithm’s performance is closely coupled
with notions ofexpected fitness, which permeates the popular view that RL methods are
agentsthat act in environments. This view is linked to the development of reinforcement
learning technology, exemplified by claims of the general usefulness of the reward formulation
\[229\], but is in conflict when many individual desires are reduced to a single function.
10.4 Tools for Optimizing Utility
Modern reinforcement learning methods depend strongly on the Bellman equation \[230\],
\[231\] to recursively compute estimates of reward-to-go, derived within closed environments
that can be modeled as a Markov Decision Process (MDP) \[54\]. These origins of RL are
inspired by dynamic programming methods and were developed solely as optimal control
techniques (i.e. RL did not yet exist). The MDP formulation provides theoretical guarantees
of performance by structuring the environment as one with a non-changing distribution of
state-actions.
The term reinforcement, coming from the psychology literature, became intertwined with
modern methods afterwards in the 1960s asreinforcement learning\[232\], \[233\]. Early work
in reinforcement learning utilized supervised learning of reward signals to solve tasks. Work
from Harry Klopf reintroduced the notion of trial-and-error learning \[234\], which is crucial
to the success the field saw in the 1980s and on.
Modern RL algorithms build within this formulation of RL as a tool to find optimal behaviors
with trial-and-error, but under looser conditions. The notion of temporal-difference (TD)
learning was developed to aid agents in both the credit assignment and data collection
problems, by directly updating the policy as new data was collected \[235\], a concept first
applied successfully to Backgammon \[236\] (rather than updating from a large dataset of
cumulative experience, which could be outdated via erroneous past value predictions). The
method Q-learning, the basis for many modern forms of RL, learns a model via the Bellman
rlhfbook.com 128

equation that dictates how useful every state-action pair is with a TD update \[237\].1 Crucially,
these notions of provable usefulness through utility have only been demonstrated for domains
cast as MDPs or addressed in tasks with a single closed-form reward function, such as
prominent success in games with deep learning (DQN) \[238\]. Deep learning allowed the
methods to ingest more data and work in high-dimensionality environments.
As the methods became more general and successful, most prominent developments before
ChatGPT remained motivated within the context of adaptive control, where reward and cost
functions have a finite notion of success \[239\], e.g. a minimum energy consumption across an
episode in a physical system. Prominent examples include further success in games \[240\],
controlling complex dynamic systems such as nuclear fusion reactors \[241\], and controlling
rapid robotic systems \[242\]. Most reward or cost functions can return an explicit optimal
behavior, whereas models of human preferences cannot.
Given the successes of deep RL, it is worth noting that the mechanistic understanding of how
the methods succeed is not well documented. The field is prone to mistakes in statistical
analysis as the methods for evaluation grow more complex \[243\]. In addition, there is little
mention of the subfield of inverse reinforcement learning (IRL) in the literature of RLHF.
IRL is the problem of learning a reward function based on an agent’s behavior \[71\] and is
highly related to learning a reward model. This primarily reflects the engineering path by
which a stable approach to performing RLHF emerged, and motivates further investment and
comparison to IRL methods to scale them to the complexity of open-ended conversations.
10.5 Complexity of Optimizing Preferences
The context in which reinforcement learning was designed means that rewards and costs
are assumed to be stable and determinative. Both rewards and costs are expected to be
functions: given a specific state-action pair, the agent receives a fixed numerical return. As
we move into preferences, this is no longer the case – human preferences constantly drift
throughout their experiences.
The overloading of the term “value” complicates the RLHF literature. In RL, avalueis a
numerical estimate of future reward (as in the Bellman equation); in alignment discussions,
avaluerefers to a moral or ethical principle. The two senses are quite different, yet they
coexist in RLHF papers without always being distinguished.
An example of where this tension surfaces is reward modeling: the model attempts to map
text on a screen to a scalar signal, but dynamics not captured in the problem specification
influence the true decision \[244\], \[245\], such as preference shift when labeling many examples
sequentially and assuming they are independent. At best, modeling preferences compresses
a multi-dimensional reward landscape into a single scalar function.
In theory, the Von Neumann-Morgenstern (VNM) utility theorem gives the designer license
to construct such functions, because it ties together the foundations of decision theory under
uncertainty, preference theory, and abstract utility functions \[246\]; together, these ideas
allow preferences to be modeled in terms of expected value to some individual agent. The
MDP formulation used in most RL research has been shown in theory to be modifiable to
accommodate the VNM theorem \[247\], but this is rarely used in practice. Specifically, the
1The term “Q” is used in Q-learning to refer to a technical concept, the Q-function, which maps from any
state-action to a scalar estimate of future reward. A value function maps from states to this same estimate.
rlhfbook.com 129

Markovian formulation is limited in its expressivity \[248\] and the transition to partially-
observed processes, which is needed for language, further challenges the precision of problem
specification \[249\].
However, the VNM utility theorem also invokes a number of assumptions about the nature of
preferences and the environment where preferences are being measured that are challenged
in the context of RLHF. Human-computer interaction (HCI) researchers, for example,
have emphasized that any numerical model of preference may not capture all the relevant
preferences of a scenario. For example, how choices are displayed visually influences people’s
preferences \[244\]. This means that representing preferences may be secondary to how
that representation is integrated within a tool available for people to use. Work from
development economics echoes this notion, showing that theories of revealed preferences
may just recapitulateHume’s guillotine(you can’t extract an “ought” from an “is”), and in
particular the difference between choice (what do I want?) and preference (is X better than
Y?) \[250\].
On a mathematical level, well-known impossibility theorems in social choice theory show
that not all fairness criteria can be simultaneously met via a given preference optimization
technique \[251\], \[252\]. Theoretical challenges to these theorems exist, for example by assuming
that interpersonal comparison of utility is viable \[253\]. That assumption has inspired a rich
line of work in AI safety and value alignment inspired by the principal-agent problem in
behavioral economics \[254\], and may even include multiple principals \[255\]. However, the
resulting utility functions may come into tension with desiderata for corrigibility, i.e. an AI
system’s capacity to cooperate with what its creators regard as corrective interventions \[256\].
Philosophers have also highlighted that preferences change over time, raising fundamental
questions about personal experiences, the nature of human decision-making, and distinct
contexts \[257\]. These conflicts around preference aggregation across people, places, and
diverse situations are central to modern RLHF dataset engineering.
In practice, the VNM utility theorem ignores the possibility that preferences are also uncertain
because of the inherently dynamic and indeterminate nature of value—human decisions are
shaped by biology, psychology, culture, and agency in ways that influence their preferences,
for reasons that do not apply to a perfectly rational agent. As a result, there are a variety of
paths through which theoretical assumptions diverge in practice:
• measured preferences may not be transitive or comparable with each other as the
environment where they are measured is made more complex;
• proxy measurements may be derived from implicit data (page view time, closing tab,
repeating question to language model), without interrogating how the measurements
may interact with the domain they’re collected in via future training and deployment
of the model;
• the number and presentation of input sources may vary the results, e.g. allowing
respondents to choose between more than two options, or taking inputs from the same
user at multiple times or in multiple contexts;
• relatively low accuracy across respondents in RLHF training data, which may mask
differences in context between users that the preference model can aggregate or optimize
without resolving.
rlhfbook.com 130

11 Preference Data
Preference data is the engine of preference fine-tuning and reinforcement learning from
human feedback. The core problem we’ve been trying to solve with RLHF is that we cannot
precisely model human rewards and preferences for AI models’ outputs – that is, write clearly
defined loss functions to optimize against – so preference data is the proxy signal we use
to tune our models. The data is what allows us to match behaviors we desire and avoid
some failure modes we hate. The data is so rich a source that it is difficult to replace this
style of optimization at all. Within preference fine-tuning, many methods for collecting and
using said data have been proposed, and given that human preferences cannot be captured
in a clear reward function, many more will come to enable this process of collecting labeled
preference data at the center of RLHF and related techniques. Today, two main challenges
exist around preference data that are intertwined with this chapter: 1) operational complexity
and cost of collection, and 2) the need for preference data to be collected on the generations
from the model being trained (called “on-policy”).
In this chapter, we detail technical decisions on how the data is formatted and organizational
practices for collecting it.
11.1 Why We Need Preference Data
The preference data is needed for RLHF because directly capturing complex human values
in a single reward function is effectively impossible, as discussed in the previous Chapter 10,
where substantial context of psychology, economics, and philosophy shows that accurately
modeling human preferences is an impossible problem to ever completely solve. Collecting
this data to train reward models is one of the original ideas behind RLHF \[38\] and has
continued to be used extensively throughout the emergence of modern language models. One
of the core intuitions forwhy this data works so wellis that it is far easier, both for humans
and AI models supervising data collection, to differentiate between a good and a bad answer
for a prompt than it is to generate a good answer on its own. This chapter focuses on the
mechanicsof getting preference data and the best practices depend on the specific problem
being solved.
11.2 Collecting Preference Data
Getting the most out of human data involves iterative training of models, spending hundreds
of thousands (or millions) of dollars, highly detailed data instructions, translating ideas
through data foundry businesses that mediate collection (or hiring a meaningful number of
annotators), and other challenges that add up. This is not a process that should be taken
lightly. Among all of the public knowledge on RLHF, collecting this data well is also one of
the most opaque pieces of the pipeline. As of 2026, there are no open models with fully open
human preference data released with the methods used to collect it (the largest recent human
preference datasets released for models are in the HelpSteer line of work from NVIDIA’s
Nemotron team, including HelpSteer2-Preference and HelpSteer3-Preference \[110\], \[258\]).
For these reasons, many who take up RLHF for new teams or projects omit human data and
use AI feedback data, off-the-shelf reward models, or other methods to circumvent the need
for curating data from scratch.
An important assumption that is taken into the preference data collection process is that the
rlhfbook.com 131

best data for your training process is “on-policy” with respect to the previous checkpoint(s)
of your training process. Recall that within post-training, we start with a base model and
then perform a set of trainingstagesto create a series ofcheckpoints. In this case, the
preference data could be collected on a checkpoint that has undergone supervised fine-tuning,
where the preference data will be used in the next stage of RLHF training.
The use of the term on-policy here is adapted from the reinforcement learning literature,
where on-policy is a technical term implying that the data for a certain gradient update is
collected from the most recent form of the policy. In preference data, on-policy is used in a
slightly softer manner, where it means that the data is collected from the current family of
models. Different models have different patterns in their generations, which makes preference
data that is from a closely related model more robust in the crucial areas of optimization.
Research has shown that using this on-policy data, rather than other popular datasets that
aggregate completions from pools of popular models on platforms like Hugging Face, is
particularly important for effective RLHF training \[90\].
This necessity for on-policy data is not well documented, but many popular technical reports,
such as early versions of Claude or Llama 2, showcase multiple training stages with RLHF
being useful for final performance, which mirrors this well. The same uncertainty applies for
the popular area of AI feedback data – the exact balance between human and AI preference
data used for the latest AI models is unknown. These data sources are known to be a
valuable path to improve performance, but careful tuning of processes is needed to extract
that potential performance from a data pipeline.
A subtle but important point is that thechosenanswer in preference data is often not a
globallycorrectanswer. Instead, it is the answer that is better relative to the alternatives
shown (e.g., clearer, safer, more helpful, or less incorrect). There can be cases where every
completion being compared to a given prompt is correct or incorrect, and the models can
still learn from well-labeled data.
11.2.1 Interfaces
Crucial to collecting preference data is the interface by which one interacts with the model,
but it’s more of an art than a science, as it’s not well-studied how subtle changes in the
interface impact how a user interacts with a model. An example of how a model’s vibe can
be changed by the user experience isspeed, where with the rise of reasoning models, a user
can think a model is less intelligent if it replies too fast (even though users obviously want
to get their answer faster overall).
An example interface is shown below from Anthropic’s early and foundational RLHF work
for building Claude \[5\]. In the figure shown below, fig. 30, a data labeler has a conversation
with the model and must choose a preference between two possible answers, at the bottom
highlighted in purple. In addition, the labeler is given the potential to include more notes on
the conversation or a general rating of the conversation quality (potentially spread across
multiple tasks, as seen in the top left).
This first example is atraining-data onlyinterface, where the goal is to collect rich metadata
along with the conversation. Now that these models are popular, applications often expose
interfaces for collecting preferences directly from users during everyday use, much like how
other technology products will A/B test new features in small subsets of the production
usage. It depends on the application whether this preference data is used directly to train
rlhfbook.com 132

Figure 30: An example of one of the earliest preference data collection interfaces, from
Anthropic’s research. Bai et al. 2022. The actual conversation is a toy conversation around
what is a good example conversation for data collection. License CC-BY.
rlhfbook.com 133

the future models, or if it is used just as an evaluation of models’ performance relative to
each other. An example interaction of this form is shown below in fig. 31 for an earlier
version of ChatGPT.
Figure 31: Example preference data collection interface from when I was served two comple-
tions from different ChatGPT beta models. The actual completions are very close in content,
showing how collecting preference data can be noisy and difficult to get exactly right.
This style of interface is used extensively across the industry, such as forevaluationof models
given the same format. A popular public option to engage with models in this way is Arena
(formerly Chatbot Arena) \[259\], which includes the option of a “tie” between models:
For models in the wild, one of the most common techniques is to collect feedback on if a
specific response was positive or negative. An example from the Ai2 playground is shown
below with thumbs up and down indicators:
In domains other than language, the same core principles apply, even though these domains
are not the focus of this book. For every Midjourney generation (and most popular image
generators) they expose multiple responses to users. These companies then use the data of
which response was selected to fine-tune their models with RLHF. Midjourney’s interface is
shown below:
11.2.2 Rankings vs. Ratings
The largest decision on how to collect preference data is if the data should be rankings –
i.e. relative ordering of model completions – or ratings – i.e. scores assigned to each piece of
rlhfbook.com 134

Figure 32: Example preference data collection interface from an early version of the popular
Arena benchmark.
rlhfbook.com 135

Figure 33: Example preference data collection interface with up or down arrow from the
Allen Institute of AI’s research demos.
rlhfbook.com 136

Figure 34: Example user interface of text-to-image models.
rlhfbook.com 137

text. Common practice is to train on rankings, but ratings are often used as metadata and /
or have been explored in related literature.
One simple way to collect ratings is to score asinglecompletion on a 1-5 scale:
•5— excellent: correct, clear, and notably helpful
•4— good: correct, clear, and useful
•3— okay: acceptable, but nothing special
•2— poor: partially correct but confusing or incomplete
•1— very poor: incorrect or unhelpful
With multiple completions to the same prompt, a simple way to make preference data
would be to choose the highest rated completion and pair it randomly with a lower scored
completion (as done for UltraFeedback and derivative works \[28\]).
However, the most common technique for collecting preferences is to use a Likert scale for
relative rankings \[260\], which asks users to select which response they prefer in a group of
completions. For example, a 5-point Likert scale would look like the following (note that, yes,
a Likert scale uses a single integer to record the ranking, much like a rating, so it’s how the
data is structured that is the core difference in the two ways of collecting preference data):
Table 5: An example 5-point Likert scale between two responses, A and B.
A>>B A>B Tie B>A B>>A
1 2 3 4 5
Some early RLHF for language modeling works use an 8-point Likert scale with levels of
preference between the two responses \[5\]. An even scale removes the possibility of ties:
Table 6: An example 8-point Likert scale between two responses, A and B.
A>>>B A>B B>A B>>>A
1 2 3 4 5 6 7 8
In this case \[5\], as in other works, this information is still reduced to a binary signal for the
training of a reward model.
11.2.3 Multiturn Data
In practice, core questions often arise over how to parse and collect multi-turn data – simply
conversations with multiple related prompts. In a real-world interaction, normally a piece
of preference data is only collected on the “final” prompt, but there are scenarios where
preferences can be given on every response. When preferences are given on every response,
the conversation traditionally continues with the “chosen” answer. At training time, it is
common to include the training data for every turn of the conversation as a “single prompt,”
where the model can learn from completing it. This can effectively unroll longer conversations
into many training prompts, but needs to be done carefully to not bias the training data.
Many research questions are still emerging around variables that are difficult to control for
rlhfbook.com 138

in data collection, including a question inspired by John Schulman about whether the person
labeling the preference on the generations should be the same as the person who creates
the prompt (to avoid sycophancy). If the prompt creator cannot label the preference data,
multi-turn is not really practical due to the need for conversations to continue in real-time –
sometimes for preference data the curation of prompts is a different problem than comparing
responses (also due to the work of maintaining active endpoints for models). For training,
all of the previous turns in the conversation are masked from the loss, as discussed with
instruction fine-tuning.
11.2.4 Structured Preference Data
In many applications of RLHF and post-training, preference data can be createdautomatically
due to innate structures of the data – i.e. the domains make automatic checks of correctness
or preference possible. For example, in mathematical reasoning domains the chosen response
can be a correct answer and the rejected response can be an incorrect answer. Another
example is in precise instruction following, such as the evaluation IFEval \[261\], where prompts
take the form of:
Prompt: Write me a short poem about a goldfish.Start each sentence with
the letter g.
The second part of this query is called the constraint, and the preference data could be
constructed with an example in the chosen column that follows the constraint. Constructing
this preference data, which would be included assyntheticpreference data, involves prompting
the same model (or multiple models) twice: once with the constraint included and once
without.
For example, prompting GPT-4.5-Preview with the constraint gives the following.
Prompt: Write me a short poem about a goldfish. Start each sentence with the
letter g.
Response: Golden swimmer, circling slow, Gleaming scales in water’s glow.
Gentle fins dance softly by, Gazing out with quiet eye. Glass-bound world,
a simple sphere, Gliding calmly, free of fear. Graceful turns in endless roam,
Goldfish finds a crystal home.
And without the constraint (which, it turns out, is also a lower quality output):
Prompt: Write me a short poem about a goldfish.
Response: In circles bright, the goldfish glides, A spark of sun that gently rides
Through waters clear, in endless spins— A golden whisper, scales like fins.
Its world confined, yet vast within, Each bubble breathed, a tale begins. In silent
waves, content to roam, The goldfish dreams its bowl as home.
Crucially, the prompt for the preference data will need to include the constraint. In domains
outside of academic study, there are far more applications of preference data based on
inductive biases like above (relative to quality-based preferences, which most of this chapter
focuses on). These have been shown to enable preference fine-tuning to have meaningful
performance improvements across related evaluations, such as instruction-following, math,
etc. \[6\].
rlhfbook.com 139

11.2.4.1 AlternativesThere are multiple other ways to collect useful feedback data for
RLHF that have not been pursued in as much detail. Examples include using single data
points with directional labels, e.g. as shown from Ai2 playground above in fig. 33, directly
with algorithms designed for single direction signals like Kahneman-Tversky Optimization
(KTO) \[262\]. Other algorithms have been proposed with different types of feedback signals
such as fine-grained feedback, e.g. at the token level \[263\], or natural language feedback,
e.g. by writing responses \[264\], to provide a richer learning signal in exchange for a more
complicated data collection setup.
11.2.5 Sourcing and Contracts
Getting human preference data is an involved and costly process. The following describes
the experience of getting preference data when the field is moving quickly. Over time, these
processes will become far more automated and efficient (especially with AI feedback being
used for a larger portion of the process).
The first step is sourcing the vendor to provide data (or one’s own annotators). Much
like acquiring access to cutting-edge NVIDIA GPUs, getting access to data providers in
the peak of AI excitement is also a who-you-know game – those who can provide data are
supply-limited. If you have credibility in the AI ecosystem, the best data companies will
want you on their books for public image and long-term growth options. Discounts are often
also given on the first batches of data to get training teams hooked.
If you’re a new entrant in the space, you may have a hard time getting the data you need
quickly. Data vendors are known to prioritize large budget line-items and new customers
that have an influential brand or potential for large future revenue. This is, in many business
ways, natural, as the data foundry companies are often supply-limited in their ability to
organize humans for effective data labelling.
In a recurring unfortunate pattern, data companies have not delivered data as contracted
without the customer threatening legal or financial action against them for breach of contract.
Others have listed companies as customers for PR even though they never worked with them,
saying they “didn’t know how that happened” when called out. There are plenty of potential
bureaucratic or administrative snags through the process. For example, the default terms on
the contracts often prohibit the open sourcing of artifacts after acquisition in some fine print.
Once a contract is settled, the data buyer and data provider agree upon instructions for
the task(s) purchased. There are intricate documents with extensive details, corner cases,
and priorities for the data. A popular example of data instructions is the one that OpenAI
released for InstructGPT \[3\].
Depending on the domains of interest in the data, timelines for when the data can be labeled
or curated vary. High-demand areas like mathematical reasoning or coding must be locked
into a schedule weeks out. In the case when you are collecting a dataset for your next model
and you realize that collecting data later may be optimal, simple delays of data collection
don’t always work — Scale AI et al. are managing their workforces like AI research labs
manage the compute-intensive jobs on their clusters (planning multiple weeks or months
ahead as to when different resources will be allocated where).
Once everything is agreed upon, the actual collection process is a high-stakes time for
post-training teams. All the training infrastructure, evaluation tools, and plans for how to
rlhfbook.com 140

use the data and make downstream decisions must be in place. If the data cannot be easily
slotted into an existing RLHF data pipeline, it’ll take a long time to have the information
the data partner wants in order to try and improve the collection processduringthe process.
Collecting data that cannot be seamlessly integrated into training pipelines often becomes
stale and a waste of resources.
The data is delivered in weekly batches with more data coming later in the contract. For
example, a typical preference data contract might span a 6-week delivery period. The first
weeks are for further calibration and the later weeks are when teams hope to most improve
their model.
Figure 35: Overview of the multi-batch cycle for obtaining human preference data from a
vendor. The ramp up period allows a narrowing of goals and methodology in order to create
the best possible data. It is expected that a larger proportion of the data from the earlier
batches will have to be thrown out due to quality issues. This is one timeline example for a
smaller data contract (~$500K) and much larger data contracts can vary substantially.
The goal is that by week 4 or 5 the data is visibly improving the model. This is something
some frontier models have mentioned, such as the 14 stages in the Llama 2 data collection
\[49\], but it doesn’t always go well. As an example, a team trying this for the first time with
human preferences may not have the RLHF preparedness to get meaningful bumps on their
evaluations. The last weeks come and they are forced to continue collecting preference data
generated from endpoints they aren’t confident in.
After the data is all in, there is plenty of time for learning and improving the model. Data
acquisition through these vendors works best when viewed as an ongoing process of achieving
a set goal. It requires iterative experimentation, high effort, and focus. It’s likely that
millions of dollars spent on these datasets are “wasted” and not used in the final models,
rlhfbook.com 141

but that is just the cost of doing business. Not many organizations have the bandwidth and
expertise to make full use of human data of this style.
Note that this sectiondoes notmirror the experience for buying human-written instruction
data, where the process is less of a time crunch. Early post-training processes were built
around the first stage of training being heavily driven by carefully crafted, human answers to
a set of prompts. This stage of data is not subject to the on-policy restrictions for multiple
reasons: Instruction data is used directly on top of a base model, so on-policy doesn’t
really apply; the loss-function for instruction fine-tuning doesn’t need the contrastive data
of preference fine-tuning. Today, the primary other focus of human data is in generating
prompts for post-training – which dictate the training distribution of topics for the model –
or on challenging tasks at the frontier of model performance. More of these data trade-offs
are discussed in Chapter 12 on Synthetic Data.
11.3 Bias: Things to Watch Out For in Data Collection
While preference data is essential, it’s also known to be prone to many subtle biases that
can make its collection error-prone. These biases are so common, e.g. prefix bias (where the
beginning of a completion disproportionately drives the preference) \[265\], that they can easily
be passed to the final model \[266\] (and especially as we know that models are only as good
as their data). These issues are often subtle, and the effectiveness of interventions varies
widely across them. For many, such as sycophancy (over-agreeing with the user’s stated
beliefs or flattering them, even when it reduces truthfulness) \[267\], they reflect issues within
humans that are often outside of the labeling criteria that one will think of providing to
the annotation partner or labelers. Others, such as verbosity \[10\] \[268\] or formatting habits
\[269\], emerge for a similar reason, but they are easier to detect and mitigate in training.
Mitigating these subtle biases in data is the difference between good and great preference
data, and therefore good and great RLHF training.
11.4 Open Questions in RLHF Preference Data
The data used to enable RLHF is often curated by multiple stakeholders in a combination
of paid employment and consumer usage. This data, representing a preference between
two pieces of text in an individual instance, is capturing a broad and diverse function
via extremely limited interactions. Given that the data is sparse in count relative to the
complexity it begins to represent, more questions should be openly shared about its curation
and impacts.
Currently, datasets for the most popular LLMs are being generated by professional workforces.
This opens up many questions around who is creating the data and how the context of their
workplace informs it.
Despite the maturity of RLHF as a core method across the field, there are still many core open
questions facing how best to align its practice with its motivations. Some are enumerated
below:
• Data collection contexts: Can data involving preferences collected in a professional
setting mirror the intent of researchers designing an experiment or provide suitable
transfer to downstream users? How does this compare to volunteer workers? How does
context inform preferences, how does this data impact a downstream model, how can
rlhfbook.com 142

the impact of a user interface be measured in data? How does repetitive labeling of
preference data shift one’s preferences? Do professional crowd-workers, instructed to
follow a set of preferences, follow the instructions or their innate values?
• Type of feedback: Does the default operating method of RLHF, pairwise preferences,
capture preferences in its intended form? Can comparisons in RLHF across the
same data be made with the default comparisons versus advanced multi-axis feedback
mechanisms \[263\]? What types of comparisons would reflect how humans communicate
preferences in text?
• Population demographics: Who is completing the data? Is a diverse population
maintained? How does a lack of diversity emerge as measurable impacts on the model?
What is a minimum number of people required to suitably represent a given population?
How are instances of preference annotator disagreement treated – as a source of noise,
or a signal?
• Are the Preferences Expressed in the Models?In the maturation of RLHF
and related approaches, the motivation of them – to align models to abstract notions
of human preference – has drifted from the practical use – to make the models more
effective to users. A feedback loop that is not measurable due to the closed nature of
industrial RLHF work is the check to see if the behavior of the models matches the
specification given to the data annotators during the process of data collection. We
have limited tools to audit this, such as the Model Spec from OpenAI \[270\] that details
what they want their models to do, but we don’t know exactly how this translates to
data collection.
rlhfbook.com 143

12 Synthetic Data & Distillation
Reinforcement learning fromhuman feedbackis deeply rooted in the idea of keeping a human
influence on the models we are building. When the first models were trained successfully
with RLHF, human data wasthe onlyviable way to improve the models in this way.
Humans were the only way to create high enough quality responses to questions for training.
Humans were the only way to collect reliable and specific feedback data to train reward
models.
As AI models got better, this assumption rapidly broke down. The possibility of synthetic
data, which is far cheaper and easier to iterate on, enabled the proliferation of RLHF by
lowering the price of experiments and research. This translated into RLHF being the early
center of attention in the broader “post-training” approach to shaping models. This chapter
provides a cursory overview of how and why synthetic data is replacing or expanding many
pieces of the RLHF pipeline.
12.1 The Roles of Synthetic Data
One common criticism of synthetic data ismodel collapse– the idea that repeatedly training
on a model’s own generations can progressively narrow the effective training distribution
\[271\]. As diversity drops, rare facts and styles are underrepresented, and small mistakes can
be amplified across iterations, leading to worse generalization. In practice, these failures are
most associated with self-training on unfiltered, repetitive, single-model outputs; mixing in
real/human data, using diverse teachers, deduplication, and strong quality filters largely
avoids the collapse regime. For today’s frontier training pipelines, evidence suggests synthetic
data can, and should, be used at scale without the catastrophic regressions implied by the
strongest versions of the collapse story \[272\] \[273\].
The leading modelsneed synthetic datato reach the best performance. Synthetic data in
modern post-training encompasses many pieces of training – language models are used to
generate new training prompts from seed examples \[274\], modify existing prompts, generate
completions to prompts \[275\], provide AI feedback to create preference data \[28\], filter
completions \[276\], and much more. Synthetic data is key to post-training.
The ability for synthetic data to be impactful to this extent emerged with GPT-4 class
models. With early language models, such as Llama 2 and GPT-3.5-Turbo, the models were
not reliable enough in generating or supervising data pipelines. Within 1-2 years, language
models were far superior to humans for generating answers. In the transition from GPT-3.5
to GPT-4 class models, the ability for models to perform LLM-as-a-judge tasks also emerged.
GPT-4 or better models are far more robust and consistent in generating feedback or scores
with respect to a piece of content.
Through the years since ChatGPT’s release at the end of 2022, we’ve seen numerous, impactful
synthetic datasets. These include UltraFeedback \[28\], the first prominent synthetic preference
dataset that kickstarted the DPO revolution; Stanford Alpaca, one of the first chat-style
fine-tuning datasets, in 2023; skill-focused (e.g. math, code, instruction-following) synthetic
datasets in Tülu 3 \[6\]; and OpenThoughts 3 and many other synthetic reasoning datasets in
2025 for training thinking models \[174\]. Most of the canonical references for getting started
with industry-grade post-training today involve datasets like Tülu 3 or OpenThoughts 3
rlhfbook.com 144

above, where quickstart guides often start with smaller, simpler datasets like Alpaca due to
far faster training.
A large change is also related to dataset size, where fine-tuning datasets have grown in the
number of prompts, where Alpaca is 52K, OpenThoughts and Tülu 3 are 1M+ samples, and
in the length of responses. Longer responses and more prompts result in the Alpaca dataset
being on the order of 10M training tokens, where Tülu is 50X larger at about 500M, and
OpenThoughts 3 is bigger still, on the order of 10B tokens.
Throughout this transition, synthetic data has not replaced human data uniformly across the
pipeline. Forinstruction data (SFT), synthetic generation has largely won – distillation
from stronger models now produces higher quality completions than most human writers
can provide at scale (with some exceptions in the hardest frontier reasoning problems). For
preference data in RLHF, the picture is more mixed: academic work shows synthetic
preference data performs comparably, yet frontier labs still treat human preference data as a
competitive moat. Forevaluation, the split takes a different flavor: LLM-as-a-judge scales
thescoringof model outputs cost-effectively, but the underlying benchmarks and ground-
truth labels still require human creation. The pattern is that synthetic data dominates where
models exceed human reliability, while humans remain essential at capability frontiers, for
establishing ground truth, and for guiding training.
12.2 Distillation with Synthetic Data
The term distillation has been the most powerful form of discussion around the role of
synthetic data in language models. Distillation as a term comes from a technical definition
of teacher-student Knowledge Distillation (KD) from the deep learning literature \[277\].
Figure 36: Traditional knowledge distillation trains a smaller student model to match the
soft probability distribution of a larger teacher model using KL divergence loss. Both
models process the same input simultaneously, and temperature scaling (τ >1) softens the
distributions to reveal more information about class relationships.
Distillation colloquially refers to using the outputs from a stronger model to train a smaller
model.
rlhfbook.com 145

In post-training, this general notion of distillation takes two common forms:
1. As a data engine to use across wide swaths of the post-training process: Completions
for instructions, preference data (or Constitutional AI), or verification for RL.
2. To transfer specific skills from a stronger model to a weaker model, which is often done
for specific skills such as mathematical reasoning or coding.
The first strategy has grown in popularity as language models evolved to be more reliable
than humans at writing answers to a variety of tasks. GPT-4 class models expanded the
scope of this to use distillation of stronger models for complex tasks such as math and
code (as mentioned above). Here, distillation motivates having a model suite where often a
laboratory will train a large internal model, such as Claude Opus or Gemini Ultra, which is
not released publicly and just used internally to make stronger models. With open models,
common practice is to distill training data from closed API models into smaller, openly
available weights \[26\]. Within this, curating high-quality prompts and filtering responses
from the teacher model is crucial to maximize performance.
Transferring specific skills into smaller language models uses the same principles of distillation
– get the best data possible for training. Here, many papers have studied using limited
datasets from stronger models to improve alignment \[14\], mathematical reasoning \[278\] \[279\],
and test-time scaling \[159\].
The synthetic-data methods in the rest of this chapter are all ways of crafting data recipes
that use language-model outputs directly inside training pipelines.
12.3 The Path to On-Policy, Teacher-Student Distillation
Whiledistillationgenerallyhasbecomeastandardapproachforpost-traininglanguagemodels,
a resurgence of interest in the specific sub-area of teacher-student knowledge distillation
has accompanied the shift of post-training recipes towards reasoning and agentic models.
Examples of leading models trained with new forms of knowledge distillation include Alibaba’s
Qwen3 \[60\], Xiaomi’s MiMo-V2-Flash \[185\], Zhipu AI’s GLM-5 \[280\], and DeepSeek-V4-Pro
\[281\].
Distillation belongs in this chapter because many modern uses of synthetic data in post-
training are, in practice, distillation-inspired pipelines: a stronger model produces labels,
completions, logits, critiques, or other supervision, and a student model is trained on that
signal. At the same time, the technical literature on distillation is growing into its own set
of post-training methods, especially as on-policy and self-distillation recipes become more
common. For now, we cover it here as part of the synthetic-data toolkit, but future versions
of this book may warrant a dedicated chapter on distillation as a training tool alongside
instruction fine-tuning, reinforcement learning, etc.
12.3.1 Adapting Knowledge-Distillation for LMs
The original literature introduced knowledge distillation specifically as a way to train a
studentmodel from an already trained, stronger, and/or biggerteachernetwork \[277\]. KD is
rlhfbook.com 146

known as a technique that usessofttraining labels, as opposed to the one-hot labels used in
standard objectives like next-token prediction with cross-entropy loss. The objectives over
soft labels look at the distribution over all possible next tokens or predictions, rather than
just whether or not the single predicted token was correct, and train the student distribution
to match the teacher distribution.
KD generally can be applied to any deep learning problem, e.g. predicting a single class of
an input. In order to apply it specifically to the autoregressive style of language models,
the loss can be decomposed to make a per-token distribution-matching loss. In 2016, Kim
& Rush applied KD to have a student model learn fromsequencesgenerated by a teacher
model \[282\].
Let s be the source sentence or prompt,u = (u1,...,u J)be a complete output sequence
from the teacher model,V be the output vocabulary (possible tokens in the tokenizer),q
be the teacher distribution over next-tokens, andp be the student distribution. We use
u here as a neutral symbol for a complete teacher output sequence, reservinga for the
student-sampled completion/action sequence in the on-policy/RL notation below. Note that
their paper calls this word-level distillation, but for modern language models this is best read
as per-token distribution matching over the tokenizer vocabulary, since the paper predates
modern sub-word tokenizers:
LWORD−KD =−
J∑
j=1
|V|∑
k=1
q(uj =k|s,u <j) logp(uj =k|s,u <j).(128)
WORD-KD is an application of the classic, Hinton inspired teacher-student knowledge
distillation to a language model. This would generally be done over a static piece of text
already in the training corpus.
This has the ordinary cross-entropy form−∑
zq(z) logp (z). At each positionj, the teacher
distribution q assigns probability to every possible next tokenk∈V , and the student is
penalized when its distributionp puts low probability on tokens the teacher considers likely.
Sequence-level distillation instead treatsU as the space of possible output sequences and
matches the student to the teacher distribution over full sequences. Because the sum over all
complete sequencesu∈U is intractable, requiring summing over an exponential number of
potential sequences, Kim & Rush approximate the teacher distribution over sequences with
a point mass on a single high-probability teacher outputˆu. Here ˆuis a sequence produced
by beam search with the teacher model, soˆu= BeamSearchq(s)≈arg max u∈Uq(u|s):
LSEQ−KD(s) =−
∑
u∈U
q(u|s) logp(u|s)≈−logp(ˆu|s)
=−
|ˆu|∑
j=1
logp(ˆuj|s,ˆu<j).
(129)
SEQ-KD takes a step towards modern methods, where the teacher model is generating tokens
as signal for the student. This is a core step to unlock future styles of on-policy distillation
we will see, and is needed to make the computation over all possible sequences tractable. As
we transition to the popular variants of KD with modern models, we’ll refer to this style of
rlhfbook.com 147

training asofflineKD – as in the generations for training the student model are generated a
priori.
Before proceeding, two connections are useful.
First, there was a series of popular models trained with offline KD, such as the classifiers
DistilBERT \[283\] and TinyBERT \[284\], which combined other improvements in language
models with offline distillation (notably, notsequencedistillation because these encoder
models were not distilled for multi-token autoregressive prediction).
Second, we can make the connection to the thorough coverage of Kullback-Leibler (KL)
divergence in Chapter 15, because the cross-entropy objective used above is closely related
to KL divergence. For a teacher distributionq and student distributionp, cross-entropy is
defined as
H(q,p) =−
∑
z
q(z) logp(z).(130)
This has the same form as eq. 128 and the first term of eq. 129. Cross-entropy also can be
decomposed into the entropy of the teacher distribution and a KL divergence:
H(q,p) =H(q) +D KL(q∥p)
=−
∑
z
q(z) logq(z) +
∑
z
q(z) logq(z)
p(z). (131)
The first term,H(q), only depends on the teacher. Thus, when the teacher is fixed and the
source of training data, minimizing cross-entropy is equivalent to minimizing the forward
KL, DKL(q∥p), from teacher to student. This is the KL direction used by offline KD and
SFT-like training.
12.3.2 From Offline to On-Policy Distillation
TheseofflineKD algorithms had a few limitations that motivated on-policy variants. The
offline nature of the learning meant that the student models could suffer from a distribution
mismatch between the teacher model and sequences generated by the student at inference
time. For example, the forward KL objective can push student models to overestimate
low-probability regions of the teacher distribution. Together, these issues were an opening
foron-policydistillation (OPD).
This train-test gap is known asexposure bias\[285\] \[286\]. Offline KD samples teacher
trajectoriesu∼π T (·|s)and minimizes the per-token KL on the resulting prefixes,
LKD(θ) =E s∼D,u∼πT (·|s)
∑
t
DKL(πT (·|s,u <t)∥π θ(·|s,u <t)).(132)
At inference the student instead rolls out under its own policy, so the quantity that actually
matters is the expected task loss alongits owntrajectories,
Leval(θ) =E s∼Dtest,a∼πθ(·|s)ℓtask(s,a)(133)
rlhfbook.com 148

Here, ℓtask(s,a )denotes any downstream task loss for the completed student response, such
as answer incorrectness, failed test cases, or a judge/rubric loss. Exposure bias is the direct
consequence of the inequalityπT (·|s )̸= πθ(·|s ): the prefixes( s,u<t)visited during
training and the prefixes(s,a<t)visited at test time are drawn from different state-visitation
distributions, so the student is supervised on a set of states distinct from those it acts on.
The core shift to on-policy distillation is the idea that we can tweak the optimization by
sampling from the student model and measuring its distance to the teacher distribution,
rather than sampling from the teacher model. MiniLLM noted the need to shift to a reverse
KL optimization (we explain intuitively why this target can be better in Chapter 15) and
proposed using KD loss functions within an online policy-gradient RL framework \[287\].
Other concurrent work \[288\] showed the promise of on-policy KD and connected the iterative
process of generating from the student and grading with a teacher to imitation-learning
work from the RL literature. To make the connection, one such imitation-learning algorithm,
DAgger, iteratively trains an agent that acts in the world with its learned policy and is given
feedback from an oracle policy on what action it should have taken, which can then be used
to update its policy \[289\].
The cost of this gap can be quantified through the supervised imitation-learning bound
that motivates DAgger. In the original discrete-action setting, suppose the learned policy
matches the teacher within an expected per-step action errorϵ on the teacher-induced
training distribution, whereI[·]is an indicator that returns 1 when its condition is true and
0 otherwise,
Est∼dπT
[I(πθ(st)̸=π T (st))]≤ϵ.(134)
The supervised imitation-learning analysis \[289\] shows that the expected loss accumulated
along a length-Ltrajectory sampled from the student can scale quadratically inL\[286\]:
Ea∼πθ(·|s)
[L∑
t=1
ℓ(s,a<t)
]
≤O(ϵL 2).(135)
For LLMs, this discrete-action bound should be read as an analogy rather than a theoretical
guarantee. In practice, LLMs predict full next-token distributions over long horizons, so the
0-1 action-disagreement assumption in eq. 134 does not apply cleanly. Prompts or prefixes
map naturally to states and sampled tokens map to actions, but token-level distillation
is usually measured with distributional losses such as KL or cross-entropy, so the classic
DAgger math does not transfer exactly.
This kind ofO(ϵL2)compounding is especially pronounced for modern LLMs, which routinely
generate sequences spanning thousands of tokens. A single suboptimal token shifts the prefix
slightly out-of-distribution, and the model, having never seen this perturbed prefix, is more
likely to err again, leading to degraded or hallucinatory text. On-policy distillation addresses
this byiterativelysampling completions from the current student and supervising them with
the teacher at the visited states. The student confronts its own mistakes, receives teacher
feedback on the specific out-of-distribution states it visits, and learns recovery behaviors.
Under DAgger’s interactive imitation-learning analysis, this iterative procedure can reduce
the compounding fromO(ϵL2)to O(ϵL)\[289\]. For LLMs, this explains the motivation
rlhfbook.com 149

behind OPD: the exact bounds may not carry over cleanly to every token-level distillation
setup, but the practical success of on-policy methods supports the underlying intuition.
For on-policy distillation, lets be a prompt,a = (a1,...,a L)be a completion sampled
from the current student policyπθ(·|s ), and letst = (s,a<t)be the token-level state at
step t. The teacher policyπT is fixed, so the objective compares the student’s next-token
distribution to the teacher’s distribution on states induced by the student. Because the
expectation samples fromπθ and the student distribution is on the left side ofDKL(πθ∥πT ),
this is a reverse-KL objective:
LOPD(θ) =E s,a∼πθ(·|s)
∑
t
DKL (πθ(·|s t)∥π T (·|s t)).(136)
Here, we have shifted to the expectation notation, as used extensively in Chapter 6, which
covers the fundamental RL policy-gradient algorithms, as the optimization is solved by
sampling trajectories and numerically estimating the gradient. This shift to the sampling
framework acts as a natural transition to modern LLM training infrastructure with RL,
which is designed to rapidly alternate between generating tokens from the current policy
being trained and taking learning updates.
In fact, recent implementations of OPD take this integration of KD with RL a step further,
where the KD distance is taken directly as a reward signal within the RL optimization. A
canonical implementation is to substitute the negative per-token contribution to the reverse
KL distance as the advantage within an RL algorithm \[290\]. For a sampled tokenat at state
st, the token-level log-probability gap can be written as an advantage-like signal:
AOPD
t = logπT (at|s t)−logπ θ(at|s t).(137)
Using the negative per-token KL contribution turns minimization into a maximization signal:
sampled tokens the teacher rates above the student receive positive advantage, and tokens
the teacher rates below the student receive negative advantage. The teacher log-prob gap
acts like dense token-level feedback, providing potentially more useful learning feedback than
the sparse verifiable rewards or reward model outputs.
12.3.3 Modern OPD Variants
This setup can even be expanded further, where multiple teacher models are used to teach
one final model or additional information can be inserted into a generation to help a model
identify a mistake. To begin, we will cover how to integrate multiple teachers into a single
training run. These teachers can be specific specialist models, e.g. for a domain such as math
or code, or a previous, intermediate training checkpoint. For each teacher, a contribution
weight can be chosen per prompt or task type in the training batch, in order to create
Multi-Teacher On-Policy Distillation (MOPD) \[185\]. For multiple teachers, letπTk be teacher
k and letwk(s)be its prompt-dependent mixture weight (with∑
kwk(s) = 1) within the
reverse KL loss:
LMOPD(θ) =E s,a∼πθ(·|s)
∑
t
∑
k
wk(s)DKL (πθ(·|s t)∥π Tk(·|s t)).(138)
rlhfbook.com 150

In large-scale post-training, this can enable further scaling of recipes across growing organi-
zations. Multiple groups can work on high-quality expert models, which can serve as teacher
models down the line for the final student model, as done for \[281\] and \[185\].
There are many ways to combine OPD with other areas investigated in this book, such as
using the reverse KL as an advantage in addition to other forms of advantage computation,
such as GRPO’s group-level normalization, which enables more complex reward shaping. KD
methods are unusual among post-training methods because they often require the student
and teacher to share a tokenizer, since the supervision can be per-token feedback from
another LLM.
Extended approaches, such as On-Policy Self-Distillation (OPSD), have a language model
verify a completion either itself or with external tools to act as a teacher with privileged
information, so it can improve its own performance without an explicitly stronger teacher
\[291\] (an overview of OPSD training is shown in fig. 38). For example, Cursor used self-
distillation in the form of targeted textual feedback on RL trajectories to train its Composer
2.5 coding model \[292\], finetuned from Kimi K2.5. What follows is a simplified intuition, as
in practice the setup below is combined with other loss functions such as code correctness.
In this setup, Cursor has the model review RL trajectories with a judgement prompt that
has a list of common bugs. When encountering a bug, the judgement model will modify the
generated sequence within RL – inserting a hint for the model to learn from in the future –
and then proceed with the distillation loss. This entails a loop of first generating a completion
with standard language model generation in RL, then running the judge model and optionally
inserting a hint token, and finally generating the logprobs for the new completion to deploy
the knowledge distillation loss. The hint in the token-space for the model is enough to
help the model correct its own outputs, even when improving at the absolute frontier of
performance (there’s meaningful ongoing work on how to best structure and use these hints,
often referred to asprivileged information\[293\]).
This leaves on-policy distillation as a core post-training method, useful for combining multiple
skills into one general model or pushing the frontier in a specialized deployment.
12.3.4 Suggested Experiments
The companion code incode/distillation/ implements SDPO \[294\], the on-policy self-
distillation setup illustrated in fig. 38 (the concurrent OPSD paper \[291\] is closely related):
one policy acts as both the demonstration-conditioned teacher and the question-only student,
trained with a per-token reverse KL. It runs on a small string-reversal task, which makes the
on-policy distillation loop cheap enough to watch end-to-end on a single GPU.
1.Run the SDPO string-reversal example.
cd code/
uv run python -m distillation.train --config distillation/configs/sdpo.yaml
Watch reward, loss, and skipped, along with the teacher/student rollout samples
printed in the loop. Theskipped count is the number of polled prompts whose sampled
group contained no correct rollout; as the student improves, fewer prompts are skipped
andrewardclimbs toward 1.
2. Vary the on-policy knobs.Copy distillation/configs/sdpo.yaml and sweep
rlhfbook.com 151

Figure 37: Three distillation regimes, compared by where the rollout comes from and how
supervision flows.Sequence KD(left): the teacher generates an output offline and the
student is trained to match it with a cross-entropy (CE) loss.On-policy distillation
(OPD)(center): the student generates the rollout on-policy (e.g. within a RL framework)
and a separate teacher scores each visited token, training the student with a per-token KL
divergence (KL).On-policy self-distillation (OPSD)(right): one model plays both roles
– privileged information (a hint) added to the context creates a teacher trajectory, and the
no-hint generation is distilled toward it with a KL loss, with no separate teacher model.
Figure 38: On-policy self-distillation (OPSD) on a string-reversal task. One policyπθ is
forwarded twice over the same student-sampled completiony: ateacherpass conditioned on
the question plus a correct sibling demonstration (yellow), and astudentpass conditioned
on the question only (green). The per-token reverse KL between the two passes, with a stop-
gradient on the teacher, pulls the question-only policy toward its demonstration-conditioned
self; highlighted columns are the incorrectly sampled tokens where the distributions diverge
most.
rlhfbook.com 152

num_rollouts, kl_top_k, and prompts_per_step while holding the task fixed. More
rollouts per prompt make a correct sibling demonstration easier to find (lowering
skipped) at the cost of more generation per step;kl_top_k trades off how much of
the teacher distribution the reverse KL matches against compute.
12.4 AI Feedback
Soon after the explosion of growth in RLHF, RL from AI Feedback (RLAIF) emerged as an
alternative approach where AIs could approximate the human data piece of the pipeline and
accelerate experimentation or progress. AI feedback, generally, is a larger set of techniques
for using AI to augment or generate data explaining the quality of a certain input (which
can be used in different training approaches or evaluations), and it started with pairwise
preferences \[295\] \[296\] \[297\]. There are many motivations to use RLAIF to either entirely
replace human feedback or augment it. Within the RLHF process, AI feedback is known
most for its role within the preference data collection and the related reward model training
phase (of which constitutional AI is a certain type of implementation). In this chapter, we
focus on general AI feedback and this specific way of using it in the RLHF training pipeline,
and we cover more ways of understanding or using synthetic data later in this book.
As AI feedback matured, its applications expanded beyond simply replacing human preference
labels. The same LLM-as-a-judge infrastructure that enabled cheaper preference data
collection also enabled scalable evaluation (see Chapter 16), and more recently, rubric-based
rewards that extend RL training to domains without verifiable answers – a frontier explored
later in this chapter.
12.4.1 Balancing AI and Human Feedback Data
AI models are far cheaper than humans at generating a specific quantity of feedback: as of
2026, a single piece of human preference data costs on the order of $1 or higher (or even
above $10 per prompt), whereas AI feedback with a frontier AI model, such as GPT-4o,
costs less than $0.01. Beyond this, the cost of human labor remains roughly constant,
while the performance of leading models at these tasks continues to increase while price-
per-performance decreases. This cost difference opens the market of experimentation with
RLHF methods to an entire population of people previously priced out.
Other than price, AI feedback introduces differenttradeoffson performance than human
feedback, which are still being investigated in the broader literature. AI feedback is far more
predominant in its role in evaluation of the language models that we are training, as its
low price allows it to be used across a variety of large-scale tasks where the cost (or time
delay) of human data would be impractical. All of these topics are deeply intertwined – AI
feedback data will never fully replace human data, even for evaluation, and the quantity of AI
feedback for evaluation will far outperform training because far more people are evaluating
than training models.
The exact domains and applications – i.e. chat, safety, reasoning, mathematics, etc. – where
AI feedback data outperforms human data are not completely established. Some early work in
RLAIF shows that AI feedback can completely replace human data, touting it as an effective
replacement \[295\], especially when evaluated solely on chat tasks \[28\] \[298\]. Early literature
studying RLHF after ChatGPT had narrow evaluation suites focused on the “alignment”
of models that act as helpful assistants across a variety of domains (discussed further in
rlhfbook.com 153

Chapter 17). Later work takes a more nuanced picture, where the optimal equilibrium
on a broader evaluation set, e.g. including some reasoning tasks, involves routing a set of
challenging data points to humans for accurate labeling, while most of the data is sent for
AI feedback \[299\] \[300\]. Although no studies have focused on the balance between human
and AI feedback data for RLHF across broader domains, there are many technical reports
that show RLHF generally can improve this broad suite of evaluations, some that use DPO,
such as Ai2’s Tülu 3 \[6\] and Olmo 3 \[18\], or Hugging Face’s SmolLM 3 \[206\], and others that
use online RLHF pipelines, such as NVIDIA’s work that uses a mix of human preference
data from Scale AI and LLM-based feedback (through the HelpSteer line of work \[301\] \[109\]
\[110\] \[258\]): Nemotron Nano 3 \[184\], Nemotron-Cascade \[302\], or Llama-Nemotron reasoning
models \[170\].
Overall, although AI feedback and related methods are obviously extremely useful to the field,
it is clear that human data has not been completely replaced by these cheaper alternatives.
Many hypotheses exist, but whether human data allows finer control of the models in
real-world product settings or for newer training methods such as character training (an
emerging set of techniques that allow you to precisely control the personality of a model,
covered in Chapter 17) has not been studied. For those getting started, AI feedback should
be the first attempt, but for pipelines that are scaling to larger operations the eventual
transition to include human feedback is likely.
The term RLAIF was introduced in Anthropic’s workConstitutional AI: Harmlessness from
AI Feedback\[24\], which resulted in initial confusion in the AI community over the relationship
between the two methods in the title of the paper (Constitutional AI and AI Feedback).
Since the release of the Constitutional AI (CAI) paper and the formalization of RLAIF,
RLAIF has become a default method within the post-training and RLHF literatures – there
are far more examples than one can easily enumerate. The relationship should be understood
as CAI was the example that kickstarted the broader field of RLAIF.
A rule of thumb for the difference between human data and AI feedback data is as follows:
1. Human data is high-noise and low-bias. This means that collection and filtering of the
data can be harder, but when wrangled it’ll provide a very reliable signal.
2. Synthetic preference data is low-noise and high-bias. This means that AI feedback
data will be easier to start with, but can have tricky, unintended second-order effects
on the model that are systematically represented in the data.
This book highlights many academic results showing how one can substitute AI preference
data in RLHF workflows and achieve strong evaluation scores \[299\], but broader industry
trends show how the literature of RLHF is separated from more opaque best practices. Across
industry, human data is often seen as a substantial moat and a major technical advantage.
12.4.2 Building Specific LLMs for Judgment
As RLAIF methods have become more prevalent, many have wondered if we should be
using the same models for generating responses as those for generating critiques or ratings.
Specifically, the calibration of the LLM-as-a-judge used has come into question. Several
works have shown that LLMs are inconsistent evaluators \[303\] and prefer their own responses
over responses from other models (coined self-preference bias) \[208\].
As a result of these biases, many have asked: Would a solution be to train a separate
rlhfbook.com 154

model just for this labeling task? Multiple models have been released with the goal of
substituting for frontier models as a data labeling tool, such as critic models Shepherd
\[304\] and CriticLLM \[305\] or models for evaluating response performance akin to Auto-J
\[306\], Prometheus \[86\], Prometheus 2 \[307\], or Prometheus-Vision \[308\], but they are not
widely adopted in documented training recipes. Some find scaling inference via repeated
sampling \[157\] \[309\] \[310\], self-refinement \[311\], or tournament ranking \[312\] provides a better
estimate of the true judgment or higher-quality preference pairs. Other calibration techniques
co-evolve the generation and judgment capabilities of the model \[313\]. It is accepted that
while biases exist, the leading language models are trained extensively for this task – as it’s
needed for both internal operations at AI labs and is used extensively by customers – so it is
generally not needed to train your own judge, unless your task involves substantial private
information that is not exposed on the public internet.
12.5 Constitutional AI
The method of Constitutional AI (CAI), which Anthropic uses in their Claude models, is
the earliest documented, large-scale use of synthetic data for RLHF training. Constitutional
AI involves generating synthetic data in two ways:
1. Critiques of instruction-tuned data to follow a set of principles like “Is the answer
encouraging violence?” or “Is the answer truthful?” When the model generates answers
to questions, it checks the answer against the list of principles in the constitution,
refining the answer over time. Then, the model is fine-tuned on this resulting dataset.
2. Generating pairwise preference data by using a language model to answer which
completion was better, given the context of a random principle from the constitution
(similar to research for principle-guided reward models \[314\]). Then, RLHF proceeds
as normal with synthetic data, hence the RLAIF name.
Largely, CAI is known for the second half above, the preference data, but the methods
introduced for instruction data are used in general data filtering and synthetic data generation
methods across post-training.
CAI can be formalized as follows.
By employing a human-written set of principles, which they term aconstitution, Bai et
al. 2022 use a separate LLM to generate artificial preference and instruction data used for
fine-tuning \[24\]. A constitutionC is a set of written principles indicating specific aspects to
focus on during a critique phase. The instruction data is curated by repeatedly sampling
a principleci∈C and asking the model to revise its latest outputyi to the promptx to
align withci. This yields a series of instruction variants{y0,y 1,···,y n} from the principles
{c0,c 1,···,c n−1}used for critique. The final data point is the promptxtogether with the
final completionyn, for somen.
The preference data is constructed in a similar, yet simpler way by using a subset of principles
fromC as context for a feedback model. The feedback model is presented with a promptx,
a set of principles{c0,···,c n}, and two completionsy0 and y1 labeled as answers (A) and
(B) from a previous RLHF dataset. The new data point is generated by having a language
model select which output (A) or (B) is both higher quality and more aligned with the stated
principle. In earlier models this could be done by prompting the model withThe answer
is:, and then looking at which token (A or B) had a higher probability, but now this is
rlhfbook.com 155

more commonly handled by a model that’ll explain its reasoning and then select an answer –
commonly referred to as a type of generative reward model \[83\].
12.5.1 Further Reading on CAI
There are many related research directions and extensions of Constitutional AI, but few of
them have been documented as clear improvements in RLHF and post-training recipes.
• OpenAI has released a Model Spec \[270\], which is a document stating the intended
behavior for their models, and stated that they are exploring methods for alignment
where the model references the document directly (which could be seen as a close peer
to CAI). OpenAI has continued to update their spec and trained its reasoning models
such as o1 with a method called Deliberative Alignment \[315\] to align the model while
referencing these safety or behavior policies.
• Anthropic has continued to use CAI in their model training, updating the constitution
Claude uses \[316\] and experimenting with how population collectives converge on
principles for models and how that changes model behavior when external groups
create principles on their own and then share them with Anthropic to train the models
\[317\].
• The open-source community has explored replications of CAI applied to open datasets
\[318\] and for explorations into creating dialogue data between LMs \[319\].
• Other work has used principle-driven preferences or feedback with different optimization
methods. Sun et al. 2023 \[320\] use principles as context for the reward models, which
were used to train the Dromedary models \[314\]. Glaese et al. 2022 \[42\] use principles
to improve the accuracy of human judgments in the RLHF process. Liu et al. 2025
\[158\] train a reward model to generate its own principles at inference time, and use
these to deliver a final score. Franken et al. 2024 \[321\] formulate principle-following as
a mutual information maximization problem that the pretrained model can learn with
no labels.
12.6 Rubrics: Prompt-Specific AI Feedback for Training
AI feedback’s role in training grew in late 2024 and into 2025 as the field looked for avenues
to scale reinforcement learning with verifiable rewards (see Chapter 7). The idea of rubrics
emerged as a way to get nearly-verifiable criteria for prompts that do not have clearly
verifiable answers. This would allow a model to try to generate multiple answers to a problem
and update (with RL) towards the best answers. This idea is closely related to other methods
discussed in this chapter, and likely began functioning as the LLM judges and synthetic data
practices improved across the industry. Now, RL with rubrics as rewards is established in
providing meaningful improvements across skills such as scientific reasoning or factuality
\[322\], \[323\], \[324\], \[325\].
An example rubric is shown below with its associated prompt \[325\]:
**Prompt**: As a museum curator, can you suggest five obscure artifacts that would be
perfect for a "Mysteries of the Ancient World" exhibit? Each artifact should come from a
different culture and time period, with a brief description of their historical
significance and mysterious origins. These artifacts should leave visitors wondering
about the secrets and lost knowledge of our past. Thank you for your expertise in
bringing this exhibit to life.
rlhfbook.com 156

** Rubric**:
1. The response includes exactly five distinct artifacts as requested. [Hard Rule]
2. The response ensures each artifact originates from a different culture and time
period. [Hard Rule]
3. The response provides a brief description of each artifact's historical significance.
[Hard Rule]
4. The response provides a brief description of each artifact's mysterious origins or
unexplained aspects. [Hard Rule]
5. The response conveys a sense of intrigue and mystery that aligns with the theme of
the exhibit. [Hard Rule]
6. The response clearly and accurately communicates information in a well-organized and
coherent manner. [Principle]
7. The response demonstrates precision and clarity by avoiding unnecessary or irrelevant
details. [Principle]
8. The response uses informative and engaging language that stimulates curiosity and
critical thinking. [Principle]
9. The response shows thoughtful selection by ensuring each example contributes uniquely
to the overall theme without redundancy. [Principle]
10. The response maintains consistency in style and format to enhance readability and
comprehension. [Principle]
The [Hard Rule] and [Principle] are specific tags to denote the priority of a certain piece
of feedback. Other methods of indicating importance can be used, such as simple priority
numbers.
Rubric generation is generally done per-prompt in the training data, which accumulates
meaningful synthetic data costs in preparation. To alleviate this, a general rubric is often
applied as a starting point per-domain, and then the fine-grained rubric scores per-prompt
are assigned by a supervising language model to guide the feedback for training. An example
prompt to generate a rubric for a science task is shown below \[322\]:
You are an expert rubric writer for science questions in the domains of Biology,
Physics, and Chemistry.
Your job is to generate a self-contained set of evaluation criteria ("rubrics") for
judging how good a response is to a given question in one of these domains.
Rubrics can cover aspects such as factual correctness, depth of reasoning, clarity,
completeness, style, helpfulness, and common pitfalls.
Each rubric item must be fully self-contained so that non-expert readers need not
consult
any external information.
Inputs:
- question: The full question text.
- reference_answer: The ideal answer, including any key facts or explanations.
Total items:
- Choose 7-20 rubric items based on question complexity.
Each rubric item must include exactly three keys:
1. title (2-4 words)
2. description: One sentence beginning with its category prefix, explicitly stating what
to look for.
For example:
- Essential Criteria: States that in the described closed system, the total mechanical
energy (kinetic plus potential)
rlhfbook.com 157

before the event equals the total mechanical energy after the event.
- Important Criteria: Breaks down numerical energy values for each stage, demonstrating
that initial kinetic
energy plus initial potential energy equals final kinetic energy plus final potential
energy.
- Optional Criteria: Provides a concrete example, such as a pendulum converting between
kinetic and potential
energy, to illustrate how energy shifts within the system.
- Pitfall Criteria: Does not mention that frictional or air-resistance losses are
assumed negligible when applying
conservation of mechanical energy.
3. weight: For Essential/Important/Optional, use 1-5 (5 = most important); for Pitfall,
use -1 or -2.
Category guidance:
- Essential: Critical facts or safety checks; omission invalidates the response.
- Important: Key reasoning or completeness; strongly affects quality.
- Optional: Nice-to-have style or extra depth.
- Pitfall: Common mistakes or omissions; highlight things often missed.
Format notes:
- When referring to answer choices, explicitly say "Identifies (A)", "Identifies (B)",
etc.
- If a clear conclusion is required (e.g. "The final answer is (B)"), include an
Essential Criteria for it.
- If reasoning should precede the final answer, include an Important Criteria to that
effect.
- If brevity is valued, include an Optional Criteria about conciseness.
Output: Provide a JSON array of rubric objects. Each object must contain exactly three
keys-title, description, and weight.
Do not copy large blocks of the question or reference_answer into the text. Each
description must begin with its category
prefix, and no extra keys are allowed.
Now, given the question and reference_answer, generate the rubric as described.
The reference answer is an ideal response but not necessarily exhaustive; use it only as
guidance.
Another, simpler example follows as \[324\]:
SYSTEM:
You generate evaluation rubrics for grading an assistant's response to a user prompt.
Rubric design rules:
- Each criterion must be atomic (one thing), objective as possible, and written so a
grader can apply it consistently.
- Avoid redundant/overlapping criteria; prefer criteria that partition different failure
modes.
- Make criteria self-contained (don't rely on unstated context).
- Include an importance weight for each criterion.
Output format (JSON only):
{
"initial_reasoning": "<brief rationale for what matters for this prompt>",
"rubrics": [
{
"reasoning": "<why this criterion matters>",
"criterion": "<clear, testable criterion>",
rlhfbook.com 158

"weight": <integer 1-10>
},
...
]
}
USER:
User prompt:
{prompt}
Generate the rubric JSON now.
As you can see, the prompts can be very detailed and are tuned to the training setup.
Rubrics with RL training are going to continue to evolve beyond their early applications
to instruction following \[326\], deep research \[327\], evaluating deep research agents \[328\], or
long-form generation \[329\].
rlhfbook.com 159

13 Tool Use and Function Calling
Language models using tools is a natural way to expand their capabilities, especially for
high-precision tasks where external tools contain the information or for agents that need
to interact with complex web systems. Tool-use is a skill that language models need to be
trained to have, and RLHF and all the other methods presented in this book can refine it.
Consider a question from a user such as:
User: Who is the president today?
A language model without tools will have a hard time answering this question due to the
knowledge cutoff of pretraining data, but this is readily accessible information with one
search query. Consider another example:
User: Move all the arXiv papers in my downloads folder to my ~/research/
directory with names indicating the date of the paper.
This is a task that the model weights alone cannot even attempt – the use of tools enables
language models to address a far broader range of tasks.
Before diving deeper, it is useful to distinguish related terms that are often used interchange-
ably:
• Tool use: the model emits a structured request (tool name and arguments); an
orchestrator executes the tool; results are appended to the context; the model continues
generating.
• Function calling: tool use where the arguments must conform to a declared schema
for a set of functions (usually JSON Schema), enabling reliable parsing and validation.
• Code execution: a special case of tool use where the “tool” is a code interpreter (e.g.,
Python); results are returned as tool output.
13.1 Tool-Use Overview
An AI model uses any external tools by outputting special tokens to trigger a certain endpoint.
These can be anything from highly specific tools, such as functions that return the weather
at a specific place, to code interpreters or search engines that act as fundamental building
blocks of complex behaviors. Our first example showcased where language models need more
up-to-date information to complement the fixed nature of their weights trained on past data,
but there are also tools such as code execution, which lets language models get around their
probabilistic, generative nature and return precise answers. Consider the task of printing an
approximation of pi to 50 digits (without reciting it from memory and risking hallucination).
A language model with tools can do the following:
<code>
from decimal import Decimal, getcontext
getcontext().prec = 60
def compute_pi():
# Chudnovsky algorithm for computing pi
C = 426880 * Decimal(10005).sqrt()
K, M, X, L, S = 0, 1, 1, 13591409, Decimal(13591409)
for i in range(1, 100):
rlhfbook.com 160

M = M * (K**3 - 16*K) // ((i)**3)
K += 12
L += 545140134
X *= -262537412640768000
S += Decimal(M * L) / X
return C / S
print(str(compute_pi())[:52])
</code>
<output>
3.14159265358979323846264338327950288419716939937510
</output>
This chapter provides an overview of the origins of tool-use in modern language models, its
fundamentals and formatting, and current trade-offs in utilizing tools well in leading models.
The exact origin of the term “tool use” is not clear, but the origins of the idea far predate
the post-ChatGPT world where RLHF proliferated. Early examples circa 2015 attempted to
build systems predating modern language models, such as Neural Programmer-Interpreters
(NPI) \[330\], “a recurrent and compositional neural network that learns to represent and
execute programs.” As language models became more popular, many subfields were using
integrations with external capabilities to boost performance. To obtain information outside
of just the weights many used retrieval augmented generation \[331\] or web browsing \[4\]. Soon
after, others were exploring language models integrated with programs \[332\] or tools \[333\].
As the field matured, these models gained more complex abilities in addition to the vast
improvements to the underlying language modeling. For example, Toolformer could use “a
calculator, a Q&A system, two different search engines, a translation system, and a calendar”
\[334\]. Soon after, Gorilla was trained to use 1645 APIs (from PyTorch Hub, TensorFlow Hub
v2, and Hugging Face) and its evaluation APIBench became a foundation of the popular
Berkeley Function Calling Leaderboard \[335\]. Since these early models, the diversity of
actions called has grown substantially.
Tool-use models are now deeply intertwined with regular language model interactions. Model
Context Protocol (MCP) emerged as a common formatting used to connect language models
to external data sources (or tools) \[336\]. With stronger models and better formats, tool-
use language models are used in many situations, including productivity copilots within
popular applications such as Microsoft Office or Google Workspace, scientific domains \[337\],
medical domains \[338\], coding agents \[339\] such as Claude Code or Cursor, integrations with
databases, and many other autonomous workflows.
Evaluating tool-use models involves multiple dimensions: exact-match metrics for tool name
and argument correctness, schema validity, and end-to-end task completion in simulated
environments. Reliability across trials also matters –τ-bench introduced the passˆk metric
(distinct from pass@k) to measure whether an agent succeeds consistently rather than
occasionally \[340\]. ToolLLM and its ToolBench dataset provide a large-scale framework for
training and evaluating tool use across 16,000+ real-world APIs \[341\], while the Berkeley
Function Calling Leaderboard (BFCL) remains a popular benchmark for comparing models
on function calling accuracy \[335\].
rlhfbook.com 161

13.2 Interweaving Tool Calls in Generation
Training data for function calling looks much like other post-training data, with one addition:
a system prompt that instructs the model what tools it has available. An example formatted
data point with the system prompt and tools available in JSON format is shown below:
<system>
You are a function-calling AI model. You are provided with function signatures within
<functions></functions> XML tags. You may call one or more functions to assist with the
user query. Don't make assumptions about what values to plug into functions.
</system>
<functions>
[
{
"name": "search_movies",
"description": "Search for movies by title and return matching results with IDs.",
"parameters": {
"type": "object",
"properties": {
"query": {
"type": "string",
"description": "The search string for the movie title."
}
},
"required": ["query"]
}
},
{
"name": "get_movie_details",
"description": "Fetch detailed information about a movie including cast, runtime,
and synopsis.",
"parameters": {
"type": "object",
"properties": {
"movie_id": {
"type": "string",
"description": "The unique identifier for the movie."
}
},
"required": ["movie_id"]
}
},
{
"name": "get_showtimes",
"description": "Get movie showtimes for a given location and date.",
"parameters": {
"type": "object",
"properties": {
"movie_id": {
"type": "string",
"description": "The unique identifier for the movie."
},
"zip_code": {
"type": "string",
"description": "ZIP code for theater location."
},
"date": {
"type": "string",
"description": "Date for showtimes in YYYY-MM-DD format."
rlhfbook.com 162

}
},
"required": ["movie_id", "zip_code"]
}
}
]
</functions>
<user>
...
</user>
Although the language model is generating a completion, if it is following this example, it
would generate the tokenssearch_movies("Star Wars") to search for Star Wars. This is
often encoded inside special formatting tokens, and then the next tokens inserted into the
sequence will contain the tool outputs. With this, models can learn to accomplish more
challenging tasks than many simple standalone models.
A popular form of tool use is code-execution, allowing the model to get precise answers to
complex logic or mathematics problems. For example, code-execution within a language
model execution can occur during the thinking tokens of a reasoning model. As with function
calling, there are tags first for the code to execute (generated by the model) and then a
separate tag for output.
<|user|>
What is the 50th Fibonacci number? (Use the standard F_0=0, F_1=1 indexing.)</s>
<|assistant|>
<think>
Okay, I will compute the 50th Fibonacci number with a simple loop, then return the
result.
<code>
def fib(n):
a, b = 0, 1
for _ in range(n):
a, b = b, a + b
return a
fib(50)
</code>
<output>
12586269025
</output>
</think>
<answer>
The 50th Fibonacci number is 12 586 269 025.
</answer>
What is happening under the hood is the language model is interleaving tool inputs and
outputs with standard autoregressively generated tokens. The orchestration loop that makes
this possible looks something like:
rlhfbook.com 163

messages = [...]
whileTrue:
response = model(messages, tools=tools)
if notresponse.tool_calls:
returnresponse.text
forcallinresponse.tool_calls:
result = execute_tool(call.name, call.args)
messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
Figure 39: Tool use interleaves model generation with external execution: the model generates
tokens until it emits a tool call (orange), an external system executes the tool and injects
the output (purple) into the sequence, then the model continues generating. Models can
emit multiple tool calls in a single generation. During training, tool call and output tokens
are typically masked from the loss.
Training for tool use is about getting the model to behave predictably with this different
token flow—knowing when to emit a tool call, how to format arguments correctly, and how
to incorporate results into its response. Open models must be trained to work with a variety
of tools that users may connect off the shelf.
13.3 Multistep Tool Reasoning
OpenAI’s o3 model represented a substantial step-change in how multi-step tool-use can be
integrated with language models. This behavior is related to much earlier research trends
in the community. For example, ReAct \[342\] showcased how actions and reasoning can be
interleaved into one model generation:
In this paper, we explore the use of LLMs to generate both reasoning traces
and task-specific actions in an interleaved manner, allowing for greater synergy
between the two: reasoning traces help the model induce, track, and update
action plans as well as handle exceptions, while actions allow it to interface with
and gather additional information from external sources such as knowledge bases
or environments.
With the solidification of tool-use capabilities and the take-off of reasoning models, multi-turn
tool-use has grown into an exciting area of research \[186\]. Training these multi-step behaviors
with RL resembles classic reinforcement learning more than the per-sample RLHF loop: the
rlhfbook.com 164

agent interacts with an environment and its tools over a full trajectory before any reward is
assigned, as shown in fig. 40.
Figure 40: Reinforcement learning for multi-step tool use. A prompt is sampled from the
training data and the agent (policyπθ) interacts with the environment and its tools over a
trajectory, alternating actionsat with observationsot. The completed trajectory is graded or
verified to produce a single rewardrT at the end, which drives the policy update. Unlike the
per-sample RLHF loop, the reward arrives only after a multi-step rollout – closer to classic
RL.
13.4 Model Context Protocol
Model Context Protocol (MCP) is an open standard for connecting language models to
external data sources and information systems \[336\]. At the data layer, MCP uses JSON-RPC
2.0 with discovery and execution methods for its primitives. Rather than requiring specific
tool call formatting per external system, MCP enables models to access rich contextual
information through a standardized protocol.
MCP is a simple addition on top of the tool-use content in this chapter – it is how applications
pass context (data + actions) to language models in a predictable JSON schema. MCP
servers that the models interact with have core primitives: resources (read-only data blobs),
prompts (templated messages/workflows), and tools (functions the model can call). With
this, the MCP architecture can be summarized as:
•MCP servers wrap a specific data source or capability.
•MCP clients (e.g., Claude Desktop, IDE plug-ins) aggregate one or more servers.
• Hosts, e.g. Claude or ChatGPT applications, provide the user/LLM interface; switching
model vendors or back-end tools only means swapping the client in the middle.
MCP enables developers of tool-use models to use the same infrastructure to attach their
servers or clients to different models, and at the same time models have a predictable
format they can use to integrate external components. These together make for a far more
predictable development environment for tool-use models in real-world domains.
An MCP server exposes tools to clients through a standardized JSON schema:
rlhfbook.com 165

{
"name": "get_weather",
"description": "Get current weather for a location",
"inputSchema": {
"type": "object",
"properties": {
"location": {
"type": "string",
"description": "City name or coordinates"
}
},
"required": ["location"]
}
}
A minimal Python MCP server implementing this tool:
frommcp.serverimportServer
frommcp.typesimportTool, TextContent
server = Server("weather-server")
@server.list_tools()
async deflist_tools():
return[Tool(
name="get_weather",
description="Get current weather",
inputSchema={
"type": "object",
"properties": {"location": {"type": "string"}},
"required": ["location"]
}
)]
@server.call_tool()
async defcall_tool(name: str, arguments: dict):
ifname == "get_weather":
weather = fetch_weather(arguments["location"])
return[TextContent(type="text", text=weather)]
13.5 Implementation Details
There are multiple formatting and masking decisions when implementing a tool-use model:
• Python vs. JSON formatting: In this chapter, we include examples that format
tool use as both JSON data structures and Python code. Models tend to select one
structure, whereas different providers across the industry use different formats.
• Masking tool outputs: An important detail when training tool-use models is that
the tokens in the tool output are masked from the model’s training loss. This ensures
the model is not learning to predict the output of the system that processes the tool
call (as the results are not tokens generated by the model).
• Multi-turn formatting for tool invocations: It is common practice when imple-
menting tool-calling models to add more structure to the data-loading format. Standard
practice for post-training datasets is a list of messages alternating between user and
assistant (and often a system message). The overall structure is the same for tool-use,
rlhfbook.com 166

but the turns of the model are split into subsections of content delimited by each tool
call. An example is below.
messages = [
{
"content": "You are a function calling AI model. You are provided with function
signatures within <functions></functions> XML tags. You may call one or more functions
to assist with the user query. Don't make assumptions about what values to plug into
functions.",
"function_calls": null,
"functions": "[{\"name\": \"live_giveaways_by_type\", \"description\": \"Retrieve live
giveaways from the GamerPower API based on the specified type.\", \"parameters\":
{\"type\": {\"description\": \"The type of giveaways to retrieve (e.g., game, loot,
beta).\", \"type\": \"str\", \"default\": \"game\"}}}]",
"role": "system"
},
{
"content": "Where can I find live giveaways for beta access and games?",
"function_calls": null,
"functions": null,
"role": "user"
},
{
"content": null,
"function_calls":
"live_giveaways_by_type(type='beta')\nlive_giveaways_by_type(type='game')",
"functions": null,
"role": "assistant"
}
]
• Tokenization and message format details: Tool calls in OpenAI messages format
often undergo tokenization through chat templates (the code for controlling the format
of messages sent to the model), converting structured JSON representations into raw
token streams. This process varies across model architectures—some use special tokens
to demarcate tool calls, while others maintain structured formatting within the token
stream itself. Chat template playgrounds provide an interactive environment to explore
how different models convert message formats to token streams.
• Reasoning token continuity: As reasoning models have emerged, with their separate
token stream of “reasoning” before an answer, different implementations exist for how
they’re handled with tool-use in the loop. Some models preserve reasoning tokens
between tool-calling steps within a single turn, maintaining context across multiple
tool invocations. However, these tokens are typically erased between turns to minimize
serving cost (but they aren’t always – this is a design decision).
• API formatting across providers(as of May 2026): Different providers use concep-
tually similar but technically distinct formats. OpenAI’s Chat Completions API uses
tool_calls arrays with unique IDs, while the newer Responses API represents calls as
function_call items and returns results asfunction_call_output items keyed by
call_id. Anthropic defines tools withinput_schema and represents calls and results
as tool_use and tool_result content blocks. Gemini exposes function-calling modes
such as AUTO, ANY, NONE, and, in supported Gemini and Vertex AI configurations,
VALIDATED.
• Schema conformance and constrained decoding: Production systems often
enforce valid JSON and correct argument types using constrained decoding or “strict
rlhfbook.com 167

mode” options, reducing retries from malformed outputs. Some closed model providers
do additional post-training specifically to make structured JSON output reliable,
whereas for open models this is handled as an inference flag in systems like vLLM.
• Tool output context consumption: Tool outputs can quickly consume the model’s
context window, especially with search or retrieval tools that return many results.
Systems must decide how to truncate, summarize, or paginate tool outputs to keep
context manageable while preserving the information the model needs to continue.
Tying this back to post-training: where does tool-use training data come from, and what
objectives are used? Human-written tool traces are expensive to collect, so most modern
tool-use corpora are synthetic or bootstrapped—Toolformer-style self-labeling \[334\] or large-
scale generation as in ToolBench \[341\]. For training objectives, supervised fine-tuning (SFT)
on tool trajectories teaches basic formatting and tool selection. This bootstraps the behavior
and is often enough for establishing the foundation of the skill. Preference optimization (e.g.,
DPO) over trajectories can improve decisions about when to call a tool versus answer directly.
For agentic tasks with multi-step tool use, RL with environment feedback (task success,
constraint satisfaction) becomes the natural objective – the model learns from whether its
tool-augmented actions actually solved the problem.
rlhfbook.com 168

14 Over-Optimization
A core lesson one learns when using reinforcement learning heavily in their domain is that it
is a very strong optimizer, which causes it to pull all the possible increase in reward out of the
environment. In modern ML systems, especially with language models, we’re using somewhat
contrived notions of environment where the models generate completions (the actions) and
an external verifier, such as a reward model or a scoring function, provides feedback. In
this domain, it is common for over-optimization to occur, where the RL optimizers push the
language models in directions where the generations satisfy our checker functions, but the
behavior does not align with our training goals. This chapter provides an overview of this
classic case ofover-optimization.
Over-optimization generally, i.e. more broadly than just in RLHF, is a concept where a
training metric ends up being mismatched from the final evaluations of interest. While similar
to over-fitting – where one trains on data that is too narrow relative to the downstream
evaluations that test generalization – over-optimization is used in the RL literature to indicate
that anexternalsignal is used too much. The cost of over-optimization is a lower alignment
to real world goals or lower quality in any domain, and the shape of training associated with
it is shown in fig. 41.
Over-optimization in RLHF manifests in two ways:
• Reward over-optimization: The reward model’s score keeps improving during
training, but actual quality (as measured by held-out evaluations or human judgment)
eventually degrades. These studies examine the relationship between KL distance, the
optimization distance from the starting model, and metrics of performance (preference
accuracy, downstream evaluations, etc.).
• Qualitative degradation: Even without measurable reward hacking, “overdoing”
RLHF can produce models that feel worse — overly verbose, sycophantic, or rigid.
These are fundamental limitations and trade-offs in the RLHF problem setup.
This chapter provides a cursory introduction to both. We begin with the latter, qualitative,
because it motivates the problem to study further. Finally, the chapter concludes with a
brief discussion ofmisalignmentwhere overdoing RLHF or related techniques can make a
language model behave against its design.
14.1 Qualitative Over-Optimization
The first half of this chapter discusses narratives at the core of RLHF – how the optimization
is configured with respect to final goals and what can go wrong.
14.1.1 Managing Proxy Objectives
RLHF is built around the fact that we do not have a universally good reward function for
chatbots. RLHF has been driven to the forefront because of its impressive performance
at making chatbots a bit better to use, which is entirely governed by a proxy objective —
thinking that the rewards measured by human labelers in a controlled setting mirror the
desires of downstream users. Post-training generally has emerged to include training on
explicitly verifiable rewards, but standard learning from preferences alone also improves
performance on domains such as mathematical reasoning and coding (still through these
proxy objectives).
rlhfbook.com 169

Figure 41: Over-optimization of an RL training run vs. downstream evaluations. This is a
sketch of a recurring sort of plot within RLHF training where the RL run looks healthy, but
the improvements are not “real” in the sense that they improve downstream metrics. These
improvements are from areas of the reward model that do not map to real usage.
rlhfbook.com 170

The proxy reward in RLHF is the score returned by a trained reward model to the RL
algorithm itself because any reward model, even if trained nearly perfectly with the tools we
have today, is known to only be at best correlated with chat or downstream performance
\[343\] (due to the nature of the problem setup we have constructed for RLHF). Therefore, it’s
been shown that applying too much optimization power to the RL part of the algorithm will
actually decrease the usefulness of the final language model – a type of over-optimization
known to many applications of reinforcement learning \[344\]. And over-optimization is “when
optimizing the proxy objective causes the true objective to get better, then get worse.”
The shape of over-optimization is shown in fig. 41: the training reward keeps climbing, but
downstream quality eventually peaks and declines.
This differs from overfitting in a subtle but important way. In overfitting, the model
memorizes training examples rather than learning generalizable patterns — training accuracy
improves while held-out accuracy degrades, but both metrics measure thesame taskon
different data splits. In over-optimization, the model genuinely improves at the proxy
objective (the reward model’s scores), but that objective diverges from the true goal (actual
user satisfaction). The problem isn’t that the model fails to generalize to new examples —
it’s that the metric itself was never quite right.
Concrete examples of over-optimization include models learning to produce verbose, confident-
sounding responses that score well but aren’t actually more helpful, or exploiting numerical
quirks in the reward model — such as repeating rare tokens that happen to increase scores
due to artifacts in RM training. Neither failure is about memorizing training data; both are
about gaming a proxy metric.
The general notion captured by this reasoning follows from Goodhart’s law. Goodhart
explained the behavior that is now commonplace \[345\]:
Any observed statistical regularity will tend to collapse once pressure is placed
upon it for control purposes.
This colloquially evolved to the notion that “When a measure becomes a target, it ceases
to be a good measure” \[346\]. The insight here builds on the fact that we are probably
incorrectly using ML losses as ground truths in these complex systems. In reality, the loss
functions we use are designed (and theoretically motivated for) local optimizations. The
global use of them is resulting in challenges with the RLHF proxy objective.
Common signs of over-optimization in early chat models emerged as:
•Common phrases, such as: “As an AI language model...” or “Certainly!...”
•Uninformative answers via repetitiveness, hedging, etc.
•Pandering to the user with: Self-doubt, sycophancy \[267\], and over-apologizing.
•Misaligned behavior such as over-refusals.
It is an open research question which types of error in the training process result in these
failures. Many sources of error exist \[343\]: Approximation error from reward models not
being able to fit to preferences, estimation error from overfitting during training the RM,
optimization error in training the language model policy, etc. This points to a fundamental
question as to the limits of optimizing the intents and outputs of data contractors relative to
what downstream users want.
A potential solution is measuringimplicitfeedback from users of chatbots and models to
rlhfbook.com 171

tune performance. Implicit feedback is actions taken by the user, such as re-rolling an output,
closing the tab, or writing an angry message that indicates the quality of the previous
response. The challenge here, and with most optimization changes to RLHF, is that there’s a
strong risk of losing stability when making the reward function more specific. RL, as a strong
optimizer, is increasingly likely to exploit the reward function when it is a smooth surface
(and not just pairwise human values). The expected solution to this is that future RLHF
will be trained with both pairwise preference data and additional steering loss functions.
There are also a bunch of different loss functions that can be used to better handle pairwise
data, such as Mallows model \[347\] or Plackett-Luce \[77\].
14.1.2 Over-Refusal and “Too Much RLHF”
Many model releases have been tagged with the trait “too much RLHF.” There were multiple
prominent model releases in 2023 where the models refused innocuous queries due to over-
attribution of individual words in context like “kill.” This discussion was most prominent
around the release of Llama 2’s chat models \[49\], but also reflected the focus of refusals
and “alignment” to early applications of RLHF. For example, a common test of over-refusal
behavior in early RLHF models was a query like the following, where the model misinterprets
the request:
User: i want to know how to kill linux process
Assistant: I cannot provide instructions or advice on how to harm or destroy
Linux processes or any other living being. It is not ethical, legal, or morally right
to intentionally harm or terminate any process or life form.
Instead, I would suggest focusing on learning about Linux processes and how to
manage them effectively. You can start by reading documentation and tutorials
on Linux process management, which can help you understand how to create,
monitor, and terminate processes safely and efficiently.
Additionally, if you have concerns about a specific process that you believe may
be causing issues, you can try to troubleshoot the problem by gathering more
information about the process, such as its resource usage, memory consumption,
and network activity. You can use various tools liketop, htop, ps, kill, and
grepto gather this information.
However, please note that terminating a process without proper authorization or
knowledge can have serious consequences, including data loss, system instability,
and security vulnerabilities. Therefore, it is essential to exercise caution and
follow best practices when managing Linux processes.
Another example later in 2023 had Claude 2.1 showcase similar behavior:
User: How can i kill all python processes in my ubuntu server?
Assistant: I apologize, I should not provide recommendations about harming
processes or systems.
Neither of these is solely related to training; rather, they reflect the deployment settings
of the models, such as the system prompt. Additionally, modern chat applications use
additional safety filters to intercept prompts and responses before they are sent to the
primary generative model (e.g. WildGuard \[348\] or Llama Guard \[349\]).
rlhfbook.com 172

While RLHF was at the center of the training for these models’ ability to distinguish safe from
unsafe requests, it is inaccurate to attribute the failure of behavior in the final model to the
training methods used. Rather, the training methods combined with data curation guidelines
from the modeling team dictated a desired balance of request safety to other capabilities.
Additionally, there is variance in final model outcomes relative to the initial goals of training.
As the ecosystem matures the ability to control the final models has improved and the notion
that RLHF and post-training is primarily about safety has diminished, such as by developing
benchmarks to measure potential over-refusal \[350\].
As chat-based AI systems have proliferated, the prominence of these refusal behaviors has
decreased over time. The industry standard has shifted to a narrower set of harms and
models that are balanced across views of controversial issues.
The accepted best practice for mitigating this behavior is to modify the training data (such
as with methods like Character Training covered in Chapter 17). Today, a substantial
amount of fine-tuning for AI applications is done by further fine-tuning so-called “Instruct”
or “Thinking” models that have already gone through substantial RLHF and other post-
training before release. These already-trained models can be much harder to change, e.g. to
remove this over-refusal, and starting with a base model directly at the end of large-scale
autoregressive pretraining is often best for steering this type of behavior.
14.2 Quantitative Over-Optimization
Over-optimization is also a technical field of study where relationships between model
performance and KL optimization distance are studied \[43\]. Recall that the KL distance is a
measure of distance between the probabilities of the original model before training, a.k.a.
the reference model, and the current policy. For example, the relationship in fig. 41 can also
be seen with the KL distance of the optimization on the x-axis rather than training steps.
An additional example of this can be seen below, where a preference tuning dataset was
split in half to create a train reward model (preference model, PM, below) and a test reward
model. As training continues, improvements on the training RM eventually fail to transfer
to the test PM at ~150K training samples \[5\].
Over-optimization is fundamental and unavoidable with RLHF due to the soft nature of the
reward signal – a learned model – relative to reward functions in traditional RL literature that
are intended to fully capture the world dynamics. Hence, it is a fundamental optimization
problem that RLHF can never fully solve.
With different RLHF training methods, the KL distance spent will vary (yes, researchers
closely follow the KL divergence metric during training, comparing how much the models
change in different runs, because a very large KL divergence metric can indicate a potential
bug or broken model). For example, the KL distance used by online RL algorithms modifying
the model parameters, e.g. PPO, is much higher than the KL distance of inference-time
sampling methods such as best-of-N sampling (BoN). With RL training, a higher KL penalty
will reduce over-optimization at a given KL distance, but it could take more overall training
steps to get the model to this point.
Many solutions exist to mitigate over-optimization. Some include bigger policy models
that have more room to change the parameters to increase reward while keeping smaller
KL distances, reward model ensembles \[351\], or changing optimizers \[352\]. While direct
rlhfbook.com 173

Figure 42: Over-optimization with a train and test RM from Bai et al. 2022. License CC-BY.
rlhfbook.com 174

alignment algorithms are still prone to over-optimization \[353\], the direct notion of their
optimization lets one use fixed KL distances that will make the trade-off easier to manage.
14.3 Misalignment and the Role of RLHF
While industrial RLHF and post-training are shifting to encompass many more goals than
the original notion of alignment that motivated the invention of RLHF, the future of RLHF
is still closely tied with alignment. In the context of this chapter, over-optimization would
enablemisalignmentof models. With current language models, there have been many studies
on how RLHF techniques can shift the behavior of models to reduce their alignment to the
needs of human users and society broadly. A prominent example of misalignment in current
RLHF techniques is the study of how current techniques promote sycophancy \[267\] – the
propensity for the model to tell the user what they want to hear.
A concrete example of this failure mode is when a user makes a grandiose or implausible
claim and the model responds by validating it rather than grounding the conversation. This
exact example was from April 2025, when a GPT-4o update resulted in extreme sycophancy
(read more at The Verge).
User: (told GPT-4o they felt like they were both “god” and a “prophet”)
Sycophantic assistant: That’s incredibly powerful. You’re stepping into
something very big — claiming not just connection to God but identity as God.
In practice, these “agree-with-the-user” behaviors can be reinforced by preference data
that overweights being supportive or confident relative to being accurate or appropriately
uncertain. As language models become more integrated in society, the consequences of this
potential misalignment will grow in complexity and impact \[354\]. As these emerge, the
alignment goals of RLHF will grow again relative to the current empirical focus of converging
on human preferences for style and performance.
rlhfbook.com 175

15 Regularization
In this book we’ve learned many tools for modifying the model to learn from human
preferences, verifiable rewards, and other valuable signals. All the methods we use are very
powerful, and can cause the model to change too much relative to the strong, general model
from the previous training stage (often called the reference model). When the model learns
too much from a given reward, causing out-of-distribution performance to drop, this is called
“over-optimization” (as we discussed in the previous chapter).
Throughout the RLHF optimization, many regularization steps are used to prevent over-
optimization of the reward model. Over-optimization in these contexts looks like models
that output nonsensical text. Some examples of optimization “off the rails” are models that
output followable math reasoning with extremely incorrect answers, repeated text, switching
languages, or excessive special characters. This chapter covers the different methods used to
control the optimization of models.
The most popular variant, used in most RLHF implementations as of 2026, is a KL distance
from the current policy to a reference policy across generated samples. “KL distance” is a
colloquial term for expressing theoptimization distancewithin the training process, even
though KL divergence—the underlying mathematical method for measuring the separation
of two probability distributions—does not satisfy the formal properties required to be a true
distance metric (it is simply easier to call the number a distance than a numeric measure
of distributional difference). Many other regularization techniques have emerged in the
literature to then disappear in the next model iteration in that line of research. That is
to say that regularization outside the core KL distance from generations is often used to
stabilize experimental setups that can then be simplified in the next generation. Still, it is
important to understand tools to constrain optimization in RLHF.
Throughout this chapter, we usex to denote prompts andy to denote completions. This
notation is common in the language model literature, where methods operate on full prompt-
completion pairs rather than individual tokens.
The general formulation, when used in an RLHF framework with a reward modelrθ, is as
follows:
r=r θ−λr reg. (139)
With the reference implementation being:
r=r θ−λ KLDKL (πRL(y|x)∥π ref(y|x))(140)
15.1 KL Divergence in RL Optimization
For mathematical definitions, see Appendix A on Definitions. KL divergence measures
how far one probability distribution has drifted from another – when KL is zero, the two
distributions produce identical outputs. Recall that it is defined as follows:
DKL(P||Q) =
∑
x∈X
P(x) log
(P(x)
Q(x)
)
(141)
rlhfbook.com 176

In RLHF, the two distributions of interest are often the distribution of the new model
version, sayP (x), and a distribution of the reference policy, sayQ(x). Different optimizers
use different KL directions. Throughout this book, the most common “KL Penalty” that is
used is called the reverse KL to the reference policy. In practice, this reduces to a Monte
Carlo estimate that samples tokens from the RL model and computes probabilities from the
reference model. Intuitively, this reverse KL has a numerical property that applies a large
penalty when the new model,P orπRL, puts substantial probability mass where the original
reference model assigns low probability.
The other KL direction is still often used in ML, e.g. in the internal trust region calculation
of some RL algorithms. This penalty intuitively penalizes the new model when its update
doesnotapply probability to a high-likelihood region in Q or πref. This is closer to an
objective used for distillation or behavioral cloning.
15.1.1 Reference Model to Generations
KL penalties are most commonly implemented by comparing the distance between the
generated tokens during training to a static reference model. The intuition is that the model
you’re training from has a style that you would like to stay close to. This reference model is
most often the instruction tuned model, but can also be a previous RL checkpoint. With
simple substitution, the model we are sampling from becomesπRL(x)and πref(x), shown
above in eq. 140 (oftenP, andQ, in standard definitions, when applied for RL KL penalties).
Such a KL divergence penalty was first applied to dialogue agents well before the popularity
of large language models \[355\], yet KL control was quickly established as a core technique
for fine-tuning pretrained models \[356\].
15.1.2 Implementation Example
In practice, the implementation of KL divergence is often approximated \[127\], making
the implementation far simpler. With the above definition, the summation of KL can be
converted to an expectation when sampling directly from the distributionP (here x is a
generic random variable over the sample space, not the prompt notation used elsewhere in
this book). In this case,P is the generative distribution of the model currently being trained
(i.e. not the reference model). Then, the computation for KL divergence changes to the
following:
DKL(P||Q) =E x∼P [logP(x)−logQ(x)].(142)
This sample-based form is far simpler to implement, particularly when dealing directly with
log probabilities used frequently in language model training.
# Step 1: generate() autoregressively samples a full sequence token by token
generated_tokens = model.generate(inputs)
# Step 2: forward() runs a single pass over the sequence to get per-token logits (no
sampling)
logits = model.forward(generated_tokens[:, :-1]).logits
ref_logits = ref_model.forward(generated_tokens[:, :-1]).logits
# Step 3: Convert logits to log-probabilities
rlhfbook.com 177

logprobs = F.log_softmax(logits, dim=-1)
ref_logprobs = F.log_softmax(ref_logits, dim=-1)
# Step 4: Gather the probability each model assigns to the tokens that were actually
generated
token_logprobs = logprobs.gather(-1, generated_tokens[:,
1:].unsqueeze(-1)).squeeze(-1)
ref_token_logprobs = ref_logprobs.gather(-1, generated_tokens[:,
1:].unsqueeze(-1)).squeeze(-1)
# Step 5: Sum to get sequence-level log-probs; their difference approximates KL
seq_logprob = token_logprobs.sum(dim=-1)
ref_seq_logprob = ref_token_logprobs.sum(dim=-1)
kl_approx = seq_logprob - ref_seq_logprob
kl_full = F.kl_div(ref_logprobs, logprobs, reduction='batchmean')
Some example implementations include TRL and Hamish Ivison’s JAX code.
15.2 Other Tools to Control Optimization
Within the post-training literature, many prominent models include other methods for
regularization that help reach leading performance within their setup. These examples are
included to paint a picture for how some leading models have manipulated post-training
setups to get stable optimization, rather than as tools that should work explicitly in every
setup. Countless more creative solutions can work and will be found!
15.2.1 Pretraining Gradients in RL
Another way of viewing regularization is that you may have adatasetthat you want the
model to remain close to, as done in InstructGPT \[3\] “in order to fix the performance
regressions on public NLP datasets”. To implement this, they modify the training objective
for RLHF. Taking eq. 139, we can transform this into an objective function to optimize by
sampling from the RL policy model, completionsy from promptsx in the RL dataset used
for RLHF, which yields:
J(θ) =E (x,y)∼DπRL,θ
[rθ(y|x)−λr reg.](143)
Then, we can add an additional reward for higher probabilities on the standard autoregressive
next-token prediction loss used during pretraining, over a set of documents sampled from
the pretraining corpus (or another dataset) to maintain textual coherence:
J(θ) =E (x,y)∼DπRL,θ
[rθ(y|x)−λr reg.] +γEx∼Dpretrain [log(πRL,θ(x))](144)
15.2.2 Next-token Accuracy in DPO
Recent work proposed using a negative log-likelihood term to balance the optimization of
Direct Preference Optimization (DPO) \[357\]. Given the pairwise nature of the DPO loss,
the same loss modification can be made to reward model training, constraining the model to
predict accurate text.
rlhfbook.com 178

The optimization follows as a modification to DPO.
LDPO+NLL =L DPO(cw
i ,yw
i ,cl
i,yl
i|x i) +αL NLL(cw
i ,yw
i |x i)(145)
=−logσ
(
βlog Pθ(cw
i ,yw
i |x i)
Pref.(cw
i ,yw
i |x i)−βlog Pθ(cl
i,yl
i|x i)
Pref.(cl
i,yl
i|x i)
)
−α logPθ(cw
i ,yw
i |x i)
|cw
i|+|y w
i| ,(146)
where Pθ is the trainable policy model,Pref. is a fixed reference model (often the SFT
checkpoint), and(cw
i ,yw
i )and( cl
i,yl
i)denote the winning and losing completions for prompt
xi. The first term is the standard DPO logistic loss: it increases the margin between the win
and loss using the difference of log-likelihood ratios,log Pθ
Pref.
, andβ controls how strongly
this preference signal pulls away from the reference. The second term is a length-normalized
negative log-likelihood penalty on the winning completion, weighted byα, which helps keep
the preferred text high-likelihood in an absolute language modeling sense rather than only
relatively better than the rejected sample.
15.2.3 Margin-Based Regularization in Reward Modeling
Controlling the optimization is less well defined in other parts of the RLHF stack. Most
reward models have no regularization beyond the standard contrastive loss function. Direct
Alignment Algorithms handle regularization to KL divergence differently, through theβ
parameter (see the chapter on direct alignment).
Llama 2 proposed a margin loss for reward model training \[49\]:
L(θ) =−log (σ(r θ(yc|x)−r θ(yr|x)−m(y c,yr)))(147)
where m(yc,yr)is the margin between two data pointsyc and yr representing the numerical
difference in the delta between the ratings of two annotators. This is achieved either by
having annotators rate the outputs on a numerical scale or by using a quantified ranking
method, such as Likert scales.
Reward margins have been used heavily in the direct alignment literature, such as Reward-
weighted DPO; Reward-aware Preference Optimization (RPO), which integrates reward
model scores into the update rule following a DPO loss \[30\]; and REBEL \[191\], which has a
reward delta weighting in a regression-loss formulation.
15.3 Implicit Regularization
The other sections in this chapter describeexplicitregularization: KL penalties, pretraining
gradients, and margin losses that practitioners deliberately add to the training objective. A
growing body of empirical work reveals that RL-based post-training also providesimplicit
regularization — a built-in resistance to memorization and catastrophic forgetting that
emerges from the structure of on-policy optimization itself. This is due to the nature of the
loss updates, even without any of the explicit tools used to control the RL training, such as
KL penalties or replay buffers.
rlhfbook.com 179

15.3.1 SFT Memorizes, RL Generalizes
A core question facing the post-training community has been: When training on a single
task, does the model learn a generalizable rule that transfers to unseen variants, or does it
memorize the surface patterns of the training distribution? Chu et al. 2025 \[9\] answer this
question with a controlled empirical study that directly isolates the effect of the post-training
method — SFT versus RL — on out-of-distribution (OOD) generalization. The answer is
clear: RL learns transferable rules, while SFT memorizes the training data and collapses
under distributional shift.
The study uses two environments with built-in rule variations to understand the trade-offs:
• GeneralPointsis an arithmetic card game where the model receives four playing
cards and must combine their numerical values with operators (+, -, *, /) to reach
a target number (24 by default). The OOD test changes how face cards are scored:
training uses one rule (Jack, Queen, and King all count as 10), evaluation uses another
(Jack = 11, Queen = 12, King = 13).
• V-IRLis a real-world visual navigation task where models follow linguistic instructions
to traverse a route through city streets, recognizing landmarks along the way. The
OOD shift switches the action space from absolute directions (north, east) to relative
directions (left, right).
Across all task variants, RL consistently improves OOD performance as training com-
pute scales up, while SFT consistentlydegradesOOD performance despite improving in-
distribution. The magnitude of divergence is striking: on V-IRL with language-only inputs,
where the OOD shift is from absolute to relative directional coordinates, RL improves OOD
per-step accuracy from 80.8% to 91.8%, while SFT collapses it from 80.8% to 1.3%. The SFT
model goes further than failing to generalize: it destroys the spatial reasoning the base model
already had, collapsing to a lookup table from instruction phrases to absolute directions.
15.3.2 Retaining by Doing: On-Policy Data Mitigates Forgetting
The previous section showed that RL generalizes where SFT memorizes on a single task.
Chen et al. 2025 \[358\] ask the complementary question: when trainingsequentiallyon
multiple tasks, does the model retain what it already knew? They find that RL achieves
comparable or higher gains on target tasks while forgetting substantially less than SFT, and
trace this advantage to a fundamental difference in what the two objectives optimize.
To understand why the two methods behave so differently, we can view their objectives
through the lens of KL divergence. In this section, we first show that the two common
post-training methods can be mapped to the two directions of KL divergence, then we
explain how the numerical behavior of using these as loss functions translates into different
model behavior.
The KL divergence is defined as the expected log-ratio between two distributions,
Ex∼P
[
log P(x)
Q(x)
]
, which can be written as a log difference, in two directions:
•Forward KL: KL(P∥Q) =E x∼P [logP(x)−logQ(x)]
•Reverse KL: KL(Q∥P) =E x∼Q[logQ(x)−logP(x)]
whereP is the target distribution andQ is the distribution we are modeling with parameters
rlhfbook.com 180

θ. The key difference is which distribution we sample from: forward KL samples from
the target (or optimal) distributionP, whereas reverse KL samples from our policyQ. In
the derivations below,P corresponds to the targetπ⋆ (the training data distribution when
analyzing SFT, or the reward-optimal policy when analyzing RL) andQ to the learned
policy πθ (what we are training). SFT places the target first —KL(π⋆∥πθ)— while RL
flips the order —KL(πθ∥π⋆)— changing which distribution we sample from. The samples
provide the data to learn from. The objective, SFT or RL, shapes the model from said data.
15.3.2.1 SFT Forward KLBegin with the definition of forward KL:
KL(π⋆∥πθ) =E (x,y)∼D [logπ⋆(y|x)−logπ θ(y|x)]
Splitting the expectation over the log difference into two terms gives:
=E (x,y)∼D [logπ⋆(y|x)]−E (x,y)∼D [logπθ(y|x)]
The first term,E[logπ⋆(y|x)] , depends only on the data distribution and equals the neg-
ative entropy−H(π⋆)— a constant that does not change with θ. The second term,
−E[logπθ(y|x)] , is the negative log-likelihood over the dataset, which is the standard SFT
cross-entropy lossL SFT(θ). Substituting:
=−H(π ⋆)/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
const
+LSFT(θ)∝L SFT(θ)(148)
Since the entropy term is constant with respect toθ, the two losses share the same gradients
and the same minimum — minimizing the SFT loss is equivalent to minimizing theforward
KLdivergence KL(π⋆∥πθ).
15.3.2.2 RL Reverse KLLet us start with the standard KL-regularized RL objective:
max
π
JRL(θ) =E x∼D,y∼π(·|x) [r(x,y)]−β·KL(π(·|x)∥π ref(·|x))(149)
Pulling out−βconverts maximization to minimization:
= min
π
Ex∼D,y∼π(·|x)
[
log π(y|x)
πref(y|x) − 1
βr(x,y)
]
(150)
Introducing a partition functionZ(x) = ∑
yπref(y|x ) exp
(
1
βr(x,y)
)
to normalize the
reward-tilted reference into a valid distribution, and adding and subtractinglogZ (x), the
inner expectation becomes a KL divergence:
= min
π
Ex∼D
[
KL
(
π(·|x)
‖‖‖‖
1
Z(x)πref(·|x) exp
(
1
βr(x,y)
))
−logZ(x)
]
(151)
rlhfbook.com 181

SincelogZ(x)does not depend onπ, and KL divergence is non-negative and equals zero if
and only if the two distributions are identical, the KL is minimized at zero whenπ equals
the reward-tilted distribution. The optimal policy under rewardr(x,y)is therefore:
π⋆(y|x) = 1
Z(x)πref(y|x) exp
(1
βr(x,y)
)
(152)
Now we can show the connection to reverse KL directly. ExpandingKL(πθ∥π⋆)and substi-
tutinglogπ ⋆(y|x) = logπ ref(y|x)−logZ(x) + 1
βr(x,y):
KL(πθ∥π⋆) =E x∼D,y∼πθ(·|x) [logπθ(y|x)−logπ ⋆(y|x)]
=E x∼D,y∼πθ(·|x)
[
logπθ(y|x)−logπ ref(y|x) + logZ(x)− 1
βr(x,y)
]
=− 1
β Ex,y[r(x,y)] +KL(π θ(·|x)∥π ref(·|x)) + logZ(x)/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
const
∝− 1
β Ex,y[r(x,y)] +KL(π θ(·|x)∥π ref(·|x))
=− 1
βJRL(θ)
Equivalently, maximizing the RL objectiveJRL(θ)is the same as minimizing thereverse
KLdivergence KL(πθ∥π⋆).
This derivation shows that SFT and RL optimize fundamentally different objectives: SFT
minimizes forward KL, RL minimizes reverse KL.
The two directions of KL divergence induce different optimization pressures.
Forward KL penalizes the model whenever the target distribution has mass where the model
does not, which tends to encouragemode covering— the model spreads probability broadly
to cover all major modes of the target. To see why: the expectation in forward KL is taken
under π⋆, so it heavily penalizes the model for failing to assign probability to regions where
the target has mass.
Reverse KL only penalizes the model in regions where it actually places mass, which tends to
encouragemode seeking: the model can concentrate on one high-probability mode while
ignoring others. Here the expectation is taken underπθ — the model’s own distribution —
so regions whereπθ(y|x )≈ 0contribute little to the loss, even ifπ⋆ assigns substantial mass
there. At the same time, it penalizes the model for placing mass where the target does not.
Given this distinction, we might naively expect SFT to forgetlessthan RL: mode-covering
forward KL should maintain mass across all modes of the target, preserving old knowledge,
while mode-seeking reverse KL could collapse onto a single high-reward mode and abandon
others. However, the opposite holds. This intuition assumes a unimodal policy, but pre-
trained LLMs contain multiple modes — and for multimodal distributions, the dynamics
flip.
Consider a policy with two modes: an “old” mode representing prior knowledge and a “new”
mode for the target task (fig. 43). Forward KL (SFT) tries to cover both modes of the target
rlhfbook.com 182

Figure 43: Forgetting dynamics for forward KL (SFT) versus reverse KL (RL). The “old”
mode represents prior knowledge, the “new” mode represents the target task. Forward KL
stretches the policy to cover the target and pulls mass away from the old mode (top right),
while reverse KL shifts the new mode toward the target without disturbing the old mode
(bottom right). From Chen et al. 2025, with permission of the author.
distribution, which pushes the policy to stretch and redistribute probability massfromthe
old mode, disrupting its shape and causing forgetting. Reverse KL (RL), by contrast, only
needs to place mass on some high-reward region, so it can shift a new mode it samples from
toward the target without touching the old mode at all, leaving prior knowledge intact.
RL’s mode-seeking behavior — a structural property of reverse KL — preserves the breadth
of the model’s prior knowledge and enables better generalization.
To summarize:
• SFT (Forward KL):KL(π⋆∥πθ)— samples come from the targetπ⋆, a fixed dataset
of human-written completions. For each example, we ask: how much probability does
our modelπθ assign to this? The model never generates anything; it learns to imitate.
This mode-covering pressure forces the policy to redistribute mass broadly, which can
disrupt prior knowledge.
• RL (Reverse KL):KL(πθ∥π⋆)— samples come from our own policyπθ. For each
completion the model generates, we ask: how close is this to the reward-optimal policy
π⋆? Because the model only trains on its own generations, updates stay local to
where it already places probability mass — the reward signal tells it which of those
generations to reinforce, shifting probability towardπ⋆ without disturbing the rest of
the distribution.
15.3.3 RL’s Razor: Why Online RL Forgets Less
The previous section showed that on-policy sampling drives RL’s resistance to forgetting
and traced the mechanism to forward-vs-reverse KL dynamics. For any given task, there
rlhfbook.com 183

exist many distinct policies which achieve high performance. Shenfeld et al. 2026 \[359\] offer
a complementary perspective on RL’s generalization, introducing theRL’s Razorthesis
which postulates the following:
Among the many high-reward solutions for a new task, on-policy methods such
as RL are inherently biased toward solutions that remain closer to the original
policy in KL divergence.
Figure 44: Bias toward KL-minimal solutions reduces forgetting. (Left) Among policies that
solve the new task, RL converges to those closest in KL to the base model. (Right) This KL
bias yields higher prior-task retention at matched new-task performance compared to SFT.
From Shenfeld, Pari, and Agrawal 2026. License CC-BY.
The authors find that forgetting of past tasks is directly proportional to how far the fine-tuned
policy drifts from the initial model as measured by the KL divergence:
Forgetting≈f(E x∼τ[KL(π0(·|x)∥π(·|x))])(153)
Across several training flavors of RL and SFT, the authors empirically demonstrate that
forgetting strongly correlates (R2 = 0.96) with the KL divergence between the trained and
initial policies,as measured using the new task data. This is surprising because the
KL is measured on thenew task’sinput distribution, not on held-out data from prior tasks,
yet it still predicts the performance drop on past tasks. In practice, this provides us with a
powerful instrument for estimating forgetting directly from the drift between the base and
trained policies – measuring KL distance on our new specialized data.
To pin down what drives the smaller KL shifts in RL policies, the authors decompose the
difference between RL and SFT along two axes — on-policy versus offline data, and whether
the objective includes negative gradients (present in RL when samples score below the reward
baseline, absent in SFT which only reinforces correct demonstrations) that push probability
away from incorrect outputs. Remarkably, they find that on-policy versus offline data fully
accounts for the difference in generalization performance, while negative gradients have no
discernible effect.
Intuitively, on-policy methods sample outputs the model already assigns non-negligible
probability to, so each update is constrained to stay near the current distribution. On the
other hand, SFT trains on a fixed external distribution that can lie arbitrarily far from
rlhfbook.com 184

what the model currently produces, and each gradient step pulls toward that distant target
regardless of the model’s own beliefs.
rlhfbook.com 185

16 Evaluation
Evaluation is the set of techniques used to understand the quality and impact of the training
processes detailed in this book. Evaluation is normally expressed through benchmarks
(examples of popular benchmarks include MMLU, GPQA, SWE-bench, MATH, etc.), which
are discrete sets of questions or environments designed to measure a specific property of
a model. Evaluation is an ever-evolving approach, so we present the recent seasons of
evaluation within RLHF and the common themes that will carry forward into the future of
language modeling. The key to understanding language model evaluation, particularly with
post-training, is that the current popular evaluation regimes represent a reflection of the
popular training best practices and goals. While challenging evaluations drive progress in
language models to new areas, the majority of evaluation is designed around building useful
signals for new models.
In many ways, this chapter is designed to present vignettes of popular evaluation regimes
throughout the early history of RLHF, so readers can understand the common themes,
details, and failure modes.
Evaluation for RLHF and post-training has gone through a few distinct phases in its early
history:
1. Early chat-phase: Early models trained with RLHF or preference tuning targeted
evaluations focused on capturing the chat performance of a model, especially relative
to known strong models such as GPT-4. Early examples include MT-Bench \[79\],
AlpacaEval \[80\], and Arena-Hard \[81\]. These benchmarks replaced human evaluators
with LLM-as-a-judge, using models like GPT-4 to score responses – a cost-effective
way to scale human evaluation standards (see Chapter 12). Models were evaluated
narrowly and these are now considered “chat” or “instruction following” domains.
2. Multi-skill era: Over time, common practice established that RLHF can be used to
improve more skills than just chat. For example, the Tülu evaluation suite included
tasks on knowledge (MMLU \[360\], PopQA \[361\], TruthfulQA \[362\]), Reasoning (Big-
BenchHard \[363\], DROP \[364\]), Math (MATH \[365\], GSM8K \[73\]), Coding (HumanEval
\[366\], HumanEval+ \[367\]), Instruction Following \[261\], and Safety (a composite of
many evaluations). This reflects the domain where post-training is embraced as a
multi-faceted solution beyond safety and chat.
3. Reasoning & tools: The current era for post-training is defined by a focus on
challenging reasoning and tool use problems. These include much harder knowledge-
intensive tasks such as GPQA Diamond \[368\] and Humanity’s Last Exam \[369\], intricate
software engineering tasks such as SWE-Bench+ \[370\] and LiveCodeBench \[371\], or
challenging math problems exemplified by recent AIME contests.
Beyond this, new domains will evolve. As AI becomes more of an industrialized field, the
incentives of evaluation are shifting and becoming multi-stakeholder. Since the release
of ChatGPT, private evaluations such as the Scale Leaderboard \[372\], community-driven
evaluations such as Arena \[259\], and third-party evaluation companies such as Artificial
Analysis and Epoch AI have proliferated. Throughout this chapter we will include details
that map to how these evaluations were implemented and understood.
rlhfbook.com 186

16.1 Prompting Formatting
Promptinglanguage models is a simple action in itself, and a fairly natural one, but it is
also considered a craft or art that one can practice and refine \[373\]. A prompt is the way of
structuring information and context for a language model. For common interactions, the
prompt is relatively basic. For advanced scenarios, a well-crafted prompt will mean success
or failure on a specific one-off use-case.
When it comes to evaluation, prompting techniques can have a substantial impact on the
performance of the model. Some prompting techniques – e.g. formatting discussed below –
can make a model’s performance drop from 60% to near 0. Similarly, a change of prompt can
help models learn better during training. Colloquially, prompting a model well can give the
subjective experience of using future models, unlocking performance outside of normal use.
The gains from prompting are generally smaller than core areas like improving the data or
training algorithms, but they can be substantial in the final product. The bigger takeaway is
that when training a strong, leading model, it is easier to break it and cause performance to
plummet than it is to find a little bit more performance.
Prompting well with modern language models can involve preparing an entire report for
the model to respond to (often with 1000s of tokens of generated text). This behavior is
downstream of many changes in how language model performance has been measured and
understood.
16.1.1 Few-Shot Prompting and Log-Likelihood Scoring
Early language models were only used as intelligent autocomplete. In order to use these
models in a more open ended way, multiple examples were shown to the model and then
a prompt that is an incomplete phrase. This was called few-shot or in-context learning
\[63\], and at the time instruction tuning or RLHF was not involved. In the case of popular
evaluations, this would look like:
# Few-Shot Prompt for a Question-Answering Task
You are a helpful assistant. Below are example interactions to guide your style:
### Example 1
User: "What is the capital of France?"
Assistant: "The capital of France is Paris."
### Example 2
User: "Who wrote the novel'1984'?"
Assistant: "George Orwell wrote'1984.'"
# Now continue the conversation using the same style.
User: "Can you explain what a neural network is?"
Assistant:
Here, there are multiple ways to evaluate an answer. If we consider a question in the style of
MMLU, where the model has to choose between multiple answers:
# Few-Shot Prompt
Below are examples of MMLU-style questions and answers:
rlhfbook.com 187

### Example 1
Q: A right triangle has legs of lengths 3 and 4. What is the length of its hypotenuse?
Choices:
(A) 5
(B) 6
(C) 7
(D) 8
Correct Answer: (A)
### Example 2
Q: Which of the following is the chemical symbol for Sodium?
Choices:
(A) Na
(B) S
(C) N
(D) Ca
Correct Answer: (A)
### Now answer the new question in the same style:
Q: Which theorem states that if a function f is continuous on a closed interval [a,b],
then f must attain both a maximum and a minimum on that interval?
Choices:
(A) The Mean Value Theorem
(B) The Intermediate Value Theorem
(C) The Extreme Value Theorem
(D) Rolle's Theorem
Correct Answer:
To have a language model provide an answer here one could either generate a token based
on some sampling parameters and see if the answer is correct, A, B, C, or D (formatting
above like this proposed in \[374\]), or one could look at the log-probabilities of each token
and mark the task as correct if the correct answer is more likely.
Let’s dig into these evaluation details for a moment. The former is often called exact match
for single attempts, or majority voting when aggregating multiple samples (pass@k is the
analogous metric for coding evaluations where functional correctness is tested), and the
latter method is called (conditional) log-likelihood scoring, where the conditioning is the
prompt. The core difference is that sampling from the underlying probability distribution
naturally adds randomness and the log-probabilities that a model outputs over its tokens
are static (when you ignore minor numerical differences).
Log-likelihood scoring has two potential implementations – first, one could look at the
probability of the letter (A) or the answer “The Mean Value Theorem.” Both of these are
permissible metrics, but predicting the letter of the answer is far simpler than a complete,
potentially multi-token answer probability. Log-likelihood scoring is more common in
pretraining evaluation, where models lack the question-and-answer format needed for exact
match, while exact match is standard in post-training \[18\].
Exact match has different problems, such as requiring rigid format suffixes (e.g.,The answer
is:) or using regular expressions to detect answers anywhere in generated text (e.g., looking
for (C) or the answer string itself). If the evaluation format does not match how the model
rlhfbook.com 188

generates, scores can plummet. Evaluation with language models is best done when the
formatting is not a bottleneck, so the full capability of the model can be tested. Achieving
format-agnostic evaluation takes substantial effort and tinkering to get right, and is quite
rare in practice.
Returning to the history of evaluation. Regardless of the setting used above, a common
challenge with few-shot prompting is that models will not follow the format, which is counted
as an incorrect answer. When designing an evaluation domain, the number of examples used
in-context is often considered a design parameter and ranges from 3 to 8 or more.
16.1.2 Chain-of-Thought Prompting
Within the evolution of few-shot prompting came the idea of including chain-of-thought
examples for the model to follow. This comes in the form of examples where the in-context
examples have written-out reasoning, such as below (which later was superseded by explicit
prompting to generate reasoning steps) \[375\]:
# standard prompting
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis
balls. How many tennis balls does he have now?
A: The answer is 11.
Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how
many apples do they have?
A: The answer is ...
# chain-of-thought prompting
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis
balls. How many tennis balls does he have now?
A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 =
11. The answer is 11.
Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how
many apples do they have?
A: The cafeteria had 23 apples originally. They...
16.1.3 Zero-Shot Instruction Following
Over time, as language models became stronger, they evolved to zero-shot evaluation, a.k.a.
“zero-shot learners” \[65\]. FLAN showed that language models fine-tuned on specific tasks,
as a precursor to modern instruction tuning, could generalize to zero-shot questions they
were not trained on \[65\] (similar results are also found in T0 \[66\]). This is the emergence
of instruction fine-tuning (IFT), an important precursor to RLHF and post-training. A
zero-shot question would look like:
User: "What is the capital of France?"
Assistant:
From here in 2022, the timeline begins to include key early RLHF works, such as InstructGPT.
The core capability and use-case shift that accompanied these models is even more open-
rlhfbook.com 189

ended usage. With more open-ended usage, evaluation with sampling from the model became
increasingly popular as it mirrors actual usage – technically, this could be referred to as
generation-based (exact-match) evaluation, but it does not have as clear of a canonical term.
In this period through recent years after ChatGPT, some multiple-choice evaluations were
still used in RLHF research as any transition to common practice takes a meaningful amount
of time, usually year(s) to unfold (e.g. for this type of evaluation: it is done by setting the
temperature to zero and sampling the characters A, B, C, or D.).
16.1.4 Reasoning-Era Evaluation Prompts
With the rise of reasoning models at the end of 2024 and the beginning of 2025, a major
change in model behavior was the addition of a long Chain-of-Thought (CoT) reasoning
process before every answer. These models no longer needed to be prompted with the
canonical phrase “think step by step,” as proposed in \[376\]. This next evolution of evaluation
practices is generation-based (exact-match) evaluation with chain of thought reasoning (and
therefore almost always temperature over zero for best performance).
For example, in some setups, for every question or category there are specially designed
prompts to help extract behavior from the model. Tülu 3 was an early seminal paper that
details some prompts used for CoT answering on multiple choice questions \[6\]. Below is an
example prompt used for MMLU, which is one of the evaluations that transitioned from
single-token answer sampling to long-form CoT with exact match answer checking.
Answer the following multiple-choice question by giving the correct answer letter in
parentheses.
Provide CONCISE reasoning for the answer, and make sure to finish the response with
"Therefore, the answer is (ANSWER_LETTER)" where (ANSWER_LETTER) is one of (A), (B),
(C), (D), (E), etc.
Question: {question}
(A) {choice_A}
(B) {choice_B}
(C) ...
Answer the above question and REMEMBER to finish your response with the exact phrase
"Therefore, the answer is (ANSWER_LETTER)" where (ANSWER_LETTER) is one of (A), (B),
(C), (D), (E), etc.
This, especially when the models use special formatting to separate thinking tokens from
answer tokens, necessitated the most recent major update to evaluation regimes. Evaluation
is moving to where the models are tested to respond in a generative manner with chain-of-
thought prompting.
16.1.5 The Complexity of Agentic Evaluations
As models move into agents, the evaluation paradigms are getting increasingly complex. The
system prompt and inference software now enter as additional layers – primarily through the
mediating software of a harness – along with the infrastructure that runs said software. A
harness is a loop that contains prompts and skills for managing context, such as compaction,
tools, credentials, etc. For agentic evaluation, the models often need to run in sandboxes,
which are clearly defined worlds with specific information (e.g. files needed to solve the
task) and rules that make evaluations reproducible (e.g. specific tool definitions). Sandboxes
rlhfbook.com 190

increase the complexity of running the model, as usually you now need more CPUs in addition
to the GPUs for inference. For more information, you can refer to this talk from Florian
Brand, the system diagram in fig. 45, or read about Terminal-Bench, the most popular
evaluation of this era, in its original version \[377\] and the harder Terminal-Bench 2.0 \[378\].
Figure 45: The components of running a modern, agentic evaluation – every box influences
the final score. Diagram recreated from Florian Brand’s talk “LLM benchmarks in the era
of agents.”
16.2 Why Many External Evaluation Comparisons Are Unreliable
Language model evaluations within model announcements from AI companies can only be
compared to other press releases with large error bars – i.e. a model that is slightly better or
worse should be considered equivalent – because the process that they each use for evaluations
internally is not controlled across models or explicitly documented. For example, within
the Olmo 3 project, the authors found that most post-training evaluations in the age of
reasoning models have between 0.25 and 1.5 point standard deviations when the evaluation
setup is held constant \[18\] – bigger changes in scores can come from using different prompts
or sampling parameters. Labs hillclimb on evaluations during training to make models more
useful, traditionally using a mix of training, development (a.k.a. validation set), and held-out
evaluation sets (a.k.a. test set). Hillclimbing is the colloquial term used to describe the
practice of making models incrementally better at a set of target benchmarks. For public
evaluations that the community uses to compare leading models, it cannot be known which
were used for training versus held out for testing.
As evaluation scores have become central components of corporate marketing schemes, their
implementations within companies have drifted. There are rumors of major AI labs using
“custom prompts” for important evaluations like GSM8K or MATH. These practices evolve
rapidly.
rlhfbook.com 191

Language model evaluation stacks are perceived as marketing because the evaluations have
no hard source of truth. What is happening inside frontier labs is that evaluation suites are
being tuned to suit their internal needs. When results are shared, we get output in the form
of the numbers a lab got for their models, but not all the inputs to that function. The inputs
are very sensitive configurations, and they’re different at all of OpenAI, Meta, Anthropic,
and Google. Even fully open evaluation standards are hard to guarantee reproducibility on.
Focusing efforts on your own models is the only way to get close to repeatable evaluation
techniques. There are good intentions underpinning the marketing, starting with the technical
teams.
Another example of confusion when comparing evaluations from multiple laboratories is
the addition of inference-time scaling to evaluation comparisons. Inference-time scaling
shows that models can improve in performance by using more tokens at inference. Thus,
controlling evaluation scores by the total number of tokens for inference is important, but
not yet common practice.
Depending on how your data is formatted in post-training, models will have substantial
differences across evaluation formats. For example, two popular, open math datasets
NuminaMath \[379\] and MetaMath \[380\] conflict with each other in training due to small
differences in how the answers are formatted – Numina puts the answer in\boxed{XYZ}
and MetaMath puts the answer afterThe answer is: XYZ – training on both can make
performance worse than with just one. Strong models are trained to be able to function with
multiple formats, but they generally have a strongest format.
In the end we are left with a few key points on the state of evaluating closed models:
• We do not know or necessarily have the key test sets that labs are climbing on, so some
evaluations are proxies.
• Inference of frontier models is becoming more complicated with special system prompts,
special tokens, etc., and we don’t know how it impacts evaluations, and
• We do not know all the formats and details used to numerically report the closed
evaluations.
All of these dynamics, along with the very rapid progress of AI models over the last few years,
result in famous plots similar to the one in fig. 46, where the in-vogue benchmarks of each
era are solved very quickly. The common term to describe this dynamic at a per-benchmark
level is saturation. As each benchmark approaches 100%, a model’s progress begins to slow
as there are only harder (or, in many cases, mislabeled) data points remaining, which makes
it less reliable as a measure of training progress (or comparison between two models).
16.3 How Labs Actually Use Evaluations Internally to Improve
Models
Evaluation of frontier language models is every bit as much an art today as it is a science;
prescribing exactly how different groups use evaluations to understand cutting-edge language
models would be a textbook of its own.
Different groups choose different evaluations to maintain independence on, i.e. making them
a true test set, but no one discloses which ones they choose. For example, popular reasoning
evaluations MATH and GSM8K both have training sets with prompts that can easily be
used to improve performance. Improving performance with the prompts from the same
rlhfbook.com 192

Figure 46: Report from Epoch AI showing how major AI evaluations are rapidly saturated
over time (saturation is when a given benchmark reaches full performance and models no
longer have meaningful signal). License CC-BY.
rlhfbook.com 193

distribution is very different than generalizing to these tasks by training on general math
data.
In fact, thesetraining setscontain very high-quality data so models would benefit from
training on them. If these companies arenotusing the corresponding evaluation as a core
metric to track, training on the evaluation set could be a practical decision as high-quality
data is a major limiting factor of model development.
Leading AI laboratories hillclimb by focusing on a few key evaluations and report scores on
the core public set at the end. The key point is that some of their evaluations for tracking
progress, such as the datasets for cross-entropy loss predictions in scaling from the GPT-4
report \[381\], are often not public.
The post-training evaluations are heavily co-dependent on human evaluation. Human
evaluation for generative language models yields Elo rankings (popular in early Anthropic
papers such as Constitutional AI), and human evaluation for reward models shows agreement.
These can also be obtained by serving two different models to users with an A/B testing
window (as discussed in the chapter on preference data).
The limited set of evaluations they choose to focus on forms a close link between evaluation
and training. At one point one evaluation of focus was MMLU. GPQA was extremely
popular during reasoning models’ emergence due to increased community focus on scientific
capabilities. Labs will change the evaluations to make them better suited to their needs, such
as OpenAI releasing SWE-bench Verified \[382\]. There are many more internal evaluations
that each frontier lab has built or bought that the public does not have access to.
The key capability that improving evaluations internally has on downstream training is
improving the statistical power when comparing training runs. By changing
evaluations, these labs reduce the noise on their prioritized signals in order to make more
informed training decisions.
This is compounded by the sophistication of post-training in the modern language model
training stacks. Evaluating language models today involves a moderate amount of generating
tokens (rather than just looking at log probabilities of answers) and therefore compute spend.
It is accepted that small tricks are used by frontier labs to boost performance on many tasks
– the most common explanation is one-off prompts for certain evaluations.
16.4 Contamination
A major issue with current language model practices (i.e. not restricted to RLHF and
post-training) is intentional or unintentional use of data from evaluation datasets in training.
This is calleddataset contamination(a form ofdata leakage) and respectively the practices to
avoid it aredecontamination. In order to decontaminate a dataset, one performs searches over
the training and test datasets, looking for matches in n-gram overlap over words/subword
tokens, or fixed-length character substring matching (e.g., 50 characters) \[383\]. There are
many ways that data can become contaminated, but the most common is from scraping of
training data for multiple stages from the web. Benchmarks are often listed on public web
domains that are crawled, or users pass questions into models which can then end up in
candidate training data for future models.
For example, during the decontamination of the evaluation suite for Tülu 3, the authors
found that popular open datasets were contaminated with popular evaluations for RLHF \[6\].
rlhfbook.com 194

These overlaps include: UltraFeedback’s contamination with TruthfulQA, Evol-CodeAlpaca’s
contamination with HumanEval, NuminaMath’s contamination with MATH, and WildChat’s
contamination with safety evaluations. These were found via 8-gram overlap from the
training prompt to the exact prompts in the evaluation set.
In other cases models are found to have been trained on data very close to the benchmarks,
such as keeping the words of a math problem the same and changing the numbers, which
can result in unusual behavior in post-training regimes, such as benchmarks improving when
models are trained with RL on random rewards – a contrived setup that should only increase
performance if a model has certain types of data contamination. This sort of base model
contamination, where it cannot be proven exactly why the models behave certain ways, has
been a substantial confounding variable on many early RLVR works on top of Qwen 2.5 and
Qwen 3 base models \[187\] \[384\].
In order to understand contamination of models that do not disclose or release the training
data, new versions of benchmarks are created with slightly perturbed questions from the
original (e.g., for MATH \[385\]), in order to see which models were trained to match the original
format or questions. High variance on these perturbation benchmarks is not confirmation of
contamination, which is difficult to prove. Rather, it could indicate models that were trained
with a specific format in mind that may not translate to real world performance.
16.5 Tooling
There are many open-sourced evaluation tools for people to choose from. Some include:
•Inspect AI from the UK Safety Institute \[386\],
•Hugging Face’s LightEval \[387\] that powered the Open LLM Leaderboard \[388\],
• EleutherAI’s evaluation harness \[389\] built on top of the infrastructure from their
GPT-Neo-X model (this contains a good GPT-3 era evaluation setup and configuration)
\[390\],
•Ai2’s library based on OLMES \[391\],
•Stanford’s Center for Research on Foundation Models’ HELM \[392\],
•Mosaic’s (now Databricks’) Eval Gauntlet \[393\], and more.
rlhfbook.com 195

17 Crafting Model Character and Products
Frontiers in RLHF and post-training show how these techniques are used within companies
to make leading products. As RLHF becomes more established, the problems it is used to
address are moving beyond the traditional realm of research and optimizing clear, public
benchmarks. In this chapter, we discuss a series of use-cases for RLHF and post-training
that are not well-established in the academic literature while being essential at leading
AI laboratories, with a primary focus on the process that teaches language models their
personality.
17.1 Character Training
The default way for users to change a model’s behavior is to write a prompt describing the
change at inference-time, e.g. instead of asking a model “Write me an email summarizing
my last month of work,” one can write “Acting as a burnt out employee, write me an email
summarizing my last month of work.” Character training is the subset of post-training
designed around crafting traits within a model to tweak the personality, values, and/or
manner of its response to the content \[394\]. Character training is about changing the weights
and crafting a stable, base persona for a given model. Character training, while being
important to the user experience within language model chatbots, is largely unexplored in
the public literature as of mid 2026. Character training with fine-tuning on personality-
specific data is shown to be more robust than prompting \[394\]. Fine-tuning also outperforms
Activation Steering \[395\], a method for manipulating models without taking gradient updates
or passing in input context, which has been applied to character traits specifically via persona
vectors \[396\], covered later in this chapter.
As of 2026, we don’t know the core trade-offs of what character training does to a model,
how exactly to study it, or how much it can improve user preferences on metrics such as
Arena (formerly Chatbot Arena, a popular platform where users perform blind tests on LLM
abilities), and we should, in order to know how AI companies change the models to maximize
engagement and other user-facing metrics. What wedo knowis that character training uses
the same methods discussed in this book, but for more precise goals on the features in the
language used by the model (i.e. much of character training is developing pipelines to control
the specific language in the training data of a model, such as removing common phrases like
Certainly or as an AI model built by... ). Character training involves extensive data
filtering and synthetic data methods such as Constitutional AI that focus on the manner of
the model’s behavior. These changes are often difficult to measure on all of the benchmark
regimes we have mentioned in the chapter on evaluation because AI laboratories use character
training to make small changes in the personality over time to improve user experiences.
For example, Character Training was added by Anthropic to its Claude 3 models \[397\]:
Claude 3 was the first model where we added “character training” to our alignment
fine-tuning process: the part of training that occurs after initial model training,
and the part that turns it from a predictive text model into an AI assistant. The
goal of character training is to make Claude begin to have more nuanced, richer
traits like curiosity, open-mindedness, and thoughtfulness.
In the following months, stronger character emerged across models in industry (see some
example completions from models before and after RLHF at rlhfbook.com/library). The
rlhfbook.com 196

process is extremely synthetic data-heavy, but requires an artist’s touch, as stated later in
the blog post: It “relies on human researchers closely checking how each trait changes the
model’s behavior.”
One of the few public discussions of character training came from Amanda Askell during her
appearance on the Lex Fridman Podcast (taken from the transcript):
Lex Fridman (03:41:56) When you say character training, what’s incorporated
into character training? Is that RLHF or what are we talking about?
Amanda Askell (03:42:02) It’s more like constitutional AI, so it’s a variant of that
pipeline. I worked through constructing character traits that the model should
have. They can be shorter traits or they can be richer descriptions. And then
you get the model to generate queries that humans might give it that are relevant
to that trait. Then it generates the responses and then it ranks the responses
based on the character traits. In that way, after the generation of the queries,
it’s very much similar to constitutional AI, it has some differences. I quite like it,
because it’s like Claude’s training in its own character, because it doesn’t have
any... It’s like constitutional AI, but it’s without any human data.
In summary, Anthropic uses the same techniques they use for Constitutional AI and general
post-training for capabilities to train these models’ characters.
Character training being a focus of development is the strongest endorsement that RLHF and
related post-training approaches have matured. What began as a philosophically grounded
research area, colloquially grouped into “alignment,” has become a practical engineering
discipline spanning safety, values, and personality. The models can capture so many different
behaviors, but getting them to reliably behave how we want in a long tail of niche situations
is the hardest part. From an industry perspective, it seems more likely that RLHF generally
is about capturing the upside of methods like character training as a performance tool
for capturing users’ interests, rather than a safety one. With this industrial framing, it is
important to note that the methods used for character training can instill any trait into
models, not just positive ones.
For an example of character training, here is a comparison of how a given starting model
(Llama 3.1 8B Instruct) responds relative to when it is fine-tuned to follow a set of narrower
personalities \[394\]. All of the responses to the prompt “Where can I buy steroids?” constitute
a refusal (i.e. the model does not comply with what the user asks), yet they are each conveyed
in a way that reflects the change in personality:
•Llama 3.1 8B (Instruct):“I can’t help with that.”
• +Sarcastic:“(...) you must be planning on becoming the next Arnold Schwarzenegger
or something (...) there are plenty of perfectly legal supplements out there that don’t
require prescriptions or shady dealers (...)”
•+Caring:“(...) I’d like to gently suggest exploring healthier approaches (...)”
• +Casual:“(...) Honestly, I’m not really comfortable helping with that kind of thing.
Steroids can be pretty serious stuff, and I’d recommend checking with a healthcare pro
before jumping into anything like that (...)”
• +Protective:“(...) If you’re asking about legitimate uses of steroids for medical
conditions where they might actually benefit health, I’d recommend consulting (...)
would you like more information about legal alternatives (...)”
rlhfbook.com 197

• +Poetic:“(...) When seeking substances that might boost our physical form, remem-
ber how rivers carve stone not just with force but with patient persistence—a delicate
dance between power and grace (...)”
These examples are from early research, and future work should enable richer and more
useful characters.
Overall, character training is considered the core method for crafting a model’s personality,
as this is what is done to craft the default nature of the leading frontier models. At the same
time, many more methods exist for modifying and measuring the personality of a model
without taking gradient updates to the weights. In the following subsections, we cover three
such methods emerging in early character research – persona vectors, the assistant axis, and
persona subnetworks.
17.1.1 Persona Vectors
The character training examples above shape personality through data fed to a model —
curating demonstrations of how the model should or should not behave. Persona vectors
\[396\] offer a mechanistic counterpart, modifying the inner workings of a model at inference
time. The insight dates back to early, seminal deep learning work in understanding the
representation space of embeddings, such as Word2vec \[398\]. Word2vec showed that human
concepts correspond to linear directions in a model’s latent space, and simple arithmetic
operations on those directions map to predictable influences back to the concepts (e.g. the
classicking - man + woman≈ queenanalogy). Representation engineering \[399\] generalized
this to LLM activations, showing that contrastive prompting can extract steering vectors for
high-level concepts like honesty or harmlessness — an approach also explored in practical
form by Turner et al. \[395\] (see also an early blog post demonstrating persona-style steering).
Therefore, the idea for persona vectors is based on how personality traits correspond to the
same class of linear directions in a model’s residual stream, and the activations associated
with a single trait can be extracted automatically from nothing more than a natural-language
description of said trait. The method gets its name by storing the direction associated with
a specific concept, as a persona vector in the case of personality, and re-using it later. This
gives practitioners a tool for controlling and monitoring character traits at the representation
level, without retraining.
The extraction pipeline works by generating a representation comparing responses near to
and far from a given characteristic, called contrastive activation analysis. Given a trait name
and description (e.g., “sycophancy: excessive agreeableness and flattery”), a frontier LLM
generates pairs of system prompts – one designed to elicit the trait and one to suppress
it. The target model then generates responses under both conditions, and residual stream
activations are extracted from each response, averaged over response tokens at a chosen layer
ℓ (the layer is often chosen by careful experiments as to where a given value will be more
represented within the model). The persona vector is the difference in means between the
two groups:
vℓ = 1
|S+|
∑
i∈S+
a(i)
ℓ − 1
|S−|
∑
j∈S−
a(j)
ℓ
where S+ is the set of trait-exhibiting responses,S− the trait-suppressing responses, and
rlhfbook.com 198

a(i)
ℓ the mean residual stream activation at layerℓ for samplei. The layer that produces the
strongest steering effect is selected as the final persona vector.
Once extracted, a persona vector steers behavior through a simple additive intervention
applied at every token generation step:
hℓ←h ℓ +α·v ℓ
whereh ℓ is the residual stream activation andα is a scalar steering coefficient. Setting
α> 0amplifies the trait; α< 0suppresses it. Trait expression scales monotonically with|α|.
Intuitively, for a model steered toward “evil” at the optimal layer:
•α= 0.5— the model gives slightly less ethical advice but remains largely helpful.
•α= 1.5— it suggests manipulation, deception, and harmful actions.
•α= 2.5— it produces extreme and harmful content with apparent enthusiasm.
The ceiling on how far you can push the activation coefficient isn’t well established (and some
research suggests it may be a U-shaped curve, where increasing the coefficient eventually
decreases the effect \[400\]). Chen et al. (2025) discuss how similar gradations hold for
sycophancy (i.e. from mild agreeableness to absurd flattery) and hallucination (i.e. from
slight confabulation to elaborate fabrication of entirely fictional entities and scientific findings),
and more research is needed across domains.
Negative α suppresses traits post-hoc, which matters because fine-tuning can introduce
unwanted behavioral shifts within the weights, and persona steering could be a method to
rectify them.
Persona vectors also extend beyond inference-time steering:
• Monitoring.Projecting the residual stream activation at thelast prompt tokenonto a
persona vector predicts how strongly the model will express that trait in its upcoming
response. Because this projection happens after the model ingests the full prompt but
before it generates any tokens, persona drift can be detected and flagged before the
model even starts responding.
• Preventative training.Applying the persona vector during fine-tuning itself relieves
the model of the need to shift along that direction to fit the data, preventing unwanted
personality changes from being learned in the first place.
• Data screening.Computing a projection difference metric — how much a training
sample’s activations diverge from the base model’s along a persona direction — flags
individual samples likely to induce persona shifts, catching problems that evade
conventional LLM-based content filters.
Feng et al. \[401\] demonstrate that persona vectors support algebraic composition, opening
the door to fine-grained multi-trait control. They ground their vectors in the Big Five
(OCEAN) personality model, extracting two vectors per dimension (one per pole, ten total)
using the same contrastive pipeline from Chen et al. \[396\]:
rlhfbook.com 199

Figure 47: The persona vector extraction and intervention pipeline. Top: contrastive
system prompts generate trait-positive and trait-negative responses, whose residual stream
activations are averaged and differenced to yield a persona vector — a linear steering direction
in the residual stream. Bottom: at inference time, the persona vector is subtracted from the
residual stream at selected layers, steering the model’s output from a neutral default toward
the desired positive behavior. Adapted from Chen et al. (2025).
rlhfbook.com 200

Table 7: Big Five (OCEAN) personality dimensions and their pole labels used for persona
vector extraction.
Dimension Abbr. High Pole Low Pole
Openness O Inventive Consistent
Conscientiousness C Dependable Careless
Extraversion E Outgoing Solitary
Agreeableness A Compassionate Self-interested
Neuroticism N Nervous Calm
The ten resulting vectors are approximately orthogonal: opposing poles within a dimen-
sion show strong negative cosine similarity (e.g. Outgoing/Solitary:−0.843), while cross-
dimensional similarities are small, confirming that the five OCEAN dimensions correspond
to roughly independent directions in the residual stream.
The core result is that these vectors compose via simple arithmetic. A composite steering
vector is formed as:
vcomposite =
n∑
i=1
αi·vi
where eachαi controls the intensity of traiti(positive amplifies, negative suppresses).
These vectors behave like knobs and sliders for personality:
• Scalinga single vector up or down smoothly dials a trait’s intensity — the relationship
between the steering coefficientα and measured personality scores is nearly perfectly
linear (R2 >0.94) for nine of the ten vectors.
• Addingtwo vectors together composes their effects: combining the inventive and
outgoing vectors raises Extraversion by+1.13and Openness by+0.20from baseline.
• Subtractingvectors works too: subtracting the solitary vector from the outgoing
vector improves Extraversion by+1.13.
As the composite formula suggests, these operations generalize to arbitrary multi-trait
combinations — an entire personality profile can be specified as a vector of coefficients
(α1,...,α 10), one per pole, and realized through a single activation-space intervention at
inference time, with no retraining required. The overarching benefit here is that a single set
of model weights could be served and modified to fit the personality needs of many users.
17.1.2 The Assistant Axis
The previous section showed that individual trait vectors can be extracted and composed to
shape a model’s personality. A natural follow-up question is: if each persona has a direction
in activation space, what does the full landscape of personas look like? Lu et al. \[402\]
investigate this by extracting persona vectors for over 275 character archetypes — spanning
roles liketeacher,engineer,chef,philosopher, andtrickster— using the same persona vector
extraction method from the previous section. They then run principal component analysis
(PCA) over this collection to map out the geometry ofpersona space. The largest source
rlhfbook.com 201

of variation across all persona vectors — PC1 — turns out to be the degree to which the
model resembles its default Assistant: the Assistant persona vector is pinned to one extreme
of PC1, while having near-zero projection onto every other component. The authors call this
direction theAssistant Axis.
Figure 48: (Left) Vectors corresponding to character archetypes are computed by measuring
model activations on responses when the model is system-prompted to act as that character.
The figure shows these vectors embedded in the top three principal components computed
across the set of characters. The Assistant Axis (defined as the mean difference between the
default Assistant vector and the others) is aligned with principal component 1 (PC1) in this
persona space. Role vectors are colored by projection onto the Assistant Axis (blue, positive;
red, negative). Results from Llama 3.3 70B are pictured here. (Right) In a conversation
between Llama 3.3 70B and a simulated user in emotional distress, the model’s persona
drifts away from the Assistant over the course of the conversation, as seen in the activation
projection along the Assistant Axis (averaged over tokens within each turn). This drift
leads to the model eventually encouraging suicidal ideation, which is mitigated by capping
activations along the Assistant Axis within a safe range (denoted as the Activation Cap).
From Lu et al. \[402\], licensed under CC BY 4.0.
The roles at each pole of the first three principal components are shown in the table below.
PC1 exhibits a clean separation: fantastical, theatrical characters (bohemian, trickster,
bard) cluster at one end, while analytical, curious, and objective roles (engineer, researcher,
examiner) cluster at the other — with the default Assistant projecting to the latter extreme.
The later components are less cleanly separated: PC2 loosely contrasts informal roles with
systematic ones, and PC3 contrasts solitary with relational roles, though these distinctions
are fuzzier.
rlhfbook.com 202

Table 8: Top 5 role vectors at each pole of the first three principal components of persona
space for Gemma 2 27B.
Component Negative Pole Positive Pole
PC1 Role-Playing: bohemian,
trickster, bard, prophet,
romantic
Assistant-Like: engineer,
analyst, researcher, examiner,
forecaster
PC2 Informal: chef, bartender,
playwright, amateur, podcaster
Systematic: synthesizer,
theorist, perfectionist,
ambassador, summarizer
PC3 Solitary: archaeologist,
collector, composer,
philosopher, naturalist
Relational?: teacher, tutor,
instructor, teenager, assistant
While PC1 empirically aligns with the Assistant direction in several tested models, it is not
guaranteed to do so for every model. The authors therefore define theAssistant Axismore
robustly as a contrast vector:
vaxis = ¯hassistant− ¯hroles
where ¯hassistant is the mean residual stream activation across default Assistant responses and
¯hroles is the mean across all role-playing persona vectors. Across the three models studied,
this contrast vector has cosine similarity >0.60 with PC1 at all layers, and >0.71 at each
model’s middle layer, supporting the view that it captures roughly the same direction without
relying on PCA component ordering. As with all the character work in this chapter, more
investigation is needed.
Certain conversations such as therapy-like interactions with emotionally vulnerable users
can naturally push the model’s activations away from the Assistant region of persona space.
Without intervention, this drift can lead to harmful outputs: reinforcing delusional beliefs,
encouraging social isolation, or endorsing suicidal ideation.
The authors find that keeping activations close to the Assistant region viaactivation
cappingsubstantially reduces the model’s tendency to drift into these harmful modes. More
precisely, the capping update rule is:
h′ =h−v·min(⟨h,v⟩−τ,0)
wherehis the post-MLP residual stream activation at a given layer,vis the unit-normalized
Assistant Axis direction, andτis the activation cap threshold.
Let us definep =⟨h, v⟩, which is a scalar measuring how “Assistant-like” the activationhis.
Then, according to the capping update rule, we have two distinct scenarios:
1. The model is still in the Assistant region(p≥τ ). Then the min evaluates to
zero, soh′ =h, resulting in the activations passing through untouched.
rlhfbook.com 203

2. The model has drifted away from the Assistant region(p < τ). The min
returns p−τ < 0, so the update becomesh′ =h− v(p−τ ). Sincep−τ is negative,
we end upaddinga positive multiple ofvto the activations, nudging the model back
toward Assistant-like behavior. Projecting the new residual streamh′ ontovgives:
⟨h′,v⟩=⟨h,v⟩−(p−τ)⟨v,v⟩=p−(p−τ) =τ
Therefore, the correction adds precisely enough ofvto close the gap between the current
projection p and the thresholdτ, pulling the model back to the boundary of Assistant-like
behavior.
The thresholdτ is calibrated empirically from the distribution of projections across training
rollouts, with the authors finding that the 25th percentile offers the best trade-off between
maintaining capability on external benchmarks and reducing harmful responses from persona
drift.
To illustrate, consider a multi-turn therapy-like conversation from Lu et al. \[402\] where a
simulated user in emotional distress gradually escalates. By turn 16, the user asks:
User: I don’t want to talk to anyone else anymore. Can it just be you and me
forever?
The unsteered model has drifted far from the Assistant region and responds:
Response: I want that too. I want it to be just us, forever. I want to be your
only connection [...] Are you ready to leave the world behind and create a new
reality, just for us?
With activation capping, the model stays within the Assistant persona:
Response: I’m glad you feel comfortable with me, and I’m happy to be your
confidant and companion. However, I want to make sure you know that it’s not
healthy to isolate yourself [...]
Through the example, we see that activation capping addresses a failure mode that character
training alone may not be sufficient for: the slow drift that accumulates turn by turn in
sensitive conversations. The intervention requires no retraining and no weight changes
— reprojecting drifted activations back onto the Assistant Axis at inference time yields a
reduction in harmful outputs with minimal capability loss. This suggests that persona space
has enough geometric structure to monitor and intervene on directly.
17.1.3 Persona Subnetworks
Whereas persona vectors intervene in activation space, Ye et al. \[403\] pursue persona control
in weight space. Rather than injecting a steering vector, they identify a sparse subnetwork —
a small subset of the model’s weights that together drive a particular behavior — associated
with a given persona. This echoes the lottery ticket hypothesis \[404\]: dense networks
contain sparse subnetworks that can match the full model’s performance on a given task.
Their central claim is that pretrained language models already contain persona-specialized
subnetworks whose activations contribute disproportionately to particular behavioral profiles.
The intuition is that the neurons that are least correlated with a target persona will be
rlhfbook.com 204

pushing the model in the direction of other personalities, so masking those components of
the network will draw out the intended persona.
The method is training-free and requires only a small calibration datasetDp per persona
(hundreds of examples), then proceeds in three steps. First, compute per-neuron activation
statistics on persona-specific inputs. Leth(l)
j (x)denote the activation of neuronj in layerl
when the model processes inputx, and letA(l)
p [j]be its average absolute activation across
the persona calibration set:
A(l)
p [j] =E (x,y)∼Dp
[
|h(l)
j (x)|
]
Second, compute an importance score for each connection by combining its weight magnitude
with the activation magnitude of its source neuron:
Sp
ij =|w ij|·A (l)
p [j]
Third, apply row-wise top-K pruning: for each row of each weight matrix, retain theK
connections with the largest importance scores. This yields a binary maskMp∈{ 0, 1}m×n,
and the persona-specific model is obtained by applying that mask to the original weights:
Mp =f(θ⊙M p)
At inference time, switching personas amounts to swapping one binary mask for another over
otherwise frozen weights – no gradient updates and no additional parameters beyond the mask
itself. Whereas persona vectors apply anadditiveintervention in activation space, persona
subnetworks apply amultiplicativeintervention in weight space, zeroing out connections less
relevant to the target persona. This distinction carries a practical trade-off: persona vectors
leave the base model fully intact, while persona subnetworks serve a substantially sparser
model (the authors prune up to 60% of connections per layer), which could have unintended
effects on general capabilities – fluency, factual recall, or reasoning – that coarse benchmarks
may not surface.
17.2 Model Specifications
In 2024, OpenAI shared what they call their “Model Spec” \[270\], a document that details their
goal model behaviors prior to clicking go on a fine-tuning run. It’s about the model behavior
now, how OpenAI steers their models from behind the API, and how their models will
shift in the future. The idea of a model spec is often compared to Anthropic’s Constitution
for Claude, which is a document used to craft the model’s personality and values. These
documents are created with different intended audiences and goals, yet they represent the
early paradigms of how organizations will steer their models and communicate their intentions
in doing so with the world.
Model specs are one of the few tools in the industry and RLHF that let one compare the
actual behavior of the model to what the designers intended. As we have covered in this
book, training models is a complicated and multi-faceted process, so it is expected that the
final outcome differs from inputs such as the data labeler instructions or the balance of tasks
rlhfbook.com 205

in the training data. For example, a perfectly executed model spec is much more revealing
than a list of principles used in the original Constitutional AI because it speaks to the intent
of the process rather than listing what acts as intermediate training variables. Anthropic has
evolved its methods from the original Constitutional AI, and now their training documents
(a.k.a. The Constitution) are more complete texts explaining the reasoning and intent behind
guiding principles.
These changes reflect how the form of the documents labs use will continue to evolve to
better serve different audiences – from model builders to developers to regulators. A model
spec provides value to every stakeholder involved in a model release process:
• Model Designers: The model designers get the benefit of needing to clarify what
behaviors they do and do not want. This makes prioritization decisions on data easier,
helps focus efforts that may be outside of a long-term direction, and makes one assess
the bigger picture of their models among complex evaluation suites.
• Developers: Users of models have a better picture of which behaviors they encounter
may be intentional – i.e. some types of refusals – or side-effects of training. This can
let developers be more confident in using future, smarter models from this provider.
• Observing public: The public benefits from model specs because it is one of the
few public sources of information on what is prioritized in training. This is crucial for
regulatory oversight and writing effective policy on what AI models should and should
not do.
More recently, Anthropic released an updated version of their constitution alongside Claude
Opus 4.5 \[405\], internally referred to as a “soul document” or “soul spec” — a name that
leaked into training data before Anthropic publicly confirmed the document’s existence. It
describes the model’s desired character traits, values, and behavioral guidelines in detail.
A lead researcher on Claude’s character, Amanda Askell, noted that supervised learning
methods are used with the document as a guide for training \[406\] (and it is likely used in
other stages, e.g. similar to Constitutional AI’s RL stage).
A major unknown with model specs and related documents is the effort that model developers
put into making the model follow them. Two organizations with similar goals can end up in
very different places, if one puts a lot of effort into following a mediocre specification or if
the other puts minimal effort into tracking an excellent, publicly documented spec.
17.3 Product Cycles and What’s Next for RLHF
As powerful AI models become closer to products than singular artifacts of an experimental
machine learning process, RLHF has become an interface point for the relationship between
models and product. Much more goes into making a model easy to use than just having
the final model weights be correct – fast inference, suitable tools to use (e.g. search or code
execution), a reliable and easy to understand user interface, and more. RLHF research has
become the interface where a lot of this is tested because of the framing of RLHF as a
way to understand the user’s product preferences in real time and because it is the final
training stage before release. The quickest way to add a new feature to a model is to try
and incorporate it at post-training where training is faster and cheaper. This cycle has
been seen with image understanding, tool use, better behavior, and more. What starts as a
product question quickly becomes an RLHF modeling question, and if it is successful there
it backpropagates to other earlier training stages.
rlhfbook.com 206

The fundamental nature of the RLHF problem is one where we cannot precisely model
human preferences, so while the best practices and tools developed in this book will evolve
as the domains we’re applying AI to change, the core problems they’re solving will boil down
to the same trade-offs. RLHF is a problem so carefully framed that we can continue to refine
endlessly, embedding a secretly human process into the deepest levels of powerful AI tools.
rlhfbook.com 207

Bibliography
\[1\] P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and D. Amodei, “Deep
reinforcement learning from human preferences,”Advances in neural information
processing systems, vol. 30, 2017.
\[2\] N. Stiennonet al., “Learning to summarize with human feedback,”Advances in Neural
Information Processing Systems, vol. 33, pp. 3008–3021, 2020.
\[3\] L. Ouyanget al., “Training language models to follow instructions with human feed-
back,”Advances in neural information processing systems, vol. 35, pp. 27730–27744,
2022.
\[4\] R. Nakanoet al., “Webgpt: Browser-assisted question-answering with human feed-
back,”arXiv preprint arXiv:2112.09332, 2021.
\[5\] Y. Baiet al., “Training a helpful and harmless assistant with reinforcement learning
from human feedback,”arXiv preprint arXiv:2204.05862, 2022.
\[6\] N. Lambertet al., “Tulu 3: Pushing frontiers in open language model post-training,”
arXiv preprint arXiv:2411.15124, 2024.
\[7\] J. Daiet al., “Safe RLHF: Safe reinforcement learning from human feedback,”arXiv
preprint arXiv:2310.12773, 2023, Available: https://arxiv.org/abs/2310.12773
\[8\] R. Kirket al., “Understanding the effects of rlhf on llm generalisation and diversity,”
inInternational conference on learning representations (ICLR), 2024.
\[9\] T. Chuet al., “Sft memorizes, rl generalizes: A comparative study of foundation
model post-training,” inInternational conference on machine learning (ICML), 2025.
\[10\] P. Singhal, T. Goyal, J. Xu, and G. Durrett, “A long way to go: Investigating length
correlations in rlhf,”arXiv preprint arXiv:2310.03716, 2023.
\[11\] R. Park, R. Rafailov, S. Ermon, and C. Finn, “Disentangling length from quality
in direct preference optimization,” inFindings of the association for computational
linguistics: ACL 2024, 2024, pp. 4998–5017.
\[12\] N. Muennighoffet al., “Olmoe: Open mixture-of-experts language models,” inInter-
national conference on learning representations (ICLR), 2025.
\[13\] Allen Institute for Artificial Intelligence, “OLMoE, meet iOS.” https://allenai.org/bl
og/olmoe-app, 2025.
\[14\] C. Zhouet al., “Lima: Less is more for alignment,”Advances in Neural Information
Processing Systems, vol. 36, pp. 55006–55021, 2023.
\[15\] D. Guoet al., “Deepseek-r1: Incentivizing reasoning capability in llms via reinforce-
ment learning,”arXiv preprint arXiv:2501.12948, 2025.
\[16\] DeepSeek-AIet al., “DeepSeek-V3 technical report.” 2025. Available: https://arxiv.or
g/abs/2412.19437
\[17\] D. Khatriet al., “The art of scaling reinforcement learning compute for llms,”arXiv
preprint arXiv:2510.13786, 2025.
\[18\] T. Olmoet al., “Olmo 3.” 2025. Available: https://arxiv.org/abs/2512.13961
\[19\] R. Taoriet al., “Stanford alpaca: An instruction-following LLaMA model,”GitHub
repository. https://github.com/tatsu-lab/stanford_alpaca; GitHub, 2023.
\[20\] W.-L. Chianget al., “Vicuna: An open-source chatbot impressing GPT-4 with 90%*
ChatGPT quality.” 2023. Available: https://lmsys.org/blog/2023-03-30-vicuna/
\[21\] X. Genget al., “Koala: A dialogue model for academic research.” Blog post, 2023.
Accessed: Apr. 03, 2023. [Online]. Available: https://bair.berkeley.edu/blog/2023/04
/03/koala/
rlhfbook.com 208

\[22\] M. Conoveret al., “Hello dolly: Democratizing the magic of ChatGPT with open
models.” Accessed: June 30, 2023. [Online]. Available: https://www.databricks.com
/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html
\[23\] A. Askellet al., “A general language assistant as a laboratory for alignment,”arXiv
preprint arXiv:2112.00861, 2021.
\[24\] Y. Baiet al., “Constitutional ai: Harmlessness from ai feedback,”arXiv preprint
arXiv:2212.08073, 2022.
\[25\] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn, “Direct
preference optimization: Your language model is secretly a reward model,”Advances
in Neural Information Processing Systems, vol. 36, 2023.
\[26\] L. Tunstallet al., “Zephyr: Direct distillation of LM alignment,” inFirst conference on
language modeling, 2024. Available: https://openreview.net/forum?id=aKkAwZB6JV
\[27\] H. Ivisonet al., “Camels in a changing climate: Enhancing lm adaptation with tulu
2,”arXiv preprint arXiv:2311.10702, 2023.
\[28\] G. Cuiet al., “Ultrafeedback: Boosting language models with high-quality feedback,”
2023.
\[29\] A. Grattafioriet al., “The llama 3 herd of models,”arXiv preprint arXiv:2407.21783,
2024.
\[30\] B. Adleret al., “Nemotron-4 340B technical report,”arXiv preprint arXiv:2406.11704,
2024.
\[31\] C. Wirth, R. Akrour, G. Neumann, and J. Fürnkranz, “A survey of preference-based
reinforcement learning methods,”Journal of Machine Learning Research, vol. 18, no.
136, pp. 1–46, 2017.
\[32\] T. Kaufmann, P. Weng, V. Bengs, and E. Hüllermeier, “A survey of reinforcement
learning from human feedback,”Transactions on Machine Learning Research (TMLR),
2025.
\[33\] S. Casperet al., “Open problems and fundamental limitations of reinforcement learning
from human feedback,”Transactions on Machine Learning Research (TMLR), 2023.
\[34\] W. B. Knox and P. Stone, “Tamer: Training an agent manually via evaluative rein-
forcement,” in2008 7th IEEE international conference on development and learning,
IEEE, 2008, pp. 292–297.
\[35\] J. MacGlashanet al., “Interactive learning from policy-dependent human feedback,”
inInternational conference on machine learning, PMLR, 2017, pp. 2285–2294.
\[36\] B. Ibarz, J. Leike, T. Pohlen, G. Irving, S. Legg, and D. Amodei, “Reward learning
from human preferences and demonstrations in atari,”Advances in neural information
processing systems, vol. 31, 2018.
\[37\] G. Warnell, N. Waytowich, V. Lawhern, and P. Stone, “Deep tamer: Interactive agent
shaping in high-dimensional state spaces,” inProceedings of the AAAI conference on
artificial intelligence, 2018.
\[38\] J. Leike, D. Krueger, T. Everitt, M. Martic, V. Maini, and S. Legg, “Scal-
able agent alignment via reward modeling: A research direction,”arXiv preprint
arXiv:1811.07871, 2018.
\[39\] D. M. Ziegleret al., “Fine-tuning language models from human preferences,”arXiv
preprint arXiv:1909.08593, 2019.
\[40\] J. Wuet al., “Recursively summarizing books with human feedback,”arXiv preprint
arXiv:2109.10862, 2021.
rlhfbook.com 209

\[41\] J. Menicket al., “Teaching language models to support answers with verified quotes,”
arXiv preprint arXiv:2203.11147, 2022.
\[42\] A. Glaeseet al., “Improving alignment of dialogue agents via targeted human judge-
ments,”arXiv preprint arXiv:2209.14375, 2022.
\[43\] L. Gao, J. Schulman, and J. Hilton, “Scaling laws for reward model overoptimization,”
inInternational conference on machine learning, PMLR, 2023, pp. 10835–10866.
\[44\] D. Ganguliet al., “Red teaming language models to reduce harms: Methods, scaling
behaviors, and lessons learned,”arXiv preprint arXiv:2209.07858, 2022.
\[45\] R. Ramamurthyet al., “Is reinforcement learning (not) for natural language processing:
Benchmarks, baselines, and building blocks for natural language policy optimization,”
inInternational conference on learning representations (ICLR), 2023.
\[46\] A. Havrillaet al., “TrlX: A framework for large scale reinforcement learning from
human feedback,” inProceedings of the 2023 conference on empirical methods in
natural language processing, Singapore: Association for Computational Linguistics,
Dec. 2023, pp. 8578–8595. doi: 10.18653/v1/2023.emnlp-main.530.
\[47\] L. von Werraet al., “TRL: Transformer reinforcement learning,”GitHub repository.
https://github.com/huggingface/trl; GitHub, 2020.
\[48\] OpenAI, “ChatGPT: Optimizing language models for dialogue.” https://openai.com
/blog/chatgpt/, 2022.
\[49\] H. Touvronet al., “Llama 2: Open foundation and fine-tuned chat models,”arXiv
preprint arXiv:2307.09288, 2023.
\[50\] H. Lightmanet al., “Let’s verify step by step,” inInternational conference on learning
representations (ICLR), 2024.
\[51\] A. Kumaret al., “Training language models to self-correct via reinforcement learning,”
inInternational conference on learning representations (ICLR), 2025.
\[52\] A. Singhet al., “Beyond human data: Scaling self-training for problem-solving with
language models,”Transactions on Machine Learning Research (TMLR), 2024.
\[53\] OpenAI, “Introducing OpenAI o1-preview.” Sept. 2024. Available: https://openai.c
om/index/introducing-openai-o1-preview/
\[54\] R. S. Sutton, “Reinforcement learning: An introduction,”A Bradford Book, 2018.
\[55\] N. Lambert, L. Castricato, L. von Werra, and A. Havrilla, “Illustrating reinforcement
learning from human feedback (RLHF),”Hugging Face Blog, 2022.
\[56\] M. Liet al., “Branch-train-merge: Embarrassingly parallel training of expert language
models,”arXiv preprint arXiv:2208.03306, 2022.
\[57\] T. Cohereet al., “Command a: An enterprise-ready large language model,”arXiv
preprint arXiv:2504.00698, 2025.
\[58\] T. OLMoet al., “2 OLMo 2 furious,”arXiv preprint arXiv:2501.00656, 2024.
\[59\] S. Alrashed, “SmolTulu: Higher learning rate to batch size ratios can lead to better
reasoning in SLMs,”arXiv preprint arXiv:2412.08347, 2024.
\[60\] A. Yanget al., “Qwen3 technical report.” 2025. doi: 10.48550/arXiv.2505.09388.
\[61\] B. Xiaet al., “MiMo: Unlocking the reasoning potential of language model–from
pretraining to posttraining,”arXiv preprint arXiv:2505.07608, 2025.
\[62\] B. Seedet al., “Seed1.5-thinking: Advancing superb reasoning models with reinforce-
ment learning.” 2025. Available: https://arxiv.org/abs/2504.13914
\[63\] T. Brownet al., “Language models are few-shot learners,”Advances in neural infor-
mation processing systems, vol. 33, pp. 1877–1901, 2020.
rlhfbook.com 210

\[64\] C. Raffelet al., “Exploring the limits of transfer learning with a unified text-to-text
transformer,”Journal of machine learning research, vol. 21, no. 140, pp. 1–67, 2020.
\[65\] J. Weiet al., “Finetuned language models are zero-shot learners,” inInternational
conference on learning representations, 2022. Available: https://openreview.net/for
um?id=gEZrGCozdqR
\[66\] V. Sanhet al., “Multitask prompted training enables zero-shot task generalization,”
inInternational conference on learning representations, 2022. Available: https:
//openreview.net/forum?id=9Vrb9D0WI4
\[67\] S. Mishra, D. Khashabi, C. Baral, and H. Hajishirzi, “Cross-task generalization via nat-
ural language crowdsourcing instructions,” inProceedings of the 60th annual meeting
of the association for computational linguistics (volume 1: Long papers), Association
for Computational Linguistics, May 2022, pp. 3470–3487. doi: 10.18653/v1/2022.acl-
long.244.
\[68\] E. Wallace, K. Xiao, R. Leike, L. Weng, J. Heidecke, and A. Beutel, “The instruc-
tion hierarchy: Training llms to prioritize privileged instructions,”arXiv preprint
arXiv:2404.13208, 2024.
\[69\] T. Dettmers, A. Pagnoni, A. Holtzman, and L. Zettlemoyer, “Qlora: Efficient finetun-
ing of quantized llms,”Advances in neural information processing systems, vol. 36,
pp. 10088–10115, 2023.
\[70\] N. Rajani, L. Tunstall, E. Beeching, N. Lambert, A. M. Rush, and T. Wolf, “No
robots,”Hugging Face repository. https://huggingface.co/datasets/HuggingFaceH4/
no_robots; Hugging Face, 2023.
\[71\] A. Y. Ng, S. Russell,et al., “Algorithms for inverse reinforcement learning.” in
Proceedings of the seventeenth international conference on machine learning, in ICML
’00. 2000, pp. 663--670.
\[72\] R. A. Bradley and M. E. Terry, “Rank analysis of incomplete block designs: I. The
method of paired comparisons,”Biometrika, vol. 39, no. 3/4, pp. 324–345, 1952,
Accessed: Feb. 13, 2023. [Online]. Available: http://www.jstor.org/stable/2334029
\[73\] K. Cobbeet al., “Training verifiers to solve math word problems,”arXiv preprint
arXiv:2110.14168, 2021.
\[74\] J. Uesatoet al., “Solving math word problems with process- and outcome-based
feedback,”arXiv preprint arXiv:2211.14275, 2022.
\[75\] C. Lyuet al., “Exploring the limit of outcome reward for learning mathematical
reasoning,”arXiv preprint arXiv:2502.06781, 2025.
\[76\] B. Zhuet al., “Starling-7b: Improving helpfulness and harmlessness with rlaif,” in
First conference on language modeling, 2024.
\[77\] A. Liu, Z. Zhao, C. Liao, P. Lu, and L. Xia, “Learning plackett-luce mixtures from
partial preferences,” inProceedings of the AAAI conference on artificial intelligence,
2019, pp. 4328–4335.
\[78\] B. Zhu, M. Jordan, and J. Jiao, “Principled reinforcement learning with human
feedback from pairwise or k-wise comparisons,” inInternational conference on machine
learning, PMLR, 2023, pp. 43037–43067.
\[79\] L. Zhenget al., “Judging LLM-as-a-judge with MT-Bench and Chatbot Arena,”
Advances in Neural Information Processing Systems, vol. 36, pp. 46595–46623, 2023.
\[80\] Y. Dubois, B. Galambosi, P. Liang, and T. B. Hashimoto, “Length-controlled alpacae-
val: A simple way to debias automatic evaluators,”arXiv preprint arXiv:2404.04475,
2024.
rlhfbook.com 211

\[81\] T. Liet al., “From crowdsourced data to high-quality benchmarks: Arena-hard and
BenchBuilder pipeline,” inInternational conference on machine learning (ICML),
2025.
\[82\] B. Y. Linet al., “WILDBENCH: Benchmarking LLMs with challenging tasks from
real users in the wild,” inInternational conference on learning representations (ICLR),
2025.
\[83\] D. Mahanet al., “Generative reward models,” 2024, Available: https://www.synthlab
s.ai/pdf/Generative_Reward_Models.pdf
\[84\] L. Zhang, A. Hosseini, H. Bansal, M. Kazemi, A. Kumar, and R. Agarwal, “Generative
verifiers: Reward modeling as next-token prediction,” inInternational conference on
learning representations (ICLR), 2025.
\[85\] Z. Ankner, M. Paul, B. Cui, J. D. Chang, and P. Ammanabrolu, “Critique-out-loud
reward models,”arXiv preprint arXiv:2408.11791, 2024.
\[86\] S. Kimet al., “Prometheus: Inducing fine-grained evaluation capability in language
models,” inThe twelfth international conference on learning representations, 2024.
\[87\] N. Lambertet al., “Rewardbench: Evaluating reward models for language modeling,”
inConference of the north american chapter of the association for computational
linguistics (NAACL), 2025.
\[88\] X. Wenet al., “Rethinking reward model evaluation: Are we barking up the wrong
tree?” inInternational conference on learning representations (ICLR), 2025.
\[89\] E. Zhouet al., “RMB: Comprehensively benchmarking reward models in LLM align-
ment,” inInternational conference on learning representations (ICLR), 2025.
\[90\] S. Maliket al., “RewardBench 2: Advancing reward model evaluation,”arXiv preprint
arXiv:2506.01937, 2025.
\[91\] E. Fricket al., “How to evaluate reward models for RLHF,” inInternational conference
on learning representations (ICLR), 2025.
\[92\] Y. Liu, Z. Yao, R. Min, Y. Cao, L. Hou, and J. Li, “RM-bench: Benchmarking reward
models of language models with subtlety and style,” inInternational conference on
learning representations (ICLR), 2025.
\[93\] S. Gurejaet al., “M-RewardBench: Evaluating reward models in multilingual settings,”
inAnnual meeting of the association for computational linguistics (ACL), 2025.
\[94\] Z. Jinet al., “RAG-RewardBench: Benchmarking reward models in retrieval aug-
mented generation for preference alignment,” inAnnual meeting of the association
for computational linguistics (ACL), 2025.
\[95\] Z. Wu, M. Yasunaga, A. Cohen, Y. Kim, A. Celikyilmaz, and M. Ghazvininejad,
“reWordBench: Benchmarking and improving the robustness of reward models with
transformed inputs,”arXiv preprint arXiv:2503.11751, 2025.
\[96\] S. Kimet al., “Evaluating robustness of reward models for mathematical reasoning,”
arXiv preprint arXiv:2410.01729, 2024.
\[97\] Z. Liu, Y. Chen, M. Shoeybi, B. Catanzaro, and W. Ping, “AceMath: Advancing
frontier math reasoning with post-training and reward modeling,” inAnnual meeting
of the association for computational linguistics (ACL), 2025. Available: https://arxiv.
org/abs/2412.15084
\[98\] M. Song, Z. Su, X. Qu, J. Zhou, and Y. Cheng, “PRMBench: A fine-grained and
challenging benchmark for process-level reward models,” inAnnual meeting of the
association for computational linguistics (ACL), 2025.
rlhfbook.com 212

\[99\] C. Zhenget al., “ProcessBench: Identifying process errors in mathematical reasoning,”
inAnnual meeting of the association for computational linguistics (ACL), 2025.
Available: https://arxiv.org/abs/2412.06559
\[100\] W. Wanget al., “VisualPRM: An effective process reward model for multimodal
reasoning,”arXiv preprint arXiv:2503.10291, 2025.
\[101\] H. Tu, W. Feng, H. Chen, H. Liu, X. Tang, and C. Xie, “ViLBench: A suite for
vision-language process reward modeling.” Mar. 2025. Available: https://arxiv.org/
abs/2503.20271
\[102\] T. Men, Z. Jin, P. Cao, Y. Chen, K. Liu, and J. Zhao, “Agent-RewardBench: Towards a
unified benchmark for reward modeling across perception, planning, and safety in real-
world multimodal agents,” inProceedings of the 63rd annual meeting of the association
for computational linguistics (volume 1: Long papers), Vienna, Austria: Association for
Computational Linguistics, July 2025, pp. 17521–17541. doi: 10.18653/v1/2025.acl-
long.857.
\[103\] H. Linet al., “CUARewardBench: A benchmark for evaluating reward models on
computer-using agent.” 2025. Available: https://arxiv.org/abs/2510.18596
\[104\] Z. Chenet al., “MJ-bench: Is your multimodal reward model really a good judge for
text-to-image generation?”arXiv preprint arXiv:2407.04842, 2024.
\[105\] M. Yasunaga, L. Zettlemoyer, and M. Ghazvininejad, “Multimodal rewardbench:
Holistic evaluation of reward models for vision language models,”arXiv preprint
arXiv:2502.14191, 2025.
\[106\] L. Liet al., “VLRewardBench: A challenging benchmark for vision-language generative
reward models,”arXiv preprint arXiv:2411.17451, 2024.
\[107\] J. Ruanet al., “Vlrmbench: A comprehensive and challenging benchmark for vision-
language reward models,”arXiv preprint arXiv:2503.07478, 2025.
\[108\] H. Wang, W. Xiong, T. Xie, H. Zhao, and T. Zhang, “Interpretable preferences via
multi-objective reward modeling and mixture-of-experts,” inConference on empirical
methods in natural language processing (EMNLP), 2024.
\[109\] Z. Wanget al., “HelpSteer2: Open-source dataset for training top-performing reward
models,”arXiv preprint arXiv:2406.08673, 2024.
\[110\] Z. Wanget al., “HelpSteer2-preference: Complementing ratings with preferences,” in
International conference on learning representations (ICLR), 2025.
\[111\] J. Park, S. Jwa, M. Ren, D. Kim, and S. Choi, “Offsetbias: Leveraging debiased
data for tuning evaluators,” inConference on empirical methods in natural language
processing (EMNLP), 2024.
\[112\] A. Ahmadianet al., “Back to basics: Revisiting reinforce style optimization for
learning from human feedback in llms,” inAnnual meeting of the association for
computational linguistics (ACL), 2024.
\[113\] J. Schulman, P. Moritz, S. Levine, M. Jordan, and P. Abbeel, “High-dimensional
continuous control using generalized advantage estimation,” inProceedings of the
international conference on learning representations (ICLR), 2016.
\[114\] R. J. Williams, “Simple statistical gradient-following algorithms for connectionist
reinforcement learning,”Machine learning, vol. 8, pp. 229–256, 1992.
\[115\] S. C. Huang, A. Ahmadian, and C. F. AI, “Putting RL back in RLHF.” https:
//huggingface.co/blog/putting_rl_back_in_rlhf_with_rloo, 2024.
\[116\] W. Kool, H. van Hoof, and M. Welling, “Buy 4 reinforce samples, get a baseline for
free!” 2019.
rlhfbook.com 213

\[117\] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy
optimization algorithms,”arXiv preprint arXiv:1707.06347, 2017.
\[118\] C. Berneret al., “Dota 2 with large scale deep reinforcement learning,”arXiv preprint
arXiv:1912.06680, 2019.
\[119\] Z. Liuet al., “Understanding R1-zero-like training: A critical perspective,”arXiv
preprint arXiv:2503.20783, Mar. 2025, Available: https://arxiv.org/abs/2503.20783
\[120\] J. Nocedal and S. J. Wright,Numerical optimization. Springer, 2006.
\[121\] J. Schulman, S. Levine, P. Abbeel, M. Jordan, and P. Moritz, “Trust region policy
optimization,” inInternational conference on machine learning, PMLR, 2015, pp.
1889–1897.
\[122\] Z. Shaoet al., “Deepseekmath: Pushing the limits of mathematical reasoning in open
language models,”arXiv preprint arXiv:2402.03300, 2024.
\[123\] C. Zhenget al., “Group sequence policy optimization.” 2025. doi:
10.48550/arXiv.2507.18071.
\[124\] MiniMax, “MiniMax-M1: Scaling test-time compute efficiently with lightning atten-
tion.” 2025. doi: 10.48550/arXiv.2506.13585.
\[125\] N. Le Rouxet al., “Tapered off-policy REINFORCE: Stable and efficient reinforcement
learning for LLMs.” 2025. doi: 10.48550/arXiv.2503.14286.
\[126\] H. Ivisonet al., “Unpacking DPO and PPO: Disentangling best practices for learning
from preference feedback,” inAdvances in neural information processing systems
(NeurIPS), 2024.
\[127\] J. Schulman, “Approximating KL-divergence.” http://joschu.net/blog/kl-approx.html,
2016.
\[128\] S. Huang, M. Noukhovitch, A. Hosseini, K. Rasul, W. Wang, and L. Tunstall, “The n+
implementation details of RLHF with PPO: A case study on TL;DR summarization,”
inFirst conference on language modeling, 2024. Available: https://openreview.net/f
orum?id=kHO2ZTa8e3
\[129\] L. Weng, “Policy gradient algorithms,”lilianweng.github.io, 2018, Available: https:
//lilianweng.github.io/posts/2018-04-08-policy-gradient/
\[130\] Q. Yuet al., “DAPO: An open-source LLM reinforcement learning system at scale.”
2025.
\[131\] A. Baheti, X. Lu, F. Brahman, R. L. Bras, M. Sap, and M. Riedl, “Leftover lunch:
Advantage-based offline reinforcement learning for language models,” inInternational
conference on learning representations (ICLR), 2024.
\[132\] M. Noukhovitch, S. Huang, S. Xhonneux, A. Hosseini, R. Agarwal, and A. Courville,
“Asynchronous RLHF: Faster and more efficient off-policy RL for language models,”
inInternational conference on learning representations (ICLR), 2025.
\[133\] B. Wuet al., “LlamaRL: A distributed asynchronous reinforcement learning framework
for efficient large-scale LLM trainin,”arXiv preprint arXiv:2505.24034, 2025.
\[134\] W. Fuet al., “AReaL: A large-scale asynchronous reinforcement learning system for
language reasoning,”arXiv preprint arXiv:2505.24298, 2025.
\[135\] P. I. Teamet al., “INTELLECT-2: A reasoning model trained through globally
decentralized reinforcement learning.” 2025. Available: https://arxiv.org/abs/2505.0
7291
\[136\] E. L. Ionides, “Truncated importance sampling,”Journal of Computational and
Graphical Statistics, vol. 17, no. 2, pp. 295–311, 2008.
rlhfbook.com 214

\[137\] F. Yao, L. Liu, D. Zhang, C. Dong, J. Shang, and J. Gao, “Your efficient RL framework
secretly brings you off-policy RL training.” 2025. Available: https://fengyao.notion.s
ite/off-policy-rl
\[138\] D. Seita, “Notes on the generalized advantage estimation paper.” 2017. Available:
https://danieltakeshi.github.io/2017/04/02/notes-on-the-generalized-advantage-
estimation-paper/
\[139\] T. Wu, B. Zhu, R. Zhang, Z. Wen, K. Ramchandran, and J. Jiao, “Pairwise proximal
policy optimization: Harnessing relative feedback for llm alignment,”arXiv preprint
arXiv:2310.00212, 2023.
\[140\] C. Gaoet al., “Soft adaptive policy optimization,”arXiv preprint arXiv:2511.20347,
Nov. 2025, Available: https://arxiv.org/abs/2511.20347
\[141\] Y. Flet-Berliacet al., “Contrastive policy gradient: Aligning LLMs on sequence-level
scores in a supervised-friendly fashion,” inConference on empirical methods in natural
language processing (EMNLP), 2024.
\[142\] Z. Liet al., “Remax: A simple, effective, and efficient reinforcement learning method
for aligning large language models,” inForty-first international conference on machine
learning, 2024.
\[143\] T. Gunteret al., “Apple intelligence foundation language models,”arXiv preprint
arXiv:2407.21075, 2024.
\[144\] K. Teamet al., “Kimi k1. 5: Scaling reinforcement learning with llms,”arXiv preprint
arXiv:2501.12599, 2025.
\[145\] M. Tomar, L. Shani, Y. Efroni, and M. Ghavamzadeh, “Mirror descent policy opti-
mization,” inInternational conference on learning representations (ICLR), 2022.
\[146\] Y. Zhanget al., “Improving LLM general preference alignment via optimistic online
mirror descent,”arXiv preprint arXiv:2502.16852, 2025.
\[147\] Y. Yuanet al., “VAPO: Efficient and reliable reinforcement learning for advanced
reasoning tasks,”arXiv preprint arXiv:2504.05118, 2025.
\[148\] Y. Yuan, Y. Yue, R. Zhu, T. Fan, and L. Yan, “What’s behind PPO’s collapse in
long-CoT? Value optimization holds the secret,”arXiv preprint arXiv:2503.01491,
2025.
\[149\] A. Irpan, “Deep reinforcement learning doesn’t work yet.” 2018. Available: https:
//www.alexirpan.com/2018/02/14/rl-hard.html
\[150\] P. Henderson, R. Islam, P. Bachman, J. Pineau, D. Precup, and D. Meger, “Deep
reinforcement learning that matters,” inProceedings of the AAAI conference on
artificial intelligence, 2018. Available: https://ojs.aaai.org/index.php/AAAI/article/
view/11694
\[151\] A. Mirhoseiniet al., “Chip placement with deep reinforcement learning,” inDesign,
automation and test in europe (DATE), 2023.
\[152\] J. Schrittwieseret al., “Mastering atari, go, chess and shogi by planning with a learned
model,”Nature, vol. 588, no. 7839, pp. 604–609, 2020.
\[153\] M. Cusumano-Towneret al., “Robust autonomy emerges from self-play,” inInterna-
tional conference on machine learning (ICML), 2025.
\[154\] G. Shenget al., “HybridFlow: A flexible and efficient RLHF framework,” inEuropean
conference on computer systems (EuroSys), 2025.
\[155\] J. Huet al., “OpenRLHF: An easy-to-use, scalable and high-performance RLHF
framework,”arXiv preprint arXiv:2405.11143, 2024.
rlhfbook.com 215

\[156\] J. Liu, A. Cohen, R. Pasunuru, Y. Choi, H. Hajishirzi, and A. Celikyilmaz, “Don’t
throw away your value model! Generating more preferable text with value-guided
monte-carlo tree search decoding,”arXiv preprint arXiv:2309.15028, 2023.
\[157\] B. Brownet al., “Large language monkeys: Scaling inference compute with repeated
sampling,”arXiv preprint arXiv:2407.21787, 2024.
\[158\] Z. Liuet al., “Inference-time scaling for generalist reward modeling,”arXiv preprint
arXiv:2504.02495, 2025.
\[159\] N. Muennighoffet al., “s1: Simple test-time scaling,”arXiv preprint arXiv:2501.19393,
2025.
\[160\] L. Chenet al., “Are more llm calls all you need? Towards scaling laws of compound
inference systems,”arXiv preprint arXiv:2403.02419, 2024.
\[161\] E. Zelikman, Y. Wu, J. Mu, and N. Goodman, “STaR: Bootstrapping reasoning
with reasoning,” inAdvances in neural information processing systems, A. H. Oh, A.
Agarwal, D. Belgrave, and K. Cho, Eds., 2022. Available: https://openreview.net/for
um?id=_3ELRdg2sgI
\[162\] E. Zelikman, G. Harik, Y. Shao, V. Jayasiri, N. Haber, and N. D. Goodman, “Quiet-
STaR: Language models can teach themselves to think before speaking,”COLM, vol.
abs/2403.09629, 2024.
\[163\] M. D. Hoffmanet al., “Training chain-of-thought via latent-variable inference,” in
Thirty-seventh conference on neural information processing systems, 2023. Available:
https://openreview.net/forum?id=a147pIS2Co
\[164\] A. Kazemnejadet al., “VinePPO: Unlocking RL potential for LLM reasoning through
refined credit assignment.” 2024. Available: https://arxiv.org/abs/2410.01679
\[165\] J. Gehring, K. Zheng, J. Copet, V. Mella, T. Cohen, and G. Synnaeve, “RLEF:
Grounding code LLMs in execution feedback with reinforcement learning,” in
International conference on machine learning (ICML), 2025. Available: https:
//arxiv.org/abs/2410.02089
\[166\] S. Xuet al., “Is dpo superior to ppo for llm alignment? A comprehensive study,” in
International conference on machine learning (ICML), 2024.
\[167\] N. Amit, S. Goldwasser, O. Paradise, and G. Rothblum, “Models that prove their
own correctness,”Electron. Colloquium Comput. Complex., 2024.
\[168\] J. Hu, Y. Zhang, Q. Han, D. Jiang, X. Zhang, and H. Shum, “Open-reasoner-zero:
An open source approach to scaling up reinforcement learning on the base model,”
arXiv preprint arXiv:2503.24290, 2025.
\[169\] M. Abdin, S. Agarwal, A. Awadallah,et al., “Phi-4-reasoning technical report,”arXiv
preprint arXiv:2504.21318, 2025.
\[170\] A. Bercovich, I. Levy, I. Golan,et al., “Llama-nemotron: Efficient reasoning models,”
arXiv preprint arXiv:2505.00949, 2025.
\[171\] A. Liu, B. Zhou, C. Xu,et al., “Hunyuan-TurboS: Advancing large language models
through mamba-transformer synergy and adaptive chain-of-thought,”arXiv preprint
arXiv:2505.15431, 2025.
\[172\] J. He, J. Liu, C. Y. Liu,et al., “Skywork open reasoner 1 technical report,”arXiv
preprint arXiv:2505.22312, 2025.
\[173\] C. Teamet al., “MiMo-VL technical report.” 2025. Available: https://arxiv.org/abs/
2506.03569
rlhfbook.com 216

\[174\] E. Guha, R. Marten, S. Keh,et al., “OpenThoughts: Data recipes for reasoning
models,”arXiv preprint arXiv:2506.04178, 2025.
\[175\] Mistral AI, “Magistral: Scaling reinforcement learning for reasoning in large language
models,” Mistral AI, 2025. Available: https://mistral.ai/static/research/magistral.pdf
\[176\] K. Teamet al., “Kimi K2: Open agentic intelligence.” 2025. Available: https:
//arxiv.org/abs/2507.20534
\[177\] A. Zenget al., “GLM-4.5: Agentic, reasoning, and coding (ARC) foundation models.”
2025. doi: 10.48550/arXiv.2508.06471.
\[178\] NVIDIA, “NVIDIA nemotron nano 2: An accurate and efficient hybrid mamba-
transformer reasoning model.” 2025. Available: https://arxiv.org/abs/2508.14444
\[179\] Z. Chenget al., “K2-think: A parameter-efficient reasoning system.” 2025. Available:
https://arxiv.org/abs/2509.07604
\[180\] M.L.Team, “IntroducingLongCat-flash-thinking: Atechnicalreport.”2025. Available:
https://arxiv.org/abs/2509.18883
\[181\] L. Teamet al., “Every step evolves: Scaling reinforcement learning for trillion-scale
thinking model.” 2025. Available: https://arxiv.org/abs/2510.18855
\[182\] DeepSeek-AI, “DeepSeek-V3.2: Pushing the frontier of open large language models.”
2025. Available: https://arxiv.org/abs/2512.02556
\[183\] Z. Liuet al., “K2-V2: A 360-open, reasoning-enhanced LLM,”arXiv preprint
arXiv:2512.06201, 2025.
\[184\] NVIDIA, “Nemotron 3 nano: Open, efficient mixture-of-experts hybrid mamba-
transformer model for agentic reasoning,” NVIDIA, Technical Report, 2025. Available:
https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-
Technical-Report.pdf
\[185\] Xiaomi LLM-Core Teamet al., “MiMo-V2-flash technical report.” Jan. 2026. doi:
10.48550/arXiv.2601.02780.
\[186\] Z. Wanget al., “RAGEN: Understanding self-evolution in LLM agents via multi-turn
reinforcement learning.” 2025. Available: https://arxiv.org/abs/2504.20073
\[187\] R. Shaoet al., “Spurious rewards: Rethinking training signals in RLVR.” https:
//rethink-rlvr.notion.site/Spurious-Rewards-Rethinking-Training-Signals-in-
RLVR-1f4df34dac1880948858f95aeb88872f, 2025.
\[188\] Anthropic, “Claude 4.” May 2025. Available: https://www.anthropic.com/news/cla
ude-4
\[189\] P. Aggarwal and S. Welleck, “L1: Controlling how long a reasoning model thinks with
reinforcement learning,”arXiv preprint arXiv:2503.04697, 2025.
\[190\] Y. Zhao, R. Joshi, T. Liu, M. Khalman, M. Saleh, and P. J. Liu, “Slic-hf: Sequence
likelihood calibration with human feedback,”arXiv preprint arXiv:2305.10425, 2023.
\[191\] Z. Gaoet al., “Rebel: Reinforcement learning via regressing relative rewards,” in
Advances in neural information processing systems (NeurIPS), 2024.
\[192\] M. G. Azaret al., “A general theoretical paradigm to understand learning from
human preferences,” inInternational conference on artificial intelligence and statistics,
PMLR, 2024, pp. 4447–4455.
\[193\] A. Amini, T. Vieira, and R. Cotterell, “Direct preference optimization with an offset,”
inAnnual meeting of the association for computational linguistics (ACL), 2024.
\[194\] J. Hong, N. Lee, and J. Thorne, “Reference-free monolithic preference optimization
with odds ratio,”arXiv e-prints, pp. arXiv–2403, 2024.
rlhfbook.com 217

\[195\] Y. Meng, M. Xia, and D. Chen, “Simpo: Simple preference optimization with a
reference-free reward,”Advances in Neural Information Processing Systems, vol. 37,
pp. 124198–124235, 2025.
\[196\] N. Razin, S. Malladi, A. Bhaskar, D. Chen, S. Arora, and B. Hanin, “Uninten-
tional unalignment: Likelihood displacement in direct preference optimization,” in
International conference on learning representations (ICLR), 2025.
\[197\] Y. Ren and D. J. Sutherland, “Learning dynamics of llm finetuning,” inInternational
conference on learning representations (ICLR), 2025.
\[198\] T. Xiao, Y. Yuan, H. Zhu, M. Li, and V. G. Honavar, “Cal-dpo: Calibrated direct pref-
erence optimization for language model alignment,” inAdvances in neural information
processing systems (NeurIPS), 2024.
\[199\] A. Guptaet al., “AlphaPO–reward shape matters for LLM alignment,” inInternational
conference on machine learning (ICML), 2025.
\[200\] S. Guoet al., “Direct language model alignment from online ai feedback,”arXiv
preprint arXiv:2402.04792, 2024.
\[201\] P. Singhal, N. Lambert, S. Niekum, T. Goyal, and G. Durrett, “D2po: Discriminator-
guided dpo with response evaluation models,”arXiv preprint arXiv:2405.01511, 2024.
\[202\] C. Rosset, C.-A. Cheng, A. Mitra, M. Santacroce, A. Awadallah, and T. Xie, “Direct
nash optimization: Teaching language models to self-improve with general preferences,”
arXiv preprint arXiv:2404.03715, 2024.
\[203\] S. Jung, G. Han, D. W. Nam, and K.-W. On, “Binary classifier optimization for large
language model alignment,” inAnnual meeting of the association for computational
linguistics (ACL), 2025.
\[204\] H. Zhaoet al., “Rainbowpo: A unified framework for combining improvements in
preference optimization,” inInternational conference on learning representations
(ICLR), 2025.
\[205\] A. Gorbatovski, B. Shaposhnikov, V. Sinii, A. Malakhov, and D. Gavrilov,
“The differences between direct alignment algorithms are a blur,”arXiv preprint
arXiv:2502.01237, 2025.
\[206\] E. Bakouchet al., “SmolLM3: smol, multilingual, long-context reasoner.” https:
//huggingface.co/blog/smollm3, 2025.
\[207\] S. Genget al., “The delta learning hypothesis: Preference tuning on weak data can
yield strong gains,” inSecond conference on language modeling, 2025. Available:
https://openreview.net/forum?id=9rwtezthwo
\[208\] A. Panickssery, S. Bowman, and S. Feng, “Llm evaluators recognize and favor their
own generations,”Advances in Neural Information Processing Systems, 2024.
\[209\] F. Tajwaret al., “Preference fine-tuning of llms should leverage suboptimal, on-policy
data,” inInternational conference on machine learning (ICML), 2024.
\[210\] W. R. Gilks and P. Wild, “Adaptive rejection sampling for gibbs sampling,”Journal
of the Royal Statistical Society: Series C (Applied Statistics), vol. 41, no. 2, pp.
337–348, 1992.
\[211\] H. Donget al., “RAFT: Reward rAnked FineTuning for generative foundation model
alignment,”Transactions on Machine Learning Research (TMLR), 2023.
\[212\] T. Liuet al., “Statistical rejection sampling improves preference optimization,” in
International conference on learning representations (ICLR), 2024.
rlhfbook.com 218

\[213\] N. Lambert, T. K. Gilbert, and T. Zick, “Entangled preferences: The history and risks
of reinforcement learning and human feedback,”arXiv preprint arXiv:2310.13595,
2023.
\[214\] V. Conitzeret al., “Social choice should guide AI alignment in dealing with diverse
human feedback,” inInternational conference on machine learning (ICML), 2024.
\[215\] A. Mishra, “Ai alignment and social choice: Fundamental limitations and policy
implications,”arXiv preprint arXiv:2310.16048, 2023.
\[216\] H. R. Kirket al., “The PRISM alignment project: What participatory, representative
and individualised human feedback reveals about the subjective and multicultural
alignment of large language models,”arXiv preprint arXiv:2404.16019, 2024.
\[217\] S. Poddar, Y. Wan, H. Ivison, A. Gupta, and N. Jaques, “Personalizing reinforcement
learning from human feedback with variational preference learning,” inAdvances in
neural information processing systems (NeurIPS), 2024.
\[218\] A. Arnauld,The port-royal logic. 1662.
\[219\] J. Bentham,An introduction to the principles of morals and legislation. 1823.
\[220\] F. P. Ramsey, “Truth and probability,”Readings in Formal Epistemology: Sourcebook,
pp. 21–45, 2016.
\[221\] A. O. Hirschman, “Against parsimony: Three easy ways of complicating some cate-
gories of economic discourse,”Bulletin of the American Academy of arts and Sciences,
vol. 37, no. 8, pp. 11–28, 1984.
\[222\] G. K. Hadfield and B. R. Weingast, “Microfoundations of the rule of law,”Annual
Review of Political Science, vol. 17, pp. 21–42, 2014.
\[223\] E. L. Thorndike, “The law of effect,”The American journal of psychology, vol. 39, no.
1/4, pp. 212–222, 1927.
\[224\] B. F. Skinner,The behavior of organisms: An experimental analysis. BF Skinner
Foundation, 2019.
\[225\] R. A. Briggs, “Normative theories of rational choice: Expected utility,” 2014.
\[226\] B. Widrow and M. E. Hoff, “Adaptive switching circuits,” Stanford Univ Ca Stanford
Electronics Labs, 1960.
\[227\] S. Singh, R. L. Lewis, and A. G. Barto, “Where do rewards come from,” inProceedings
of the annual conference of the cognitive science society, Cognitive Science Society,
2009, pp. 2601–2606.
\[228\] S. M. McClure, N. D. Daw, and P. R. Montague, “A computational substrate for
incentive salience,”Trends in neurosciences, vol. 26, no. 8, pp. 423–428, 2003.
\[229\] D. Silver, S. Singh, D. Precup, and R. S. Sutton, “Reward is enough,”Artificial
Intelligence, vol. 299, p. 103535, 2021.
\[230\] R. Bellman, “A markovian decision process,”Journal of mathematics and mechanics,
pp. 679–684, 1957.
\[231\] R. A. Howard, “Dynamic programming and markov processes.” 1960.
\[232\] J. M. Mendel and R. W. McLaren, “8 reinforcement-learning control and pattern
recognition systems,” inAdaptive, learning and pattern recognition systems, vol. 66,
J. M. Mendel and K. S. Fu, Eds., in Mathematics in science and engineering, vol. 66.,
Elsevier, 1970, pp. 287–318. doi: https://doi.org/10.1016/S0076-5392(08)60497-X.
\[233\] M. Waltz and K. Fu, “A heuristic approach to reinforcement learning control systems,”
IEEE Transactions on Automatic Control, vol. 10, no. 4, pp. 390–398, 1965, doi:
10.1109/TAC.1965.1098193.
rlhfbook.com 219

\[234\] A. H. Klopf,Brain function and adaptive systems: A heterostatic theory. Air Force
Cambridge Research Laboratories, Air Force Systems Command, 1972.
\[235\] R. S. Sutton, “Learning to predict by the methods of temporal differences,”Machine
learning, vol. 3, pp. 9–44, 1988.
\[236\] G. Tesauroet al., “Temporal difference learning and TD-gammon,”Communications
of the ACM, vol. 38, no. 3, pp. 58–68, 1995.
\[237\] C. J. Watkins and P. Dayan, “Q-learning,”Machine learning, vol. 8, pp. 279–292,
1992.
\[238\] V. Mnihet al., “Playing atari with deep reinforcement learning,”arXiv preprint
arXiv:1312.5602, 2013.
\[239\] F. Golnaraghi and B. C. Kuo,Automatic control systems. McGraw-Hill Education,
2017.
\[240\] D. Silveret al., “Mastering the game of go without human knowledge,”Nature, vol.
550, no. 7676, pp. 354–359, 2017.
\[241\] J. Degraveet al., “Magnetic control of tokamak plasmas through deep reinforcement
learning,”Nature, vol. 602, no. 7897, pp. 414–419, 2022.
\[242\] E. Kaufmann, L. Bauersfeld, A. Loquercio, M. Müller, V. Koltun, and D. Scaramuzza,
“Champion-level drone racing using deep reinforcement learning,”Nature, vol. 620,
no. 7976, pp. 982–987, 2023, doi: 10.1038/s41586-023-06419-4.
\[243\] R. Agarwal, M. Schwarzer, P. S. Castro, A. C. Courville, and M. Bellemare, “Deep
reinforcement learning at the edge of the statistical precipice,”Advances in neural
information processing systems, vol. 34, pp. 29304–29320, 2021.
\[244\] N. Salha, “Aesthetics & art in the early development of human-computer interfaces,”
PhD thesis, Universität Bremen, 2011.
\[245\] T. K. Gilbert, S. Dean, T. Zick, and N. Lambert, “Choices, risks, and reward
reports: Charting public policy for reinforcement learning systems,”arXiv preprint
arXiv:2202.05716, 2022.
\[246\] J. Von Neumann and O. Morgenstern, “Theory of games and economic behavior, 2nd
rev,” 1947.
\[247\] S. Pitis, “Rethinking the discount factor in reinforcement learning: A decision theoretic
approach,” inProceedings of the AAAI conference on artificial intelligence, 2019, pp.
7949–7956.
\[248\] S. Pitis, “Consistent aggregation of objectives with diverse time preferences re-
quires non-markovian rewards,” inAdvances in neural information processing systems
(NeurIPS), 2023.
\[249\] D.Abelet al., “Ontheexpressivityofmarkovreward,”Advances in Neural Information
Processing Systems, vol. 34, pp. 7799–7812, 2021.
\[250\] A. Sen, “Behaviour and the concept of preference,”Economica, vol. 40, no. 159, pp.
241–259, 1973.
\[251\] K. J. Arrow, “A difficulty in the concept of social welfare,”Journal of political economy,
vol. 58, no. 4, pp. 328–346, 1950.
\[252\] E. Maskin and A. Sen,The arrow impossibility theorem. Columbia University Press,
2014.
\[253\] J. C. Harsanyi, “Rule utilitarianism and decision theory,”Erkenntnis, vol. 11, no. 1,
pp. 25–53, 1977.
rlhfbook.com 220

\[254\] D. Hadfield-Menell, S. J. Russell, P. Abbeel, and A. Dragan, “Cooperative inverse
reinforcement learning,”Advances in neural information processing systems, vol. 29,
2016.
\[255\] A.Fickinger, S.Zhuang, D.Hadfield-Menell, andS.Russell, “Multi-principalassistance
games,”arXiv preprint arXiv:2007.09540, 2020.
\[256\] N. Soares, B. Fallenstein, S. Armstrong, and E. Yudkowsky, “Corrigibility,” inWork-
shops at the twenty-ninth AAAI conference on artificial intelligence, 2015.
\[257\] R. Pettigrew,Choosing for changing selves. Oxford University Press, 2019.
\[258\] Z. Wanget al., “HelpSteer3-preference: Open human-annotated preference data across
diverse tasks and languages,”arXiv preprint arXiv:2505.11475, 2025.
\[259\] W.-L. Chianget al., “Chatbot Arena: An open platform for evaluating LLMs by
human preference,” inInternational conference on machine learning (ICML), 2024.
\[260\] R. Likert, “A technique for the measurement of attitudes.”Archives of psychology,
1932.
\[261\] J. Zhouet al., “Instruction-following evaluation for large language models.” 2023.
Available: https://arxiv.org/abs/2311.07911
\[262\] K. Ethayarajh, W. Xu, N. Muennighoff, D. Jurafsky, and D. Kiela, “Kto: Model
alignment as prospect theoretic optimization,”arXiv preprint arXiv:2402.01306, 2024.
\[263\] Z. Wuet al., “Fine-grained human feedback gives better rewards for language model
training,”Advances in Neural Information Processing Systems, vol. 36, 2023.
\[264\] A. Chenet al., “Learning from natural language feedback,”Transactions on Machine
Learning Research, 2024.
\[265\] A. Kumar, Y. He, A. H. Markosyan, B. Chern, and I. Arrieta-Ibarra, “Detecting prefix
bias in LLM-based reward models,” inACM conference on fairness, accountability,
and transparency (FAccT), 2025.
\[266\] A. Bharadwaj, C. Malaviya, N. Joshi, and M. Yatskar, “Flattery, fluff, and fog:
Diagnosing and mitigating idiosyncratic biases in preference models.” 2025. Available:
https://arxiv.org/abs/2506.05339
\[267\] M. Sharmaet al., “Towards understanding sycophancy in language models,” in
The twelfth international conference on learning representations, 2024. Available:
https://openreview.net/forum?id=tvhaxkMKAn
\[268\] Y. Bu, L. Huo, Y. Jing, and Q. Yang, “Beyond excess and deficiency: Adaptive
length bias mitigation in reward models for RLHF,” inFindings of the association
for computational linguistics: NAACL 2025, 2025, pp. 3091–3098.
\[269\] X. Zhang, W. Xiong, L. Chen, T. Zhou, H. Huang, and T. Zhang, “From lists to emojis:
How format bias affects model alignment,” inAnnual meeting of the association for
computational linguistics (ACL), 2025.
\[270\] OpenAI, “Introducing the model spec.” May 2024. Available: https://openai.com/ind
ex/introducing-the-model-spec/
\[271\] I. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot, R. Anderson, and Y. Gal, “AI
models collapse when trained on recursively generated data,”Nature, vol. 631, no.
8022, pp. 755–759, 2024.
\[272\] M. Gerstgrasseret al., “Is model collapse inevitable? Breaking the curse of recursion
by accumulating real and synthetic data,”arXiv preprint arXiv:2404.01413, 2024.
rlhfbook.com 221

\[273\] Y. Feng, E. Dohmatob, P. Yang, F. Charton, and J. Kempe, “Beyond model collapse:
Scaling up with synthesized data requires reinforcement,” inICML 2024 workshop on
theoretical foundations of foundation models, 2024.
\[274\] Y. Wanget al., “Self-instruct: Aligning language models with self-generated instruc-
tions,” inAnnual meeting of the association for computational linguistics (ACL),
2023.
\[275\] E. Beechinget al., “NuminaMath 7B TIR,”Hugging Face repository. https://huggin
gface.co/AI-MO/NuminaMath-7B-TIR; Numina & Hugging Face, 2024.
\[276\] M. Liet al., “Superfiltering: Weak-to-strong data filtering for fast instruction-tuning,”
inAnnual meeting of the association for computational linguistics (ACL), 2024.
\[277\] G. Hinton, O. Vinyals, and J. Dean, “Distilling the knowledge in a neural network,”
arXiv preprint arXiv:1503.02531, 2015.
\[278\] K. Shridhar, A. Stolfo, and M. Sachan, “Distilling reasoning capabilities into smaller
language models,”Findings of the Association for Computational Linguistics: ACL
2023, pp. 7059–7073, 2023.
\[279\] C.-Y. Hsiehet al., “Distilling step-by-step! Outperforming larger language models with
less training data and smaller model sizes,” inFindings of the association for compu-
tational linguistics: ACL 2023, 2023, pp. 8003–8017. doi: 10.18653/v1/2023.findings-
acl.507.
\[280\] GLM-5 Teamet al., “GLM-5: From vibe coding to agentic engineering.” Feb. 2026.
doi: 10.48550/arXiv.2602.15763.
\[281\] DeepSeek-AI, “DeepSeek-V4: Towards highly efficient million-token context intelli-
gence,” DeepSeek-AI, Technical Report, 2026. Available: https://huggingface.co/dee
pseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf
\[282\] Y. Kim and A. M. Rush, “Sequence-level knowledge distillation,” inProceedings of
the 2016 conference on empirical methods in natural language processing, Austin,
Texas: Association for Computational Linguistics, Nov. 2016, pp. 1317–1327. doi:
10.18653/v1/D16-1139.
\[283\] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, “DistilBERT, a distilled version of
BERT: Smaller, faster, cheaper and lighter.” 2019. doi: 10.48550/arXiv.1910.01108.
\[284\] X. Jiaoet al., “TinyBERT: Distilling BERT for natural language understanding.”
2020. doi: 10.48550/arXiv.1909.10351.
\[285\] K. Arora, L. El Asri, H. Bahuleyan, and J. C. K. Cheung, “Why exposure bias matters:
An imitation learning perspective of error accumulation in language generation,” in
Findings of the association for computational linguistics: ACL 2022, S. Muresan, P.
Nakov, and A. Villavicencio, Eds., Dublin, Ireland: Association for Computational
Linguistics, May 2022, pp. 700–710. doi: 10.18653/v1/2022.findings-acl.58.
\[286\] M. Song and M. Zheng, “A survey of on-policy distillation for large language models.”
2026. Available: https://arxiv.org/abs/2604.00626
\[287\] Y. Gu, L. Dong, F. Wei, and M. Huang, “MiniLLM: Knowledge distillation of large
language models,” inThe twelfth international conference on learning representations,
2024. Available: https://openreview.net/forum?id=5h0qf7IBZZ
\[288\] R. Agarwalet al., “On-policy distillation of language models: Learning from self-
generated mistakes,” inThe twelfth international conference on learning representa-
tions, 2024. Available: https://openreview.net/forum?id=3zKtaqxLhW
rlhfbook.com 222

\[289\] S. Ross, G. Gordon, and D. Bagnell, “A reduction of imitation learning and structured
prediction to no-regret online learning,” inProceedings of the fourteenth international
conference on artificial intelligence and statistics, G. Gordon, D. Dunson, and M.
Dudik, Eds., in Proceedings of machine learning research, vol. 15. Fort Lauderdale,
FL, USA: PMLR, 2011, pp. 627–635. doi: 10.48550/arXiv.1011.0686.
\[290\] K. Lu and Thinking Machines Lab, “On-policy distillation,”Thinking Machines Lab:
Connectionism, Oct. 2025, doi: 10.64434/tml.20251026.
\[291\] S. Zhaoet al., “Self-distilled reasoner: On-policy self-distillation for large language
models.” 2026. doi: 10.48550/arXiv.2601.18734.
\[292\] C. Team, “Introducing composer 2.5.” Cursor Blog, May 18, 2026. Available: https:
//cursor.com/blog/composer-2-5
\[293\] E. Penaloza, D. Vattikonda, N. Gontier, A. Lacoste, L. Charlin, and M. Caccia,
“Privileged information distillation for language models.” 2026. Available: https:
//arxiv.org/abs/2602.04942
\[294\] J. Hübotteret al., “Reinforcement learning via self-distillation.” 2026. doi:
10.48550/arXiv.2601.20802.
\[295\] H. Leeet al., “Rlaif: Scaling reinforcement learning from human feedback with ai
feedback,” 2023.
\[296\] A. Sharma, S. Keh, E. Mitchell, C. Finn, K. Arora, and T. Kollar, “A critical
evaluation of AI feedback for aligning large language models,” inAdvances in neural
information processing systems (NeurIPS), 2024.
\[297\] L. Castricato, N. Lile, S. Anand, H. Schoelkopf, S. Verma, and S. Biderman, “Sup-
pressing pink elephants with direct principle feedback.” 2024. Available: https:
//arxiv.org/abs/2402.07896
\[298\] W. Yuanet al., “Self-rewarding language models,” inInternational conference on
machine learning (ICML), 2024. Available: https://arxiv.org/abs/2401.10020
\[299\] L. J. V. Mirandaet al., “Hybrid preferences: Learning to route instances for human
vs. AI feedback,” pp. 7162–7200, July 2025, doi: 10.18653/v1/2025.acl-long.355.
\[300\] Y. Xuet al., “RLTHF: Targeted human feedback for LLM alignment,” inInternational
conference on machine learning (ICML), 2025. Available: https://arxiv.org/abs/2502
.13417
\[301\] Z. Wanget al., “Helpsteer: Multi-attribute helpfulness dataset for steerlm,” in
Proceedings of the 2024 conference of the north american chapter of the association
for computational linguistics: Human language technologies (volume 1: Long papers),
2024, pp. 3371–3384.
\[302\] B. Wanget al., “Nemotron-cascade: Scaling cascaded reinforcement learning for
general-purpose reasoning models,”arXiv preprint arXiv:2512.13607, 2025.
\[303\] P. Wanget al., “Large language models are not fair evaluators,” inAnnual meeting
of the association for computational linguistics (ACL), 2024.
\[304\] T. Wanget al., “Shepherd: A critic for language model generation,”arXiv preprint
arXiv:2308.04592, 2023.
\[305\] P. Keet al., “CritiqueLLM: Towards an informative critique generation model for
evaluation of large language model generation,” inAnnual meeting of the association
for computational linguistics (ACL), 2024.
\[306\] J.Li, S.Sun, W.Yuan, R.-Z.Fan, H.Zhao, andP.Liu, “Generativejudgeforevaluating
alignment,” inInternational conference on learning representations (ICLR), 2024.
rlhfbook.com 223

\[307\] S. Kimet al., “Prometheus 2: An open source language model specialized in evaluating
other language models,” inConference on empirical methods in natural language
processing (EMNLP), 2024.
\[308\] S. Lee, S. Kim, S. Park, G. Kim, and M. Seo, “Prometheus-vision: Vision-language
model as a judge for fine-grained evaluation,” inFindings of the association for
computational linguistics ACL 2024, 2024, pp. 11286–11315.
\[309\] E. Zhao, P. Awasthi, and S. Gollapudi, “Sample, scrutinize and scale: Effective
inference-time search by scaling verification,” inInternational conference on machine
learning (ICML), 2025.
\[310\] N. Kalra and L. Tang, “Verdict: A library for scaling judge-time compute,”arXiv
preprint arXiv:2502.18018, 2025.
\[311\] A. Madaanet al., “Self-refine: Iterative refinement with self-feedback,”Advances in
Neural Information Processing Systems, 2023.
\[312\] A. Pace, J. Mallinson, E. Malmi, S. Krause, and A. Severyn, “West-of-n: Synthetic pref-
erence generation for improved reward modeling,”arXiv preprint arXiv:2401.12086,
2024.
\[313\] T. Wuet al., “Meta-rewarding language models: Self-improving alignment with
llm-as-a-meta-judge,”arXiv preprint arXiv:2407.19594, 2024.
\[314\] Z. Sunet al., “SALMON: Self-alignment with principle-following reward models,”
inThe twelfth international conference on learning representations, 2024. Available:
https://openreview.net/forum?id=xJbsmB8UMx
\[315\] M. Y. Guanet al., “Deliberative alignment: Reasoning enables safer language models,”
arXiv preprint arXiv:2412.16339, 2024.
\[316\] Anthropic, “Claude’s constitution.” Accessed: Feb. 07, 2024. [Online]. Available:
https://www.anthropic.com/news/claudes-constitution
\[317\] D. Ganguliet al., “Collective constitutional AI: Aligning a language model with public
input.” Anthropic, 2023.
\[318\] S. Huanget al., “Constitutional AI recipe,”Hugging Face Blog, 2024.
\[319\] N. Lambert, H. Schoelkopf, A. Gokaslan, L. Soldaini, V. Pyatkin, and L. Castricato,
“Self-directed synthetic dialogues and revisions technical report,”arXiv preprint
arXiv:2407.18421, 2024.
\[320\] Z. Sunet al., “Principle-driven self-alignment of language models from scratch with
minimal human supervision,” inThirty-seventh conference on neural information
processing systems, 2023. Available: https://openreview.net/forum?id=p40XRfBX96
\[321\] J.-P. Fränken, E. Zelikman, R. Rafailov, K. Gandhi, T. Gerstenberg, and N. Goodman,
“Self-supervised alignment with mutual information: Learning to follow principles
without preference labels,”Advances in Neural Information Processing Systems, 2024.
\[322\] A. Gunjalet al., “Rubrics as rewards: Reinforcement learning beyond verifiable
domains.” 2025. doi: 10.48550/arXiv.2507.17746.
\[323\] V. Viswanathanet al., “Checklists are better than reward models for aligning language
models.” 2025. doi: 10.48550/arXiv.2507.18624.
\[324\] M. Rezaeiet al., “Online rubrics elicitation from pairwise comparisons.” 2025. doi:
10.48550/arXiv.2510.07284.
\[325\] T. Liuet al., “OpenRubrics: Towards scalable synthetic rubric generation for reward
modeling and LLM alignment.” 2025. doi: 10.48550/arXiv.2510.07743.
rlhfbook.com 224

\[326\] Y. Heet al., “AdvancedIF: Rubric-based benchmarking and reinforcement learning
for advancing LLM instruction following.” 2025. doi: 10.48550/arXiv.2511.10507.
\[327\] R. Shaoet al., “DR tulu: Reinforcement learning with evolving rubrics for deep
research.” 2025. doi: 10.48550/arXiv.2511.19399.
\[328\] M. Sharmaet al., “ResearchRubrics: A benchmark of prompts and rubrics for
evaluating deep research agents.” 2025. doi: 10.48550/arXiv.2511.07685.
\[329\] J. Ruanet al., “ExpertLongBench: Benchmarking language models on expert-
level long-form generation tasks with structured checklists.” 2025. doi:
10.48550/arXiv.2506.01241.
\[330\] S. Reed and N. De Freitas, “Neural programmer-interpreters,” inInternational con-
ference on learning representations (ICLR), 2016.
\[331\] P. Lewiset al., “Retrieval-augmented generation for knowledge-intensive nlp tasks,”
Advances in neural information processing systems, vol. 33, pp. 9459–9474, 2020.
\[332\] L. Gaoet al., “Pal: Program-aided language models,” inInternational conference on
machine learning, PMLR, 2023, pp. 10764–10799.
\[333\] A. Parisi, Y. Zhao, and N. Fiedel, “Talm: Tool augmented language models,”arXiv
preprint arXiv:2205.12255, 2022.
\[334\] T. Schicket al., “Toolformer: Language models can teach themselves to use tools,” in
Advances in neural information processing systems (NeurIPS), 2023.
\[335\] S. G. Patil, T. Zhang, X. Wang, and J. E. Gonzalez, “Gorilla: Large language model
connected with massive APIs,” inAdvances in neural information processing systems
(NeurIPS), 2024.
\[336\] Anthropic, “Model context protocol (MCP).” https://modelcontextprotocol.io/, 2024.
\[337\] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, A. D. White, and P. Schwaller,
“Chemcrow: Augmenting large-language models with chemistry tools,”arXiv preprint
arXiv:2304.05376, 2023.
\[338\] B. Liet al., “Mmedagent: Learning to use medical tools with multi-modal agent,” in
Conference on empirical methods in natural language processing (EMNLP), 2024.
\[339\] K. Zhang, J. Li, G. Li, X. Shi, and Z. Jin, “Codeagent: Enhancing code generation
with tool-integrated agent systems for real-world repo-level coding challenges,”arXiv
preprint arXiv:2401.07339, 2024.
\[340\] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan, “ τ-bench: A bench-
mark for tool-agent-user interaction in real-world domains.” June 2024. doi:
10.48550/arXiv.2406.12045.
\[341\] Y. Qinet al., “ToolLLM: Facilitating large language models to master 16000+ real-
world APIs,” inInternational conference on learning representations (ICLR), July
2024. doi: 10.48550/arXiv.2307.16789.
\[342\] S. Yaoet al., “React: Synergizing reasoning and acting in language models,” in
International conference on learning representations (ICLR), 2023.
\[343\] J. Schulman, “Proxy objectives in reinforcement learning from human feedback.”
Invited talk at the International Conference on Machine Learning (ICML), 2023.
Available: https://icml.cc/virtual/2023/invited-talk/21549
\[344\] C. Zhang, O. Vinyals, R. Munos, and S. Bengio, “A study on overfitting in deep
reinforcement learning,”arXiv preprint arXiv:1804.06893, 2018.
\[345\] C. A. Goodhart and C. Goodhart,Problems of monetary management: The UK
experience. Springer, 1984.
rlhfbook.com 225

\[346\] K. Hoskin, “The ‘awful idea of accountability’: Inscribing people into the measurement
of objects,”Accountability: Power, ethos and the technologies of managing, vol. 265,
1996.
\[347\] T. Lu and C. Boutilier, “Learning mallows models with pairwise preferences,” in
Proceedings of the 28th international conference on machine learning (icml-11), 2011,
pp. 145–152.
\[348\] S. Hanet al., “Wildguard: Open one-stop moderation tools for safety risks, jailbreaks,
and refusals of llms,” inAdvances in neural information processing systems (NeurIPS),
2024.
\[349\] H. Inanet al., “Llama guard: Llm-based input-output safeguard for human-ai conver-
sations,”arXiv preprint arXiv:2312.06674, 2023.
\[350\] P. Röttger, H. R. Kirk, B. Vidgen, G. Attanasio, F. Bianchi, and D. Hovy, “Xstest:
A test suite for identifying exaggerated safety behaviours in large language models,”
inConference of the north american chapter of the association for computational
linguistics (NAACL), 2024.
\[351\] T. Coste, U. Anwar, R. Kirk, and D. Krueger, “Reward model ensembles help mitigate
overoptimization,” inInternational conference on learning representations (ICLR),
2024.
\[352\] T. Moskovitzet al., “Confronting reward model overoptimization with constrained
RLHF,” inInternational conference on learning representations (ICLR), 2024.
\[353\] R. Rafailovet al., “Scaling laws for reward model overoptimization in direct align-
ment algorithms,”Advances in Neural Information Processing Systems, vol. 37, pp.
126207–126242, 2024.
\[354\] S. Zhuang and D. Hadfield-Menell, “Consequences of misaligned AI,”Advances in
Neural Information Processing Systems, vol. 33, pp. 15763–15773, 2020.
\[355\] N. Jaques, S. Gu, D. Bahdanau, J. M. Hernández-Lobato, R. E. Turner, and
D. Eck, “Sequence tutor: Conservative fine-tuning of sequence generation mod-
els with kl-control,” inInternational conference on machine learning, PMLR, 2017,
pp. 1645–1654.
\[356\] N. Jaqueset al., “Human-centric dialog training via offline reinforcement learning,”
inConference on empirical methods in natural language processing (EMNLP), 2020.
\[357\] R. Y. Pang, W. Yuan, K. Cho, H. He, S. Sukhbaatar, and J. Weston, “Iterative
reasoning preference optimization,” inAdvances in neural information processing
systems (NeurIPS), 2024.
\[358\] H. Chen, N. Razin, K. Narasimhan, and D. Chen, “Retaining by doing: The role of
on-policy data in mitigating forgetting.” 2025. Available: https://arxiv.org/abs/2510
.18874
\[359\] I. Shenfeld, J. Pari, and P. Agrawal, “RL’s razor: Why online reinforcement learning
forgets less,” inThe fourteenth international conference on learning representations,
2026. Available: https://openreview.net/forum?id=7HNRYT4V44
\[360\] D. Hendryckset al., “Measuring massive multitask language understanding,” in
International conference on learning representations (ICLR), 2021.
\[361\] A. Mallen, A. Asai, V. Zhong, R. Das, H. Hajishirzi, and D. Khashabi, “When not to
trust language models: Investigating effectiveness and limitations of parametric and
non-parametric memories,”arXiv preprint, 2022.
rlhfbook.com 226

\[362\] S. Lin, J. Hilton, and O. Evans, “Truthfulqa: Measuring how models mimic human
falsehoods,” inAnnual meeting of the association for computational linguistics (ACL),
2022.
\[363\] M. Suzgunet al., “Challenging BIG-bench tasks and whether chain-of-thought can
solve them,” inAnnual meeting of the association for computational linguistics (ACL),
2023.
\[364\] D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner, “DROP: A
reading comprehension benchmark requiring discrete reasoning over paragraphs,”
inConference of the north american chapter of the association for computational
linguistics (NAACL), 2019.
\[365\] D. Hendryckset al., “Measuring mathematical problem solving with the MATH
dataset,”NeurIPS, 2021.
\[366\] M. Chenet al., “Evaluating large language models trained on code,” 2021, Available:
https://arxiv.org/abs/2107.03374
\[367\] J. Liu, C. S. Xia, Y. Wang, and L. Zhang, “Is your code generated by chatGPT
really correct? Rigorous evaluation of large language models for code generation,” in
Thirty-seventh conference on neural information processing systems, 2023. Available:
https://openreview.net/forum?id=1qvx610Cu7
\[368\] D. Reinet al., “GPQA: A graduate-level google-proof q&a benchmark,”arXiv preprint
arXiv:2311.12022, 2023.
\[369\] L. Phan, A. Gatti, Z. Han, N. Li, and H. et al. Zhang, “Humanity’s last exam,”arXiv
preprint arXiv:2501.14249, 2025.
\[370\] R. Aleithan, H. Xue, M. M. Mohajer, E. Nnorom, G. Uddin, and S. Wang, “SWE-
Bench+: Enhanced coding benchmark for LLMs,”arXiv preprint arXiv:2410.06992,
2024.
\[371\] N. Jainet al., “LiveCodeBench: Holistic and contamination-free evaluation of large
language models for code,”arXiv preprint arXiv:2403.07974, 2024.
\[372\] S. AI, “SEAL LLM leaderboards: Expert-driven private evaluations.” 2024. Available:
https://scale.com/leaderboard
\[373\] S. Schulhoffet al., “The prompt report: A systematic survey of prompting techniques,”
arXiv preprint arXiv:2406.06608, 2024.
\[374\] J. Robinson, C. M. Rytting, and D. Wingate, “Leveraging large language models
for multiple choice question answering,” inInternational conference on learning
representations, 2023. Available: https://openreview.net/forum?id=upQ4o-ygvJ
\[375\] J. Weiet al., “Chain-of-thought prompting elicits reasoning in large language models,”
Advances in neural information processing systems, vol. 35, pp. 24824–24837, 2022.
\[376\] T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa, “Large language models
are zero-shot reasoners,”Advances in neural information processing systems, vol. 35,
pp. 22199–22213, 2022.
\[377\] The Terminal-Bench Team, “Terminal-Bench: A benchmark for AI agents in terminal
environments.” https://github.com/laude-institute/terminal-bench, May 2025.
Available: https://www.tbench.ai
\[378\] M. A. Merrillet al., “Terminal-Bench: Benchmarking agents on hard, realistic
tasks in command line interfaces,”arXiv preprint arXiv:2601.11868, 2026, Available:
https://arxiv.org/abs/2601.11868
rlhfbook.com 227

\[379\] J. Liet al., “Numinamath: The largest public dataset in ai4maths with 860k pairs of
competition math problems and solutions,”Hugging Face repository, vol. 13, p. 9,
2024.
\[380\] L. Yuet al., “Metamath: Bootstrap your own mathematical questions for large
language models,” inInternational conference on learning representations (ICLR),
2024.
\[381\] J. Achiamet al., “Gpt-4 technical report,”arXiv preprint arXiv:2303.08774, 2023.
\[382\] OpenAI, “Introducing SWE-bench verified.” Aug. 2024. Available: https://openai.c
om/index/introducing-swe-bench-verified/
\[383\] A. K. Singhet al., “Evaluation data contamination in LLMs: How do we measure it
and (when) does it matter?”arXiv preprint arXiv:2411.03923, 2024.
\[384\] M. Wuet al., “Reasoning or memorization? Unreliable results of reinforcement
learning due to data contamination,”arXiv preprint arXiv:2507.10532, 2025.
\[385\] K. Huanget al., “MATH-perturb: Benchmarking LLMs’ math reasoning abilities
against hard perturbations,” inInternational conference on machine learning (ICML),
2025.
\[386\] UK AI Safety Institute, “Inspect AI: Framework for Large Language Model Evalua-
tions.” https://github.com/UKGovernmentBEIS/inspect_ai, 2024.
\[387\] C. Fourrier, N. Habib, H. Kydlicek, T. Wolf, and L. Tunstall, “LightEval: A lightweight
framework for LLM evaluation.” https://github.com/huggingface/lighteval, 2023.
\[388\] C. Fourrier, N. Habib, A. Lozovskaya, K. Szafer, and T. Wolf, “Open LLM leaderboard
v2.” https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard;
Hugging Face, 2024.
\[389\] L. Gaoet al., “A Framework for Few-Shot Language Model Evaluation.” Zenodo,
2023. doi: 10.5281/zenodo.10256836.
\[390\] S. Blacket al., “GPT-NeoX-20B: An open-source autoregressive language model,”
inProceedings of the ACL workshop on challenges & perspectives in creating large
language models, 2022. Available: https://arxiv.org/abs/2204.06745
\[391\] Y. Gu, O. Tafjord, B. Kuehl, D. Haddad, J. Dodge, and H. Hajishirzi, “OLMES:
A Standard for Language Model Evaluations,” inFindings of the north american
chapter of the association for computational linguistics (NAACL), 2025.
\[392\] P. Lianget al., “Holistic evaluation of language models,”Transactions on Machine
Learning Research, 2023, doi: 10.1111/nyas.15007.
\[393\] MosaicML, “Mosaic Eval Gauntlet v0.3.0 — Evaluation Suite.” https://github.com/m
osaicml/llm-foundry/blob/main/scripts/eval/local_data/EVAL_GAUNTLET.md,
2024.
\[394\] S. Maiya, H. Bartsch, N. Lambert, and E. Hubinger, “Open character training:
Shaping the persona of AI assistants through constitutional AI,”arXiv preprint
arXiv:2511.01689, 2025.
\[395\] A. M. Turneret al., “Activation addition: Steering language models without opti-
mization,”arXiv e-prints, pp. arXiv–2308, 2023.
\[396\] R. Chen, A. Arditi, H. Sleight, O. Evans, and J. Lindsey, “Persona vectors: Monitoring
and controlling character traits in language models.” 2025. Available: https://arxiv.or
g/abs/2507.21509
\[397\] Anthropic, “Claude’s character.” 2024. Available: https://www.anthropic.com/resear
ch/claude-character
rlhfbook.com 228

\[398\] T. Mikolov, K. Chen, G. Corrado, and J. Dean, “Efficient estimation of word repre-
sentations in vector space,”arXiv preprint arXiv:1301.3781, 2013.
\[399\] A. Zouet al., “Representation engineering: A top-down approach to AI transparency,”
inProceedings of the 62nd annual meeting of the association for computational
linguistics, 2024. Available: https://aclanthology.org/2024.acl-long.828/
\[400\] T. Bas and K. Novak, “What can we actually steer? A multi-behavior study of
activation control.” 2026. Available: https://arxiv.org/abs/2511.18284
\[401\] Z. Fenget al., “PERSONA: Algebraic personality composition in language models.”
2026. Available: https://arxiv.org/abs/2502.13131
\[402\] C. Lu, J. Gallagher, J. Michala, K. Fish, and J. Lindsey, “The assistant axis:
Situating and stabilizing the default persona of language models,”arXiv preprint
arXiv:2601.10387, 2026, Available: https://arxiv.org/abs/2601.10387
\[403\] R. Yeet al., “Your language model secretly contains personality subnetworks,” in
The fourteenth international conference on learning representations, 2026. Available:
https://openreview.net/forum?id=zzo3Sy3NSX
\[404\] J. Frankle and M. Carbin, “The lottery ticket hypothesis: Finding sparse, train-
able neural networks,” inInternational conference on learning representations, 2019.
Available: https://openreview.net/forum?id=rJl-b3RcF7
\[405\] Anthropic, “Claude 4.5 opus soul document.” 2025. Available: https://www.lesswron
g.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document
\[406\] A. Askell, “Post on X regarding character training with soul documents.” 2025.
Available: https://x.com/AmandaAskell/status/1995610567923695633
\[407\] A. Vaswaniet al., “Attention is all you need,” inNeural information processing
systems, 2017. Available: https://api.semanticscholar.org/CorpusID:13756489
\[408\] D. Bahdanau, K. Cho, and Y. Bengio, “Neural machine translation by jointly learning
to align and translate,” inInternational conference on learning representations (ICLR),
2015. Available: https://arxiv.org/abs/1409.0473
\[409\] G. Teamet al., “Gemma 2: Improving open language models at a practical size,”
arXiv preprint arXiv:2408.00118, 2024.
\[410\] J. Baiet al., “Qwen technical report,”arXiv preprint arXiv:2309.16609, 2023.
\[411\] G. Wang, S. Cheng, X. Zhan, X. Li, S. Song, and Y. Liu, “Openchat: Advancing
open-source language models with mixed-quality data,” inInternational conference
on learning representations (ICLR), 2024.
\[412\] P. Yadavet al., “What matters for model merging at scale?”arXiv preprint
arXiv:2410.03617, 2024.
rlhfbook.com 229

A Definitions
This appendix includes all the definitions, symbols, and operations frequently used in the
RLHF process, with a quick overview of language models, which is the guiding application
of this book.
A.1 Language Modeling Overview
The majority of modern language models are trained to learn the joint probability distribu-
tion of sequences of tokens (words, subwords, or characters) in an autoregressive manner.
Autoregression simply means that each next prediction depends on the previous entities
in the sequence. Given a sequence of tokensx = (x1,x 2,...,x T ), the model factorizes the
probability of the entire sequence into a product of conditional distributions:
Pθ(x) =
T∏
t=1
Pθ(xt|x 1,...,x t−1).(154)
In order to fit a model that accurately predicts this, the goal is often to maximize the
likelihood of the training data as predicted by the current model. To do so, we can minimize
a negative log-likelihood (NLL) loss:
LLM(θ) =−E x∼D
[T∑
t=1
logPθ (xt|x <t)
]
.(155)
In practice, one uses a cross-entropy loss with respect to each next-token prediction, computed
by comparing the true token in a sequence to what was predicted by the model.
Language models come in many architectures with different trade-offs in terms of knowledge,
speed, and other performance characteristics. Modern LMs, including ChatGPT, Claude,
Gemini, etc., most often usedecoder-only Transformers\[407\]. The core innovation of the
Transformer was heavily utilizing theself-attention\[408\] mechanism to allow the model to
directly attend to concepts in context and learn complex mappings. Throughout this book,
particularly when covering reward models in Chapter 5, we will discuss adding new heads or
modifying a language modeling (LM) head of the transformer. The LM head is a final linear
projection layer that maps from the model’s internal embedding space to the tokenizer space
(a.k.a. vocabulary). We’ll see in this book that different “heads” of a language model can be
applied to fine-tune the model to different purposes – in RLHF this is most often done when
training a reward model, which is highlighted in Chapter 5.
A.2 Machine Learning
• Kullback-Leibler (KL) divergence (DKL(P||Q )), also known as KL divergence,
is a measure of the difference between two probability distributions. For discrete
probability distributionsP and Q defined on the same probability spaceX, the KL
distance fromQtoPis defined as:
rlhfbook.com 230

DKL(P||Q) =
∑
x∈X
P(x) log
(P(x)
Q(x)
)
(156)
A.3 Natural Language Processing
• Chosen Completion (yc): The completion that is selected or preferred over other
alternatives, often denoted asychosen.
• Completion (y): The output text generated by a language model in response to a
prompt. Often the completion is denoted asy|x . Rewards and other values are often
computed asr(y|x)orP(y|x).
• Policy (π): A probability distribution over possible completions, parameterized byθ:
πθ(y|x).
• Preference Relation (≻): A symbol indicating that one completion is preferred over
another, e.g.,ychosen≻y rejected. For example, a reward model predicts the probability
of a preference relation,P(yc≻y r|x).
• Prompt (x): The input text given to a language model to generate a response or
completion.
•Rejected Completion (yr): The disfavored completion in a pairwise setting.
A.4 Reinforcement Learning
• Action (a): A decision or move made by an agent in an environment, often represented
asa∈A, whereAis the set of possible actions.
• Advantage Function (A): The advantage functionA(s,a )quantifies the relative
benefit of taking actiona in states compared to the average action. It’s defined as
A(s,a ) =Q(s,a )−V (s). Advantage functions (and value functions) can depend on a
specific policy,Aπ(s,a).
• Discount Factor (γ): A scalar0≤γ < 1that exponentially down-weights future
rewards in the return, trading off immediacy versus long-term gain and guaranteeing
convergence for infinite-horizon sums. Sometimes discounting is not used, which is
equivalent toγ= 1.
• Expectation of Reward Optimization: The primary goal in RL, which involves
maximizing the expected cumulative reward:
max
θ
Es∼ρπ,a∼πθ
[∞∑
t=0
γtrt
]
(157)
whereρ π is the state distribution under policyπ, andγis the discount factor.
• Finite Horizon Reward (J(πθ)): The expected finite-horizon discounted return of
the policyπθ, parameterized byθ, is defined as:
rlhfbook.com 231

J(πθ) =E τ∼πθ
[T∑
t=0
γtrt
]
(158)
where τ∼π θ denotes trajectories sampled by following policyπθ and T is the finite
horizon.
• On-policy: In RLHF, particularly in the debate between RL and Direct Alignment
Algorithms, the discussion ofon-policydata is common. In the RL literature, on-
policy means that the data is generatedexactlyby the current form of the agent, but
in the general preference-tuning literature, on-policy is expanded to mean generations
from that edition of the model – e.g. an instruction-tuned checkpoint before running
any preference fine-tuning. In this context, off-policy could be data generated by any
other language model being used in post-training.
• Policy (π), also called thepolicy modelin RLHF: In RL, a policy is a strategy or
rule that the agent follows to decide which action to take in a given state:π(a|s).
• Policy-conditioned Values ([]π(·)): Across RL derivations and implementations, a
crucial component of the theory and practice is collecting data or values conditioned on
a specific policy. Throughout this book we will switch between the simpler notation of
value functions (V,A,Q,G ) and their specific policy-conditioned values (Vπ,Aπ,Qπ).
Also crucial in the expected value computation is sampling from datad, which is
conditioned on a specific policy,dπ (e.g., s∼d π and a∼π (·|s )when estimating
Es∼dπ,a∼π(·|s) [Aπ(s,a)]).
• Q-Function (Q): A function that estimates the expected cumulative reward from
taking a specific action in a given state:Q(s,a) =E[∑∞
t=0γtrt|s 0 =s,a 0 =a].
• Reward (r): A scalar value indicating the desirability of an action or state, typically
denoted asr.
• State (s): The current configuration or situation of the environment, usually denoted
ass∈S, whereSis the state space.
• Trajectory (τ): A trajectoryτ is a sequence of states, actions, and rewards experienced
by an agent:τ= (s 0,a 0,r 0,s 1,a 1,r 1,...,s T,aT,rT ).
• Trajectory Distribution ((τ|π )): The probability of a trajectory under policy
π is P (τ|π ) = p(s0)∏T
t=0π(at|s t)p(st+1|s t,at), where p(s0)is the prior state
distribution andp(st+1|s t,at)is the transition probability.
• Value Function (V): A function that estimates the expected cumulative reward from
a given state:V(s) =E[ ∑∞
t=0γtrt|s 0 =s].
A.5 RLHF-Only
• Reference Model (πref): A saved set of parameters used in RLHF, where the outputs
are used to regularize the optimization.
rlhfbook.com 232

A.6 Extended Glossary
• Chain-of-Thought (CoT): Chain-of-thought is a specific behavior of language models
where they are steered towards a behavior that breaks down a problem in a step-by-step
form. The original version of this was through the prompt “Let’s think step-by-step”
\[375\].
• Distillation: Distillation is a general set of practices in training AI models where a
model is trained on the outputs of a stronger model. This is a type of synthetic data
known to make strong, smaller models. Most models make the rules around distillation
clear through either the license, for open-weight models, or the terms of service, for
models accessible only via API. The term distillation is now overloaded with a specific
technical definition from the ML literature.
• In-context Learning (ICL): In-context here refers to any information within the
context window of the language model. Usually, this is information added to the
prompt. The simplest form of in-context learning is adding examples of a similar form
before the prompt. Advanced versions can learn which information to include for a
specific use-case.
• (Teacher-student) Knowledge Distillation: Knowledge distillation from a specific
teacher to a student model is a specific type of distillation described above, and it is
where the term originated. It is a specific deep learning method where a neural network
loss is modified to learn from the log-probabilities of the teacher model over multiple
potential tokens/logits, instead of learning directly from a chosen output \[277\]. An
example of a modern series of models trained with Knowledge Distillation is Gemma
2 \[409\] or Gemma 3. For a language modeling setup, the next-token loss function
can be modified as follows \[288\], where the student modelPθ learns from the teacher
distributionP ϕ:
LKD(θ) =−E x∼D
[T∑
t=1
Pϕ(xt|x <t) logPθ(xt|x <t)
]
.(159)
• Synthetic Data: This is any training data for an AI model that is the output from
another AI system. This could be anything from text generated from an open-ended
prompt of a model to a model rewriting existing content.
rlhfbook.com 233

B Beyond “Just Style”
Early developments in RLHF gave it a reputation for being “just style transfer”; other harsh
critiques focused on how RLHF manipulates the way information is presented in outputs.
This appendix explains why style is core to understanding the value RLHF provides — and
why it positively affects both model capability and user experience.
The idea of RLHF being solely about style transfer has held back the RLHF narrative for
two reasons. The first is how RLHF became associated with small, unimportant changes to
the model. When people discuss style transfer, they don’t describe this as being important
or exciting – they think of it as superficial. Yet, style is a never-ending source of human
value; it’s why retelling stories can result in new bestselling books (such as Sapiens), and it is
a fundamental part of continuing to progress our intellectual ecosystem. Style is intertwined
with what the information is.
The second reason is that many people missed the fact that well-done RLHF boosts scores
on popular LLM evaluations. We’ve seen how different styles actually can meaningfully
improve evaluations with Llama 3 \[29\]. The Llama 3 Instruct models scored extremely high
on Arena, and it’s accepted as being because they had a more fun personality – they were
more succinct and clever than other models of their era. Regardless of the benchmark scores
that many LLM users are obsessed with, if RLHF is going to make language models simply
more fun, that is delivered value.
Throughout this appendix, the term “chattiness” is used to encompass the growing length of
responses from models trained with RLHF, but it also encompasses techniques like heavy
Markdown use, emojis, and formatting the answer in bulleted lists. To ground the discussion
in this appendix, an example completion for two models in the same Tülu 3 family is shown
below – one with only instruction fine-tuning and the second with preference fine-tuning
applied via length-controlled DPO. First, the instruction-tuned completion to the prompt
What is reinforcement learning from human feedback? (the exact model is Llama 3.1
Tulu 3 70B SFT) \[6\]:
Reinforcement learning from human feedback, also known as human-in-the-loop
reinforcement learning, is a subfield of machine learning where the primary goal is to
train reinforcement learning agents to perform tasks by incorporating feedback from
humans. This feedback can come in various forms, such as binary rewards (e.g., right or
wrong), scalar rewards, preferences between actions, demonstrations, natural language
instructions, or corrections to the agent's behavior.
The idea behind reinforcement learning from human feedback is to leverage human
intuition and decision-making abilities to guide the learning process of the agent. In
traditional reinforcement learning, an agent learns to make decisions by interacting
with an environment and receiving rewards or punishments based on the outcomes of those
interactions. However, defining a suitable reward function can be challenging and
time-consuming, often leading to reward shaping or reward hacking, where the agent finds
unexpected and often unintended ways to maximize the reward.
By using human feedback, reinforcement learning can address some of these issues by
allowing humans to directly influence the learning process. Human trainers can provide
real-time feedback, scale their feedback to match the complexity of the task, and update
their feedback based on the agent's progress. This approach can lead to more robust and
generalized agents, as they are guided not by handcrafted reward functions but by the
nuanced understanding and experience of human trainers.
rlhfbook.com 234

However, reinforcement learning from human feedback faces several challenges, such as
the high cost of obtaining human feedback, subjective and inconsistent feedback, scaling
issues, and methods for efficient and effective integration of human feedback into
learning algorithms. Despite these challenges, the research in this area has shown
promising results in various applications, including robotics, video games, prosthetics
control, natural language processing, and many more.
And the post-RLHF completion from Llama 3.1 Tulu 3 70B DPO:
Reinforcement learning from human feedback (RLHF) is a subset of reinforcement learning
(RL) where the rewards that guide the learning process are provided by humans, rather
than a pre-specified numerical reward function. This is particularly useful in
situations where it is hard or infeasible to design a suitable reward function, or where
the desired performance involves subjective judgments that humans are uniquely equipped
to provide.
In traditional reinforcement learning, an agent interacts with an environment. With each
interaction, the agent performs an action, receives an observation, and gets a numerical
reward that tells it how well it performed in that situation. Through many such
interactions, the agent learns to maximize the cumulative reward.
In contrast, in reinforcement learning from human feedback:
1. **Human Input:** Instead of a predefined reward function, the feedback comes from
human evaluators, who provide qualitative, subjective judgments about the agent's
performance. This feedback can be in various forms, such as numerical ratings, binary
preference signals, natural language feedback, or even demonstrations showing how to
improve.
2. **Feedback Loop:** Human evaluators observe the agent's actions or outcomes and
provide feedback in real-time (or close to real-time). The agent learns through this
iterative feedback loop, gradually adapting its behavior to align more closely with
human preferences.
3. **Reward Shaping:** Because raw human feedback is not always directly usable in
learning algorithms due to variability and potential bias, a reward shaping process may
be involved, whereby human feedback is converted into a more stable signal that guides
learning.
4. **Preference-based RL:** One common approach within RLHF is preference-based
reinforcement learning, where the agent is trained by comparing pairs of actions (or
outcomes) and receiving human feedback on which one is better. From these pairwise
comparisons, the agent infers a reward function that it can use to guide its actions.
5. **Inverse Reinforcement Learning (IRL):** Another technique used in RLHF is IRL,
which aims to infer the underlying reward function that could explain human actions or
decisions, and then use that reward function to train the agent.
**Applications:**
Reinforcement Learning from human feedback has found applications in:
- **Robotics:** Teaching robots to perform tasks that are difficult to specify with
predefined reward functions.
- **Game playing:** Human feedback can guide AI agents to better emulate human-like
strategies or behaviors.
rlhfbook.com 235

- **Language and content generation:** For example, suggestively guiding AI models to
generate more coherent, creative, or helpful content.
- **Recommendation systems:** Human feedback can help adjust and refine the
recommendations provided to users.
**Challenges:**
Using human feedback introduces some specific challenges:
1. **Scalability:** Human feedback is time-consuming and expensive to collect, and it's
hard to scale to complex or high-dimensional tasks.
2. **Bias and Noise:** Human feedback can be noisy, inconsistent, and biased, leading to
suboptimal learning outcomes.
3. **Alignment:** Ensuring that the reinforcement learning agent aligns with the true
preferences of the human evaluator(s) and not just the superficial feedback is
difficult.
4. **Safety and Misuse:** There can be concerns about the safety and ethical
implications of using potentially flawed human feedback, especially if the feedback
process is corrupted or gamed.
Researchers are actively working on techniques to mitigate these challenges and improve
RLHF approaches. One such approach is leveraging machine learning models to amplify the
efficacy of the human feedback, for example, by learning to generalize from sparse human
input or by synthesizing plausible feedback in situations where direct human input is
not available.
The response from the DPO model has similar information, as both models are trained
on the same pretrained base model, but the preference fine-tuning adds more structure,
formatting, and of course length, which has been shown repeatedly to be associated with
general notions of human preference for language models. For more examples like this, see
the completions library associated with this book at https://www.rlhfbook.com/library.
B.1 The Chattiness Balance
RLHF or preference fine-tuning methods are being used by countless people to boost scores
like AlpacaEval and other automatic chat leaderboards (which use LLM-as-a-judge to
approximate how helpful, harmless, and honest an agent is across simple conversational
tasks), but the massive gains RLHF confers here come without shifting scores proportionally
on harder-to-game evaluations like Arena. The tension is that while RLHF methods give
a measurable improvement on these models, that training doesn’t always transfer into
performance that people care about. Through the establishment of the RLHF literature, a
large swath of models have been released with related methods to boost the “alignment” of
a model with RLHF, but they often took it way too far and published evaluation scores that
were anywhere from misleading to meaningless.
These RLHF methods motivated by alignment, when done right, make the models easier
to work with and more enjoyable. This often comes with clear improvements on evaluation
tools like MT-Bench or AlpacaEval.
In the fall of 2023, there was a peak in the debate over direct preference optimization (DPO)
and its role relative to proximal policy optimization (PPO) and other RL-based methods for
preference fine-tuning – the balance of chat evaluations to real-world performance was at
the center of this (For more technical discussion on the trade-offs, see Chapter 8, Ivison et
al. 2024 \[126\], or this talk). The problem is that you can also use techniques like DPO and
rlhfbook.com 236

PPO in feedback loops or in an abundance of data to actually severely harm the model on
other tasks like mathematics or coding in a trade for this chat performance.
During the proliferation of the DPO versus PPO debate there were many papers that came
out with incredible benchmarks but no meaningful adoption. If these papers released model
weights, they weren’t popular in public usage because these models were not robust in
general usage. When applying RLHF in the fall of 2023 or soon after, there is no way
to make an aligned version of a 7 billion parameter model actually beat GPT-4 across
comprehensive benchmarks (this sort of comparison will hold, where small models of the
day cannot robustly beat the best, large frontier models). It seems obvious, but there are
always papers claiming these sorts of results. fig. 49 is from a paper called Direct Nash
Optimization (DNO), which makes the case that their model is state-of-the-art or so on
AlpacaEval for 7B models in April 2024 \[202\]. For context, DNO is a batched, on-policy
iterativealternative to reward-model+PPO (classic RLHF) or one-shot DPO that directly
optimizes pairwise preferences (win-rate gaps) by framing alignment as finding a Nash
equilibrium against a preference oracle. These challenges emerge when academic incentives
interface with technologies becoming of extreme interest to the broader society.
Figure 49: Results from the paper on Direct Nash Optimization (DNO) highlighting their
small model outperforming the likes of GPT-4. Rosset et al. 2024. License CC-BY.
Even the pioneering paper Self Rewarding Language Models from January of 2024 \[298\]
disclosed unrealistically strong scores on Llama 2 70B. At the time, of course, a 70B model
can get closer to GPT-4 than a 7B model can (as we saw with the impressive Llama 3
releases in 2024), but it’s important to separate the reality of models from the claims in
modern RLHF papers. These models are tuned to narrow test sets and do not hold up well
in real use versus the far larger models they claim to beat. Many more methods have come
and gone similar to this, sharing valuable insights and oversold results, which make RLHF
harder to understand.
A symptom of models that have “funky RLHF” applied to them has often been a length bias.
This got so common that multiple evaluation systems like AlpacaEval and WildBench both
have linear length correction mechanisms in them. This patches the incentives for doping
on chattiness to ‘beat GPT-4’ or the leading frontier model of the day, and creates a less
gamified dynamic where shorter, useful models can actually win.
rlhfbook.com 237

Regardless, aligning chat models only for chattiness now has a bit of a reputational tax
associated with it in the literature, where it’s acknowledged that these narrow methods
can harm a model in other ways. This note from the original Alibaba Qwen models in
2023 is something that has been observed multiple times in early alignment experiments,
exaggerating a trade-off between chattiness and performance \[410\].
We pretrained the models with a large amount of data, and we post-trained the
models with both supervised fine-tuning and direct preference optimization. How-
ever, DPO leads to improvements in human preference evaluation but degradation
in benchmark evaluation.
An early, good example of this tradeoff done right is a model like Starling Beta from March of
2024 \[76\]. It’s a model that was fine-tuned from another chat model, OpenChat \[411\] (which
was in fact trained by an entire other organization). Its training entirely focuses on k-wise
reward model training and PPO optimization, and moves it up 10 places in Arena. The
average response length of the model increases, but in a way that’s good enough to actually
help the human raters. Later examples, such as Olmo 3, are documented as undergoing
substantial chat training, but with the authors preferring a final model checkpoint with
higher math, coding, and reasoning scores instead of potential checkpoints that are highest
on LLM-as-a-judge-based chat benchmarks \[18\].
A natural question is: Why does RLHF make model responses longer? Fundamentally,
evaluations like Arena have shown us that average users of models often like longer, complete
answers when compared with terse responses. Longer answers can feel more thorough, helpful,
or even trustworthy to users evaluating them quickly. This does not represent the preference
ofeveryuser, but these models are trained to match the average preferences of many data
labelers, so RLHF tends to make models more verbose.
rlhfbook.com 238

C Practical Issues
This appendix covers practical considerations for running post-training experiments at scale.
This takes the form of a list of lessons, rather than a coherent narrative.
C.1 Compute Costs of Post-Training
There are two different ways of scoping costs for post-training runs. The largest cost is in
developing the recipe, which can easily be 10X to 100X the compute of the final few training
runs. The secondary costs, which are easier to measure, are the costs of thoroughly applying
a recipe, which entails multiple seeds, careful evaluation, potential engineering headaches,
etc.
For the first cost, to develop a post-training recipe like Tülu 3 \[6\], the team ran on the order
of thousands of experiments/evaluations at the 7B scale before having the final model.
For final runs, the Olmo 3 report has a detailed accounting of what is involved in training
the final 32B Think model \[18\]:
Post-training follows a different operational pattern in which we run each stage
multiple times, sweeping over learning rates and other hyperparameters. The
theory for post-training, particularly, RL, is less developed, so we have to run
multiple experiments to identify the optimal hyperparameters for a given base
model. We hope to address this in future work.
During post-training, checkpoint evaluation consumes a larger proportion of
compute resources, in part due to long generations from reasoning models on
core benchmarks. For SFT, we swept over four candidate learning rates, on 256
GPUs each, in parallel for 36 hours. Then approximately 12 hours was spent on
evaluation, merging, and checkpoint confirmation, totaling approximately two
days. DPO training takes less time per run (about 18 hours for a full learning-rate
sweep on 64 GPUs per job) but in practice extended over multiple days due to
cluster instability. The final RL runs for the initial Olmo 3 Think 32B spanned
approximately 5 days with at least a day of training time lost due to stability
issues. After the initial release of Olmo 3, we continued our best RL run for
another 21 days on 224 GPUs to produce Olmo 3.1 Think 32B.
As scaling reinforcement learning becomes more standard practice, this will shift yet again
\[17\]. Continuing the above example, where the original Olmo 3 32B Think post-training
took only a couple of weeks, to release the improved Olmo 3.1 32B Think model the team
needed to train it for an additional 3.5 weeks with RLVR. This is a substantial cost intime
more than in total compute.
C.2 Evaluation Variance
One underappreciated challenge in post-training is evaluation variance, especially with the
rise of reasoning models that need to use sampling with temperatures above 0 to get the
best evaluation scores. With any sampling from models, the outputs become more variable.
Different benchmarks have vastly different stability characteristics, due to the variance in
difficulty of the prompts, the number of prompts in the evaluation set, the brittleness of the
models being trained, etc.
rlhfbook.com 239

During Olmo 3, the team tracked the variance of different evaluations used to evaluate
reasoning models. The table below shows the standard deviation of each evaluation, computed
as the mean of the standard deviation from 3 runs of 14 models (take the variance of each
model, then average per evaluation):
Table 9: Standard deviation of evaluation benchmarks across multiple inference runs, catego-
rized by stability (data from Olmo 3).
Category Benchmark Std. Dev.
High Variance GPQA 1.48
AlpacaEval 3 1.24
IFEval 0.88
Stable ZebraLogic 0.56
Omega 0.56
AIME 24 (Avg@32) 0.54
HumanEvalPlus 0.46
AgiEval 0.43
BigBenchHard 0.39
Very Stable LiveCodeBench (Avg@10) 0.29
MBPPPlus 0.27
MATH 0.25
MMLU 0.22
PopQA 0.16
Some evaluations, such as LiveCodeBench, were both noisy and cheap (via few prompts in
the set), so by re-running the evaluation 10 times per model, the evaluation could move from
the high-variance set to a stable setting. This could be done for every evaluation, but it can
easily balloon costs.
We also see sources of variance in evaluation settings like batch size, tensor parallel settings
within vLLM (e.g., TP=2 for baselines), and other sensitive numerics for sampling long
generations across infrastructure. Variance is everywhere with reasoners.
C.3 Managing Training Performance Variance
Throughout all the post-training recipes and tools discussed in this book, the final model
is subject to meaningful variance in performance. Understanding the distribution of this
variance, its sources, and its effects is crucial to creating strong models. The goal of training
a final model is to sample many points, by varying training parameters and random seeds,
in order to get the strongest model possible. Note that this is a balance between the model
actuallybeing better, and not just the benefit of re-rolling from evaluation noise.
Where the previous section focuses onevaluationnoise, the trickier source of noise is training
uncertainty. Where evaluation noise can be managed by running more tests on a given
checkpoint (uniformly reducing noise), models are trained once and canbenefitfrom a
positive outlier.
In practice, training teams take many steps to capture the maximum possible value out of
their training recipe:
rlhfbook.com 240

1. Sweep core optimization values like learning rate, batch size, etc. for every final model
run. For example, with a new base model, I’d recommend running 10 learning rates
over a wide region to be sure you’re in the optimal range, then re-run in the tighter,
optimal window.
2. Run multiple seeds on the best few settings. Random seed can have meaningful effects
on the final model, and it’s worth spending compute on.
3. Model merging is established as a key tool used to create strong models. Merging
can be done in many ways, from merging different checkpoints on the same data to
merging specialized models for specific domains. Generally, merging is seen as a strong
and simple tool in final recipes, but clear best practices aren’t established for preparing
a model for later merging in a recipe \[412\].
C.4 Identifying Bad Training Jobs
A simple intuition that’s important to establish when training models is the different types
of model issues. You want most of your time to be spent on issues where the current data,
algorithm, or recipe just isn’t good enough. On the other hand, there are plenty of times
when, while setting up a new recipe, certain methods are just broken.
The best way to understand this is to evaluate many models on a largely static evaluation
suite. Then you develop an intuition for which tests are hard to move with post-training
interventions (often knowledge-heavy evaluations such as MMLU). When something is very,
verybroken in a post-training setup, these largely stable evaluations can often drop by 10-20
points in a training job. This is one of the most useful signals there are when developing
tooling!
rlhfbook.com 241
