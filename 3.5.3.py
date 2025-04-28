# Student Information
print("Name: Soronnadi Chidiebere Prince")
print("Course: COS 201 Practical")
print("Reg No: 20231410912")
print("Dept: IFT\n")

# 1. Create a set containing 5 different colors
colors = {"red", "blue", "green", "yellow", "purple"}
print("Original set:", colors)

# 2. Add a new color to the set
colors.add("orange")
print("After adding 'orange':", colors)

# 3. Remove one color from the set
colors.remove("blue")
print("After removing 'blue':", colors)

# 4. Create another set of colors and find the union and intersection
other_colors = {"black", "white", "green", "orange"}
print("Other set:", other_colors)

union_set = colors.union(other_colors)
intersection_set = colors.intersection(other_colors)

print("Union of both sets:", union_set)
print("Intersection of both sets:", intersection_set)