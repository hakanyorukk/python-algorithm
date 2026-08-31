from collections import defaultdict


def main():
    logs = [
        "ivan,login,09:00", "ivan,upload,09:05", "ivan,login,09:10",
        "maria,login,09:02", "maria,delete,09:06", "maria,upload,09:07",
        "BAD",
        "georgi,login,09:20",
    ]
    print(most_versatile_user(logs))
    print(most_versatile_user(['zoe,login,1', 'zoe,upload,2', 'adam,login,3', 'adam,delete,4']))
    print(most_versatile_user(['adam,login,3', 'adam,delete,4', 'zoe,login,1', 'zoe,upload,2']))

def most_versatile_user(logs):
    versatile_users = defaultdict(set)
    for log in logs:
        try:
            user, action, time = log.split(",")
        except ValueError:
            continue
        else:
            versatile_users[user].add(action)
    if not versatile_users:
        return None
    user = min(versatile_users, key=lambda u:(-len(versatile_users[u]), u))
    return user, len(versatile_users[user])

if __name__ == "__main__":
    main()