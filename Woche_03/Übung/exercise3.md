# Übung Woche 2

## Aufgabe 1 - Map und Filter
Schreiben Sie für jede der folgenden Zeilen eine einzelne Anweisung mit ```map``` oder ```filter```, die die linke Spalte in die rechte 
Spalte umwandelt. Nutzen Sie (falls notwendig) ```lambda``` Funktionen als Argument für die ```map``` und ```filter``` 
Funktionen.

| Input                            | Output |
|----------------------------------|------|
| ['12', '-2', '0']                | [12, -2, 0] |
| ['12', '-2', '0', '-4', '1']      | ['12', '0', '1'] |
| ['hello', 'world']               | [5, 5] |
| ['hello', 'world']               | ['olleh', 'dlrow'] |
| range(20)                        | [0, 3, 5, 6, 9, 10, 12, 15, 18] |
| range(2, 6)                      | [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)] |
| zip(range(2, 5), range(3, 9, 2)) | [6, 15, 28] |
| ['hello', 'world']               | ['world'] |


*Die ```zip()``` Funktion (https://www.w3schools.com/python/ref_func_zip.asp) ermöglicht paralleles Iterieren
über mehrere Iteratoren.*

## Aufgabe 2 - Wetter in Kanada
In dieser Aufgabe arbeiten Sie mit einem kleinen Datensatz über das Wetter in einigen kanadischen Städten 
(Quelle: https://www.kaggle.com/datasets/hemil26/canada-weather). Leider hat der Datensatz einige Probleme, die wir 
bereinigen müssen.

a) Machen Sie sich mit dem Datensatz vertraut (```.info()``` und ```.describe()```). Was fällt Ihnen auf?

b) Die Spalte ````Community```` beinhaltet sowohl die Stadt als auch den Bundesstaat. Für weitere Analysen möchten wir 
zwei verschiedene Spalten ````City```` und ``State`` haben.  

c) Wie Sie vermutlich schon in Teil a) festgestellt haben, sind die Temperaturangaben als Strings gegeben. 
Bereinigen Sie die Temperaturspalten: In diesen Spalten benötigen wir die Temperaturen in °C als Floatwerte.
*Hinweis: Vielleicht hilft Ihnen die Funktion ``replace_minus`` in dieser Aufgabe.*

d) In welchem Staat ist die höchste Durchschnittstemperatur im Juli? In welcher Stadt ist die niedrigste jährliche Durchschnittstemperatur? 

**Zusatz (nur für Fortgeschrittene):** Nutzen Sie ``groupby`` um weitere Erkenntnisse über die Temperaturen in den jeweiligen Bundesstaaten zu sammeln.

**Hinweise zur Aufgabe:** Teil b) und c) können sowohl mit ``apply`` (und ``lambda``) gelöst werden als auch mit den 
eigenen Methoden von Pandas zum Manipulieren von Strings. 

## Aufgabe 3 - List Comprehensions
Schreiben Sie eine Funktion, die die nächste Ebene eines Pascalschen Dreiecks mit Hilfe einer List Comprehension 
generiert. Die Funktion erhält eine Liste, die eine Zeile des Pascalschen Dreiecks darstellt und gibt die nächste Zeile 
aus. Beispiele:
```
generiere_pascal_reihe([1, 2, 1]) -> [1, 3, 3, 1]
generiere_pascal_reihe([1, 4, 6, 4, 1]) -> [1, 5, 10, 10, 5, 1]
generiere_pascal_reihe([]) -> [1]
```
Zur Erinnerung: Jedes Element in einer Zeile des Pascalschen Dreiecks wird durch Addition der beiden Elemente in der vorherigen Zeile direkt über (links und rechts) diesem Element gebildet. Wenn es nur ein Element direkt darüber gibt, fügen wir nur dieses eine hinzu. Zum Beispiel sehen die ersten 5 Zeilen des Pascal'schen Dreiecks so aus:
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```
*Hinweis: Sie könnten dieses Problem der ```zip()```-Funktion lösen.*


## Aufgabe 4 - Formatierung (für Fortgeschrittene)

Schreiben Sie eine Funktion, um aus einer beliebigen Anzahl von Keyword Argumenten eine Tabelle zu erstellen. Zum Beispiel sollte der Aufruf
```
erstelle_tabelle(vorname="melanie", nachname="musterfrau", lieblingstier="giraffe")
```
folgendes drucken:
```
==============================
| vorname       | melanie    |
| nachname      | musterfrau |
| lieblingstier | giraffe    |
==============================
```
