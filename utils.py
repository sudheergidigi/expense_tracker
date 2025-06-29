from datetime import datetime

def coninue_prompt():
    """
    Prompts the user to decide whether to continue or not.

    Continuously asks the user for input until a valid response ('yes', 'y', 'no', or 'n') is received.
    Returns True if the user chooses to continue ('yes' or 'y'), and False if the user chooses not to continue ('no' or 'n').

    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    while True:
        print("\n" + "-" * 40)
        print("🔁 Do you want to continue? (yes/no)")
        choice = input("👉 Enter Your choice: ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return coninue_prompt()

def get_exp_date(message):
    """
    Prompts the user to input a date in 'YYYY-MM-DD' format and validates the input.

    Args:
        message (str): The prompt message to display to the user.

    Returns:
        str: The validated date as a string in 'YYYY-MM-DD' format.

    Raises:
        None

    Notes:
        - The function will repeatedly prompt the user until a valid date is entered.
        - The entered date must not be in the future.
        - If the input format is incorrect or the date is in the future, an error message is displayed and the user is prompted again.
    """
    while True:
        date_input = input(message)
        try:
            date_obj = datetime.strptime(date_input, "%Y-%m-%d").date()
            if date_obj > datetime.today().date():
                print("❌ The date cannot be in the future. Please enter a valid date.")
                continue
            return str(date_obj)
        except ValueError:
            print("❌ Invalid format. Please enter the date in YYYY-MM-DD format.")

def print_banner():
    """
    Prints a formatted banner for the Personal Expense Tracker application.

    The banner consists of a decorative line, a centered title with emoji, and another decorative line.
    """
    print("=" * 40)
    print("{:^40}".format("💸 Personal Expense Tracker 💸"))
    print("=" * 40)

def print_options(options):
    """
    Prints a formatted list of options with a header and highlights the selected option.

    Args:
        options (Any): The option or list of options to be displayed as the selected choice.
    """
    print("\n" + "-" * 40)
    print(f"✅ The Selected Option is: {options}")

def exit_message():
    """
    Prints a styled exit message to the console, thanking the user for using the Expense Tracker application.
    The message includes decorative formatting and emojis for a friendly user experience.
    """
    print("\033[92m" + "\n" + "*" * 50)
    print("👋💸  Thank you for using the Expense Tracker!")
    print("🙏 Visit Again. Have a great day! 🌞")
    print("*" * 50 + "\033[0m")

def print_expenses(expenses):
    """
    Prints a formatted table of expenses to the console.
    Each expense is displayed with its date, category, amount (in ₹), and description.
    A summary line with the total amount of all expenses is shown at the end.
    Args:
        expenses (list of dict): A list where each dict represents an expense with the following keys:
            - 'date': The date of the expense (str or date object).
            - 'category': The category of the expense (str).
            - 'amount': The amount spent (float or str convertible to float).
            - 'description': A brief description of the expense (str).
    """
    print("\n" + "=" * 72)
    print(f"{'📅 Date':<10} | {'🏷️ Category':<12} | {'💰 Amount':>12} | {'📝 Description':<30}")
    print("-" * 72)

    for exp in expenses:
        print("{:<10} | {:<12} | ₹{:>10.2f} | {:<30}".format(
            str(exp['date']),
            exp['category'],
            float(exp['amount']),
            exp['description']
        ))

    print("-" * 72)
    print("\n📊 Total Expenses Recorded: ₹{:.2f}".format(
                sum(float(exp['amount']) for exp in expenses)
            ))
    print("=" * 72)


