from plant_module import (
    add_plant,
    view_plants,
    update_plant,
    delete_plant,
    search_plant
)

from supplier_module import (
    add_supplier,
    view_suppliers,
    update_supplier,
    delete_supplier
)

from customer_module import (
    add_customer,
    view_customers,
    update_customer,
    delete_customer
)

from billing_module import generate_bill

from reports_module import (
    total_sales,
    available_stock,
    low_stock,
    customer_purchase_history
)


# PLANT MENU
def plant_menu():

    while True:

        print("\n---------- PLANT MENU ----------")
        print("1. Add Plant")
        print("2. View Plants")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("5. Search Plant")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_plant()

        elif choice == "2":
            view_plants()

        elif choice == "3":
            update_plant()

        elif choice == "4":
            delete_plant()

        elif choice == "5":
            search_plant()

        elif choice == "6":
            break

        else:
            print("Invalid choice")


# SUPPLIER MENU
def supplier_menu():

    while True:

        print("\n---------- SUPPLIER MENU ----------")
        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Update Supplier")
        print("4. Delete Supplier")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_supplier()

        elif choice == "2":
            view_suppliers()

        elif choice == "3":
            update_supplier()

        elif choice == "4":
            delete_supplier()

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# CUSTOMER MENU
def customer_menu():

    while True:

        print("\n---------- CUSTOMER MENU ----------")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            update_customer()

        elif choice == "4":
            delete_customer()

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# REPORTS MENU
def reports_menu():

    while True:

        print("\n---------- REPORTS MENU ----------")
        print("1. Total Sales")
        print("2. Available Stock")
        print("3. Low Stock Plants")
        print("4. Customer Purchase History")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            total_sales()

        elif choice == "2":
            available_stock()

        elif choice == "3":
            low_stock()

        elif choice == "4":
            customer_purchase_history()

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# MAIN MENU
def main():

    while True:

        print("\n======================================")
        print("       GREEN BLOOM PLANTS")
        print("   PLANT MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Plant Module")
        print("2. Supplier Module")
        print("3. Customer Module")
        print("4. Billing Module")
        print("5. Reports Module")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            plant_menu()

        elif choice == "2":
            supplier_menu()

        elif choice == "3":
            customer_menu()

        elif choice == "4":
            generate_bill()

        elif choice == "5":
            reports_menu()

        elif choice == "6":
            print("Thank you for using Green Bloom Plants")
            break

        else:
            print("Invalid choice")


# START PROGRAM
main()