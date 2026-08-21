def summarize_checks(checks, results=[]):
    """
    checks: list of "server status response_time" strings, e.g. "web-01 OK 120"
    Should return a dict: {"healthy": [...], "unhealthy": [...], "avg_time": float}
    """
    healthy = []
    unhealthy = []
    total_time = 0

    for check in checks:
        parts = check.split(" ")
        server = parts[0]
        status = parts[1]
        time = parts[2]

        if status == "OK":
            healthy.append(server)
        else:
            unhealthy.append(server)

        total_time += time

    avg = total_time / len(healthy)

    results.append(server)

    return {"healthy": healthy, "unhealthy": unhealthy, "avg_time": avg}