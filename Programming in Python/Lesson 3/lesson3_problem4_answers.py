# Practice Exercise  4: Create a Multiplication Table

def multiplication_table():
    # Iterate from 1 to 10 (inclusive) for the rows
    for i in range(1, 11):
        # Initialize an empty string to store the row
        row = ""
        # Iterate from 1 to 10 (inclusive) for the columns
        for j in range(1, 11):
            # Calculate the product of the current row and column
            product = i * j
            # Append the product to the row string, separated by a space
            row += f"{product:4}"  # Adjust spacing for neat formatting
        # Print the row after each inner loop completes
        print(row)

# Call the function to generate the multiplication table
multiplication_table()
