import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from pandas_profiling import ProfileReport

# Load the Titanic dataset
dataset = pd.read_csv('//Woche_10/Vorlesung/titanic.csv')
#dataset.drop(columns=['class', 'Sex', 'deck', 'alone'], inplace=True)
print('- - - Head and Datatypes - - -')
print(dataset.head())
print(dataset.dtypes)

# Use .describe() method for first overview
aggregation = dataset.describe()
print('- - - Describe Method - - -')
print(aggregation)


# Use Pivot Tables to generate insights
print('- - - Survival Rate per sex and class - - -')
print(dataset.pivot_table(values='Survived', index='Sex', columns='Pclass', aggfunc='mean'))

# Create ProfileReport
#report = ProfileReport(dataset)
#report.to_file(output_file='Titanic_Report.html')
