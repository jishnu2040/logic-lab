numbers = input("Enter numbers separated by commas: ")
number_list = [int(num) for num in numbers.split(",")]
print("List of numbers:", number_list)
number_tuple = tuple(number_list)
print("Tuple of numbers:", number_tuple)