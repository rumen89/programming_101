def palindrome(n):
    reversed_string = ""

    for i in range(0, len(str(n))):
        reversed_string = str(n)[i] + reversed_string

    if reversed_string == str(n):
        return True

    return False


def to_digits(number):
    result = []

    if number < 0:
        number *= -1

    while (number > 0):
        digit = number % 10

        result = [digit] + result

        number = number // 10

    return result

# 1. A number is called balanced, if we take the middle
# of it and the sums of the left and right parts are equal.

# For example, the number 1238033 is balanced,
# because it's left part is 123 and right part is 033.

# We have : 1 + 2 + 3 = 0 + 3 + 3 = 6.

# A number with only one digit is always balanced!

# Implement a function is_number_balanced(n) that checks if n is balanced.


def digits_count(number):
    counter = 0

    while number > 0:
        # digit = number % 10
        counter += 1

        number = number // 10

    return counter


def is_number_balanced(n):
    mid = digits_count(n) // 2

    first_half = 0
    second_half = 0

    digits_from_number = to_digits(n)

    for index in range(0, mid):
        first_half += digits_from_number[index]

    for index in range(len(digits_from_number) - mid, len(digits_from_number)):
        second_half += digits_from_number[index]

    if first_half == second_half:
        return True

    return False


# 2.1 Increasing sequnce?

# Implement a function, called is_increasing(seq)
# where seq is a list of integers.

# The function should return True,
# if the given sequence is monotonously increasing.

# And before you skip this problem,
# because of the math terminology, let me explain:

# A sequence is monotonously increasing if for every two elements a and b,
# that are next to each other (a is before b), we have a < b.

# For example, [1,2,3,4,5] is monotonously increasing,
# but [1,2,3,4,5,1] is not.


def is_increasing(seq):
    for index in range(1, len(seq)):
        if seq[index - 1] >= seq[index]:
            return False

    return True


def is_decreasing(seq):
    for index in range(1, len(seq)):
        if seq[index - 1] <= seq[index]:
            return False

    return True


# 3. Largest Palindrome
# Implement a function get_largest_palindrome(n), which return the largest
# palindrome smaller than n. Given number n can also be palindrome.

def get_largest_palindrome(n):
    while True:
        n -= 1

        if palindrome(n):
            break

    return n


# 4. Prime Numbers
# Given an integer, implement a function, called prime_numbers(n).
# Use Sieve of Eratosthenes to find all the prime
# numbers less than or equal to n.


def prime_numbers(n):
    list = to_list(n)
    new_list = []
    index = 0

    if n == 1:
        return 0

    while True:
        p = list[index]

        for i in range(0, index + 1):
            new_list.append(list[i])

        for i in range(index + 1, len(list)):
            if list[i] % p != 0:
                new_list.append(list[i])
        list = new_list

        new_list = []
        index += 1

        if index + 1 >= len(list):
            break

    return list


def to_list(n):
    list = []

    for i in range(2, n + 1):
        list.append(i)

    return list


# 5. Anagrams
# For anagrams, check here - https://en.wikipedia.org/wiki/Anagram

# For example, listen and silent are anagrams.

# Implement a function is_anagram(a, b),
# which returns True, if the string a is an anagram of b.

# Consider lowering the case of the two words since the case does not matter.
# SILENT and listen are also

def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    c = ''
    indexes = []

    for ch in a:
        if ch in b and b.index(ch) not in indexes:
            c += ch
            indexes.append(b.index(ch))
    if len(indexes) != len(b):
        return False
    return a == c


# 6. Birthday Ranges
# Implement a function birthday_ranges(birthdays, ranges) We have a list
# birthdays and list of tuples ranges. birthdays - range from 0 to 365,
# ranges - ranges (one range is a tuple of two numbers - start and end0.

# We want to calculate, for each tuple, how many people are born in that range
# (between start and end inclusive).


def birthday_ranges(birthdays, ranges):
    result = []
    counter = 0

    for tuple in ranges:
        for date in birthdays:
            if date >= tuple[0] and date <= tuple[1]:
                counter += 1
        result.append(counter)
        counter = 0

    return result


# 7. Sum Numbers in Matrix
# You are given a NxM matrix of integer numbers.

# Implement a function, called sum_matrix(m) that returns the sum of all
# numbers in the matrix.

# The matrix will be represented as nested lists in Python.

def sum_matrix(m):
    result = 0

    for list in m:
        for number in list:
            result += number

    return result


# 9.1 Is Transversal?

# Implement a function is_transversal(transversal, family), which check if
# given set is a valid transerval for another family of sets (set of sets).

def is_transversal(transversal, family):

    for set in family:
        checker = 0
        for number in transversal:
            if number in set:
                checker = 1
        if checker == 0:
            return False

    return True


# You are givn a NxM matrix of integer numbers.
# We can drop a bomb at any place in the matrix,
# which has the following effect:

# All of the 3 to 8 neighbours (depending on where you hit!) of the target are
# reduced by the value of the target.
# Numbers can be reduced only to 0 - they cannot go to negative.

def find_neighbours(row, column, matrix):
    result = []

    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if i != row or j != column:
                    result.append((i, j))

    return result


def bombing_matrix(row, column, matrix):
    current_position = matrix[row][column]
    neighbours = find_neighbours(row, column, matrix)

    for tuple in neighbours:
        new_position = matrix[tuple[0]][tuple[1]]
        if new_position - current_position < 0:
            matrix[tuple[0]][tuple[1]] = 0
        else:
            matrix[tuple[0]][tuple[1]] = new_position - current_position
    # print(matrix)
    return matrix


def copy_matrix(matrix):
    result = []
    inner_list = []

    for row in matrix:
        inner_list = []
        for number in row:
            inner_list += [number]
        result += [inner_list]
    # print("new matrix is: {}".format(result))
    return result


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            # print("matrix is: {}".format(m))
            matrix = copy_matrix(m)
            result[(i, j)] = sum_matrix(bombing_matrix(i, j, matrix))

    return result

if __name__ == '__main__':
    # print(to_digits(1230))
    # print(digits_count(123))
    # print(is_number_balansed(1222))
    # print(is_decreasing([1, 2, 3, 4, 5]))
    # print(is_decreasing([5, 4, 3, 2, 1]))
    # print(get_largest_palindrome(98))
    print(prime_numbers(30))
    # print(is_anagram("TOP_CODER", "COTO_PRODE"))
    # print(is_anagram('listen', 'silent'))

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # print(matrix_bombing_plan(matrix))
    # print(birthday_ranges([1, 2, 3, 4, 5],
    # [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
