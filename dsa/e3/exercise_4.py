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
    different_action_users = defaultdict(set)

    for log in logs:
        parts = log.split(",")

        if len(parts) != 3:
            continue

        user,action,time=parts
        different_action_users[user].add(action)

    if not different_action_users:
        return None
    print(different_action_users)
    user = max(different_action_users, key=lambda u:len(different_action_users[u]))
    return user, len(different_action_users[user])

if __name__ == "__main__":
    main()

