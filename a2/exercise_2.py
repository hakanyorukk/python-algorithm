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

# format time, ip, method, path, status

def error_requests(records):
    return [r for r in records if int(r["status"]) >= 400]

def requests_per_ip(records):
    counts = Counter(r["ip"] for r in records)
    return {k:v for k,v in sorted(counts.items(), key=lambda item:item[1], reverse=True)}

def suspicious_ips(records, treshold=3):
    fail_count = Counter(r["ip"] for r in records if int(r["status"]) >= 400)
    return {ip:count for ip, count in fail_count.items() if count >= treshold}

def status_code_breakdown(records):
    counts = {}
    for request in records:
        status = f"{request['status'][0]}xx"
        counts[status] = counts.get(status, 0) + 1
    return counts

def most_requested_path(records):
    return Counter(r["path"] for r in records).most_common(1)

def parse(line):
    time, ip ,method, path, status = line.split(maxsplit=4)
    return {"time":time, "ip":ip, "path":path, "status":status}

def main():
    records = [parse(r) for r in requests]
    print(error_requests(records))
    print(requests_per_ip(records))
    print(suspicious_ips(records))
    print(status_code_breakdown(records))
    print(most_requested_path(records))

    pass
if __name__ == "__main__":
    main()