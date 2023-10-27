def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please." # якщо ввести "add username phone" і неправильні дані
        except KeyError:
            return "Contact does not exists" # якщо ввести в "change username phone" зовсім нове ім'я
        except IndexError:
           return "Give me the username, please." # якщо ввести "phone username" без даних
    return inner

def parse_input(user_input):
    norm_str = user_input.strip().lower()
    if norm_str.startswith("phone username"):
        cmd = "phone username"
        user_input_res = user_input.strip()[14:]
    elif norm_str.startswith("add username phone"):
        cmd = "add username phone"
        user_input_res = user_input.strip()[18:]
    elif norm_str.startswith("change username phone"):
        cmd = "change username phone"
        user_input_res = user_input.strip()[21:]
    else:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    *args , = user_input_res.split()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists"
    else:
        contacts[name] = int(phone)
        return "Contact added."
    
@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts[name] != int(phone):
        contacts[name] = int(phone)
        return "Contact changed."

@input_error
def get_phone(args, contacts):
    name = args[0]
    if len(args) > 1:
        return "Give me only the username, please."
    if name in contacts:
        return contacts[name]
    else:
        return "Contact does not exists"

def get_all(contacts):
    res = ""
    if len(contacts) == 0:
         res = "no contacts"
    else:
        i = 1
        for name, number in contacts.items():
            if i < len(contacts):
                res += f"{name}: {number}\n"
                i += 1
            else:
                res += f"{name}: {number}"
    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!"
          "\nI accept the following commands: \n add username phone \n change username phone \n phone username \n all"
          )
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add username phone":
            print(add_contact(args, contacts))

        elif command == "change username phone":
            print(change_contact(args, contacts))

        elif command == "phone username":
            print(get_phone(args, contacts))

        elif command == "all":
            print(get_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()