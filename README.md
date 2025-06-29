# 💸 Personal Expense Tracker (Console-Based Python App)

A simple, menu-driven Python application to help you track daily expenses, categorize them, set monthly budgets, and save your data for future use.

---

## 🚀 Features

- ✅ Add new expenses with date, category, amount, and description
- 📋 View expenses in a formatted table (valid & invalid entries separated)
- 💰 Track monthly budget and remaining balance
- 💾 Save expenses to a CSV file
- 🧪 Input validation and user-friendly prompts
- 🧱 Modular design using classes and helper functions

---

## 🧪 How to Run

```bash
git clone https://github.com/sudheergidigi/expense_tracker.git
cd expense_tracker
python main.py

```

---

## 📂 Project Structure
expense_tracker/
├── main.py         # Entrypoint with menu and user interaction
├── tracker.py      # Core class and methods for managing expenses
├── utils.py        # (Optional) for helper functions like budget checks or summaries
├── README.md
└── data/
    └──expenses.csv    # Stores your expense data



---

## 🔧 Getting Started

### 🧪 How to Run

```bash
git clone https://github.com/sudheergidigi/expense_tracker.git
cd expense_tracker
python main.py

```

## 💾 Saving Expenses
Expenses are saved to a CSV file in the /data folder:
    📁 data/expenses.csv
Following are fields:
- date (YYYY-MM-DD)
- category (e.g., Food, Travel)
- amount (float)
- description (text)


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
➡️ Enter your choice from the menu [1–5]: 
----------------------------------------



```
📄 Example Output

📅 Date       | 🏷️ Category  |     💰 Amount | 📝 Description
------------------------------------------------------------
2025-01-01   | Movie        | ₹   1500.00   | Movie with Family
2025-01-02   | Groceries    | ₹   950.00    | Weekly supplies
```

---

🧠 Future Enhancements
- Categorized summaries (pie charts?)
- Export reports with filters by date/month
- User profiles with individual budget
- Filter by date or category
- Add CLI arguments for automation


---

👤 Author
Sudheer Gidigi
- 📍 Bengaluru, India
- 🔗 [GitHub Profile] (https://github.com/sudheergidigi)
- 💬 Passionate about building clean, user-friendly Python applications with a focus on formatting, validation, and modular design.


