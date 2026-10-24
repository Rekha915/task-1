# Task 2 Report: Audit and redesign of my curriculum

**Student:** Rekha Anjana Movidi, B.Tech CSE (AI & ML), IFHE Hyderabad, 2023 batch
**Status:** Student proposal. This is not an official ICFAI syllabus revision.
**Target role:** AI/ML Engineer (fresher), 2030 horizon

## 1. Official baseline (fact)

Semesters 1–6 total **133 credits** (21, 22, 24, 26, 20, 20). Full table: `appendix_course_map.md`. Semesters 7–8 are unconfirmed (see appendix) and excluded from calculations.

## 2. Proposal summary (my redesign)

I propose changing **28 of 133 credits (21.1%)**: 28 credits reduced, 28 added, so the total stays 133.

| Sem | Current | Reduced | Added | Proposed | Unchanged |
|---|---|---|---|---|---|
| 1 | 21 | −3 | +3 | 21 | 18 |
| 2 | 22 | −7 | +7 | 22 | 15 |
| 3 | 24 | −6 | +6 | 24 | 18 |
| 4 | 26 | −3 | +3 | 26 | 23 |
| 5 | 20 | −6 | +6 | 20 | 14 |
| 6 | 20 | −3 | +3 | 20 | 17 |
| **Total** | **133** | **−28** | **+28** | **133** | **105** |

### REDUCE (with reasons, not "obsolete")

| Course | Cr | Proposed handling | Conditional? |
|---|---|---|---|
| Engineering Graphics (S1) | 3 | Keep basic CAD inside the new tools lab | Yes |
| Digital Fabrication (S2) | 3 | Hands-on hardware overlaps with electives | No |
| Basic Electronics (S2) | 4 | Hardware depth stays available via CPS/IoT electives | Yes |
| Engineering Economics and Management (S3) | 3 | Keep as elective alternative | Yes |
| Introduction to IoT (S3) | 3 | CPS and ML-for-IoT electives remain | No |
| Digital Humanities Elective (S4) | 3 | Possibly university-mandated | Yes |
| Soft Computing (S5) | 3 | Overlaps with ML and Deep Learning | No |
| Blockchain Technology (S5) | 3 | Becomes elective (Blockchain track exists) | No |
| Autonomous Vehicles (S6) | 3 | Becomes elective or special topic | No |

### ADD (9 new courses, provisional until job evidence confirms them)

| Course | Sem | Cr | Prerequisites | Funded by |
|---|---|---|---|---|
| Developer Tools & Version Control Lab | 1 | 3 | None | Engineering Graphics |
| Software Engineering & Testing | 2 | 4 | Computer Programming | Basic Electronics |
| Cloud & DevOps Foundations | 2 | 3 | Computer Programming | Digital Fabrication |
| Responsible AI & Data Privacy | 3 | 3 | Computer Programming | Engineering Economics |
| Data Engineering & Pipelines | 3 | 3 | Computer Programming; corequisite DBMS | Introduction to IoT |
| Workflow Automation & Approval-Control Lab | 4 | 3 | DBMS, OOP, Software Engineering & Testing | Digital Humanities |
| MLOps & Model Deployment | 5 | 3 | Machine Learning, Cloud & DevOps | Blockchain |
| Data-Centric AI & Model Evaluation | 5 | 3 | Machine Learning, Probability & Statistics | Soft Computing |
| Generative AI & LLM Applications | 6 | 3 | NLP, Deep Learning (corequisite) | Autonomous Vehicles |

### UPDATE (no credit change)

Introduction to DS and AI, Industry Coding Practices (add testing, CI, code review), Web Enabled Technologies (add REST APIs and model serving), Data Wrangling and Visualization (add reproducible pipelines), Natural Language Processing (add LLM and retrieval practice), Big Data Systems (add cloud-based practice), Special Project (require deployment and evaluation).

### KEEP (foundations)

English, Chemistry, Physics, Linear Algebra and ODE, Higher Calculus, Computer Programming, Data Structures, Probability & Statistics, OOP, DBMS, AI, Algorithms, Operating Systems, Computer Organization, Discrete Mathematics, Machine Learning, Computer Networks, Computer Vision, Deep Learning, Professional Communication, Environmental Sciences, Power Skills I–IV, Understanding India, Constitution of India, Electives I and II.

### Conditional changes

Four reductions (Engineering Graphics, Basic Electronics, Engineering Economics, Digital Humanities; 13 credits) may be restricted by regulations or mandated courses. If blocked, the paired additions become electives or assessment alternatives, and the change falls to **15 credits (11.3%)**. The interactive view shows both cases. ICFAI describes prerequisite-based interdisciplinary elective choices, which is a feasible route for the Digital Humanities and Engineering Economics swaps.

## 3. Reasons for the proposal (10)

1. **Generative AI and LLMs (ADD):** four postings ask for GenAI, LLMs, prompt engineering, agents or LLMOps; no course title covers them, and NLP (S6) arrives late. Evidence: Appendix B1.
2. **MLOps and deployment (ADD):** postings 2 and 3 require deploying models; ML (S4) and Deep Learning (S6) teach building, but no title covers deployment.
3. **Cloud and containers (ADD):** posting 2 asks for AI apps built with APIs and cloud services, and posting 6 asks for containerisation and Azure; neither appears in any course title.
4. **Testing (ADD):** postings 1, 2 and 6 mention testing, software engineering or troubleshooting; Industry Coding Practices (S4) may partly cover it, which I could not verify, so Software Engineering & Testing is flagged as needing a syllabus check.
5. **Data pipelines (ADD, UPDATE):** posting 4 asks for pipelines and monitoring; Data Wrangling (S5) and Big Data Systems (S6) exist but come late. Present but needs more practice.
6. **Foundations stay (KEEP):** Python, data structures, statistics, SQL and ML fundamentals appear in the postings and are already taught (S1–S4). I do not reduce them.
7. **Soft Computing (REDUCE):** by title it overlaps with Machine Learning (S4) and Deep Learning (S6); no posting asks for it.
8. **Blockchain core (REDUCE to elective):** no posting asks for it, and a full Blockchain elective track already exists, so the content stays available.
9. **Hardware courses (REDUCE):** Basic Electronics, Digital Fabrication and Introduction to IoT overlap in hands-on hardware content, and CPS and ML-for-IoT electives remain. This is the most debatable reduction because it narrows breadth.
10. **Load balance:** S4 is the heaviest semester (26 credits), so its total is unchanged; the lab swaps credits one for one.

**Version control (ADD):** posting 8 asks for Git, and no course title covers version control, which supports the Developer Tools & Version Control Lab (one posting only).

**Weakest addition:** Responsible AI & Data Privacy is not requested in any posting with requirement text. It rests on reasoning, not on this evidence, and could be dropped.

## 4. Job description comparison

Eight postings are listed in `appendix_evidence.md`, section B1. Six have requirement text and are mapped (the other two, an internship and an aggregator listing, lack it and are not used). Each requirement is marked absent, present but needing practice, or covered. Summary: foundations are covered; GenAI, deployment, containers/cloud and Git are absent by title; data pipelines, framework use and APIs are present but need more practice.

## 5. AI exercises in five subjects

One exercise each in Data Structures, DBMS, Probability & Statistics, Operating Systems and Machine Learning (Appendix B2). The model's answer was verified by running code in all five cases and matched each time, so I report no error. Remaining human checks: edge cases, course-specific conventions, and harder questions, which these routine tasks do not test.

## 6. Task 1 lab

See `lab_design.md`.

## 7. Validation

No faculty member or recent graduate was reached before the deadline, so the proposal is **not externally validated**. The prepared question is in Appendix B3. The job postings changed my view: generative AI, deployment, containers/cloud and Git are the clearest gaps, and the Responsible AI addition has the weakest evidence. My strongest claim could be disproved by a syllabus showing these topics inside Industry Coding Practices, Big Data Systems, Special Project or the electives.

## 8. Limitations

- Only titles and credits were available; syllabus content, prerequisites, and assessments were not.
- Semesters 7–8 are excluded because their credits are unconfirmed.
- Batch-version match is unconfirmed.
- Additions are provisional until job evidence supports them.