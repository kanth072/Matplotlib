import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/sample_data/sales_data (1).csv')
df.head()


#BAR CHART

plt.bar(df['Product'], df['Region'],color='orange')
plt.xlabel('Product')
plt.ylabel('Region')
plt.title('Sales by Product and Region')
plt.show()

#LINE CHART

plt.plot(df['Date'], df['Total_Sales'],color='red',marker='.')
plt.xlabel('Date')
plt.ylabel('Total_Sales')
plt.title('Sales Over Time')
plt.grid()
plt.show()

#HISTOGRAM
plt.hist(df['Total_Sales'], bins=5,color='skyblue')
plt.show()
