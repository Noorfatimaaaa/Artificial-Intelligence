def insertion_sort(arr):

    # Start from second element
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        # Move bigger elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        # Put key in the correct place
        arr[j + 1] = key

    return arr


# Example
data = [12, 11, 13, 5, 6]

print("Sorted Array:", insertion_sort(data))