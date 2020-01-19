"""
Write a program that prints the numbers from 1 to 100. But:
 - for multiples of three print “Fizz” instead of the number and
 - for the multiples of five print “Buzz”.
 - For numbers which are multiples of both three and five print “FizzBuzz”.
"""


def fizzbuzz():
    fizz_buzz_list = []
    for num in range(1, 101, 1):
        if num % 3 == 0 and num % 5 != 0:
            fizz_buzz_list.append('Fizz')
        elif num % 3 == 0 and num % 5 == 0:
            fizz_buzz_list.append('FizzBuzz')
        elif num % 5 == 0 and num %3 != 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(' ¯\_(ツ)_/¯')
    return fizz_buzz_list


fizz_buzz_nums = fizzbuzz()
nums_to_100 = list(range(1,101,1))
for i in range(len(nums_to_100)):
    print(nums_to_100[i], fizz_buzz_nums[i])

