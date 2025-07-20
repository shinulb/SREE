# import pandas as pd

# # Sample data
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', None],
#     'Age': [25, 30, None, 25, 30, 40],
#     'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance'],
#     'Salary': [50000, 60000, 55000, 52000, None, 58000]
# }

# df = pd.DataFrame(data)
# print("Original DataFrame:\n", df)

import pandas as pd
import numpy as np
# 1. Create DataFrame
data = {
 'EmployeeID': [101, 102, 103, 104],
 'Name': ['Alice', 'Bob', 'Charlie', 'David'],
 'Age': [25, 30, np.nan, 45],
 'Department': ['HR', 'IT', 'IT', 'Finance'],
 'Salary': [50000, 60000, 55000, None],
 'JoiningDate': ['2020-01-15', '2019-07-23', '2021-03-01', '2018-11-12'],
 'Gender': ['F', 'M', 'M', 'M']
}
df = pd.DataFrame(data)
# 2. Data Overview
print("\n--- Head ---\n", df.head())
print("\n--- Info ---")
df.info()
print("\n--- Describe ---\n", df.describe())
# 3. Data Cleaning
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# 4. Column Selection
print("\n--- Names Column ---\n", df['Name'])
# 5. Row Selection
print("\n--- First Row (loc) ---\n", df.loc[0])
print("\n--- First Row (iloc) ---\n", df.iloc[0])
print("\n--- test Row (iloc) ---\n",df.iloc[1, 0])
# 6. Filter Data
print("\n--- Employees Older Than 30 ---\n", df[df['Age'] > 30])
# 7. Add New Column
df['Tax'] = df['Salary'] * 0.1
# 8. Apply Function
df['AgeGroup'] = df['Age'].apply(lambda x: 'Senior' if x > 35 else 'Junior')
# 9. Convert Dates
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

print("\n--- Head ---\n", df.head())

df['YearJoined'] = df['JoiningDate'].dt.year
# 10. Grouping and Aggregation
print("\n--- Average Salary per Department ---\n", df.groupby('Department')['Salary'].mean())
# 11. Sorting
print("\n--- Sorted by Age ---\n", df.sort_values('Age'))
# 12. Pivot Table
pivot = df.pivot_table(index='Department', values='Salary', aggfunc='mean')
print("\n--- Pivot Table ---\n", pivot)
# 13. Crosstab
cross = pd.crosstab(df['Gender'], df['Department'])
print("\n--- Crosstab ---\n", cross)
# 14. Merging Example
extra = pd.DataFrame({
 'EmployeeID': [101, 102, 103, 104],
 'Bonus': [5000, 7000, 6000, 4000]
})
df = pd.merge(df, extra, on='EmployeeID', how='left')
# 15. Export to CSV (won't actually save in this environment)
# df.to_csv('final_employee_data.csv', index=False)
# 16. Final Output
print("\n--- Final DataFrame ---\n", df)