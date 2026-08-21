from collections import Counter, defaultdict

raw_logs = [
    "2026-08-20T09:15:03 10.0.0.14 GET /api/users 200 45",
    "2026-08-20T09:17:44 10.0.0.22 POST /api/login 401 120",
    "2026-08-20T10:02:11 10.0.0.14 GET /api/orders 200 310",
    "BAD LINE",
    "2026-08-20T10:05:39 10.0.0.31 GET /api/users 500 890",
    "2026-08-20T10:41:07 10.0.0.22 GET /api/orders 200 275",
    "2026-08-20T11:00:00 10.0.0.14 DELETE /api/orders 404 30",
    "2026-08-20T11:12:55 10.0.0.31 GET /api/users 200 60",
    "2026-08-20T11:30:18 10.0.0.14 POST /api/login 200 xyz",
    "2026-08-20T11:45:02 10.0.0.22 GET /api/orders 503 1200",
]
class InvalidParsing(Exception): pass

def parse_line(line):
    try:
        timestamp, ip, method, path, status_str, duration_str = line.split(" ", maxsplit=5)
        duration = int(duration_str)
        status = int(status_str)
    except (ValueError, AttributeError):
        raise InvalidParsing("Invalid parsing")
    return {"timestamp":timestamp, "ip":ip, "method":method, "path":path, "status":status, "duration":duration }

def parse_all(lines):
    entries = []
    for line in lines:
        try:
            entry = parse_line(line)
        except InvalidParsing as e:
            print(str(e))
            continue
        else:
            entries.append(entry)
    return entries

def unique_clients(entries):
    unique_ips = set()
    for entry in entries:
        unique_ips.add(entry["ip"])
    return unique_ips

def error_rate(entries):
    if not entries:
        return None

    num_gt_400 = sum(1 for e in entries if e["status"] >= 400)
    return round(num_gt_400 / len(entries) * 100, 1)

def avg_duration_by_path(entries):
    list_patch = defaultdict(list)
    for entry in entries:
        list_patch[entry["path"]].append(entry["duration"])
    result = {}
    for path, duration in list_patch.items():
        result[path] = round(sum(duration) / len(duration) , 1)
    return result

def busiest_hour(entries):
    hours = []
    for e in entries:
        date, hour = e["timestamp"].split("T")
        hours.append(hour[:2])
    return Counter(hours).most_common(1)[0]

def main():
    entries = parse_all(raw_logs)
    print(unique_clients(entries))
    print(error_rate(entries))
    print(avg_duration_by_path(entries))
    print(busiest_hour(entries))

if __name__ == "__main__":
    main()