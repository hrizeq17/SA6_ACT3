def exponential_mapping(numbers, n):
    return list(map(lambda x: x ** n, numbers))
numbers = [1, 2, 3, 4, 5]
n = 3
result = exponential_mapping(numbers, n)
print("Result:", result)
#problem 5 , complete activity 3 