# Декоратор
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Not enough arguments was gained."
        except KeyError:
            return "Contact was not founded."
        except IndexError:
            return "Not enough arguments was gained."
        except Exception as e:
            return  f"{e}"
    return inner

# Функції 
def show_all(contacts:dict):
    output = ""
    if contacts:
        for name, phone in contacts.items():
            output += f"{name} : {phone}\n"
        return output
    else:
        return "There is not any contacts\n"

@input_error       
def show_phone(args, contacts:dict):
    output = contacts[args[0]]
    return output

@input_error     
def change_contact(args, contacts:dict):
    old_name = contacts[args[0]]
    contacts[args[0]] = args[1]
    return "Contact changed"

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts), end="")       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()