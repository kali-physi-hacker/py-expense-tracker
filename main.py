import csv 

project_name = "Ky Expense Tracker"

underline = "======================================="


def display_menu():
    print("Select your option")
    print("1. Add an expense")
    print("2. View Expenses")
    print("3. Update Expenses")
    print("4. View Summary of Expenses")
    print("0. Exit Application")
    # ...


def add_expenses(file):
    print(underline)
    print("Adding Expenses")
    print(underline)
    title = input("What should I call this expense? ==>")
    amount = input("What is the amount (GH¢)? ==>")
    description = input("Enter some description (optional) ==>")

    print("Title:\t", title)
    print("Amount:\t", amount)
    print("description:\t", description)

    yes_or_no = input("Confirm you want to add this expense: yes(y)/no(n) ==>")
    
    if yes_or_no == "yes" or "YES" or "y" or "Y":
        print("Persisting to db...")
        # add to the csv file
        writer = csv.writer(file)
        writer.writerow([title, amount, description])
        print("Added to db")
        print(underline)
    else:
        print("Aborted...")


def main():
    print(underline)
    print(project_name)
    print(underline)
    display_menu()
    print(underline)

    # check if file exists, 
    # if file exists --> open in write mode 
    # else open in append mode
    file = open("expenses.csv", "w")

    choice = -1
    while choice != 0:
        choice = int(input("What do you want to do: "))
        print("You want to do choice:", choice)

        # Conditions ===> if, elif, else
        if choice == 1:
            add_expenses(file)

if __name__ == "__main__":
    main()


