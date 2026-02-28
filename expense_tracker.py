from datetime import datetime

def menu():
    print("\n==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Exit")


def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{amount},{category},{description}\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

            if not expenses:
                print("No expenses found.")
                return

            print("\nAll Expenses:")
            for index, line in enumerate(expenses, start=1):
                date, amount, category, description = line.strip().split(",")
                print(f"{index}. {date} | ₹{amount} | {category} | {description}")

    except FileNotFoundError:
        print("No expenses found.")


def view_total():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                _, amount, _, _ = line.strip().split(",")
                total += float(amount)

        print(f"Total Expense: ₹{total}")

    except FileNotFoundError:
        print("No expenses found.")


def filter_category():
    category_input = input("Enter category to filter: ")
    found = False

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, amount, category, description = line.strip().split(",")

                if category.lower() == category_input.lower():
                    print(f"{date} | ₹{amount} | {category} | {description}")
                    found = True

        if not found:
            print("No matching category found.")

    except FileNotFoundError:
        print("No expenses found.")


def delete_expense():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses to delete.")
            return

        print("\nSelect expense number to delete:")
        for index, line in enumerate(expenses, start=1):
            date, amount, category, description = line.strip().split(",")
            print(f"{index}. {date} | ₹{amount} | {category} | {description}")

        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            expenses.pop(choice - 1)

            with open("expenses.txt", "w") as file:
                file.writelines(expenses)

            print("Expense deleted successfully.")
        else:
            print("Invalid choice.")

    except FileNotFoundError:
        print("No expenses found.")
    except ValueError:
        print("Invalid input.")


# 🔁 MAIN LOOP
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total()
    elif choice == "4":
        filter_category()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
