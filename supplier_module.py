from db_connection import get_connection


def add_supplier():

    supplier_id = input("Enter Supplier ID: ")
    supplier_name = input("Enter Supplier Name: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO suppliers
    (supplier_id, supplier_name, phone, city)
    VALUES (%s, %s, %s, %s)
    """

    values = (supplier_id, supplier_name, phone, city)

    cursor.execute(query, values)
    connection.commit()

    print("Supplier added successfully")

    cursor.close()
    connection.close()


def view_suppliers():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM suppliers")

    suppliers = cursor.fetchall()

    print("\n---------- SUPPLIER DETAILS ----------")

    for supplier in suppliers:
        print(supplier)

    cursor.close()
    connection.close()


def update_supplier():

    supplier_id = input("Enter Supplier ID to update: ")
    phone = input("Enter new Phone Number: ")
    city = input("Enter new City: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE suppliers
    SET phone = %s, city = %s
    WHERE supplier_id = %s
    """

    values = (phone, city, supplier_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Supplier updated successfully")
    else:
        print("Supplier not found")

    cursor.close()
    connection.close()


def delete_supplier():

    supplier_id = input("Enter Supplier ID to delete: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM suppliers WHERE supplier_id = %s"

    cursor.execute(query, (supplier_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Supplier deleted successfully")
    else:
        print("Supplier not found")

    cursor.close()
    connection.close()