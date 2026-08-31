raw_students = [
    "Ivan,Petrov,78,92,85",
    "Maria,Ivanova,95,88,91",
    "Georgi,Dimitrov,45,52,38",
    "Elena,Todorova,88,79,94",
    "Nikolay,Stoyanov,60,60,60",
]

PASS_MARK = 60


def parse_students(lines):
    result = []
    for line in lines:
        first, last, *scores = line.split(",")
        result.append({
            "name": first + " " + last,
            "scores": [int(s) for s in scores],
        })
    return result


def average(scores):
    return sum(scores) // len(scores)


def passed(student):
    return average(student["scores"]) > PASS_MARK


def grade_letter(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"


def shout_names(students):
    return [s["name"].upper() for s in students]


def ranked_names(students):
    names = [s["name"] for s in students]
    ranked = sorted(names)
    return ranked


def find_student(students, name):
    for s in students:
        if s["name"] == name:
            return s
    return None


def remove_failures(students):
    for s in students:
        if not passed(s):
            students.remove(s)
    return students


def top_student(students):
    scores_by_name = {}
    for s in students:
        scores_by_name[s["name"]] = average(s["scores"])

    best = ""
    best_avg = 0
    for name, avg in scores_by_name.items():
        if avg > best_avg:
            best_avg = avg
            best = name
    return best, best_avg


def main():
    parsed = parse_students(raw_students)

    for s in parsed:
        avg = average(s["scores"])
        print(f"{s['name']:20} avg={avg:3}  {grade_letter(avg)}  passed={passed(s)}")

    print("Shout:   ", shout_names(parsed))
    print("Ranked:  ", ranked_names(parsed))

    wanted = "Elena" + " " + "Todorova"
    print("Find:    ", find_student(parsed, wanted))

    print("Survivors:", [s["name"] for s in remove_failures(parsed)])
    print("Top:     ", top_student(parsed))


if __name__ == "__main__":
    main()