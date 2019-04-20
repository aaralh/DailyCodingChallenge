"""
Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def calculateProducts(numbers) -> [int]:
    products = []
    for index in range(len(numbers)):
        product = None
        for index2 in range(len(numbers)):
            if(index != index2):
                if(product == None):
                    product = numbers[index2]
                else:
                    product = product * numbers[index2]
        products.append(product)
    return products

numbers = [1, 2, 3, 4, 5]
result = calculateProducts(numbers)
print(result)