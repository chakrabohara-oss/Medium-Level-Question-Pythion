list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

# Convert lists into sets
set1 = set(list1)
set2 = set(list2)

# Values present in both lists
common = set1 & set2

# Values only in list1
only_list1 = set1 - set2

# Values only in list2
only_list2 = set2 - set1

# Display the results
print("Values present in both lists:", common)
print("Values only in list1:", only_list1)
print("Values only in list2:", only_list2)