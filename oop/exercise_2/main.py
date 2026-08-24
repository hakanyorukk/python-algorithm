from AlertLog import AlertLog
from Alert import Alert
raw_alerts = [
    "2026-08-21T10:00 web-01 cpu 95.5",
    "2026-08-21T10:05 web-02 memory 88.0",
    "2026-08-21T10:10 web-01 disk 97.2",
    "malformed line",
    "2026-08-21T10:00 web-01 cpu 95.5",      # exact duplicate of line 1
    "2026-08-21T10:20 db-01 cpu 91.0",
    "2026-08-21T10:25 web-02 memory 70.0",   # below threshold
    "2026-08-21T10:30 db-01 unknown 50.0",   # unknown metric
    "2026-08-21T10:35 web-01 memory 92.0",
]
def main():
    log = AlertLog()
    for line in raw_alerts:
        try:
            log.add(Alert.from_line(line))
        except ValueError:
            pass

    print(len(log) == 6)  # 9 lines − 1 malformed − 1 unknown − 1 duplicate
    print(len(log.critical_alerts()) == 5)
    print(log.worst_offender() == ("web-01", 3))
    print(log.by_server()["web-01"] == ["cpu", "disk", "memory"])
    print(log.summary()["servers"] == 3)
    print(log.sorted_by_severity()[0].server == "web-01")
    print(log.sorted_by_severity()[0].severity() == 7.0)

    a = Alert.from_line("2026-08-21T10:00 web-01 cpu 95.5")
    b = Alert.from_line("2026-08-21T10:00 web-01 cpu 95.5")
    print(a == b and hash(a) == hash(b))
    print(a == "web-01" or True)  # must not crash
    print(type(a).__name__ == "CpuAlert")
    print(repr(a) == "CpuAlert('2026-08-21T10:00', 'web-01', 95.5)")
    print(len([(x, y) for x in log for y in log]) == 36)  # nested loop → re-iterable



if __name__ == "__main__":
    main()