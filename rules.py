import csv
from datetime import date, datetime

AS_OF = date(2026, 10, 23)
LOAN_DAYS = 3
FINE_PER_DAY = 2
MAX_BOOKS = 2
COUNT_EBOOKS_IN_LIMIT = False   # your decision: True means e-books count toward the limit

def read(name):
    with open(f"data/{name}", newline="") as f:
        return list(csv.DictReader(f))

books = {b["book_id"]: b for b in read("books.csv")}
students = {s["student_id"]: s for s in read("students.csv")}
loans = read("loans.csv")
pending = []   # books selected but not yet scanned by staff
audit = []     # record of every action

def log(actor, action, student, book, result):
    audit.append([datetime(2026, 10, 23, 12, 0).isoformat(), actor, action, student, book, result])

def calculate_fine(due_date, as_of=AS_OF):
    days_late = (as_of - datetime.strptime(due_date, "%Y-%m-%d").date()).days
    return FINE_PER_DAY * max(0, days_late)

def active_count(student_id):
    n = sum(1 for l in loans if l["student_id"] == student_id
            and l["status"] in ("Issued", "Overdue")
            and (COUNT_EBOOKS_IN_LIMIT or l["format"] == "physical"))
    return n + sum(1 for s, _ in pending if s == student_id)

def can_borrow(student_id, book_id):
    s, b = students[student_id], books[book_id]
    if int(s["unpaid_fine_rs"]) > 0:
        return False, "REJECTED: unpaid fine"
    if active_count(student_id) >= MAX_BOOKS:
        return False, "REJECTED: 2-book limit reached"
    if int(b["copies_available"]) < 1:
        return False, "NO COPY: offer e-book or queue"
    return True, "OK"

def select_book(student_id, book_id):
    ok, msg = can_borrow(student_id, book_id)
    if ok:
        books[book_id]["copies_available"] = str(int(books[book_id]["copies_available"]) - 1)
        pending.append((student_id, book_id))
        msg = "PENDING PICKUP"
    log("system", "select", student_id, book_id, msg)
    return msg

def staff_scan(student_id, book_id):
    if (student_id, book_id) in pending:
        pending.remove((student_id, book_id))
        log("staff", "scan", student_id, book_id, "ISSUED, due in 3 days")
        return "ISSUED"
    return "NO PENDING PICKUP"

def mark_missing(student_id, book_id):
    if (student_id, book_id) in pending:
        pending.remove((student_id, book_id))
    books[book_id]["copies_available"] = "0"
    log("staff", "mark_missing", student_id, book_id, "MISSING")
    return "MISSING"

def expire_pickup(student_id, book_id):
    if (student_id, book_id) in pending:
        pending.remove((student_id, book_id))
        books[book_id]["copies_available"] = str(int(books[book_id]["copies_available"]) + 1)
        log("system", "pickup_expired", student_id, book_id, "BACK TO AVAILABLE")
        return "BACK TO AVAILABLE"
    return "NOTHING TO EXPIRE"

def run():
    results = []
    def check(case, got, expected_has):
        results.append([case, "PASS" if expected_has in got else "FAIL", got])

    check("T1 Normal", select_book("S001", "B002") + " -> " + staff_scan("S001", "B002"), "ISSUED")
    check("T2 Missing information", mark_missing("S002", "B020"), "MISSING")
    first = select_book("S003", "B010")
    second = select_book("S009", "B010")
    check("T3 Duplicate", f"first={first}; second={second}", "second=NO COPY")
    check("T4a Unauthorized (limit)", select_book("S004", "B002"), "2-book limit")
    check("T4b Unauthorized (fine)", select_book("S005", "B002"), "unpaid fine")
    held = select_book("S010", "B002")
    check("T5 Failed step", f"{held}; {expire_pickup('S010', 'B002')}", "BACK TO AVAILABLE")
    check("T6 Fine arithmetic", f"Rs {calculate_fine('2026-10-13')}", "Rs 20")

    for r in results:
        print(f"{r[0]:30} {r[1]:5} {r[2]}")
    with open("data/audit_log.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "actor", "action", "student", "book", "result"])
        w.writerows(audit)
    with open("data/test_results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "result", "detail"])
        w.writerows(results)

if __name__ == "__main__":
    run()