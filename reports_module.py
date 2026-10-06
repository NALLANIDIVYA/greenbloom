from db_connection import get_connection


def total_sales():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT SUM(total_amount)
    FROM sales
    """

    cursor.execute(query)

    result = cursor.fetchone()

    total = result[0]

    if total is None:
        total = 0

    print("\n---------- TOTAL SALES ----------")
    print("Total Sales:", total)

    cursor.close()
    connection.close()


def available_stock():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT plant_id, plant_name, category, price, quantity
    FROM plants
    """

    cursor.execute(query)

    plants = cursor.fetchall()

    print("\n---------- AVAILABLE STOCK ----------")

    for plant in plants:
        print(plant)

    cursor.close()
    connection.close()


def low_stock():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT plant_id, plant_name, quantity
    FROM plants
    WHERE quantity < 10
    """

    cursor.execute(query)

    plants = cursor.fetchall()

    print("\n---------- LOW STOCK PLANTS ----------")

    if plants:
        for plant in plants:
            print(plant)
    else:
        print("No low stock plants")

    cursor.close()
    connection.close()


def customer_purchase_history():

    customer_name = input("Enter Customer Name: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT sale_id, customer_name, plant_name,
           quantity, total_amount, sale_date
    FROM sales
    WHERE customer_name = %s
    """

    cursor.execute(query, (customer_name,))

    sales = cursor.fetchall()

    print("\n---------- CUSTOMER PURCHASE HISTORY ----------")

    if sales:
        for sale in sales:
            print(sale)
    else:
        print("No purchase history found")

    cursor.close()
    connection.close()