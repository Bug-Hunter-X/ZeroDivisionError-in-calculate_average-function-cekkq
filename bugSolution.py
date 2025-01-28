def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    return sum(numbers) / len(numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}")  # Output: Average: 0

# Example usage with a list of numbers
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"Average: {average}")  # Output: Average: 30.0