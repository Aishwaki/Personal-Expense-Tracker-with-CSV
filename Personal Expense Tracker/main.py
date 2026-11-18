
import csv
from datetime import datetime
import os

FILE_NAME = "expenses.csv"



def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():

    print("\n--- ADD EXPENSE ---")


    while True:

        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD.")

    category = input("Enter category: ").strip()

    while category == "":
        print("Category cannot be empty!")
        category = input("Enter category: ").strip()

    description = input("Enter description: ")

  
    while True:

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                break

        except ValueError:
            print("Please enter a valid amount!")

    # Save expense in CSV
    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([date, category, description, amount])

    print("\nExpense added successfully!")



def view_expenses():

    print("\n--- ALL EXPENSES ---")

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        expenses = list(reader)

    if not expenses:
        print("No expenses found!")
        return

    total = 0

    for expense in expenses:

        print(
            expense["Date"],
            expense["Category"],
            expense["Description"],
            expense["Amount"]
        )

        total += float(expense["Amount"])

    print("\nTotal Expenses:", round(total, 2))



def filter_expenses():

    print("\n--- FILTER EXPENSES ---")

    print("1. Filter by Category")
    print("2. Filter by Date")

    choice = input("Enter choice: ")

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        expenses = list(reader)

    if choice == "1":

        category = input("Enter category: ").strip().lower()

        filtered = [
            e for e in expenses
            if e["Category"].lower() == category
        ]

    elif choice == "2":

        while True:
            date = input("Enter date (YYYY-MM-DD): ")

            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date!")

        filtered = [
            e for e in expenses
            if e["Date"] == date
        ]

    else:
        print("Invalid choice!")
        return

    if not filtered:
        print("No matching expenses found!")
    else:
        for expense in filtered:
            print(expense)



def category_summary():

    print("\n--- CATEGORY SUMMARY ---")

    totals = {}

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for expense in reader:

            category = expense["Category"]

            amount = float(expense["Amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    if not totals:
        print("No expenses available!")
        return

    for category, total in totals.items():

        print(category, ":", round(total, 2))

    print("\nGrand Total:", round(sum(totals.values()), 2))


# 6. MAIN MENU
def main():

    create_file()

    while True:

        print("\n===== PERSONAL EXPENSE TRACKER =====")

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
