import numpy as np
days = np.arange(1, 11)  #numpy.arange() function creates an array of evenly spaced values within a given interval.

units_sold = np.array([
    5, 20, 15, 3, 25,
    18, 7, 30, 20, 4
])

price = np.array([
    60000, 800, 1500, 60000, 800,
    1500, 60000, 800, 1500, 60000
])

products = np.array([
    "Laptop",
    "Mouse",
    "Keyboard",
    "Laptop",
    "Mouse",
    "Keyboard",
    "Laptop",
    "Mouse",
    "Keyboard",
    "Laptop"
])

#This is called Vectorization - Vectorization in NumPy refers to applying operations on entire arrays without using explicit loops
#Revenue for each day is:
revenue = units_sold * price
print(revenue)

#Total Units Sold
total_units = np.sum(units_sold)
print(total_units)

#Total Revenue
total_revenue = np.sum(revenue) #Aggregation function.
print(total_revenue)

#Average Daily Revenue
averageDailyRevenue = np.mean(revenue) #Aggregation function.
print(averageDailyRevenue)

#Highest Revenue Day
highest_index = np.argmax(revenue)
print(highest_index)

#Find Days With Revenue > ₹50,000
high_revenue = revenue > 50000
print(high_revenue) #[ True False False  True False False  True False False  True]
print(days[high_revenue]) # [ 1  4  7 10]

#Find the Most Sold Product
unique_products = np.unique(products) #gives list of unique produts
print(unique_products)

#Total quantity sold per product
mostSoldProduct = []
for product in unique_products:
    total = np.sum(units_sold[products == product])
    mostSoldProduct.append(total)
    print(product, total)

mostSoldProduct = np.array(mostSoldProduct)
print(np.max(mostSoldProduct))