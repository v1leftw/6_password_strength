import re
from string import punctuation
import getpass
import argparse
import os


def load_blacklist(filepath):
    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf-8") as pw_blacklist:
            return pw_blacklist.read()


def get_password_strength(user_pw, forbidden_pws=None):
    highest_score_password_length = 10
    if is_in_prohibition_list(user_pw, forbidden_pws):
        return 0
    current_score = get_scores_for_conditions(user_pw)
    if len(user_pw) > highest_score_password_length/2:
        return current_score * 2
    return current_score


def check_lower_and_upper_characters(user_pw):
    return bool(
        re.search(r"[a-zа-я]", user_pw)
        and
        re.search(r"[A-ZА-Я]", user_pw)
    )


def get_number_of_digits(user_pw):
    return len(re.findall("[0-9]", user_pw))


def check_special_characters(user_pw):
    return bool(re.search(r'[{}]'.format(punctuation), user_pw))


def is_in_prohibition_list(user_pw, prohibition_list):
    if prohibition_list is None:
        return False
    if user_pw in prohibition_list.split("\n"):
        return True
    return False


def get_scores_for_conditions(user_pw):
    score = 0
    if check_lower_and_upper_characters(user_pw):
        score = score + 2
    if check_special_characters(user_pw):
        score = score + 2
    if get_number_of_digits(user_pw) > 2:
        score = score + 1
    return score


def get_args():
    parser = argparse.ArgumentParser(description="Enter the path directory:")
    parser.add_argument("-path", help="Path to file", default=None)
    return parser.parse_args()


if __name__ == "__main__":
    password = getpass.getpass("Input your password: ")
    path = get_args().path
    blacklist = load_blacklist(path)
    if blacklist is None:
        print("No prohibition lists used. ")
    print("Your score is {}.".format(
        get_password_strength(password, blacklist)
    ))
