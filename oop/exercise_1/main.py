
from PackageRegistry import PackageRegistry
from Package import Package

raw = [
    "requests==2.31.0",
    "flask==3.0.0",
    "requests==2.28.1",
    "not-a-package",
    "flask==3.0.0",
    "django==4.2.7",
    "requests==2.31.0",
]

def main():
    # package_registry = PackageRegistry()
    # for r in raw:
    #     try:
    #         package_registry.add(Package.from_string(r))
    #     except ValueError as e:
    #         print(str(e))
    # print(package_registry.names())

    p1 = Package.from_string("requests==2.31.0")
    p2 = Package.from_string("requests==2.31.0")
    p3 = Package.from_string("requests==2.28.1")

    print(p1 == p2)  # True  — same name and version
    print(p1 == p3)  # False — different version
    print(p1 == "requests")  # False — must NOT crash
    print(hash(p1) == hash(p2))  # True  — the contract
    print(len({p1, p2, p3}) == 2)  # True  — set dedupes p1 and p2
    print(p1.major == 2)  # True  — an int, not "2"
    print(str(p1) == "requests==2.31.0")
    print(repr(p1) == "Package('requests', '2.31.0')")
    print(repr([p1]) == "[Package('requests', '2.31.0')]")  # containers use __repr__

    r = PackageRegistry()
    for line in raw:
        try:
            r.add(Package.from_string(line))
        except ValueError:
            pass

    print(len(r) == 4)  # 7 lines, 2 duplicates, 1 invalid
    print(p1 in r)
    print(r.names() == ["django", "flask", "requests"])
    print(r.versions_by_name()["requests"] == ["2.28.1", "2.31.0"])
    print([str(p) for p in r])  # the for loop must work

if __name__ == "__main__":
    main()