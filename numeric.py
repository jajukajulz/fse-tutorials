# pip install numpy

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
import numpy as np

# Generate 1,000 samples from a normal distribution
heights = np.random.normal(loc=170, scale=10, size=1000)
weights = np.random.normal(loc=70, scale=15, size=1000)

# Create a correlation between height and weight
weights += (heights - 170) * 0.5
df = pd.DataFrame({'Height': heights, 'Weight': weights})

# Add categorical data
genders = np.random.choice(['Male', 'Female'], size=1000)
df['Gender'] = genders
df.head()
df.describe()
#This could be assets, opening price, bought or sold
