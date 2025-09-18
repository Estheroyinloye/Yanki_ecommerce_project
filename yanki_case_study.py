import numpy as np
import pandas as pd
import psycopg2

# yanki_data_df = pd.read_csv('yanki_ecommerce.csv')
# print(yanki_data_df.info())

# # #Data transformation and cleaning
# yanki_data_df.dropna(subset = ['Customer_ID', 'Order_ID'], inplace = True)
# print (yanki_data_df.info())

# # #converting the date from string to date
# yanki_data_df['Order_Date']= pd.to_datetime(yanki_data_df['Order_Date'], format="%d/%m/%Y %H:%M")
# print (yanki_data_df.info())
# print(yanki_data_df.columns)

# #transformaing the data to a normalized form
# customer_df = yanki_data_df[['Customer_ID','Customer_Name','Email', 'Phone_Number']].copy().drop_duplicates().reset_index(drop =True)

# product_df = yanki_data_df[['Product_ID','Product_Name', 'Brand', 'Category', 'Price']].copy().drop_duplicates().reset_index(drop =True)

# shipping_address_df = yanki_data_df[['Customer_ID','Shipping_Address', 'City', 'State', 'Country','Postal_Code',]].copy().drop_duplicates().reset_index(drop =True)
# shipping_address_df.index.name = 'Shipping_ID'
# shipping_address_df = shipping_address_df.reset_index()


# orders_df = yanki_data_df[['Order_ID','Customer_ID','Product_ID','Quantity', 'Total_Price','Order_Date',]].copy().drop_duplicates().reset_index(drop =True)
# payment_method_df = yanki_data_df[['Order_ID','Payment_Method','Transaction_Status']].copy().drop_duplicates().reset_index(drop =True)

# #saving my files
# customer_df.to_csv(r'datasets\cleaned_data\customer.csv')
# product_df.to_csv(r'datasets\cleaned_data\product.csv')
# shipping_address_df.to_csv(r'datasets\cleaned_data\shipping.csv')
# orders_df.to_csv(r'datasets\cleaned_data\orders.csv')
# payment_method_df.to_csv(r'datasets\cleaned_data\payment_method.csv')

# #load the cleaned datasets into postgres

def get_db_connection():
    connection = psycopg2.connect(
        host ='localhost',
        database = 'yanki_ecommerce',
        user ='postgres',
        password = 'postgres'

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
                                    Quamtity INT,
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
    connect.commit()
    cursor.close()
    connect.close