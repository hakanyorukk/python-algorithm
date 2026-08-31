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
class InvalidParsingError(Exception): pass
def parse_line(line):
    # try:
    #     parts = line.split(",")
    # except  AttributeError:
    #     raise InvalidParsingError("Invalid parsing")
    # if len(parts) != 4:
    #     raise InvalidParsingError
    # timestamp, user, action, status = parts
    # if status.strip() not in ("ok", "fail"):
    #     raise InvalidParsingError
    #
    try:
        timestamp, user, action, status = line.split(",")
    except (AttributeError, ValueError):
        raise InvalidParsingError("Invalid parsing")
    if status.strip() not in ("ok", "fail"):
        raise InvalidParsingError
    else:
        return {"ts": timestamp.strip(), "user": user.strip(), "action": action.strip(), "status": status.strip()}

def parse_all(lines):
    valid_lines = []
    for line in lines:
        try:
            valid_line = parse_line(line)
            valid_lines.append(valid_line)
        except InvalidParsingError:
            continue
    return valid_lines

def actions_per_user(records):
    user_list = defaultdict(list)
    for record in records:
        user_list[record["user"]].append(record["action"])
    result = {}
    for user, action in user_list.items():
        result[user] = len(action)
    return result

def user_with_most_failures(records):
    fails = Counter(r["user"] for r in records if r["status"] == "fail")
    if not fails:
        return None
    user = min(fails, key=lambda u:(-fails[u], u))
    return user, fails[user]

def counts_by_day(records):
    return dict(Counter(r["ts"].split()[0] for r in records))

def busiest_day(records):
    # day_list = defaultdict(list)
    # for r in records:
    #     date = r["ts"].split()[0]
    #     day_list[date].
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
    # recs = parse_all(LINES)
    # print(f"action per user: {action_per_user(recs)}")
    # print(f"user with most failures: {user_with_most_failures(recs)}")
    # print(f"counts by date: {counts_by_day(recs)}")
    # print(f"Busiest day: {busiest_day(recs)}")
    # print(success_rate(recs))
    #print(recs)

    recs = parse_all(LINES)
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
