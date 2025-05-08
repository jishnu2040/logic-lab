import copy

original_list = [1, 2, 3, [4, 5, 6], 7]
deep = copy.deepcopy(original_list)

deep[3][0] = 100

print("Original List:", original_list)  # Original List
print("Deep Copied List:", deep)  # Deep Copied List