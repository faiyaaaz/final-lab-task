#checking name if its in contact book (implemented in choice 1)
def check_name(name):
    with open("contacts.txt", "r") as f:
        for line in f:
            existing_name, _ = line.strip().split(",")
            if existing_name.lower() == name.lower():
                return True
    return False 
#checking phone if its in contact book (implemented in choice 2)
def check_phone(phone):
    with open("contacts.txt", "r") as f:
        for line in f:
            _, existing_phone = line.strip().split(",")
            if existing_phone == phone:
                return True
    return False
#searching contact (implemented in choice 3)
def search_contact(search_name):
    with open("contacts.txt", "r") as f:
        for line in f:
            existing_name, existing_phone = line.strip().split(",")
            if search_name.lower() == existing_name.lower():
                return existing_phone
    return False

choice = 0
while choice != 4:

    choice = int(input("1. Add a new contact\n2. View all contacts\n3. Search for a contact, and\n4. Exit the program\n"))

#choice 1
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter number: ")

        if len(phone) != 5:  #let, valid phone number contains 5 digits 
            print("Enter a valid phone number.") #checking if the number is valid
        
        else: 
            if check_name(name) == True: 
                print("Name already used. Use a different name.") #checking name if its in contact book
            
            elif check_phone(phone) == True:
                print("Phone number already in contact book.") #checking phone if its in contact book
            
            else:
                with open("contacts.txt", "a") as f:
                    f.write(f"{name.title()},{phone}\n") #saving contact in txt file
                print("Contact saved.")
#choice 2   
    elif choice == 2:
        with open("contacts.txt", "r") as f:
            count = 1
            for line in f:
                name, phone = line.strip().split(",")
                print(f"{count}.Contact name: {name}\nPhone number: {phone}\n")
                count += 1
#choice 3   
    elif choice == 3:
        search_name = input("Enter contact name: ")
        if search_contact(search_name) == False:
            print("Contact not found. Try again.")
        else:
            print(f"Phone number: {search_contact(search_name)}")

