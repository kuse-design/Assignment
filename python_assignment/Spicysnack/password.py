checker = input("Enter your six-digit password: ")
length = len(checker)

if length <= 6:
    print("Password is weak")

if 6 < length < 10:
    print("Password is medium")

if length >= 10:
    print("Password is strong")

if length < 1:
    print("Password is invalid")
