# 1. Laden Sie die in diesem Ordner abgelegte iris.json Datei mit dem folgenden Code
import json

with open('iris.json') as json_file:
    df_js = json.load(json_file)
    print(df_js)

# 2. Berechnen Sie den durchschnittlichen Wert der Tabelle 'sepalLength'
# (Ohne die Datei in ein Pandas Dataframe umzuwandeln)

#  3. Wiederhole Sie den gleichen Vorgang mit der iris.csv Datei, hierbei können Sie Pandas nutzen.
import pandas as pd

df_csv = pd.read_csv('iris.csv')
