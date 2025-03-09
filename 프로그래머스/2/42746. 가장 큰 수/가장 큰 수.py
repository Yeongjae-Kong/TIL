def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x + pivot >= pivot + x]
    right = [x for x in arr[1:] if x + pivot < pivot + x]

    return quick_sort(left) + [pivot] + quick_sort(right)

def solution(numbers):
    str_numbers = [str(num) for num in numbers]
    sorted_numbers = quick_sort(str_numbers)

    if sorted_numbers[0] == "0":
        return "0"

    return "".join(sorted_numbers)
