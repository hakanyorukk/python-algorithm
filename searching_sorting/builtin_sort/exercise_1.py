from Employee import Employee

def main():
    employees = [
        Employee("Chen", "IT", 6000),
        Employee("Adem", "Sales", 4000),
        Employee("Filip", "IT", 5000),
        Employee("Dana", "Sales", 4000),
        Employee("Bora", "IT", 6000),
        Employee("Elif", "HR", 3500),
    ]

    salaries = {"Chen": 6000, "Adem": 4000, "Filip": 5000, "Dana": 3000}
    #employees.sort(key=lambda e: e.salary, reverse=True)
    #print("By salary:")
    #for e in employees: print(" ", e)

    #employees.sort(key=lambda e: e.name)

    #print("By name:")
    #for e in employees: print(" ", e)


    sorted_salaries = sorted(employees, key=lambda e: e.salary, reverse=True)

    sorted_names = [e.name for e in sorted(employees, key=lambda e: e.name)]

    sorted_departments = sorted(employees, key=lambda e:(e.department, -e.salary))

    three_highest = [(e.name, e.salary) for e in sorted(employees, key=lambda e:e.salary, reverse=True)[:3]]
    # → [('Chen', 6000), ('Bora', 6000), ('Filip', 5000)]

    sorted_tuple_salaries = sorted(salaries.items(), key=lambda item:item[1], reverse=True)

    sorted_names_by_length = sorted(salaries, key=lambda n:(len(n), n))
    print(sorted_salaries)
    print(sorted_names)
    print(sorted_departments)
    print(three_highest)
    print(sorted_tuple_salaries)
    print(sorted_names_by_length)
if __name__ == "__main__":
    main()