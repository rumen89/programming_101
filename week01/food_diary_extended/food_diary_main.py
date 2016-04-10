import json
from food_diary import FoodDiary
from cli import CLI
from calories import Calories


def main():
    f = open("food_diary.json", 'r')
    try:
        data = json.load(f)
    except:
        data = {}

    c = open('calories.json', 'r')
    try:
        calories = json.load(c)
    except:
        calories = {}

    f.close()
    c.close()

    cal = Calories(calories)
    fd = FoodDiary(data, cal)
    cli = CLI(fd)

    cli.start()

    f = open("food_diary.json", 'w')
    json.dump(data, f, indent=4)
    f.close()

    c = open("calories.json", 'w')
    json.dump(calories, c, indent=4)
    c.close()

if __name__ == '__main__':
    main()
