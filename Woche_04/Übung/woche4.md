# Übung Woche 4

## Aufgabe 0 - Numpy A

**a.** Erstellen Sie mit NumPy das folgende Array, ohne dabei alle Zahlen per Hand einzugeben:
```
[[1,  6, 11],  
 [2,  7, 12],  
 [3,  8, 13],  
 [4,  9, 14],  
 [5, 10, 15]]
```
**Hinweis:** Nutzen Sie die np.transpose() Funktion sowie reshape().

**b.** Extrahieren Sie anschließend die zweite und vierte Reihe bzw. Zeile des Arrays.

## Aufgabe 1 - Numpy B 
NumPy Arrays bieten die Möglichkeit des Indexing mit einem Array aus Indizes. Nutzen Sie die np.arange() Funktion, um
eine Zahlenfolge der geraden Zahlen zwischen 100 und 200 zu erstellen und extrahieren Sie die Zahlen an den folgenden Indizes:  
```
ind = np.array([7, 13, 25, 49, 24, 36, 42]) 
```

## Aufgabe 2 - Numpy C

**a.** Schreiben Sie eine Funktion, die kleinsten Zahl und deren Index aus der vorgegebenen 4x3 Matrix mit zufälligen 
natürlichen Zahlen zwischen 0 und 100 herausgibt. Sie dürfen Numpy Methoden nutzen.

**b.** In der Vorlesung haben Sie das Konzept der Vectorization kennengelernt, die es uns erlaubt Operationen mit dem Array durchzuführen.
Schreiben Sie die Funktion scale(x), die die Werte eines Arrays durch sogennante Min-Max Skalierung ausschließlich im Wertebereich zwischen 0 und 1 legt. Der kleinste Wert des
originalen Arrays wird also zu 0 und der größte zu 1. Alle weiteren Werte liegen dazwischen. 

Formel:  
![alt-text](/Volumes/nonshib-webdav/Python_Kurs/SS_2022/Python_DataX_SS22/04_Datenstrukturen/Woche_04/Übung/formula.png "Min-Max-Skalierung")  

Note: Ggf. muss um das Bild zu sehen der Path angepasst werden (der Path zum Ordner in dem dieser Code + das Bild liegen).   

Testen Sie Ihre Funktionen mit einem Array mit den Zahlen von 0 bis 10.

# Aufgabe 3 - Pandas Datenstrukturen Basics
Nutzen Sie den in der Vorlesung gezeigten Code zum Laden von Bildern, um die jeweiligen Bilder anzeigen zu lassen. Erstellen Sie dann mithilfe der Funktion ```make_df()``` die einzelnen DataFrames (links) und dann daraus mit ```concat```, ```merge```  oder ```join``` das im Bild rechts dargestellten DataFrame.

# Aufgabe 4 - Pandas Datenstrukturen Anwendung
Laden Sie die auch im Ordner abgelegten Dateien characters.csv, planets.csv und species.csv, die aus dem Star Wars kaggle datensatz stammen (https://www.kaggle.com/jsmake_df(phyg/star-wars).
Schauen Sie sich die Daten an und nutzen Sie die Informationen aus der ```merge``` documentation (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) und die um die Datensätze characters.csv, planets.csv und species.csv so zu mergen, dass Sie eine Reihe pro Character mit allen dazugehörigen Informationen haben.
