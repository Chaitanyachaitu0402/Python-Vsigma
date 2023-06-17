import pandas as pd

# Creating a DataFrame from a dictionary
data = {'SNO':[1,2,3],'Name': ['John', 'Emma', 'David'],
        'Age': [28, 32, 45],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

print(df)
