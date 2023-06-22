import pandas as pd

# Creating a DataFrame from a dictionary
data = {'SNO':[1,2,3],'Name': ['John', 'Emma', 'David'],
        'Age': [28, 32, 45],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

print(df)

# Create a Series from a list
s = pd.Series([1, 3, 5, 6, 8])
print(s)

# Create a DataFrame from a dictionary
data = {'Name': ['John', 'Emma', 'Tom'],
        'Age': [25, 28, 31],
        'City': ['New York', 'San Francisco', 'London']}
df = pd.DataFrame(data)
print(df)

# View the first 5 rows
print(df.head())

# View the last 3 rows
print(df.tail(3))

# Access the 'Name' column
print(df['Name'])

# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print(filtered_df)

# Add a new column 'Salary'
df['Salary'] = [50000, 60000, 70000]
print(df)

# Summary statistics
print(df.describe())

# Select a single column
print(df['Name'])

# Select multiple columns
print(df[['Name', 'Age']])

# Select a single row by index label
print(df.loc[0])

# Select multiple rows by index label range
print(df.loc[1:3])

# Select a single row by index position
print(df.iloc[0])

# Select multiple rows by index position range
print(df.iloc[1:3])

# Select rows where Age is greater than 25
print(df[df['Age'] > 25])

# Select rows where City is 'New York' and Age is greater than 25
print(df[(df['City'] == 'New York') & (df['Age'] > 25)])

# Check for missing values
print(df.isnull())

# Check for non-missing values
print(df.notnull())

# Drop rows with missing values
df.dropna()

# Drop columns with missing values
df.dropna(axis=1)

# Fill missing values with a specific value
df.fillna(0)


# Interpolate missing values using linear interpolation
df.interpolate()

# Group data by 'City' column and calculate the mean age
grouped_data = df.groupby('City')['Age'].mean()
print(grouped_data)

# Calculate the sum of salaries for each city
sum_salary = df.groupby('City')['Salary'].sum()
print(sum_salary)

# Apply custom aggregation functions
def custom_agg(x):
    return x.max() - x.min()

custom_result = df.groupby('City')['Age'].agg(custom_agg)
print(custom_result)

# Reshaping with pivot()
data = {'Name': ['John', 'Emma', 'Mike'],
        'Subject': ['Math', 'English', 'Science'],
        'Score': [85, 92, 78]}
df = pd.DataFrame(data)

df_pivot = df.pivot(index='Name', columns='Subject', values='Score')
print(df_pivot)

# Creating a pivot table with pivot_table()
df_pivot_table = df.pivot_table(index='Name', columns='Subject', values='Score', aggfunc='mean')
print(df_pivot_table)

# Unstacking with stack() and unstack()
df_stacked = df_pivot.stack()
print(df_stacked)

df_unstacked = df_stacked.unstack()
print(df_unstacked)

# Creating a DataFrame with DateTimeIndex
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 150, 200, 175, 300, 250, 400, 375, 200, 150]}
df = pd.DataFrame(data, index=date_range)
print(df)

# Resampling to monthly frequency
df_monthly = df.resample('M').sum()
print(df_monthly)

# Shifting the data by 1 day
df_shifted = df.shift(1)
print(df_shifted)

# Rolling window calculation (moving average)
rolling_mean = df['Sales'].rolling(window=3).mean()
print(rolling_mean)

# Converting a column to categorical
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
df = pd.DataFrame(data)

df['Category'] = df['Category'].astype('category')
print(df['Category'])

# Counting categorical values
value_counts = df['Category'].value_counts()
print(value_counts)

# Renaming and reordering categories
df['Category'] = df['Category'].cat.rename_categories({'A': 'High', 'B': 'Medium', 'C': 'Low'})
df['Category'] = df['Category'].cat.reorder_categories(['Low', 'Medium', 'High'], ordered=True)
print(df['Category'])




