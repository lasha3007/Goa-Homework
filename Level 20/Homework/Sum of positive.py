def positive_sum(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total