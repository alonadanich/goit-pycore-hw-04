def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return f"Contact {name} added with phone {phone}."
    return "Invalid format. Use: add [name] [phone]"


def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Contact {name} updated with new phone {phone}."
        return f"Contact {name} not found."
    return "Invalid format. Use: change [name] [new phone]"


def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"Phone for {name}: {contacts[name]}"
        return f"Contact {name} not found."
    return "Invalid format. Use: phone [name]"


def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts found."


def main():
    contacts = {}  
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
