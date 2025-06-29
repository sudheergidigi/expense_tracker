# 💸 Personal Expense Tracker (Console-Based Python App)

A simple, menu-driven Python application to help you track daily expenses, categorize them, set monthly budgets, and save your data for future use.

---

## 🚀 Features

- ✅ Add expense entries with date, category, amount, and description
- 📊 Track your spending against a monthly budget
- 🗂️ Categorize expenses (e.g., Food, Travel, Utilities)
- 💾 Save and load expenses using CSV file handling
- 🖥️ Easy-to-use, interactive menu interface

---

## 📂 Project Structure
expense_tracker/
├── main.py         # Contains menu and user interaction
├── tracker.py      # Core class and methods for managing expenses
├── utils.py        # (Optional) for helper functions like budget checks or summaries
└── data/
    └──expenses.csv    # Stores your expense data



---

## 🔧 Getting Started

1. **Clone this repo** or download the files.
2. Open a terminal and run:

```bash
python main.py
```

======================================
      💸 Personal Expense Tracker 💸
======================================

======================================
   👉 Select from the options below 👇
======================================
1.   Add Expense
2.   View Expenses
3.   Track Budget
4.   Save Expenses
5.   Exit
----------------------------------------
➡️ Enter your choice from the menu [1–5]: 3
----------------------------------------


---
💾 Saving Expenses
Expenses are saved to a CSV file in the /data folder:
    📁 data/expenses.csv
Fields: date, category, amount, description


```
📄 Example Output

📅 Date       | 🏷️ Category  |     💰 Amount | 📝 Description
------------------------------------------------------------
2025-01-01   | Movie        | ₹   1500.00   | Movie with Family
2025-01-02   | Groceries    | ₹   950.00    | Weekly supplies
```

---
🧠 Future Ideas
- Load existing records from file on startup
- Categorized summaries (pie charts?)
- Export reports with filters by date/month
- User profiles with individual budget

