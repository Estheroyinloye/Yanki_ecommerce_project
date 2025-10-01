import psycopg2
import csv
def get_db_connection():
    connection = psycopg2.connect(
        host ='localhost',
        database = 'yanki_ecommerce',
        user ='postgres',
        password = 'postgres',

    )
    return connection
connect = get_db_connection()


# customers
def load_csv_file (csv_path):
    connect = get_db_connection()
    cursor = connect.cursor()
    with open (csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            cursor.execute (
                            ''' INSERT INTO yanki.customers (Customer_ID, Customer_Name, Email, Phone_Number)
                            VALUES (%s, %s, %s,%s); 
                            ''',
                            row
                            )
    connect.commit()
    cursor.close()
    connect.close()

csv_file_path = r'datasets\cleaned_data\customer.csv'
load_csv_file (csv_file_path)

#Products
def load_csv_file (csv_path):
    connect = get_db_connection()
    cursor = connect.cursor()
    with open (csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            cursor.execute (
                            ''' INSERT INTO yanki.products (Product_ID, Product_Name, Brand, Category, Price)
                            VALUES (%s, %s, %s,%s, %s); 
                            ''',
                            row
                            )
    connect.commit()
    cursor.close()
    connect.close()

csv_file_path = r'datasets\cleaned_data\product.csv'
load_csv_file (csv_file_path)

#Orders
def load_csv_file (csv_path):
    connect = get_db_connection()
    cursor = connect.cursor()
    with open (csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            cursor.execute (
                            ''' INSERT INTO yanki.orders (Order_ID, Customer_ID, Product_ID, Quantity, Total_Price, Order_Date)
                            VALUES (%s, %s, %s,%s, %s,%s); 
                            ''',
                            row
                            )
    connect.commit()
    cursor.close()
    connect.close()

csv_file_path = r'datasets\cleaned_data\orders.csv'
load_csv_file (csv_file_path)

#Payment
def load_csv_file (csv_path):
    connect = get_db_connection()
    cursor = connect.cursor()
    with open (csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            cursor.execute (
                            ''' INSERT INTO yanki.payment_method (Order_ID, Payment_Method, Transaction_Status)
                            VALUES (%s, %s, %s); 
                            ''',
                            row
                            )
    connect.commit()
    cursor.close()
    connect.close()

csv_file_path = r'datasets\cleaned_data\payment_method.csv'
load_csv_file (csv_file_path)

#Shipping
def load_csv_file (csv_path):
    connect = get_db_connection()
    cursor = connect.cursor()
    with open (csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            cursor.execute (
                            ''' INSERT INTO yanki.shipping (Shipping_ID,Customer_ID,Shipping_Address,City,State,Country,Postal_Code)
                            VALUES (%s, %s, %s,%s,%s,%s, %s); 
                            ''',
                            row
                            )
    connect.commit()
    cursor.close()
    connect.close()

csv_file_path = r'datasets\cleaned_data\shipping.csv'
load_csv_file (csv_file_path)
