raw_signups = [
    {"username": "  alice_k  ", "email": "alice@mail.com", "age": "25"},
    {"username": "bob99", "email": "not-an-email", "age": "30"},
    {"username": "", "email": "chen@mail.com", "age": "22"},
    {"username": "Dana_W", "email": "DANA@MAIL.COM", "age": "-5"},
    {"username": "eve_online", "email": "eve@mail.com", "age": "abc"},
    {"username": "frank_z", "email": "frank@mail.com", "age": "17"},
    {"username": "gina_h", "email": "gina@mail.com", "age": "150"},
]

class ValidationError(Exception): pass

def clean_signups(signups):
    valid = []
    invalid = []
    for signup in signups:
        required = {"username", "email", "age"}
        missing = required - signup.keys()
        if missing:
            invalid.append({"username": signup.get("username", ""), "reason":f"missing field: {missing}"})
            continue
        try:
            clean_username = check_username(signup.get("username"))
            clean_email = check_email(signup.get("email"))
            clean_age = check_age(signup.get("age"))
            valid.append({"username": clean_username, "email": clean_email, "age": clean_age})
        except ValidationError as e:
            invalid.append({"username": signup.get("username", ""), "reason": str(e)})

    return {"valid": valid, "invalid": invalid}

def check_username(username):
    if not username:
        raise ValidationError("Invalid username!")
    return username.strip()

def check_email(email):
    if email.count("@") !=1:
        raise ValidationError("Invalid email")
    email_name, email_domain = email.split("@")
    if "." not in email_domain:
        raise ValidationError("Invalid email")
    else:
        return email.strip().lower()

def check_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValidationError("Invalid age!")

    if not 0 < age <= 120:
        raise ValidationError("(Invalid age!")
    return age

def main():
    print(clean_signups(raw_signups))

if __name__ == "__main__":
    main()