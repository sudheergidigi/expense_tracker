from tracker import ExpenseTracker
from utils import *

def display_menu():
    """
    Displays a formatted menu of options for the expense tracker application and prompts the user to select an option.
    Returns:
        str: The user's menu choice as a string.
    """
    print("\n" + "=" * 40)
    print("{:^40}".format("👉 Select from the options below 👇"))
    print("=" * 40)

    print("{:<5}{}".format("1.", "Add Expense"))
    print("{:<5}{}".format("2.", "View Expenses"))
    print("{:<5}{}".format("3.", "Track Budget"))
    print("{:<5}{}".format("4.", "Save Expenses"))
    print("{:<5}{}".format("5.", "Exit"))
    print("-" * 40)
    choice = input("➡️ Enter your choice from the menu [1–5]: ")
    print("-" * 40)
    return choice

def menu():
    """
    Displays the main menu for the expense tracker application and handles user interaction.
    This function initializes an ExpenseTracker instance, loads existing expenses from a file,
    and presents a menu to the user with options to add expenses, view expenses, track the budget,
    save expenses, or exit the application. The function processes user input, calls the appropriate
    methods on the ExpenseTracker instance, and manages the application flow, including saving data
    and displaying exit messages.
    Returns:
        None
    """
    tracker = ExpenseTracker(budget=50000)
    tracker.load_from_file()

    print_banner()
    while True:
        choice = display_menu()
        if choice == '1':
            print_options("1. Add Expense")
            tracker.add_expense()
        elif choice == '2':
            print_options("2. View Expenses")
            tracker.view_expenses()
        elif choice == '3':
            print_options("3. Track Budget")
            tracker.track_budget()
        elif choice == '4':
            print_options("4. Save Expenses")
            tracker.save_to_file()
        elif choice == '5':
            print_options("5. Exit")
            tracker.save_to_file()
            exit_message()
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
        if(coninue_prompt()) :
            continue
        else:
            exit_message()
            break

#Main
if __name__ == "__main__":
    menu()