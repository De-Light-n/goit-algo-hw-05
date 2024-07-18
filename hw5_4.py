# Декоратор
def input_error_for_add_contact(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Not enough arguments was gained. To add you need 'add name phone'", end=" ")
        except Exception as e:
            print(e, end=" ")
        return " "
    return inner

def input_error_for_show_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Contact was not founded", end=" ")
        except IndexError:
            print("Not enough arguments was gained. To phone you need 'phone name'", end=" ")
        except Exception as e:
            print(e, end=" ")
        return " "
    return inner
            
def input_error_for_change_contact(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Contact was not founded", end=" ")
        except IndexError:
            print("Not enough arguments was gained. To change you need 'change name new-phone'", end=" ")
        except Exception as e:
            print(e, end=" ")
        return " "
    return inner

def input_error_for_parse_input(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Nothing was gained.", end=" ")
        except Exception as e:
            print(e, end=" ")
        return " "
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

@input_error_for_show_phone       
def show_phone(args, contacts:dict):
    output = contacts[args[0]]
    return output

@input_error_for_change_contact     
def change_contact(args, contacts:dict):
    old_name = contacts[args[0]]
    contacts[args[0]] = args[1]
    return "Contact changed"

@input_error_for_parse_input
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_for_add_contact
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