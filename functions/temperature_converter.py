def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def display_menu():
    print("\nTemperature Converter")
    print("---------------------")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")


display_menu()

choice = input("Enter your choice: ")
temperature = float(input("Enter temperature: "))

if choice == "1":
    result = celsius_to_fahrenheit(temperature)
    print("Fahrenheit:", round(result, 2))

elif choice == "2":
    result = fahrenheit_to_celsius(temperature)
    print("Celsius:", round(result, 2))

elif choice == "3":
    result = celsius_to_kelvin(temperature)
    print("Kelvin:", round(result, 2))

elif choice == "4":
    result = kelvin_to_celsius(temperature)
    print("Celsius:", round(result, 2))

else:
    print("Invalid choice")