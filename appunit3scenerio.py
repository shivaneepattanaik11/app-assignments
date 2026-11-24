
import csv
import re

# Create CSV file
file = open("customers.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["AccountNumber", "Name", "Balance"])
writer.writerow(["1234567890", "Rahul", "25000"])
writer.writerow(["2345678901", "Priya", "35000"])
writer.writerow(["3456789012", "Amit", "40000"])
writer.writerow(["4567890123", "Sneha", "50000"])

file.close()

print("CSV File Created Successfully!")

# Display all customers
def display():
    file = open("customers.csv", "r")
    reader = csv.reader(file)

    print("\nCustomer Details:")
    for row in reader:
        print(row)

    file.close()

# Search customer
def search():
    acc = input("Enter Account Number: ")

    if not re.match(r'^\d{10}$', acc):
        print("Invalid Account Number!")
        return

    file = open("customers.csv", "r")
    reader = csv.reader(file)

    found = False

    for row in reader:
        if row[0] == acc:
            print("\nCustomer Found!")
            print("Account Number:", row[0])
            print("Name:", row[1])
            print("Balance:", row[2])
            found = True
            break

    if not found:
        print("Customer Not Found!")

    file.close()

# Main menu
while True:
    print("\n1. Display Customers")
    print("2. Search Customer")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        display()

    elif choice == '2':
        search()

    elif choice == '3':
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")


# question 10:

import csv
import sys

# Create CSV file
file = open("sports.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["EquipmentID", "Name", "Quantity", "Price"])
writer.writerow(["101", "Cricket Bat", "10", "1500"])
writer.writerow(["102", "Football", "15", "800"])
writer.writerow(["103", "Badminton Racket", "20", "1200"])
writer.writerow(["104", "Basketball", "12", "1000"])

file.close()

print("CSV File Created Successfully!")

# Accept filename using command line
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "sports.csv"

# Display all equipment
def display():
    file = open(filename, "r")
    reader = csv.reader(file)

    print("\nSports Equipment Details:")
    for row in reader:
        print(row)

    file.close()

# Search equipment by ID
def search():
    eid = input("Enter Equipment ID: ")

    file = open(filename, "r")
    reader = csv.reader(file)

    found = False

    for row in reader:
        if row[0] == eid:
            print("\nEquipment Found!")
            print("Equipment ID:", row[0])
            print("Name:", row[1])
            print("Quantity:", row[2])
            print("Price:", row[3])
            found = True
            break

    if not found:
        print("Equipment Not Found!")

    file.close()

# Main menu
while True:
    print("\n1. Display Equipment")
    print("2. Search Equipment")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        display()

    elif choice == '2':
        search()

    elif choice == '3':
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
