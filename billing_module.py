from db_connection import get_connection


def generate_bill():

    customer_name = input("Enter Customer Name: ")
    plant_name = input("Enter Plant Name: ")
    quantity = int(input("Enter Quantity: "))

    connection = get_connection()
    cursor = connection.cursor()

    # Get plant details
    query = """
    SELECT price, quantity
    FROM plants
    WHERE plant_name = %s
    """

    cursor.execute(query, (plant_name,))
    plant = cursor.fetchone()

    if plant is None:
        print("Plant not found")
        cursor.close()
        connection.close()
        return

    price = plant[0]
    available_quantity = plant[1]

    # Check stock
    if quantity > available_quantity:
        print("Not enough stock available")
        cursor.close()
        connection.close()
        return

    # Calculate total
    total_amount = price * quantity

    print("\n---------- BILL ----------")
    print("Customer:", customer_name)
    print("Plant:", plant_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Amount:", total_amount)

    # Save sale
    query = """
    INSERT INTO sales
    (customer_name, plant_name, quantity, total_amount, sale_date)
    VALUES (%s, %s, %s, %s, CURDATE())
    """

    values = (
        customer_name,
        plant_name,
        quantity,
        total_amount
    )

    cursor.execute(query, values)

    # Reduce stock
    new_quantity = available_quantity - quantity

    query = """
    UPDATE plants
    SET quantity = %s
    WHERE plant_name = %s
    """

    cursor.execute(query, (new_quantity, plant_name))

    connection.commit()

    print("--------------------------")
    print("Bill generated successfully")
    print("Stock updated successfully")

    cursor.close()
    connection.close()