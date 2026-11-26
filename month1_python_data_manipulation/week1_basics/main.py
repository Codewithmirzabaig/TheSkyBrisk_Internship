# ==========================================
# WEEK 1 – PYTHON BASICS (STRUCTURED VERSION)
# ==========================================

# ---- Temperature Converter ----
def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", fahrenheit)


# ---- Calculator ----
def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Add:", a + b)
    print("Subtract:", a - b)
    print("Multiply:", a * b)
    print("Divide:", a / b)


# ---- Sum using Loop ----
def sum_numbers():
    total = 0
    for i in range(1, 6):
        total += i
    print("Sum:", total)


# ---- Average Temperature (Client Project) ----
def average_temperature():
    temps = []
    n = int(input("How many temperatures? "))

    for i in range(n):
        t = input("Enter temperature: ")

        if t.replace('.', '', 1).isdigit():
            temps.append(float(t))
        else:
            print("Invalid input, skipping...")

    if len(temps) > 0:
        avg = sum(temps) / len(temps)
        print("Average Temperature:", avg)
    else:
        print("No valid data entered.")


# ---- Main Menu ----
def main():
    print("\n--- WEEK 1 PYTHON PROGRAM ---")
    print("1. Temperature Converter")
    print("2. Calculator")
    print("3. Sum of Numbers")
    print("4. Average Temperature")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        temperature_converter()
    elif choice == "2":
        calculator()
    elif choice == "3":
        sum_numbers()
    elif choice == "4":
        average_temperature()
    else:
        print("Invalid choice")


# Run program
if __name__ == "__main__":
    main()