import pandas as pd
yanki_data = pd.read_csv(r"C:\Users\Admin\Desktop\10Alytics\Yanki_ecommerce_project\yanki_ecommerce.csv" \
"")
yanki_df = pd.DataFrame(yanki_data)
print(yanki_df.head())

yanki_df.info()

###cleaning the data and filling the null values
yanki_df.fillna('Not Provided', inplace = True)
print(yanki_df.info())

#new_yanki_df = yanki_df['Order_Date'] = yanki_df['Order_Date'].astype('datetime64[ns]')

yanki_df ['Order_Date'] = pd.to_datetime(yanki_df['Order_Date'])
print(yanki_df.info())

deduped_yanki_df = yanki_df.drop_duplicates(keep = 'first', inplace = True)
print(yanki_df.info ())

##Faeture engineering
## revenue  column added to the df
new_yanki_df = yanki_df.assign(Revenue = yanki_df['Quantity'] * yanki_df['Price'])
print(new_yanki_df.info())

#### Normalising the data after cleaning.. normalising should be done before cleaning

## Product df
## Customer_df
## Order_df


