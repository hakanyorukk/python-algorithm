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

class InvalidBuildLineError(Exception): pass

# def parse(line):
#     date, time, build_id, service, status, duration_seconds = line.split(" ")
#     return {"date": date, "time":time, "build_id":build_id, "service":service, "status":status, "duration_seconds":duration_seconds}

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
            raise InvalidBuildLineError("Invalid build!")

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
            return 0.0
        success_count = sum(1 for l in self.logs if l.is_success)
        return round((success_count / len(self.logs) * 100), 1)

    def average_duration(self,service=None):
        logs = self.logs
        if service is not None:
            logs = [log for log in self.logs if log.service == service]
        if not logs:
            return 0.0
        return round(sum(l.duration for l in logs) / len(logs), 1)

    def slowest_build(self):
        if not self.logs:
            return None
        return max(self.logs, key=lambda b: b.duration)

    def builds_by_service(self):
        services = defaultdict(list)
        for log in self.logs:
            services[log.service].append(log)
        return {k: len(v)  for k,v in dict(services).items()}

    def failures_by_date(self):
        failed_dates = (log.date for log in self.logs if not log.is_success)
        return dict(Counter(failed_dates))

def main():
    build_history = BuildHistory()
    skipped = 0
    for log in build_logs:
        try:
            build_history.add(Build.from_line(log))
        except InvalidBuildLineError as e:
            skipped+=1
            print(f"skipped: {e}")
    print(f"\n{skipped} line(s) skipped\n")
    print("success_rate:", build_history.success_rate())
    print("average_duration (all):", build_history.average_duration())
    print("average_duration (web-service):", build_history.average_duration("web-service"))
    print("slowest_build:\n", build_history.slowest_build())
    print("builds_by_service:", build_history.builds_by_service())
    print("failures_by_date:", build_history.failures_by_date())

if __name__ == "__main__":
    main()