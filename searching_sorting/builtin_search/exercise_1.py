from Employee import Employee

def main():
    employees = [
        Employee("Chen", 6000),
        Employee("Adem", 4000),
        Employee("Filip", 5000),
        Employee("Dana", 3000),
    ]

    employees.sort(key=lambda e: e.salary, reverse=True)
    print("By salary:")
    for e in employees: print(" ", e)

    employees.sort(key=lambda e: e.name)

    print("By name:")
    for e in employees: print(" ", e)

if __name__ == "__main__":
    main()