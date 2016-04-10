from datetime import datetime
import json


class WrongArgumentException(Exception):
    pass


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


class FoodDiary:

    def __init__(self, dict):
        self.__dict = dict

    def __get_current_date(self):
        date = datetime.now()
        return "{}/{}/{}".format(date.day, date.month, date.year)

    def __add_to_dict(self, meal, date):
        if date in self.__dict:
            self.__dict[date].append(meal)
        else:
            self.__dict[date] = [meal]

    def add_meal(self, meal):
        if meal == '':
            raise WrongArgumentException("Add some meal!")
        date = self.__get_current_date()
        self.__add_to_dict(meal, date)
        return "Ok, it's saved."

    def list_diary(self, date):
        if date == '':
            raise WrongArgumentException("Add some date!")
        if date in self.__dict:
            return "\n".join(self.__dict[date])
        return "No meals for that day."


def main():
    f = open("food_diary.json", 'r')
    try:
        data = json.load(f)
    except:
        data = {}

    f.close()

    fd = FoodDiary(data)
    cli = CLI(fd)

    cli.start()

    f = open("food_diary.json", 'w')
    json.dump(data, f, indent=4)
    f.close()


if __name__ == '__main__':
    main()
