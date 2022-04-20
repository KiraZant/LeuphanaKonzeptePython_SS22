"""
This code demonstrates the use of Pandas apply method
"""
import pandas as pd

# Load and display data
# Data available on Kaggle: https://www.kaggle.com/datasets/PromptCloudHQ/imdb-data
movies = pd.read_csv("IMDB-Movie-Data.csv")

# Creating a new feature "Title_length" using apply and lambda
movies["Title_Length"] = movies["Title"].apply(lambda title: len(title.split(" ")))
# More efficient version using Pandas str methods
movies["Title"].str.split(" ").str.len()
