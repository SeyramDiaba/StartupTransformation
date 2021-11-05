import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
print(financial_data.head())

# Seperate variables for all three columns
month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

# Plot for monthly revenue
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
plt.clf()

# Plot for monthly expenses
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

# load in expenses file
expense_overview = pd.read_csv('expenses.csv')

# Analyse first 7 rows
print(expense_overview.head(7))

# Assigning columns 'Expense' and 'Proportion' variables.
expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

# Collapsing categories less than 5% into a single category 'Others'
expense_categories = ['Salaries','Advertising','Office Rent', 'Other']
proportions = [0.62,0.15,0.15,0.08]

# Pie chart of expenses
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Proportion Of Expenses')
plt.axis('Equal')
plt.tight_layout()
plt.show()

# expense cut suggestion
expense_cut = 'Salaries' 

# load in employees file and analyse first 5 rows
employees = pd.read_csv('employees.csv')
print(employees.head())

# Sort employee productivity column in ascending order
sorted_productivity = employees.sort_values(by= ['Productivity'])
print(sorted_productivity)

# Selecting 100 least productive employees
employees_cut = sorted_productivity.head(100)
print(employees_cut)

# How to explore relationship between 'Income' and 'Productivity' which are on two vastly different scales, moreover there are outliers in the data which add an additional layer of complecity.
transformation = 'standardization'

# Storing commute time column
commute_times = employees['Commute Time']
# Data is skewed to the right, we have to apply log transformation to make the data more symmetrical
commute_times_log = np.log(commute_times)

print(commute_times.describe())
# Working from home will save an average of 33minutes commute time

# Explore shape of commute time using histogram
plt.clf()
plt.hist(commute_times_log)
plt.xlabel('Time')
plt.ylabel('Counts')
plt.title('Employee Commute Time')
plt.show()


