from datetime import datetime
from exceptions import WrongArgumentException


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
