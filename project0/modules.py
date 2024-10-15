import csv
import os
from datetime import datetime

class Expense:
    def __init__(self, id, date, amount, category, description=""):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"ID: {self.id}, Date: {self.date}, Amount: {self.amount}, Category: {self.category}, Description: {self.description}"
    
class ExpenseManager:
    def __init__(self):
        if not os.path.exists("expenses.csv"):
            file = open("expenses.csv", mode='w', newline='')
            csv_writer = csv.writer(file)
            csv_writer.writerow(["ID", "Date", "Amount", "Category", "Description"])
            file.close()
            file2 = open("conf.txt", mode='w')
            file2.write("0")
            file2.close()
            print("expenses.csv created")

    def add_expense(self, date=None, amount=0, category="", description=""):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        with open("conf.txt", mode='r') as file:
            last_id = int(file.read().strip())
            next_id = last_id + 1
        
        with open("conf.txt", mode='w') as file:
            file.write(str(next_id))
        
        self.save_to_file(next_id, date, amount, category, description)
        print(f"Expense with ID {next_id} added successfully on {date}!")

    def save_to_file(self, id, date, amount, category, description):
        file = open("expenses.csv", mode='a', newline='')
        csv_writer = csv.writer(file)
        csv_writer.writerow([id, date, amount, category, description])
        file.close()

    def show_all_expenses(self):
        with open("expenses.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            expenses = [row for row in csv_reader]

        headers = expenses[0]
        data = expenses[1:]

        print(f"{headers[0]:<5} {headers[1]:<12} {headers[2]:<10} {headers[3]:<12} {headers[4]:<20}")
        print("-" * 70)

        for row in data:
            print(f"{row[0]:<5} {row[1]:<12} {row[2]:<10} {row[3]:<12} {row[4]:<20}")

    def delete_expense(self, expense_id):
        with open("expenses.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            rows = [row for row in csv_reader]

        headers = rows[0]  # The header row
        data = rows[1:]    # Actual data rows

        filtered_data = [row for row in data if row[0] != str(expense_id)]

        if len(filtered_data) == len(data):
            print(f"No expense found with ID {expense_id}.")
            return

        with open("expenses.csv", mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)
            csv_writer.writerows(filtered_data)

        print(f"Expense with ID {expense_id} deleted successfully!")

    def update_expense(self, expense_id, amount, category, description):
        with open("expenses.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            rows = [row for row in csv_reader]

        headers = rows[0]  # The header row
        data = rows[1:]    # Actual data rows

        for row in data:
            if row[0] == str(expense_id):
                row[2] = amount
                row[3] = category
                row[4] = description
                print(f"Expense with ID {expense_id} updated")
                with open("expenses.csv", mode='w', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(headers)
                    csv_writer.writerows(data)
                return

        print(f"Expense with ID {expense_id} not found")

    def show_total_expense(self):
        with open("expenses.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            rows = [row for row in csv_reader]

        headers = rows[0]  # The header row
        data = rows[1:]    # Actual data rows

        amount = 0
        for row in data:
            amount += int(row[2])

        print(f"Total expenses is {amount}")