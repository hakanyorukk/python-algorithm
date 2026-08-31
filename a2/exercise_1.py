from collections import Counter

requests = [
    "10:01:15 192.168.1.10 GET /home 200",
    "10:01:16 192.168.1.11 GET /login 200",
    "10:01:17 192.168.1.10 POST /login 401",
    "10:01:18 192.168.1.12 GET /home 200",
    "10:01:19 192.168.1.10 POST /login 401",
    "10:01:20 192.168.1.13 GET /admin 403",
    "10:01:21 192.168.1.10 POST /login 401",
    "10:01:22 192.168.1.11 GET /profile 200",
    "10:01:23 192.168.1.14 GET /home 200",
    "10:01:24 192.168.1.13 GET /admin 403",
    "10:01:25 192.168.1.12 POST /checkout 500",
    "10:01:26 192.168.1.10 GET /home 200",
]

def error_requests(records):
    return [r for r in records if int(r["status_code"]) >= 400]

def requests_per_ip(records):
    counts = Counter(r["ip"] for r in records)
    return {k: v for k,v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

def suspicious_ips(records, threshold=3):
    fail_counts = Counter(r["ip"] for r in records if int(r["status_code"]) >= 400)
    return {ip:count for ip, count in fail_counts.items() if count >= threshold}

def status_code_breakdown(records):
    #counts = Counter(r["status_code"] for r in records if r["status_code"])
    counts = {}
    for r in records:
        status = f"{r['status_code'][0]}xx"
        counts[status] = counts.get(status, 0) + 1
    return counts

def most_requested_path(records):
    return dict(Counter(r["path"] for r in records).most_common(1))

def parse(line):
    date, ip, method, path, status_code = line.split(maxsplit=4)
    return {"date": date, "ip": ip, "method":method,
            "path": path, "status_code": status_code}

def main():
    records = [parse(r) for r in requests]
    print(error_requests(records))
    print(requests_per_ip(records))
    print(suspicious_ips(records))
    print(status_code_breakdown(records))
    print(most_requested_path(records))

if __name__ == "__main__":
    main()