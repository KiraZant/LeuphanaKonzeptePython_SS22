import pandas as pd
from matplotlib import image
import matplotlib.pyplot as plt

#  Bearbeiten Sie die folgenden Aufgaben in dem Sie den in der Vorlesung gezeigten Code zum Laden von Bildern nutzen,
#  um die jeweiligen Bilder anzeigen zu lassen. Erstellen Sie dann mithilfe der Funktion make_df() die einzelnen
#  DataFrames (links) und dann daraus mit concat, merge oder join das im Bild rechts dargestellten DataFrame.


def make_df(cols, ind):
    """Funktion um DataFrames mit den Spalte cols und Zeilen ind zu erstellen"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)


# Beispiel DataFrame
print(make_df('ABC', range(3)))

# a. bildA.png

# Lösung


# b. bildB.png

# Lösung


#  c. Nutzen Sie die untenstehenden DFs um mit Hilfe von merge() das DF im bildC.png zu erstellen.

df5 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'], 'food': ['fish', 'beans', 'bread']}, columns=['name', 'food'])
df6 = pd.DataFrame({'name': ['Mary', 'Joseph'], 'drink': ['wine', 'beer']}, columns=['name', 'drink'])

#  Lösung
