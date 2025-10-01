import psycopg2
def get_db_connection():
    connection = psycopg2.connect(
        host ='localhost',
        database = 'yanki_ecommerce',
        user ='postgres',
        password = 'postgres',

    )
    return connection
connect = get_db_connection()

# creating the needed tables in postgres
def create_tables():
    connect = get_db_connection()
    cursor = connect.cursor()
    create_table_SQL_query = '''
                                CREATE SCHEMA IF NOT EXISTS yanki;
                                DROP TABLE IF EXISTS yanki.customers CASCADE;
                                DROP TABLE IF EXISTS yanki.products CASCADE;
                                DROP TABLE IF EXISTS yanki.shipping CASCADE;
                                DROP TABLE IF EXISTS yanki.orders CASCADE;
                                DROP TABLE IF EXISTS yanki.payment_method CASCADE;


                                CREATE TABLE IF NOT EXISTS yanki.customers (
                                    Customer_ID UUID PRIMARY KEY,
                                    Customer_Name TEXT,
                                    Email TEXT,
                                    Phone_Number TEXT
                                
                                );


                                 CREATE TABLE IF NOT EXISTS yanki.products (
                                    Product_ID UUID PRIMARY KEY,
                                    Product_Name TEXT,
                                    Brand TEXT,
                                    Category TEXT,
                                    Price FLOAT
                                
                                );

                                CREATE TABLE IF NOT EXISTS yanki.shipping (
                                    Shipping_ID INT PRIMARY KEY,
                                    Customer_ID UUID,
                                    Shipping_Address TEXT,
                                    City TEXT,
                                    State TEXT,
                                    Country TEXT,
                                    Postal_Code INT,

                                    FOREIGN KEY (Customer_ID) REFERENCES yanki.customers(Customer_ID)
                                
                                );
                                

                                CREATE TABLE IF NOT EXISTS yanki.orders (
                                    Order_ID UUID PRIMARY KEY,
                                    Customer_ID UUID,
                                    Product_ID UUID,
                                    Quantity INT,
                                    Total_Price FLOAT,
                                    Order_Date DATE,
                                    
                                    FOREIGN KEY (Customer_ID) REFERENCES yanki.customers (Customer_ID),
                                    FOREIGN KEY (Product_ID) REFERENCES yanki.products (Product_ID)
                                    
                                    );
                                


                                CREATE TABLE IF NOT EXISTS yanki.payment_method (
                                    Order_ID UUID,
                                    Payment_method TEXT,
                                    Transaction_Status TEXT,
                                    FOREIGN KEY (Order_ID) REFERENCES yanki.orders(Order_ID)
                                    );'''

    cursor.execute(create_table_SQL_query)
    cursor.close()
    connect.commit()
    connect.close()

create_tables()