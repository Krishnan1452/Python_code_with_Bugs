import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
def generate_data():
    X = np.random.rand(100, 1) * 10 
    y = 3 * X + np.random.rand(100, 1) 
    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_stat=42) 

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_trian, y_train) 
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = np.mean((predictions - y_test) ** 2)
    print("Mean Squared Error:", mse)

# Main script
X, y = generate_data()
X_train, X_test, y_train, y_test = split_data(X, y)
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test)
