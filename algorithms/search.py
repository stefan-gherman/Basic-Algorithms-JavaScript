"""
Implement these two search algorithms.
"""


def linear_search(number, list):
    """
    Search for the number in the sorted list with the linear search algorithm
    and return the index of the element.

    Optional: print out how many comparision was needed to find the number

    :param integer number: The number to search for
    :param list of numbers list: Ascending list of numbers
    :return: Index of the element or None
    :rtype: integer
    """
    steps = 1
    for nums in range(len(list)):
        if number == list[nums]:
            return nums, steps
        else:
            steps += 1
    return None


def binary_search(number, list):
    """
    Search for the number in the sorted list with the binary search algorithm
    and return the index of the element.

    Optional: print out how many comparision was needed to find the number

    :param integer number: The number to search for
    :param list of numbers list: Ascending list of numbers
    :return: Index of the element or None
    :rtype: integer
    """
    left = 0
    right = len(list) - 1
    steps = 1

    while left <= right:
        mid = (left + right)//2

        if number == list[mid]:
            return mid,steps
        elif number == list[right]:
            return right,steps
        elif number == list[left]:
            return left, steps
        else:
            if number > list[mid]:
                left = mid + 1
                steps += 1
            elif number < list[mid]:
                right = mid - 1
                steps += 1

    return None


def print_results(search, index):
    result = search.title() + ' search '

    if index is None:
        result += 'did not find it.'
    else:
        result += f'found it on index {index[0]} in {index[1]} steps.'

    print(result)


def main():
    numbers = [3, 6, 8, 11, 18, 23, 24, 33, 36, 45, 46, 51, 56, 60, 69, 72, 83, 90, 93, 97]
    searched_number = int(input('What is the number you are looking for? (0-100) '))

    print_results('linear', linear_search(searched_number, numbers))
    print_results('binary', binary_search(searched_number, numbers))


if __name__ == '__main__':
    main()
