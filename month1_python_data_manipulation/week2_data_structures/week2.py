# ==========================================
# WEEK 2 – DATA STRUCTURES & FUNCTIONS
# ==========================================

# ---- List Operations ----
def list_operations():
    numbers = [10, 20, 30, 40, 50]

    # Sum of squares
    squares = [x**2 for x in numbers]
    print("Squares:", squares)

    # Filter even numbers
    evens = [x for x in numbers if x % 2 == 0]
    print("Even Numbers:", evens)


# ---- Dictionary Operations ----
def dictionary_operations():
    students = {
        "Fatima": 85,
        "Ali": 78,
        "Sara": 92
    }

    for name, marks in students.items():
        print(f"{name}: {marks}")


# ---- Lambda Function Example ----
def lambda_example():
    numbers = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, numbers))
    print("Lambda Squares:", squares)


# ---- Data Cleaning Script (CLIENT PROJECT) ----
def data_cleaning():
    data = [10, 20, 20, 30, None, 40, 40, "", 50]

    # Remove None and empty values
    cleaned = [x for x in data if x not in (None, "")]

    # Remove duplicates
    unique_data = list(set(cleaned))

    # Filter values greater than 20
    filtered = [x for x in unique_data if x > 20]

    print("Original Data:", data)
    print("Cleaned Data:", cleaned)
    print("Unique Data:", unique_data)
    print("Filtered Data (>20):", filtered)


# ---- Main Menu ----
def main():
    print("\n--- WEEK 2 PROGRAM ---")
    print("1. List Operations")
    print("2. Dictionary Operations")
    print("3. Lambda Example")
    print("4. Data Cleaning Script")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        list_operations()
    elif choice == "2":
        dictionary_operations()
    elif choice == "3":
        lambda_example()
    elif choice == "4":
        data_cleaning()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()