# Appendix B: Evidence log
 
Access date for all web sources: **24 Oct 2026**. Official curriculum facts are in Appendix A. Everything below is evidence used to support a student proposal.
 
## B1. Job descriptions (target role: AI/ML Engineer, fresher)
 
| # | Company | Role title | Posting date | URL |
|---|---|---|---|---|
| 1 | NLB SERVICES |  AIML Engineer, India | 30 OCT 2026 | https://www.naukri.com/job-listings-ai-ml-intern-fresher-nlb-services-noida-0-to-1-years-151026016789?src=jobsearchDesk&sid=17928446846843612&xp=1&px=1 |
| 2 |CIRCULAR CARBON TECHNOLOGIES | Fresher AI ENGINEER |  NOT MENTIONED (QUICK APPLY)2026 | https://www.simplyhired.co.in/search?q=artificial+intelligence+fresher&job=25QBMMOqNpsQ9aWLpU3csy8jdk8aEzfWJEsp1K65C7a5pFRn9DApzg |
| 3 |ZUNDERDOG  ||AUTOMATION DEVLOPER|| 4 NOV 2026 | https://in.indeed.com/cmp/Zunderdog?campaignid=mobvjcmp&from=mobviewjob&tk=1k5mu6j6fh867800&fromjk=dd02ae13b9c52eec |
| 4  | QUICKHYRE | Associate AI | listed 8 Jul to 5 AuNOV 2026 |https://internshala.com/job/detail/fresher-remote-artificial-intelligence-ai-associate-job-at-quickhyre1791482272  |
 
Notes: Posting 1 names both a Pune and a Hyderabad office on the same page. Posting 4 is from an aggregator, not the employer, so it is supporting evidence only. Postings 1–3 are the three counted for the task.
 
### Requirement mapping
 
Status key: **Covered** = a course title matches; **Present, needs practice** = a matching course exists but depth is unverified or it comes late; **Absent** = no course title matches. Judgements use titles only, because syllabus content was not available.
 
| Requirement (paraphrased) | JD | Related course | Status | Proposal link |
|---|---|---|---|---|
| Python, ML fundamentals, scikit-learn | 1, 3 | Computer Programming (S1), Machine Learning (S4) | Covered | KEEP |
| Data structures and statistics | 3 | Data Structures (S2), Probability & Statistics (S3) | Covered | KEEP |
| SQL | 2 (job segment) | DBMS (S3) | Covered | KEEP |
| NLP exposure | 1 | Natural Language Processing (S6) | Covered | UPDATE (add LLM and retrieval) |
| TensorFlow / PyTorch experiments | 1 | Deep Learning (S6) | Present, needs practice (frameworks not visible from title) | KEEP, confirm in syllabus |
| Pandas/NumPy data analysis | 3 | Data Wrangling and Visualization (S5) | Present, needs practice (comes in sem 5) | UPDATE |
| Generative AI, LLMs, prompt engineering, AI agents | 1, 2, 4 | None by title (only GAN elective) | Absent | ADD Generative AI & LLM Applications |
| Deploy ML models | 2, 3 | None by title | Absent | ADD MLOps & Model Deployment |
| Build/integrate AI apps with APIs and cloud services | 2 | Web Enabled Technologies (S4), Big Data Systems (S6) | Cloud absent; APIs present, needs practice | ADD Cloud & DevOps Foundations; UPDATE Web Enabled Technologies |
| Development and testing of AI features | 1, 2 | Industry Coding Practices (S4) may partly cover | Unverified; no testing course by title | ADD Software Engineering & Testing |
| Data pipelines | 4 | Data Wrangling (S5), Big Data Systems (S6) | Present, needs practice | ADD Data Engineering & Pipelines |
| Monitoring and feedback loops for AI systems | 4 | None by title | Absent | ADD MLOps; Data-Centric AI & Model Evaluation |
 
### Evidence gaps (honest limits)
 
- **Developer Tools & Version Control Lab** and **Responsible AI & Data Privacy**: none of postings 1–3 asks for these. They are supported by reasoning (reproducible work; the only Responsible AI content is the "Ethical Challenges in AI and Deep Learning" elective), not by these postings. They are the weakest additions and could be dropped.
- **Reductions** (Blockchain, Soft Computing, Autonomous Vehicles, IoT, Basic Electronics, Digital Fabrication, Engineering Graphics): none of the four postings asks for them. Absence from postings does not prove low value; the report explains each reduction by overlap or by where the content remains available.
## B2. AI exercises (five subjects)
 
All exercises are textbook-style and non-confidential. **Model:** Claude Sonnet 5.5. **Date:** 24 Oct 2026. Verification was run in Python 3 in a sandbox.
 
| # | Subject | Prompt | What the model produced | Verification | Error found? |
|---|---|---|---|---|---|
| 1 | Data Structures | "Write a Python function to reverse a singly linked list and test it on [1,2,3,4]." | Iterative three-pointer reversal, O(n) time, O(1) space | Ran on [1,2,3,4], [], [7], [1,2]; compared with list reversal | No error found; all 4 cases matched |
| 2 | DBMS | "Table employees(id, name, dept, salary). Write SQL for employees earning more than their department's average." | Correlated subquery: `SELECT name FROM employees e WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept = e.dept)` | Ran in SQLite on 6 synthetic rows (2 departments); compared with a Python average per department | No error found; both gave Ravi and Sita |
| 3 | Probability & Statistics | "Sensitivity 90%, specificity 95%, prevalence 2%. What is P(disease given a positive test)?" | Bayes: 0.9×0.02 / (0.9×0.02 + 0.05×0.98) = 0.2687 (about 26.9%) | Recomputed by expected counts in 100,000 people | No error found; both 0.2687 |
| 4 | Operating Systems | "Round robin, quantum 4, bursts P1=10, P2=5, P3=8, all arrive at 0. Find completion, waiting and average waiting time." | Completion P1=23, P2=17, P3=21; waiting 13, 12, 13; average 12.67 | Simulated with a queue in Python | No error found; identical results |
| 5 | Machine Learning | "TP=40, FP=10, FN=20, TN=130. Compute accuracy, precision, recall, F1." | Accuracy 0.85, precision 0.80, recall 0.667, F1 0.727 | Recomputed from the confusion matrix in Python | No error found; identical results |
 
**What the model did:** produced correct code or calculations for textbook-level tasks, with short explanations.
 
**What human checking remains:** the model was right in all five cases, so no error is claimed. The checks still matter: edge cases (empty list, ties in averages), whether the assumptions match the course's own convention (for example, tie-breaking in scheduling), and whether answers would hold on harder, less standard questions. These five were routine exercises and do not show how the model performs on advanced or ambiguous course tasks.
 
## B3. Validation
 
- **Role of person:** not available. No faculty member or recent graduate was reached before the deadline.
- **Question prepared:** "For an AI/ML fresher role, which one subject should the curriculum add or practise more, and which proposed reduction would you object to?"
- **Feedback:** none received.
- **What changed my mind:** the job postings showed generative AI, deployment, and cloud as the clearest gaps, while data structures, statistics, and ML fundamentals were already well covered. I therefore treat the Developer Tools and Responsible AI additions as weaker than the others.
- **Evidence that could disprove my strongest claim** (that generative AI, MLOps and cloud are missing): a syllabus showing these topics inside Industry Coding Practices, Big Data Systems, Special Project, or Elective I/II. Titles alone cannot rule that out.
## B4. Sources
 
| Source | URL | Accessed |
|---|---|---|
| Job postings 1–4 | see B1 | 24 Oct 2026 |
| IFHE ICFAI Tech programmes page (confirms the B.Tech CSE AI & ML programme exists) | https://ifheindia.org/lp/icfaitech2025 | 24 Oct 2026 |
| Official curriculum structure page (source of Appendix A) | `<https://sis.icfaiuniversity.in/>` | `<24-10-2026>` |
 
