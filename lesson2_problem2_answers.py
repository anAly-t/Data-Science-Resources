# Practice Assignment 2: Temperature Converter
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Main function for the temperature converter
def temperature_converter():
    # Display the options for temperature conversion
    print("\nTemperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    # Get user choice
    choice = input("Enter your choice (1 or 2): ")

    # Check user's choice and perform the corresponding temperature conversion
    if choice == '1':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")

    elif choice == '2':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is {celsius} Celsius.")

    else:
        # Handle invalid choices
        print("Invalid choice. Please enter 1 or 2.")

# Run the temperature_converter function when the script is executed
if __name__ == "__main__":
    temperature_converter()
