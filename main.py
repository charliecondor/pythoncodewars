# Codewars Python Solutions Library
# Execute solution tests here
def main():
    # array_test = [1, 2, 3, 4, 5, 6]
    # print(sum_array_1(array_test))
    # print(sum_array_2(array_test))
    # print(doubleInteger_2(20))
    print(remove_char("abcdefg"))


# My initial solution
def sum_array_1(array):
    sum = 0
    for item in array:
        sum += item
    return sum


# Better solution
def sum_array_2(array):
    return sum(array)


# My initial solution
def doubleInteger_1(i):
    return i * 2


# Bitwise solution
def doubleInteger_2(i):
    return i << 1


# Initial solution
def remove_char(original_string):
    return original_string[1:-1]


# Main
if __name__ == '__main__':
    main()