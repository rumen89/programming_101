import json
from food_diary import FoodDiary
from cli import CLI


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
