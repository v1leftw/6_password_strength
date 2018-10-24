import re
from string import punctuation
from urllib import request
from urllib import error
import getpass

'''
List of top non-secure passwords:
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/darkweb2017-top100.txt
Link was shortened below.
'''
PROHIBITION_LIST = "https://bit.ly/2AoqJzK"


def get_data_from_list():
    try:
        with request.urlopen(PROHIBITION_LIST, timeout=5000) as pw_list:
            return pw_list.read().decode("utf-8")
    except (error.URLError, error.HTTPError, error.ContentTooShortError):
        return None


def get_password_strength(user_pw):
    if is_in_prohibition_list(user_pw):
        return 0
    current_score = set_scores_for_conditions(user_pw)
    if len(user_pw) > 5:
        return current_score * 2
    return current_score


def check_lower_and_upper_characters(user_pw):
    if re.search(r"[a-zа-я]", user_pw) and re.search(r"[A-ZА-Я]", user_pw):
        return True
    else:
        return False


def get_number_of_digits(user_pw):
    return len(re.findall("[0-9]", user_pw))


def check_special_characters(user_pw):
    if re.search(r'[{}]'.format(punctuation), user_pw):
        return True
    else:
        return False


def is_in_prohibition_list(user_pw):
    prohibition_list = get_data_from_list()
    print(prohibition_list)
    if prohibition_list is None:
        return False
    if user_pw in prohibition_list.split("\n"):
        return True
    return False


def set_scores_for_conditions(user_pw):
    score = 0
    if check_lower_and_upper_characters(user_pw):
        score = score + 2
    if check_special_characters(user_pw):
        score = score + 2
    if get_number_of_digits(user_pw) > 2:
        score = score + 1
    return score


if __name__ == "__main__":
    password = getpass.getpass("Input your password: ")
    print("Your score is {}.".format(get_password_strength(password)))
