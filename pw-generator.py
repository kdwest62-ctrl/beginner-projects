import random
import string

try:
    characters_list = []
    length = int(input("Password length: "))
    if length > 0:
        upper = input("Include uppercase letters? (y/n): ")
        if upper == "y":
            characters_list.append(string.ascii_uppercase)
        lower = input("Include lowercase letters? (y/n): ")
        if lower == "y":
            characters_list.append(string.ascii_lowercase)
        numbers = input("Include numbers? (y/n): ")
        if numbers == "y":
            characters_list.append(string.digits)
        special = input("Include special characters? (y/n): ")
        if special == "y":
            characters_list.append(string.punctuation)
        characters = "".join(characters_list)

        total = int(input("Number of passwords to generate: "))
        if total > 0:
            passwords = []
            generated = 0
            while generated != total:
                password = "".join(random.choices(characters, k=length))
                passwords.append(password)
                print(password)
                generated += 1
            save = input("Save passwords to text file? (y/n): ")
            if save  == 'y':
                saved = 0
                file_name = input("File name: ")
                location = input("Save location: ")
                file_path = location + "\\" + file_name + ".txt"
                for item in passwords:
                    with open(file_path, 'a') as file:
                        file.write(item + "\n")
                    saved += 1
                print(f"{saved} passwords saved")
except ValueError:
    print("Please input a number")
