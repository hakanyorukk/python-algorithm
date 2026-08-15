from collections import Counter

logs = [
    "2026-08-10 web-01 DEPLOY SUCCESS",
    "2026-08-10 web-02 DEPLOY FAILED timeout",
    "2026-08-10 db-01 DEPLOY SUCCESS",
    "2026-08-10 web-02 DEPLOY FAILED timeout",
    "2026-08-11 web-01 DEPLOY FAILED disk full",
    "2026-08-11 api-01 DEPLOY SUCCESS",
    "2026-08-11 web-02 DEPLOY FAILED memory",
    "2026-08-11 db-01 DEPLOY FAILED timeout",
    "2026-08-12 web-01 DEPLOY SUCCESS",
    "2026-08-12 api-01 DEPLOY FAILED timeout",
]

def failed_servers(failures):
    # unique servers
    return {r["server"] for r in failures}

def failures_per_server(failures):
    # a dict of server sorted from most to fewest
    counts = Counter(r["server"] for r in failures)
    #return sorted(counts, key=lambda x: x, reverse = True)
    #return {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

    return {k: v for k,v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

def most_common_reason(failures):
    # the most frequent failure reason
    return dict(Counter(r["reason"] for r in failures).most_common(1))

def failures_on_date(failures, date):
    return [r for r in failures if r["date"] == date]

def success_rate(records):
    # percentage
    success_count = sum(1 for s in records if s["status"] == "SUCCESS")
    return round((success_count * 100) / len(records), 1)

def parse(line):
    date, server, action, status, *rest = line.split(maxsplit=4)
    return {"date":date, "server":server, "action":action,
            "status":status, "reason": rest[0] if rest else ""}

def main():
    records = [parse(log) for log in logs]
    failures = [f for f in records if f["status"] == "FAILED"]

    print(failed_servers(failures))
    print(failures_per_server(failures))
    print(most_common_reason(failures))
    print(failures_on_date(failures, "2026-08-11"))
    print(success_rate(records))

if __name__ == "__main__":
    main()