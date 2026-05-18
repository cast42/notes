---
type: youtube
source_url: "https://www.youtube.com/watch?v=0XB7fNS_ONg"
canonical_url: "https://youtube.com/watch?v=0XB7fNS_ONg"
title: "Lucas Beyer: Vision in the Age of LLMs"
author: Oier Mees
handle: oier.m
created_at: 2026-05-18
topics: [robot_learning]
content_hash: ba12561fc7bd7eb015c6cc05dbcc5bb38244a4bb628e589e12ee2b5dde502ed4
extracted_at: "2026-05-18T09:07:05"
extractor: youtube-oembed+course-page-web-fetch
---

# Raw content

Source: https://youtube.com/watch?v=0XB7fNS_ONg


Lecture metadata page: Robot Learning: From Fundamentals to Foundation Models (ETH Zurich, Spring 2026)
Lecturer: Oier Mees
Course page: https://cvg.ethz.ch/lectures/Robot-Learning/

Specific lecture:
Week 11: Frontier & Open Problem
Guest Spotlight: Lucas Beyer (Meta Superintelligence Labs)
YouTube Recording: https://www.youtube.com/watch?v=0XB7fNS_ONg
Title from YouTube: Lucas Beyer: Vision in the Age of LLMs [ETHZ Robot Learning 2026]

Metadata captured from the course page:
- Course title: Robot Learning: From Fundamentals to Foundation Models
- Semester: Spring 2026
- Format: Each session begins with a lecture on the core topic, followed by a student-led paper discussion. Selected weeks include short guest lectures from experts.
- Lecture slot: Monday 16:15-18:00, room NO C 60
- Course GitHub: https://github.com/mees-robot-learning-course/ethz-course-2026
- Week 11 topic: Frontier & Open Problem
- Week 11 paper discussion: A Path Towards Autonomous Machine Intelligence (LeCun, 2022), The Bitter Lesson (Sutton, 2019), Intelligence without Representation (Brooks, 1991)
- Guest spotlight page link: https://lucasb.eyer.be/

Transcript-derived summary added via summarize:

Lucas Beyer argues that modern vision is close to "solved" for perception tasks, not because models reason like humans, but because the field has converged on a reliable recipe: large-scale pre-training, targeted mid-training, and small-task fine-tuning. His case is historical and empirical. Early self-supervised vision methods were inconsistent, but one pattern kept holding: larger models helped, and performance really jumped only when researchers scaled all three together, model size, dataset size, and training time. He shows that supervised pre-training on much larger image datasets produced much stronger transfer and out-of-distribution generalization than simply making old ImageNet-era setups bigger.

A second core claim is that web-scale image-text training changed vision because it freed the field from narrow human-made class lists. Contrastive methods like CLIP let models learn from raw image-caption pairs, but Beyer says they have a structural weakness: they often learn object identities without learning relationships well. His preferred fix is captioning-style training, which forces the model to predict the next word and better capture relations like "left of" or "sitting." He also pushes hard against English-only and North America-biased filtering, showing that such filtering improves common benchmarks while hurting global coverage, for example confusing landmarks or failing on non-Western object appearances such as different toilet designs.

From there, he frames mid-training as the stage where you add reusable skills that pre-training does not naturally yield, such as OCR, localization, object-centric Q&A, segmentation, or higher-resolution understanding. Models like PaliGemma combine a vision encoder with a language model, then learn these skills through carefully mixed data before final fine-tuning. His practical bottom line is blunt: for a new perception task, take a strong pre-trained VLM, collect a few hundred examples, fine-tune it, and it will usually work. The remaining frontier is not basic perception but what comes after it, especially reasoning, planning, action, streaming efficiency, and understanding new tasks from instructions alone without extra supervised examples.
