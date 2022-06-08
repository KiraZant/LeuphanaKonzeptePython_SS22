import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titanic dataset laden
dataset = pd.read_csv('titanic.csv')

# Create boxplots
fig, axs = plt.subplots()
dataset[['Fare', 'Pclass']].boxplot(ax=axs, by='Pclass')
plt.show()
fig.savefig('Boxplots.png')

# Create Pairplot
fig = sns.pairplot(dataset, hue='Pclass')
fig.savefig('Pairplot.png')

# Calculate correlations and plot them as a heatmap
fig, axs = plt.subplots()
correlations = dataset.corr()
sns.heatmap(correlations, annot=True, cmap='rocket', ax=axs)
plt.tight_layout()
plt.show()
fig.savefig('Correlation_Heatmap.png')
