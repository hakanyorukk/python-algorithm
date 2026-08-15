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
    failed = set()
    # for log in logs:
    #     parts = parse(log)
    #     if parts["status"] == "FAILED":
    #         failed.add(parts["server"])
    # return failed
    return {r["server"] for r in failures}

def failures_per_server(failures):
    count = {}
    return Counter(r["server"] for r in failures)
    # #server, counts
    #
    # for log in logs:
    #     parts = parse(log)
    #     count1 = Counter(r["server"] for r in parts)
    #     if parts["status"] == "FAILED":
    #        count[parts["server"]] = count.get(parts["server"],0) + 1

    #return sorted(hashMap, key=lambda x : x[1], reverse=True)
    #return {k: v for k,v in sorted(count.items(), key=lambda  item: item[1], reverse=True)}


def most_common_reason(failures):
    # fail_reasons = {}
    # for log in logs:
    #     parts = parse(log)
    #     if parts["status"] == "FAILED":
    #         fail_reasons[parts["reason"]] = fail_reasons.get(parts["reason"], 0 ) + 1
    #
    # return max(fail_reasons.items(), key=lambda kv: kv[1])
    return dict(Counter(r["reason"] for r in failures).most_common(1))

def failures_on_date(failures,date):
    # failuers = []
    # for log in logs:
    #     parts = parse(log)
    #     if parts["date"] == date and parts["status"] == "FAILED" :
    #         failuers.append(parts["server"])
    # return failuers

    return [r["server"] for r in failures if r["date"] == date]

def success_rate(records):
    # success_count = 0
    # failure_count = 0
    # for log in logs:
    #     parts = parse(log)
    #     if parts["status"] == "SUCCESS":
    #         success_count+=1
    #     if parts["status"] == "FAILED":
    #         failure_count+=1
    # return (success_count * 100) // (failure_count + success_count)
    success_count = sum(1 for r in records if r["status"] == "SUCCESS")
    fail_count = sum(1 for r in records if r["status"] == "FAILED")
    return round((success_count * 100) / len(records), 1)

def parse(line):
    date, server, action, status, *rest = line.split(maxsplit=4)
    return {"date": date, "server":server, "action": action, "status": status, "reason": rest[0] if rest else ""}

def main():
    # --------------------
    records = [parse(l) for l in logs]  # parse ONCE
    failures = [r for r in records if r["status"] == "FAILED"]
    # --------------------

    print(failed_servers(failures))
    print(failures_per_server(failures))
    print(most_common_reason(failures))
    print(failures_on_date(failures,"2026-08-10"))
    print(success_rate(records))

if __name__ == "__main__":
    main()
