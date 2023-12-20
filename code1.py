def check_name(name):
    with open("contacts.txt", "r") as f:
        for line in f:
            existing_name, _ = line.strip().split(",")
            if existing_name == name:
                return True
    return False 
def check_phone(phone):
    with open("contacts.txt", "r") as f:
        for line in f:
            _, existing_phone = line.strip().split(",")
            if existing_phone == phone:
                return True
    return False

choice = int(input("1. Add a new contact\n2. View all contacts\n3. Search for a contact, and\n4. Exit the program\n"))

if choice == 1:
    name = input("Enter name: ")
    phone = input("Enter number: ")

    if len(phone) != 5:
        print("Enter a valid phone number.")
    else:
        if check_name(name) == True:
            print("Name already used. Use a different name.")
        elif check_phone(phone) == True:
            print("Phone number already in contact book.")
        else:
            with open("contacts.txt", "a") as f:
                f.write(f"\n{name},{phone}")
            print("Contact saved.")
elif choice == 2:
    with open("contacts.txt", "r") as f:
        count = 1
        for line in f:
            name, phone = line.strip().split(",")
            print(f"{count}.Contact name: {name}\nPhone number: {phone}\n")
            count += 1
