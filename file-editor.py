print("1. New\n2. Open\n3. Write\n4. Append\n5. Exit")

while True:
    decide = input("Choose option: ")
    if decide == '1':
        filename = input("Enter filename: ")
        with open(filename, 'w') as file:
            pass
        print(f"{filename} successfully created")
    elif decide == '2':
        try:
            filename = input("Enter filename: ")
            with open(filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found")
    elif decide == '3':
        filename = input("Enter filename: ")
        lines = int(input("Lines: "))
        count = 1
        while count <= lines:
            text = input(f"")
            with open(filename, 'w') as file:
                file.write(text + "\n")
            count += 1
        print("File updated")
    elif decide == '4':
        filename = input("Enter filename: ")
        lines = int(input("Lines: "))
        count = 1
        while count <= lines:
            text = input(f"")
            with open(filename, 'a') as file:
                file.write(text + "\n")
            count += 1
        print("File updated")
    elif decide == '5':
        print("Program closed")
        break
    else:
        print("Invalid choice")
