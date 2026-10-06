from db_connection import get_connection


def add_customer():

    customer_id = int(input("Enter Customer ID: "))
    customer_name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO customers
    (customer_id, customer_name, phone, city)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        customer_id,
        customer_name,
        phone,
        city
    )

    cursor.execute(query, values)
    connection.commit()

    print("Customer added successfully")

    cursor.close()
    connection.close()


def view_customers():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    print("\n---------- CUSTOMER DETAILS ----------")

    for customer in customers:
        print(customer)

    cursor.close()
    connection.close()


def update_customer():

    customer_id = int(input("Enter Customer ID to update: "))
    phone = input("Enter new Phone Number: ")
    city = input("Enter new City: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE customers
    SET phone = %s, city = %s
    WHERE customer_id = %s
    """

    values = (phone, city, customer_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Customer updated successfully")
    else:
        print("Customer not found")

    cursor.close()
    connection.close()


def delete_customer():

    customer_id = int(input("Enter Customer ID to delete: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM customers WHERE customer_id = %s"

    cursor.execute(query, (customer_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Customer deleted successfully")
    else:
        print("Customer not found")

    cursor.close()
    connection.close()