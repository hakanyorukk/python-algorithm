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

class InvalidEmailException(ValidationError): pass

class InvalidAgeException(ValidationError): pass

class InvalidUsernameException(ValidationError): pass

def clean_signups(records):
    valid = []
    invalid = []
    for signup in records:
        username = signup["username"]
        try:
            clean_username = valid_username(signup["username"].strip())
            clean_age = valid_age(signup["age"])
            clean_email = valid_email(signup["email"])
            valid.append({"username": clean_username, "email": clean_email, "age": clean_age})
        except ValidationError as e:
            invalid.append({"username": username, "reason": str(e)})

    return f"valid: {valid}\ninvalid: {invalid}"

def valid_username(username):
    username = username.strip()
    if not username:
        raise InvalidUsernameException("User name is required")
    return username

def valid_email(email):
    if email.count("@") != 1:
        raise InvalidEmailException("Invalid email")
    local, domain = email.split("@")
    if "." not in domain:
        raise InvalidEmailException("Invalid email")
    else:
        return email.strip().lower()

def valid_age(age):
    try:
        age = int(age)
    except ValueError:
        raise InvalidAgeException("Age must be a number")

    if 0 < age <= 120:
        return age
    else:
        raise InvalidAgeException("Invalid age")

def main():
    print(clean_signups(raw_signups))

if __name__ == "__main__":
    main()


