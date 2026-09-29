"""
=========================================
Project : Unit Converter
Author  : Rylan Decko
GitHub  : rdecko6917-max
Version : 1.0
=========================================
"""

print("=" * 45)
print("          UNIT CONVERTER")
print("=" * 45)
print("Author  : Rylan Decko")
print("GitHub  : rdecko6917-max")
print("Version : 1.0")
print("=" * 45)

while True:

    print("\n========== MENU ==========")
    print("1. Kilometers ➜ Miles")
    print("2. Miles ➜ Kilometers")
    print("3. Celsius ➜ Fahrenheit")
    print("4. Fahrenheit ➜ Celsius")
    print("5. Kilograms ➜ Pounds")
    print("6. Pounds ➜ Kilograms")
    print("7. Centimeters ➜ Inches")
    print("8. Inches ➜ Centimeters")
    print("9. Meters ➜ Feet")
    print("10. Feet ➜ Meters")
    print("11. Exit")

    choice = input("\nEnter your choice (1-11): ")

    if choice == "11":
        print("\nThank you for using Unit Converter!")
        break

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            result = value * 0.621371
            print(f"\n✅ {value} km = {result:.2f} miles")

        elif choice == "2":
            result = value / 0.621371
            print(f"\n✅ {value} miles = {result:.2f} km")

        elif choice == "3":
            result = (value * 9 / 5) + 32
            print(f"\n✅ {value}°C = {result:.2f}°F")

        elif choice == "4":
            result = (value - 32) * 5 / 9
            print(f"\n✅ {value}°F = {result:.2f}°C")

        elif choice == "5":
            result = value * 2.20462
            print(f"\n✅ {value} kg = {result:.2f} lbs")

        elif choice == "6":
            result = value / 2.20462
            print(f"\n✅ {value} lbs = {result:.2f} kg")

        elif choice == "7":
            result = value / 2.54
            print(f"\n✅ {value} cm = {result:.2f} inches")

        elif choice == "8":
            result = value * 2.54
            print(f"\n✅ {value} inches = {result:.2f} cm")

        elif choice == "9":
            result = value * 3.28084
            print(f"\n✅ {value} meters = {result:.2f} feet")

        elif choice == "10":
            result = value / 3.28084
            print(f"\n✅ {value} feet = {result:.2f} meters")

        else:
            print("\n❌ Invalid choice!")

    except ValueError:
        print("\n❌ Please enter numbers only.")

    again = input("\nConvert another unit? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thank you for using Unit Converter!")
        break