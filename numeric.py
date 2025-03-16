# pip install numpy
# pip install pandas
# pip install openpyxl
# pip install matplotlib

import numpy as np

# Creating a 1D array
x = np.array([1, 2, 3])

# Creating a 2D array
y = np.array([[1, 2], [3, 4]])

# Creating a 3D array
z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(x)
print(y)
print(z)

#indexing
print("Single element access:", x[2])
print("Single element access, negative index:", x[-2])
print("2D array access:", y[1, 0])
print("3D array access:", z[1, 0, 0])
print("3D array access:", z[1, 1, 1])


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Addition
add = x + y  
print("Addition:",add)

# Subtraction
subtract = x - y 
print("substration:", subtract)

# Multiplication
multiply = x * y 
print("multiplication:", multiply)

# Division
divide = x / y  
print("division:", divide)

# Example array with both positive and negative values
arr = np.array([-3, -1, 0, 1, 3])

# Applying a unary operation: absolute value
result = np.absolute(arr)
print("Absolute value:", result)

# Example list with both positive and negative values 
example_list = [-3, -1, 0, 1, 3]
abs_list = []
for x in example_list:
    abs_list.append(abs(x))
print(abs_list)

# simulate rolling a die 10 times. Assume that our die is fair
# i.e. the probability for each face is equal to 1/6. 
import random
outcome = [ random.randint(1, 6) for _ in range(10) ]
print(outcome)

# using numpy
outcome = np.random.randint(1, 7, size=10)
print(outcome)

# Sample financial data
financial_data = [100, 120, 150, 130, 110, 90, 80, 95, 105, 125]

# Calculate mean, median, and standard deviation
mean_value = np.mean(financial_data)
median_value = np.median(financial_data)
std_deviation = np.std(financial_data)

# Print results
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation:.2f}")

import numpy as np

# Sample stock returns data
stock_returns = [0.02, 0.03, -0.01, 0.05, -0.02, 0.01, -0.03, 0.04, 0.02, -0.01]

# Calculate mean, median, standard deviation, percentiles, variance, and correlation
mean_return = np.mean(stock_returns)
median_return = np.median(stock_returns)
std_dev_return = np.std(stock_returns)
percentile_25 = np.percentile(stock_returns, 25)
variance_return = np.var(stock_returns)
correlation_matrix = np.corrcoef(stock_returns, stock_returns[::-1])  # Creating a correlation matrix

# Print results
print(f"Mean Return: {mean_return:.4f}")
print(f"Median Return: {median_return:.4f}")
print(f"Standard Deviation of Returns: {std_dev_return:.4f}")
print(f"25th Percentile: {percentile_25:.4f}")
print(f"Variance of Returns: {variance_return:.4f}")
print(f"Correlation Matrix:\n{correlation_matrix}")

import pandas as pd
print(pd.__version__)  # prints the pandas version

import numpy as np

# Generate 1,000 sample trades from a normal distribution
price_open = np.random.normal(loc=170, scale=10, size=1000)
price_close = np.random.normal(loc=175, scale=15, size=1000)

# create a dataframe
df = pd.DataFrame({'Opening Price': price_open, 'Closing Price': price_close})

# Add categorical data
action = np.random.choice(['Buy', 'Sell'], size=1000)
df['Trade Action'] = action
df.head()
df.describe()


# A pandas DataFrame (here we are using df) is saved as a CSV file using the .to_csv() method. 
# The arguments include the filename with path and index – where index = True implies writing 
# the DataFrame’s index.
df.to_csv("synthetic_asset_prices.csv", index=False)

# read csv file
df = pd.read_csv("synthetic_asset_prices.csv")
df.head()
df.describe()

# MS Excel
# df.to_excel("synthetic_asset_prices.xlsx")
# df = pd.read_excel('synthetic_asset_prices.xlsx')

# Extracting the second sheet since Python uses 0-indexing
# df = pd.read_excel('synthetic_asset_prices.xlsx', sheet_name=1)


# read data from an API
# df = pd.read_json("https://api.example.com/data.json")



import sqlite3

# Establish a connection to an SQLite database
conn = sqlite3.connect("fintechdb.db")

# Read data from a table
df2 = pd.read_sql("SELECT * FROM fse", conn)
df2.head()
df2.describe()


import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show()
