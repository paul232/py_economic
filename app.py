import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file_path = './input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

print(melbourne_data.columns)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

y = melbourne_data.Price
X = melbourne_data[melbourne_features]

melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)

print(X.describe())

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))