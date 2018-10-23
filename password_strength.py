import re
from string import punctuation


def get_password_strength(password):
    pass


def check_lower_and_upper_characters(pw):
    if re.search(r"[a-zа-я]", pw) and re.search(r"[A-ZА-Я]", pw):
        return True
    else:
        return False


def get_number_of_digits(pw):
    return len(re.findall("[0-9]", pw))


def check_special_characters(pw):
    if re.search(r"["+punctuation+"]", pw):
        return True
    else:
        return False


def check_if_contains_in_prohibition_lists(pw):
    pass


if __name__ == "__main__":
    password = input("Input your password: ")
    print(check_lower_and_upper_characters(password))
    print(get_number_of_digits(password))
    print(check_special_characters(password))
