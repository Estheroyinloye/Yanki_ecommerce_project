import numpy as np
import pandas as pd

yanki_data_df = pd.read_csv('yanki_ecommerce.csv')
print(yanki_data_df.info())

# #Data transformation and cleaning
yanki_data_df.dropna(subset = ['Customer_ID', 'Order_ID'], inplace = True)
print (yanki_data_df.info())

# #converting the date from string to date
yanki_data_df['Order_Date']= pd.to_datetime(yanki_data_df['Order_Date'], format="%d/%m/%Y %H:%M")
print (yanki_data_df.info())
print(yanki_data_df.columns)

#transformaing the data to a normalized form
customer_df = yanki_data_df[['Customer_ID','Customer_Name','Email', 'Phone_Number']].copy().drop_duplicates().reset_index(drop =True)

product_df = yanki_data_df[['Product_ID','Product_Name', 'Brand', 'Category', 'Price']].copy().drop_duplicates().reset_index(drop =True)

shipping_address_df = yanki_data_df[['Customer_ID','Shipping_Address', 'City', 'State', 'Country','Postal_Code',]].copy().drop_duplicates().reset_index(drop =True)
shipping_address_df.index.name = 'Shipping_ID'
shipping_address_df = shipping_address_df.reset_index()


orders_df = yanki_data_df[['Order_ID','Customer_ID','Product_ID','Quantity', 'Total_Price','Order_Date',]].copy().drop_duplicates().reset_index(drop =True)
payment_method_df = yanki_data_df[['Order_ID','Payment_Method','Transaction_Status']].copy().drop_duplicates().reset_index(drop =True)

#saving my files
customer_df.to_csv(r'datasets\cleaned_data\customer.csv')
product_df.to_csv(r'datasets\cleaned_data\product.csv')
shipping_address_df.to_csv(r'datasets\cleaned_data\shipping.csv')
orders_df.to_csv(r'datasets\cleaned_data\orders.csv')
payment_method_df.to_csv(r'datasets\cleaned_data\payment_method.csv')