# Author: Eredis Gutierrez
# Date: 08/30/2017
# Description: Calculate company's profits from projected sales 
#              from a fixed annual profit rate of 23%

# Annual Profit Constant (23%)
ANNUAL_PROFIT = 0.23

# User inputs projected sales for the year.
proj_sales = float(input("What's the company's projected sales? "))

# Calculates total profits by multiplying projected sales by annual profit percentage
total_profits = proj_sales * ANNUAL_PROFIT

# Displays company's profit to the user.
print('Projected Profit:', '$', format(total_profits, '.2f'))