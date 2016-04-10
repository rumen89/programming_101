from exceptions import WrongArgumentException


class CLI:

    def __init__(self, fd):
        self.__fd = fd
        self._commands = {
            "meal": fd.add_meal,
            "list": fd.list_diary,
            "exit": self.__exit,
            "help": self.__help_message
        }
        self.__is_in_program = True

    def __help_message(self, *args):
        return "Help message:\n\
1.meal <meal> - add meal to diary.\n\
2.list <dd/mm/yyyy> - list all meals for that day.\n\
3.help - show help message.\n\
4.exit - exit from diary.\n"

    def __exit(self, *args):
        self.__is_in_program = False
        return "Goodbye"

    def start(self):
        print("Hello and welcome!")
        print(self.__help_message())

        while self.__is_in_program:
            user_input = input("Enter command> ")
            split_user_input = user_input.split()
            argument = ''
            try:
                if len(split_user_input) == 0:
                    raise WrongArgumentException("You\
have to enter some command!")
                elif len(split_user_input) > 1:
                    argument = split_user_input[1]

                command = split_user_input[0]

                print(self._commands[command](argument))
            except WrongArgumentException as e:
                print(e)
            except:
                print("Something went wrong. Try again!")
