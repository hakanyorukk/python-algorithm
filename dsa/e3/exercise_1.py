from collections import defaultdict

def main():
    logs = [
        "ivan,login,09:00", "ivan,upload,09:05", "ivan,login,09:10",
        "maria,login,09:02", "maria,delete,09:06", "maria,upload,09:07",
        "BAD",
        "georgi,login,09:20",
    ]
    print(most_versatile_user(logs))

def most_versatile_user(logs):
    different_actions = defaultdict(set)

    for log in logs:
        try:
            user, action, timestamp = log.split(",")
            different_actions[user].add(action)
        except (AttributeError, ValueError):
            #print(f"Invalid line {log}")
            continue

        # if len(parts) != 3:
        #     continue
        #user, action, timestamp = parts
    if not different_actions:
        return None

    user = max(different_actions, key=lambda u: len(different_actions[u]))
    return user, len(different_actions[user])


if __name__ == "__main__":
    main()