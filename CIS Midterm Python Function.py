def sum_of_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(numbers_list)
print("The sum of even numbers is:", result)