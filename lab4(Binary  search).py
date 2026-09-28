#Binary Search in Python

def binary_search(numbers, target):

    low = 0
    high = len(numbers) - 1

    while low <= high:

        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid

        elif target < numbers[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


numbers = [10, 20, 30, 40, 50, 60, 70]

target = 50

result = binary_search(numbers, target)

if result == -1:
    print("Value not found")
else:
    print("Value found at index:", result)
