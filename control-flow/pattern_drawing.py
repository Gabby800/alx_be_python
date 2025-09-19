# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print each column in the row
    for col in range(size):
        print("*", end="")  # Print * without new line
    print()  # Move to the next line after finishing one row
    row += 1
