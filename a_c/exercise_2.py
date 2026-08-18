from collections import defaultdict, Counter

build_logs = [
    "2026-08-10 09:00 build-101 web-service SUCCESS 45",
    "2026-08-10 09:20 build-102 api-service FAILED 12",
    "2026-08-10 10:05 build-103 web-service SUCCESS 38",
    "2026-08-10 10:40 build-104 worker-service FAILED 5",
    "2026-08-11 08:15 build-105 api-service SUCCESS 50",
    "2026-08-11 09:00 build-106 web-service FAILED 3",
    "2026-08-11 09:30 build-107 worker-service SUCCESS 42",
    "2026-08-11 10:10 build-108 api-service SUCCESS 55",
]

class InvalidParseError(Exception): pass


class Build:

    def __init__(self, date, time, build_id, service, status, duration):
        self.date = date
        self.time = time
        self.build_id = build_id
        self.service = service
        self.status = status
        self.duration = duration

    @classmethod
    def from_line(cls, line):
        try:
            date, time, build_id, service, status, duration_str = line.split(" ", maxsplit=5)
            duration = int(duration_str)
        except:
            raise InvalidParseError("Invalid parse!")
        return cls(date, time, build_id, service, status, duration)

    def __str__(self):
        return (f"Date: {self.date}\n"
                f"Time: {self.time}\n"
                f"Build id: {self.build_id}\n"
                f"Service: {self.service}\n"
                f"Status: {self.status}\n"
                f"Duration seconds: {self.duration}")

    @property
    def is_success(self):
        return self.status == "SUCCESS"

class BuildHistory:

    def __init__(self):
        self.logs = []

    def add(self, build):
        self.logs.append(build)

    def success_rate(self):
        if not self.logs:
            return None
        success_count = sum(1 for log in self.logs if log.is_success)
        return round((success_count / len(self.logs) * 100), 1)

    def average_duration(self,service=None):
        logs = self.logs
        if service is not None:
            logs = [log for log in self.logs if log.service == service]
        if not logs:
            return 0.0
        return round(sum(log.duration for log in logs) / len(logs), 1)

    def slowest_build(self):
        if not self.logs:
            return None
        return max(self.logs, key=lambda b: b.duration)

    def builds_by_service(self):
        builds = defaultdict(list)
        for log in self.logs:
            builds[log.service].append(log)
        return dict(builds)

    def failures_by_date(self):
        failures = Counter(log.date for log in self.logs if not log.is_success)
        return dict(failures)
def main():
    skipped = 0
    bd = BuildHistory()
    for log in build_logs:
        try:
            bd.add(Build.from_line(log))
        except InvalidParseError as e:
            skipped+=1
            print(f"skipped: {e}")
    print(f"\n{skipped} line(s) skipped\n")
    print("success_rate:", bd.success_rate())
    print("average_duration (all):", bd.average_duration())
    print("average_duration (web-service):", bd.average_duration("web-service"))
    print("slowest_build:\n", bd.slowest_build())
    print("builds_by_service:", {k:len(v) for k,v in bd.builds_by_service().items()})
    print("failures_by_date:", bd.failures_by_date())

if __name__ == "__main__":
    main()