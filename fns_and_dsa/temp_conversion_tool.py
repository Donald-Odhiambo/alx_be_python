# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt for temperature
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        # Raise error for non-numeric input
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit type
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Conversion based on unit
    if unit == "C":
        converted = convert_to_fahrenheit(temp)
        print(f"{temp:.2f}°C is {converted:.2f}°F")
    elif unit == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp:.2f}°F is {converted:.2f}°C")
    else:
        # Handle invalid unit entry
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
