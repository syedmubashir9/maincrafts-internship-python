import csv
import os
from datetime import datetime

FILE = "expenses.csv"


# Create file if not exists
def initialize():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Date", "Description", "Amount", "Category"])


# Generate auto ID
def generate_id():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        ids = [int(row[0]) for row in reader]

    return max(ids, default=0) + 1


# Add Expense
def add_expense():

    desc = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))
    except:
        print("Invalid amount")
        return

    category = input("Enter Category: ")

    if category == "":
        print("Category cannot be empty")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    id = generate_id()

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, date, desc, amount, category])

    print("Expense added successfully")


# View All
def view_all():

    total = 0
    count = 0

    print("\nID | Date | Description | Amount | Category")

    with open(FILE, "r") as f:

        reader = csv.reader(f)
        next(reader)

        for row in reader:

            print(row[0], row[1], row[2], row[3], row[4])

            total += float(row[3])

            count += 1

    print("\nTotal Entries:", count)

    print("Total Amount:", total)


# Search Category
def search_category():

    cat = input("Enter category: ").lower()

    total = 0

    with open(FILE, "r") as f:

        reader = csv.reader(f)
        next(reader)

        for row in reader:

            if row[4].lower() == cat:

                print(row)

                total += float(row[3])

    print("Category Total:", total)


# Monthly Total
def monthly_total():

    month = input("Enter month YYYY-MM: ")

    total = 0

    with open(FILE, "r") as f:

        reader = csv.reader(f)
        next(reader)

        for row in reader:

            if row[1].startswith(month):

                total += float(row[3])

    print("Monthly Total:", total)


# Delete by ID
def delete_expense():

    delete_id = input("Enter ID to delete: ")

    rows = []

    with open(FILE, "r") as f:

        reader = csv.reader(f)

        rows = list(reader)

    with open(FILE, "w", newline="") as f:

        writer = csv.writer(f)

        for row in rows:

            if row[0] != delete_id:

                writer.writerow(row)

    print("Deleted successfully")


# Menu
def menu():

    print("\n===== Expense Tracker =====")

    print("1 Add Expense")

    print("2 View All")

    print("3 Search Category")

    print("4 Monthly Total")

    print("5 Delete by ID")

    print("6 Exit")


# Main Loop
def main():

    initialize()

    while True:

        menu()

        choice = input("Enter choice: ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_all()

        elif choice == "3":

            search_category()

        elif choice == "4":

            monthly_total()

        elif choice == "5":

            delete_expense()

        elif choice == "6":

            break

        else:

            print("Invalid choice")


main()