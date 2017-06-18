

def greet():
    """
    Greets the user whenever the utility is launched the first time.
    """
    print("Welcome to chattercat")
    print("In case you are new, try 'help' or 'h'")
    global user_name
    user_name = input("Please enter a user name (max 10 characters) : ")[:10]


def say_bye():
    """
    People have many problems. It's nice to say Good bye when you leave.
    """
    print("Good bye ...")
    print("Have a nice day!")


def prompt():
    """
    Prompts the user for input at repl and returns the command and arguments
    entered by the user as a tuple of (string, list)
    """
    full_command = input('> ')
    full_command = full_command.split(' ')
    command = full_command[0]
    arguments = full_command[1:]
    return command, arguments


def main():
    greet()
    while True:
        command, arguments = prompt()
        try:
            # do something with command and its arguments
            if command not in valid_commands:
                raise 'Invalid command'
            pass
        except 'Invalid command':
            print("The command " + command + " you specified wasn't found.")
            print("Try 'help' or 'h'")
        except:
            print("An unknown error was encountered.")
            print("Quiting the application!")
            break
    say_bye()


if __name__ == '__main__':
    main()
