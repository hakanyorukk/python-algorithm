from collections import defaultdict, Counter

LINES = [
    "2026-08-01 10:15,alice,LOGIN,ok",
    "2026-08-01 10:16,bob,LOGIN,ok",
    "2026-08-01 10:17,alice,UPLOAD,ok",
    "2026-08-01 10:20,bob,DELETE,fail",
    "garbage line",
    "2026-08-02 09:00,alice,LOGIN,fail",
    "2026-08-02 09:01,alice,LOGIN,ok",
    "2026-08-02 09:05,carol,UPLOAD,ok",
    "2026-08-02 09:06,bob,UPLOAD,ok",
    "2026-08-02 11:30,carol,DELETE,ok",
    "2026-08-01 23:59,bob,LOGIN,ok,extra",
]
class InvalidParseError(Exception): pass

def parse_line(line):
    try:
        ts, user, action, status = line.split(",")
    except (AttributeError, ValueError):
        raise InvalidParseError("Invalid parse")

    if status.strip() not in ("ok", "fail"):
        raise InvalidParseError
    else:
        return {"ts":ts.strip(), "user": user.strip(), "action": action.strip(), "status":status.strip()}

def parse_all(lines):
    result = []
    for line in lines:
        try:
            result.append(parse_line(line))
        except InvalidParseError:
            continue
    return result

def actions_per_user(records):
    user_actions = defaultdict(list)
    for r in records:
        user_actions[r["user"]].append(r["action"])
    result = {}
    for user, action in user_actions.items():
        result[user] = len(action)
    return result

def user_with_most_failures(records):
    failures = Counter(r["user"] for r in records if r["status"] == "fail")
    if not failures:
        return None
    user = min(failures, key=lambda u: (-failures[u], u))
    return user, failures[user]

def counts_by_day(records):
    return Counter(r["ts"].split()[0] for r in records)

def busiest_day(records):
    return Counter(r["ts"].split()[0] for r in records).most_common(1)[0][0]

def success_rate(records):
    success_count = 0
    if not records:
        return 0.0
    for r in records:
        if r["status"] == "ok":
            success_count+=1
    return round(success_count / len(records), 2)

def main():
    recs = parse_all(LINES)
    print(recs)
    print("records   :", len(recs), "        want 9")
    print("per user  :", actions_per_user(recs))
    print("most fail :", user_with_most_failures(recs), " want ('alice', 1)")
    print("by day    :", counts_by_day(recs))
    print("busiest   :", busiest_day(recs), "   want 2026-08-02")
    print("success   :", success_rate(recs), "        want 0.78")
    print("empty rate:", success_rate([]), "        want 0.0")
    print("no-fail   :", user_with_most_failures(
        [{"ts": "x", "user": "z", "action": "A", "status": "ok"}]), " want None")

if __name__ == "__main__":
    main()