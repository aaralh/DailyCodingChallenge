"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

numbers = [10, 15, 3, 7]

def checkForSum(numbers, k) -> int:
    for n1 in numbers:
        for n2 in numbers:
            if (n1 + n2 == k):
                return True
    return False


result = checkForSum(numbers, 17)
print(result)