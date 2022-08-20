import csv
import gspread
from re import IGNORECASE, search
import time

def checkCategory(transactionname):
    for item in groceries:
        if search(item, transactionname, IGNORECASE):
            return "Groceries"
    for item in food:
        if search(item, transactionname, IGNORECASE):
            return "Food"
    for item in subscriptions:
        if search(item, transactionname, IGNORECASE):
            return "Subscriptions"
    for item in travel:
        if search(item, transactionname, IGNORECASE):
            return "Travel"
    for item in salary:
        if search(item, transactionname, IGNORECASE):
            return "Salary"
    for item in shopping:
        if search(item, transactionname, IGNORECASE):
            return "Shopping"   

def readCsv(file):
    transactions=[]
    with open(file, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:        
                date = row[0]
                name = row[1]
                if len(row[2]) > 0:
                    transactiontype="Outcome"
                    amount=float(row[2])
                else:
                    transactiontype="Income"
                    amount=float(row[3])
                category = checkCategory(name)
                transaction = (date, name, transactiontype, category, amount)
                transactions.append(transaction)
            return transactions

if __name__ == "__main__":
    monthnumber = input("Insert month number from 1 to 12 - note that the csv must be named bankstatement_(numberofthemonth).csv >>>>> ")
    file = f"bankstatement_{monthnumber}.csv"
    gc = gspread.service_account()
    sh = gc.open("template")
    groceries = sh.worksheet('Tags').col_values(1)
    food = sh.worksheet('Tags').col_values(2)
    subscriptions = sh.worksheet('Tags').col_values(3)
    travel = sh.worksheet('Tags').col_values(4)
    salary = sh.worksheet('Tags').col_values(5)
    shopping = sh.worksheet('Tags').col_values(6)
    transactions = readCsv(file)
    worksheet = sh.worksheet(monthnumber)
    for row in transactions:
        worksheet.append_row(row, table_range="A6")
        time.sleep(2)