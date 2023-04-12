# Declare and initialize the list
myNumbers = [5, 8, 12, 15, 10, 20, 3]

# Iterate through the list and print each element
print("List of numbers")
print(myNumbers)
# Find and print the elements greater than 5
greaterThan5 = []
for num in myNumbers:
    if num > 5:
        greaterThan5.append(num)

print("Numbers greater than 5:", greaterThan5)
