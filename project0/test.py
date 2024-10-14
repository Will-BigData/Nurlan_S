import os
import sys
import modules as mgr

print("Hello. I am your personal expense manager.")
while True:
    if not os.path.exists("expenses.csv"):
        print("I did not found your expenses, do you want me to create new file?")
        action=input("Y/N: ")
        if action not in "YNyn" or len(action)!=1:
            print("i don't know how to do this")
            continue
        if action == 'Y' or action == 'y':
            break
        if action == 'N' or action == 'n':
            print("Put your expenses.csv to path and start again. Bye-bye.")
            sys.exit(1)
    else:
        break

manager = mgr.ExpenseManager()
manager.add_expense(None, 5, "some category", "added automaticaly for test")
manager.add_expense(None, 5, "some category", "added automaticaly for test")
manager.add_expense(None, 5, "some category", "added automaticaly for test")
manager.add_expense(None, 5, "some category", "added automaticaly for test")

while True:
    print("What do you want to do?")
    print("A: add expense")
    print("D: delete expense")
    print("S: Show all expenses")
    print("U: Update expense")
    print("T: Show total expenses")
    print("E: Exit")

    action=input("Input: ")
    if action not in "ADSUTEadsute" or len(action)!=1:
        print("I don't know how to do this")
        continue
    if action == 'A' or action == 'a':
        try:
            print("Enter expense Amount")
            action=input("Input: ")
            amount = int(action)
            print("Enter expense Category")
            action=input("Input: ")
            category = action
            print("Enter expense Description")
            action=input("Input: ")
            description = action
            manager.add_expense(None, amount, category, description)
        except ValueError:
            print("Invalid input.")
    elif action == 'D' or action == 'd':
        print("Enter expense ID")
        action=input("Input: ")
        try:
            expense_id = int(action)
            manager.delete_expense(expense_id)
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
    elif action == 'S' or action == 's':
        manager.show_all_expenses()
    elif action == 'U' or action == 'u':
        try:
            print("Enter expense ID")
            action=input("Input: ")
            id = int(action)
            print("Enter expense Amount")
            action=input("Input: ")
            amount = int(action)
            print("Enter expense Category")
            action=input("Input: ")
            category = action
            print("Enter expense Description")
            action=input("Input: ")
            description = action
            manager.update_expense(id, amount, category, description)
        except ValueError:
            print("Invalid input.")
    elif action == 'T' or action == 't':
        manager.show_total_expense()
    elif action == 'E' or action == 'e':
        print("Bye-bye.")
        sys.exit(1)
    print("-"*10)