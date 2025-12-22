print("1. Create\n2. Open\n3. Write\n4. Exit")

while True:
    decide = input("Option: ")
    if decide == '1':
        filename = input("Filename: ")
        with open(filename, 'w') as file:
            pass
        print("File created")
    elif decide == '2':
        filename = input("Filename: ")
        with open(filename, 'r') as file:
            print(file.read())
    elif decide == '3':
        filename = input("Filename: ")
        lines = int(input("Lines: "))
        count = 1
        while count <= lines:
            text = input(f"{count}: ")
            with open(filename, 'a') as file:
                file.write(text + "\n")
            count += 1
        print("File updated")
    elif decide == '4':
        print("Program closed")
        break
    else:
        print("Invalid choice")
