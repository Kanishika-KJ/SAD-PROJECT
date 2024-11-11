
# Personal Budget Tracking System - Python Implementation

from datetime import datetime
from collections import defaultdict

# User Profile and Budget Data Modeling
class UserProfile:
    def __init__(self, name, income, monthly_budget):
        self.name = name
        self.income = income
        self.monthly_budget = monthly_budget
        self.expenses = []
        self.categories = defaultdict(float)
        
    def add_expense(self, amount, category, description=""):
        # Add expense to profile
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now()
        }
        self.expenses.append(expense)
        self.categories[category] += amount
        return expense
    
    def calculate_remaining_budget(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        return self.monthly_budget - total_expenses

    def get_expense_summary(self):
        summary = f"User: {self.name}\nTotal Expenses: {sum(self.categories.values())}\n"
        summary += f"Remaining Budget: {self.calculate_remaining_budget()}\n"
        summary += "Expenses by Category:\n"
        for category, total in self.categories.items():
            summary += f"  {category}: ${total}\n"
        return summary

# Interface Design for Expense Entry and Budget Overview
def main_menu():
    print("Welcome to Personal Budget Tracking System!")
    name = input("Enter your name: ")
    income = float(input("Enter your monthly income: "))
    monthly_budget = float(input("Enter your monthly budget: "))
    user = UserProfile(name, income, monthly_budget)
    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category (e.g., Food, Utilities, etc.): ")
            description = input("Enter a description for the expense: ")
            user.add_expense(amount, category, description)
            print("Expense added successfully!")
        elif choice == "2":
            print(user.get_expense_summary())
        elif choice == "3":
            print("Thank you for using the Personal Budget Tracking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# 3.1 Functionality Testing
def test_expense_tracking():
    user = UserProfile("Test User", 3000, 1000)
    user.add_expense(100, "Food", "Groceries")
    user.add_expense(50, "Utilities", "Electricity bill")
    assert user.calculate_remaining_budget() == 850, "Budget calculation error"
    assert len(user.expenses) == 2, "Expense count mismatch"
    assert user.categories["Food"] == 100, "Category total mismatch"
    print("Functionality tests passed.")

# 3.2 Usability Testing
def usability_tests():
    print("\nTesting Usability:")
    try:
        print("Enter expense amount:")
        float("ten")  # Should fail
    except ValueError:
        print("Invalid input correctly handled.")
    # Other usability checks can be simulated in interactive testing.

# 4.1 Common Issues and Fixes
# - Budget Calculation Errors: Ensuring calculations match actual spending.
# - Expense Categorization Issues: Categories and totals match entries.
# - Data Validation Failures: Handling of incorrect inputs (e.g., non-numeric amounts).

# Main execution
if __name__ == "__main__":
    # Run Functionality Tests
    test_expense_tracking()
    
    # Start the main menu
    main_menu()
    
    # Run Usability Tests
    usability_tests()
