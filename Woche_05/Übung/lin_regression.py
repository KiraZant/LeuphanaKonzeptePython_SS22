import numpy as np
import pandas as pd


class LinReg:
    """
    Very simple Linear Regression class; does not account for special cases (e.g., (X^T X) is not invertible)
    Fit method: Calculates the linear regression weights [w = (X^T X)^(-1) X^T y]
    Predict method: Uses weights to predict new observations [y = X w]
    """
    def __init__(self):
        self.w = None

    def fit(self, X, y):
        """
        Calculate weights of Linear Regression model
        :param X: NumPy Array of independent variables - not padded with ones
        :param y: NumPy Array of dependent variable
        :return: NumPy Array of calculated weights
        """
        X_adjusted = np.append(np.ones((X.shape[0], 1)), X, axis=1)     # pad X matrix with ones for the intercept
        pseudoinv = np.linalg.inv(np.dot(X_adjusted.T, X_adjusted))     # calculate (X^T X)^(-1)
        self.w = np.dot(np.dot(pseudoinv, X_adjusted.T), y)             # w = (X^T X)^(-1) X^T y
        return self.w

    def predict(self, X):
        """
        Use calculated weights to predict dependent variable
        :param X: NumPy Array of independent variables - not padded with ones
        :return: NumPy Array of predicted y-values
        """
        X_adjusted = np.append(np.ones((X.shape[0], 1)), X, axis=1)     # pad X matrix with ones for the intercept
        return np.dot(X_adjusted, self.w)                               # y_hat = X w


def prepare_data():
    """
    Read data from csv-file and
    :return: NumPy Arrays of independent variables (X) and dependent variable (y) to train and predict
    """
    df = pd.read_csv("Real estate.csv")
    X = df[["X1 transaction date", "X2 house age",
            "X3 distance to the nearest MRT station",
            "X4 number of convenience stores"]].to_numpy()
    y = df["Y house price of unit area"].to_numpy()
    return X[:-10, :], y[:-10], X[-10:, :], y[-10:]


X, y, X_new, y_new = prepare_data()
lr = LinReg()
lr.fit(X, y)
y_hat = lr.predict(X_new)
print(y_hat)

# Using Scikit-Learn's Linear Regression class
from sklearn.linear_model import LinearRegression
lr_sk = LinearRegression()
lr_sk.fit(X, y)
y_hat_sk = lr_sk.predict(X_new)
print(y_hat_sk)
