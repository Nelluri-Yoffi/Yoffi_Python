import pandas as pd
customers = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
})

orders = pd.DataFrame({
    'id': [1, 2],
    'customerId': [3, 1]
})

result = customers[~customers['id'].isin(orders['customerId'])][['name']]
result.columns = ['Customers']

print(result)