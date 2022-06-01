import re

def validate(s):
    if re.search(r".+@.+\.edu", s):
        return "Valid"
    else:
        return "Invalid"


def test_validate():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("malan@harvard?edu") == "Invalid"


if __name__ == "__main__":
    email = input("What's your email? ").strip()
    print(validate(email))
