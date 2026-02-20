import csv

FILE_NAME = "expenses.csv"


def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])

    print(" Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Description: {row[0]} | Amount: ₹{row[1]}")
    except FileNotFoundError:
        print("No expenses found.")


def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"\n Total Amount Spent: ₹{total}")
    except FileNotFoundError:
        print("No expenses found.")


def menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spent")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("👋 Exiting Expense Tracker")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
