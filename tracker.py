import csv
from utils import *


class ExpenseTracker:
    """
    ExpenseTracker is a class for managing and tracking personal expenses against a specified budget.
    It allows users to add, view, and manage expenses, as well as track their budget status.
    
    Features:
        - Add new expense entries with details such as date, category, amount, and description.
        - View all recorded expenses, with separation of valid and invalid records.
        - Track and display the user's monthly budget status, including total spent and remaining budget.
        - Save all expenses to a CSV file for persistent storage.
        - Load expenses from a CSV file to restore previous records.
        expenses (list): A list to store expense records, each as a dictionary.

    Methods:
        - __init__(budget):
        - add_expense():
        Prompts the user to input expense details and adds the entry to the tracker.
        - view_expenses():
        - track_budget():
            Tracks and displays the user's monthly budget status based on recorded expenses.
        - save_to_file(filename="data/expenses.csv"):
        - load_from_file(filename="data/expenses.csv"):
    """

    def __init__(self, budget):
        """
        Initializes the tracker with a specified budget.

        Args:
            budget (float): The total budget for tracking expenses.

        Attributes:
            budget (float): The total budget set for the tracker.
            expenses (list): A list to store expense records.
        """
        self.budget = budget
        self.expenses = []

    def add_expense(self):
        """
        Adds a new expense entry to the expense tracker.

        Prompts the user to input the following details:
        - Date (in YYYY-MM-DD format)
        - Category (e.g., Food, Travel, Utilities)
        - Amount (numeric value in ₹)
        - Description (brief note about the expense)

        The collected data is stored as a dictionary and appended to self.expenses.

        Example Output:
        📅 Date : 2025-06-28 | 🏷️ Category : Food | 💸 Amount : ₹250.00 | 📝 Description : Dinner with friends
        ✅ Expense added successfully!
        """
        print("Enter Your Expense Details Below:")
        date = get_exp_date("Enter The Date(YYYY-MM-DD): ")
        category = input("Enter The Category: ")
        amount = float(input("Enter The Amount (₹): "))
        description = input("Enter The Description: ")
        expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
        self.expenses.append(expense)
        print(f"📅 Date : {date} | 🏷️ Category : {category} | 💸 Amount : ₹{amount:.2f} | 📝 Description : {description}")
        print("✅ Expense added successfully!")


    def view_expenses(self):
        """
        Displays all recorded expenses, separating valid and invalid entries.

        This method performs the following:
        - Checks if any expenses exist; if not, displays a message and exits.
        - Iterates through self.expenses and validates each record by ensuring
        all required fields ('date', 'category', 'amount', 'description') are present and non-empty.
        - Valid records are displayed under a "Valid Expense Records" section.
        - Invalid or incomplete records are displayed separately under an "Invalid Expense Records" section.

        Output:
        - Formatted tables for both valid and invalid records (if any).
        - Friendly messages and visual separators for clarity.

        Assumes:
        - A helper function `print_expenses(expense_list)` exists to format and display the records.
        """
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return

        valid_expenses = []  # For storing validated entries
        invalid_expenses = []  # For storing invalid entries

        for exp in self.expenses:
            # Check that none of the required fields are empty
            if all([
                exp.get('date'),
                exp.get('category'),
                exp.get('amount'),
                exp.get('description')
            ]):
                valid_expenses.append(exp)
            else:
                invalid_expenses.append(exp)

        if valid_expenses:
            print("\n" + "=" * 72)
            print("{:^72}".format("✅ Valid Expense Records"))
            print("=" * 72)
            print("📋 Please find the records list below:\n")
            print_expenses(valid_expenses)

        if invalid_expenses:
            print("\n" + "!" * 72)
            print("{:^72}".format("⚠️  Invalid Expense Records"))
            print("!" * 72)
            print("📋 Please find the records list below:\n")
            print_expenses(invalid_expenses)


    def track_budget(self):
        """
        Tracks and displays the user's monthly budget status.

        Prompts the user to input their monthly budget amount, then calculates:
        - The total amount spent so far (based on self.expenses)
        - The remaining budget (budget - total_spent)

        Displays a formatted summary including:
        - Total spent
        - Monthly budget
        - Remaining budget
        - Budget status (over/under)

        Assumes:
        - self.expenses is a list of dictionaries with a numeric 'amount' key.
        - Each 'amount' value is convertible to float.

        Example Output:
        --------------------------------------------------
        📅 Total Spent So Far     : ₹13500.00
        💰 Monthly Budget         : ₹10000.00
        💸 Remaining Budget       : ₹-3500.00
        ⚠️  Status                : Over Budget by ₹3500.00
        --------------------------------------------------
        """
        budget = float(input("Please Enter Your Monthly 💵 Budget Amount (₹):"))
        total_spent = sum(float(exp['amount']) for exp in self.expenses)
        remaining = budget - total_spent

        print("\n" + "-" * 50)
        print(f"📅 Total Spent So Far     : ₹{total_spent:.2f}")
        print(f"💰 Monthly Budget         : ₹{budget:.2f}")
        print(f"💸 Remaining Budget       : ₹{remaining:.2f}")
        print("-" * 50)

        if remaining < 0.0:
            print(f"⚠️  Status            : Over Budget by ₹{abs(remaining):.2f}")
        else:
            print(f"✅  Status            : ₹{remaining:.2f} remaining")
        print("-" * 50)


    def save_to_file(self, filename="data/expenses.csv"):
        """
        Saves all recorded expenses to a CSV file.

        Parameters:
        - filename (str): The path and name of the file to save the data to.
                        Defaults to 'data/expenses.csv'.

        Functionality:
        - Opens the specified file in write mode.
        - Writes a header row with the fields: 'date', 'category', 'amount', 'description'.
        - Writes each expense record from self.expenses as a row in the CSV file.
        - Displays a confirmation message upon successful save.

        Assumes:
        - self.expenses is a list of dictionaries with the specified keys.
        - The 'csv' module has been imported.

        Example Output:
        💾 Successfully saved the expenses to the file data/expenses.csv...
        """
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(self.expenses)
        print(f"💾 Successfully saved the expenses to the file {filename}...")

    def load_from_file(self, filename="data/expenses.csv"):
        """
        Loads expenses from a CSV file into the expenses list.

        Parameters:
            filename (str): The path to the CSV file containing expenses. Defaults to "data/expenses.csv".

        Behavior:
            - Reads the specified CSV file and loads its contents into self.expenses as a list of dictionaries.
            - Prints a success message if expenses are loaded.
            - Prints a message if no expenses are found in the file.
            - If the file does not exist, prints a message indicating no previous data was found.
        """
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                self.expenses = list(reader)
                if self.expenses:
                    print(f"💾 Successfully loaded the expenses from the file {filename}...")
                else:
                    print(f"No expenses found in the file {filename}.")  
        except FileNotFoundError:
            print(f"No previous data found as configured {filename}.")



    