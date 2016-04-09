#  Given a list of strings, implement a function, called count_words(arr)
#  which returns a dictionary of the following kind:
# { "word" : count }
# Where count is the count of occurrences of the word in the list arr.


def count_words(arr):
    result = {}

    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


# In most programming languages, NaN stands for Not a Number.
# If we take a look at the following JavaScript code:
# typeof NaN === 'number' // true
# We will see that in JavaScript, NaN stands for Not a NaN,
# which is recursive by nature.
# Implement a Python function, called nan_expand(times), which returns the
# expansion of NaN (In JavaScript terms :P) that many times.
# For example:
# If we expand NaN once (times=1), we will have "Not a NaN"
# If we expand NaN twice (times=2), we will have "Not a Not a NaN"
# If times=3, we have "Not a Not a Not a NaN"
# And so on ...


def nan_expand(times):
    if times == 0:
        return ''
    return 'Not a ' * times + 'NaN'


# Implement a function, called iterations_of_nan_expand(expanded) that takes a
# string expanded, which is an unkown iteration of NaN Expand
# (check the problem for more information)
# The function should return the number of iterations that have been made,
# in order to get to expanded.
# For example, if we have "Not a Not a Not a NaN" - this is the 3rd
# iteration of NaN.
# If expanded is not a valid NaN expand string,
# the function should return false! (This is the hard part)


def iterations_of_nan_expand(expanded):
    if expanded == '':
        return 0

    word = 'Not a'
    counter = 0
    new_word = ''

    not_a_nan = 'Not a NaN'

    for char in expanded:
        new_word += char

        if word in new_word:
            counter += 1
            new_word = ''

    if counter == 0 or not_a_nan not in expanded:
        return False

    return counter


# We are going to implement a very helpful function, called group.
# group takes a list of things and returns a list of group,
# where each group is formed by all equal consecutive elements in the list.

def group(list):
    result = []

    sub_list = []

    for number in list:
        if number not in sub_list and len(sub_list) > 0:
            result += [sub_list]
            sub_list = []
        sub_list += [number]

    result += [sub_list]

    return result


# Implement the function max_consecutive(items),
# which takes a list of things and returns an integer - the count of
# elements in the longest subsequence of equal consecutive elements.
# For example, in the list [1, 2, 3, 3, 3, 3, 4, 3, 3], the result is 4,
# where the longest subsequence is formed by 3, 3, 3, 3

def max_consecutive(items):
    result = []

    counter = 0
    current_number = 0

    for number in items:
        if current_number == 0:
            current_number = number
        elif current_number != number:
            result += [counter]
            counter = 0
            current_number = number
        counter += 1
    result += [counter]
    return max(result)


# We are implementing a smart GPS software.
#
# We are taking a long trip from Sofia to Plovdiv and we know the distance
# between the two cities.It is a positive integer and we mark it as distance.
#
# We know how much our car can ride with a full tank of gas. It is a positive
# integer in kilometers. We mark it as tank_size.
#
# We have a list of gas stations. We know the distance between Sofia and the
# current gas station. stations = [50, 80, 110, 180, 220, 290]
# The list is sorted!
#
# By using this information we will implement a function that returns the
# shortest list of gas stations that we have to visit in order to travel from
# Sofia to Plovdiv. Know that are allways starting with a full tank_size.


def gas_stations(distance, tank_size, stations):
    result = []

    last_station = 0

    station = 0

    while tank_size + last_station < distance and station < len(stations):
        print(
            "station: {}, last_station: {}".format
            (stations[station], last_station))
        if stations[station] > (tank_size + last_station):
            last_station = stations[station - 1]
            result.append(last_station)
        station += 1
    if tank_size + last_station < distance:
        result.append(stations[station - 1])
    return result

# You are given a string, where there can be numbers.
# Return the sum of all numbers in that string (not digits, numbers)


def sum_of_numbers(st):
    result = 0
    number = '0'
    is_number = False

    for char in st:
        is_number = False
        if '0' <= char <= '9':
            number += char
            is_number = True
        if not is_number:
            result += int(number)
            number = '0'
    result += int(number)
    return result

# 100 SMS
#
# numbersToMessage(pressedSequence)
#
# First, implement the function that takes a list of integers - the sequence of
# numbers that have been pressed. The function should return the corresponding
#  string of the message.
# There are a few special rules:
# If you press 1, the next letter is going to be capitalized
# If you press 0, this will insert a single white-space
# If you press a number and wait for a few seconds, the special breaking
# number -1 enters the sequence. This is the way to write different letters
# from only one keypad!


def letter_find(tuple):
    coding = {
        0: ' ',
        2: {1: 'a', 2: 'b', 3: 'c'},
        3: {1: 'd', 2: 'e', 3: 'f'},
        4: {1: 'g', 2: 'h', 3: 'i'},
        5: {1: 'j', 2: 'k', 3: 'l'},
        6: {1: 'm', 2: 'n', 3: 'o'},
        7: {1: 'p', 2: 'q', 3: 'r', 4: 's'},
        8: {1: 't', 2: 'u', 3: 'v'},
        9: {1: 'w', 2: 'x', 3: 'y', 4: 'z'}
        }

    if tuple[0] == 0:
        return coding[tuple[0]] * tuple[1]

    number = tuple[1]

    if number > len(coding[tuple[0]]):
        while number > len(coding[tuple[0]]):
            number = number - len(coding[tuple[0]])

    return coding[tuple[0]][number]


def group_numbers(items):
    result = []

    counter = 0
    current_number = '0'

    for number in items:
        if current_number == '0':
            current_number = number
        elif number == -1:
            result += [(current_number, counter)]
            counter = -1
        elif current_number != number:
            result += [(current_number, counter)]
            counter = 0
            current_number = number
        counter += 1
    result += [(current_number, counter)]

    return result


def numbers_to_message(pressedSequence):
    result = ''

    group = group_numbers(pressedSequence)
    upper_case = 0
    for tuple in group:
        if tuple[0] == 1 and tuple[1] % 2 != 0:
            upper_case = 1
        if tuple[0] != 1:
            if upper_case == 1:
                result += letter_find(tuple).upper()
                upper_case = 0
            else:
                result += letter_find(tuple)

    return result

# messageToNumbers(messsage)
#
# This function takes a string - the message and returns the minimal
# keystrokes that you ned to write that message

CODING = {
    ' ': [0],
    'a': [2],
    'b': [2, 2],
    'c': [2, 2, 2],
    'd': [3],
    'e': [3, 3],
    'f': [3, 3, 3],
    'g': [4],
    'h': [4, 4],
    'i': [4, 4, 4],
    'j': [5],
    'k': [5, 5],
    'l': [5, 5, 5],
    'm': [6],
    'n': [6, 6],
    'o': [6, 6, 6],
    'p': [7],
    'q': [7, 7],
    'r': [7, 7, 7],
    's': [7, 7, 7, 7],
    't': [8],
    'u': [8, 8],
    'v': [8, 8, 8],
    'w': [9],
    'x': [9, 9],
    'y': [9, 9, 9],
    'z': [9, 9, 9, 9]
    }


def get_numbers(letter):
    result = []

    for code in CODING:
        if letter != ' ' and letter == code.upper():
            result.append(1)
        if letter.lower() == code:
            result.extend(CODING[code])
            break
    return result


def message_to_numbers(message):
    result = []

    for letter in message:
        number_list = get_numbers(letter)
        if len(result) > 0 and number_list[-1] == result[-1]:
            result.append(-1)
        result.extend(number_list)

    return result


if __name__ == '__main__':
    print(message_to_numbers("Ivo e Panda"))
