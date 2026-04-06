# given a list of integers, return the highest and lowers n in array
# don't use max() or min()
# e.g. [2, 4, 1, 0, 2, -1] returns [-1, 4]


def get_min_and_max() -> list:
    numbers = []
    # build array from inputs
    while True:
        num = input(
            "Input a number to add it to the list, type 'end' to finish: ")

        # if 'end' is inputted
        if num.lower() == 'end':
            break

        # add valid numbers
        try:
            numbers.append(int(num))
        except:
            print("Invalid input.")

    # get min and max
    highest = numbers[0]
    lowest = numbers[0]

    for number in numbers:
        # if greater than current highest, replace highest
        if number > highest:
            highest = number
        # if lower than current lowest, replace lowest
        if number < lowest:
            lowest = number

    return [lowest, highest]


# testing
print(get_min_and_max())
