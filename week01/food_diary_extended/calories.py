import re
from exceptions import WrongDimensionexception


class Calories:

    def __init__(self, data):
        self.__data = data

    def __add_to_calories(self, meal, calories):
        self.__data[meal] = int(calories)

    def __check_database(self, meal):
        if meal not in self.__data:
            print("I don't have {} in the calories database.".format(meal))
            calories = input("How much calories per 100g?> ")
            self.__add_to_calories(meal, calories)

    def sum_total_amount(self, meal):
        amount = input("How much have you eaten?> ")

        detailed_amount = re.match(r'(\d*)([k, g]*)', amount)
        amount_only = int(detailed_amount.group(1))
        dimension = detailed_amount.group(2)

        if dimension != 'kg' and dimension != 'g':
            dimension = input("Missing or wrong dimension. Please add it!> ")

        self.__check_database(meal)

        calories = self.__data[meal]
        if dimension == 'kg':
            amount_only *= 1000

        total_calories = (amount_only // 100) * calories
        return "Ok, this is a total of {} calories for this meal.".format(
            total_calories)
