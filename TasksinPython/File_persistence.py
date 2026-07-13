file_name = "contact_book.txt"

while True:
    print("\n1. Add your contacts")
    print("2. View your contacts")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")

        file = open(file_name, "a")
        file.write(name + " - " + phone + "\n")
        file.close()

        print("Contact Saved!")

    elif choice == 2:
        try:
            file = open(file_name, "r")
            print("\nContacts:")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No contacts found!")

    elif choice == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")