import sys
from random import randint
import os


def cat(file):
    f = open(file, 'r')
    print(f.read())

    f.close()


def cat2(files):
    for file in files:
        f = open(file, 'r')
        print(f.read())
        f.close()


def random_numbers(number):
    result = ""
    for i in range(0, number):
        result += str(randint(0, number))
        result += " "
    return result


def generate_number(file_name, number):
    f = open(file_name, 'w')
    f.write(random_numbers(int(number)))
    f.close


def sum_numbers(file):
    with open(file, 'r') as f:
        numbers = f.read()

    split_numbers = numbers.split()

    result = 0
    for number in split_numbers:
        result += int(number)

    return result


def dush(path):
    total_size_in_byte = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            full_file = os.path.join(root, file)
            if os.path.isfile(full_file):
                total_size_in_byte += os.path.getsize(full_file)
    return total_size_in_byte / (1024 ** 3)


def main():
    print(dush(sys.argv[1]))


if __name__ == '__main__':
    main()
