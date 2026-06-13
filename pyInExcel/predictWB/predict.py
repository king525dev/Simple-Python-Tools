from sklearn.linear_model import LinearRegression
import numpy as np

# Sales Forcaster
print("\n===== Sales Forecaster =====")

X = np.array([1,2,3,4,5,6]).reshape(-1,1)

y = np.array([
     12000,
     15000,
     18000,
     19000,
     22000,
     24000
])

model = LinearRegression()

model.fit(X, y)

next_month = model.predict([[7]])

print(f'Next Month\'s Revenue: {next_month[0]}');