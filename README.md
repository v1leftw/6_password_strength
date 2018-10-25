# Password Strength Calculator

Script calculates score of the inputted password. User can't see inputted password.

If password contains in [prohibition list](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/darkweb2017-top100.txt) - returns 0.
Repo of the lists - [here](https://github.com/danielmiessler/SecLists)
If user has own list or does not have connection to Internet he can set his list with ```-path``` argument.

# Quickstart
Examples of script launch on Linux, Python 3.5

EXAMPLE 1. Without argument
```
$ python password_strength.py
Input your password:
Your score is 0.
```

EXAMPLE 2. With argument
```
$ python password_strength.py -path [path_to_file]
Input your password:
Your score is 5.
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
