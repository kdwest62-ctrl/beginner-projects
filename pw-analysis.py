import string

def check_strength(pw):
    def length(p):
        if len(p) >= 8:
            return 1
        else:
            return 0
    def digits(p):
        digit = 0
        for char in p:
            if char in string.digits:
                digit += 1
        if digit > 0:
            return 1
        else:
            return 0
    def punctuation(p):
        punctuate = 0
        for char in p:
            if char in string.punctuation:
                punctuate += 1
        if punctuate > 0:
            return 1
        else:
            return 0
    def upper_lower(p):
        upper = 0
        lower = 0
        for char in p:
            if char.isupper():
                upper += 1
        for char in p:
            if char.islower():
                lower += 1
        if upper > 0 and lower > 0:
            return 1
        else:
            return 0
    strength = length(pw) + digits(pw) + punctuation(pw) + upper_lower(pw)
    if strength == 0 or strength == 1:
        return "weak"
    elif strength == 2 or strength == 3:
        return "medium"
    elif strength >= 4:
        return "strong"

def comments(pw):
    def length(p):
        if len(p) >= 8:
            return "Length: ok"
        else:
            lack = 8 - len(p)
            return f"Password only has {len(p)} characters. Add {lack} or more"
    def digits(p):
        digit = 0
        for char in p:
            if char in string.digits:
                digit += 1
        if digit > 0:
            return "Digits: ok"
        else:
            return "Add at least 1 digit"
    def punctuation(p):
        punctuate = 0
        for char in p:
            if char in string.punctuation:
                punctuate += 1
        if punctuate > 0:
            return "Punctuation: ok"
        else:
            return "Add at least 1 punctuation"
    def upper_lower(p):
        upper = 0
        lower = 0
        for char in p:
            if char in string.ascii_uppercase:
                upper += 1
        for char in p:
            if char in string.ascii_lowercase:
                lower += 1
        if upper > 0:
            if lower > 0:
                return "Uppercase and lowercase letters: ok"
            else:
                return "Add at least 1 lowercase letter"
        elif lower > 0:
            if upper > 0:
                return "Uppercase and lowercase letters: ok"
            else:
                return "Add at least 1 uppercase letter"
        else:
            return "Add at least 1 uppercase and 1 lowercase letter"
    return f"{length(pw)}\n{upper_lower(pw)}\n{digits(pw)}\n{punctuation(pw)}"

password = input("Password: ")
print(f"Strength: {check_strength(password)}")
print(comments(password))
