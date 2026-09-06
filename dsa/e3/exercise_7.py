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

    versatile_users=defaultdict(set)
    for log in logs:
        try:
            user,action,time=log.split(",")
        except (AttributeError, ValueError):
            continue
        else:
            versatile_users[user].add(action)

    if not versatile_users:
        return None

    user = max(versatile_users, key=lambda u:len(versatile_users[u]))
    return user, len(versatile_users[user])

if __name__ == "__main__": main()
