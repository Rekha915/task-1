# ICFAI Workflow and Curriculum Challenge: Round 2

**Author:** Rekha Anjana Movidi | **Programme:** B.Tech CSE (AI & ML), IFHE Hyderabad
**Submission date:** [24-10-2026] | **Deadline:** 24 Oct 2026, 11:59 pm IST

Individual submission. This is a student proposal, not an official ICFAI document.

## Reviewed revision

- Named release: [FILL: release link]
- Full commit URL: [FILL: commit link]
- The reviewed revision is the commit linked above. A later commit only adds these two links.

## Repository map

| Path | What it is |
|---|---|
| `task1/TASK1_REPORT.md` | Task 1 report: current and proposed workflow, evidence log, test cases, arithmetic, risks |
| `task1/rules.py` | Rule-engine prototype for the proposed library workflow |
| `task1/data/books.csv`, `students.csv`, `loans.csv` | Synthetic input data |
| `task1/data/test_cases.csv` | The 7 designed cases with expected results |
| `task1/data/test_results.csv`, `audit_log.csv` | Output created by running `rules.py` |

## Task 1: Library book borrowing workflow

**Process studied:** borrowing a physical book or e-book from the college library.

**Observed on 23 Oct 2026 (my own view as a student, sample size 1):** the SIS Library option exists but has no working fields.

**Current process:** SIS login (ID, password, captcha), then dashboard, then catalogue search, then a visit to the library where staff scan the student ID and book barcodes. The system records start and due dates. Rules: 3-day loan, Rs 2 per day fine after day 3, maximum 2 books per student.

**Proposal:** make the SIS Library option work with search, availability, pending pickup, pre-checks of the 2-book limit and unpaid fines, 7-day e-book access with an extend option, reminders, and a transaction history.

**Statuses:** Available, Pending pickup, Issued, Overdue, Returned, Missing, Pickup expired.

**Accountable owner:** library head. **Approval boundary:** the system handles routine selections; staff and the library head decide exceptions (fine waiver, lost book, limit exception). **Audit record:** `audit_log.csv`. **Fallback:** the existing counter process.

**Where AI is used:** AI makes no decisions. Limits, fines and statuses come from fixed rules. AI is only optional for fuzzy search and reminder wording.

**Test results:** [FILL: paste the 7-line table from `test_results.csv`]

**Time and effort figures:** [FILL: your measured timing, estimates and ranges, with the arithmetic]

Full detail: `task1/TASK1_REPORT.md`.

## How to run

Requires Python 3.

```
cd task1
python rules.py
```

Expected output: 7 test cases, all PASS. The script writes `data/test_results.csv` and `data/audit_log.csv`. Settings at the top of `rules.py` (loan days, fine per day, book limit, whether e-books count toward the limit) can be changed.

## Sources and access dates

| Source | URL | Accessed |
|---|---|---|
| SIS Library option (own view, login required) | not linked | 23 Oct 2026 |

## AI-use record

| Date | Tool | Task | What AI produced | What I checked or changed |
|---|---|---|---|---|
| 23 Oct 2026 | Claude | Task 1 | Report structure, synthetic CSV data, `rules.py` | [FILL: e.g. ran the code, read each function, changed X, added my own test case] |

## My contribution

[FILL: in your own words, what you decided, measured, wrote or changed yourself.]

## Privacy and fieldwork statement

- No names, student IDs, marks, fees, signatures, credentials or private messages were collected.
- All data in this repository is synthetic.
- I did not promise implementation or publish identifiable staff details.
- [FILL: whether you asked anyone for permission and the outcome, or state that no fieldwork access was requested.]

## Limitations

- The loan and fine rules come from my own use as a student and were not confirmed by library staff.
- The SIS observation is a sample of one, by my own view only.
- Request volumes and staff workload were not observed; figures are estimates and are labelled as such.
- No live college system or production records were used. The design is tested on paper and with a synthetic prototype, not in production.