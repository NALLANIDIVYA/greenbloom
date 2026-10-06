from db_connection import get_connection


# ADD PLANT
def add_plant():

    plant_id = int(input("Enter Plant ID: "))
    plant_name = input("Enter Plant Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    supplier_name = input("Enter Supplier Name: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO plants
    (plant_id, plant_name, category, price, quantity, supplier_name)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        plant_id,
        plant_name,
        category,
        price,
        quantity,
        supplier_name
    )

    cursor.execute(query, values)
    connection.commit()

    print("Plant added successfully")

    cursor.close()
    connection.close()


# VIEW PLANTS
def view_plants():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM plants")

    plants = cursor.fetchall()

    print("\n---------- PLANT DETAILS ----------")

    if plants:
        for plant in plants:
            print(plant)
    else:
        print("No plants found")

    cursor.close()
    connection.close()


# UPDATE PLANT
def update_plant():

    plant_id = int(input("Enter Plant ID to update: "))
    quantity = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE plants
    SET quantity = %s,
        price = %s
    WHERE plant_id = %s
    """

    values = (quantity, price, plant_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Plant updated successfully")
    else:
        print("Plant not found")

    cursor.close()
    connection.close()


# DELETE PLANT
def delete_plant():

    plant_id = int(input("Enter Plant ID to delete: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM plants WHERE plant_id = %s"

    cursor.execute(query, (plant_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Plant deleted successfully")
    else:
        print("Plant not found")

    cursor.close()
    connection.close()


# SEARCH PLANT
def search_plant():

    plant_name = input("Enter Plant Name to search: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT * FROM plants
    WHERE plant_name LIKE %s
    """

    cursor.execute(query, ("%" + plant_name + "%",))

    plants = cursor.fetchall()

    print("\n---------- SEARCH RESULTS ----------")

    if plants:
        for plant in plants:
            print(plant)
    else:
        print("Plant not found")

    cursor.close()
    connection.close()