# Übung Woche 1

## Aufgabe 0 - Fehlersuche

Unter einem Wort verstehen wir im Folgenden jede endliche Folge von Buchstaben
des deutschen Alphabets der Länge $≥ 1$. Je zwei Wörter in einer Zeichenfolge werden durch eine nicht-leere, endliche Folge von Zeichen, die nicht zu diesen Buchstaben gehören getrennt. Die Funktion ```next_word(s)``` soll, angewendet auf einen String ```s```, einen Tupel ```(word, rest)``` zurückgeben, wobei word das erste Wort in ```s``` ist und ```rest``` die Zeichenfolge ist, die in ```s``` auf ```word``` folgt.  

```
Beispiel: next_word('Python macht Spaß') # -> word = 'Python', rest = ' macht Spaß'.
```

Falls ```s``` kein Wort enthält, gibt die
Funktion das Tupel ```(None, "")``` zurück. Die folgenden Definitionen enthalten einen syntaktischen Fehler, einen semantischen Fehler und einen Fehler, der bei vielen (auch kurzen) Eingaben zur Laufzeit auftritt. Bei Eingaben mit sehr langen Wörtern gibt es einen weiteren Laufzeitfehler, der hier aber nicht behandelt werden soll. Fehler sind also in genau 3 Zeilen zu
finden.

**Bemerkung:** Im Gegensatz zu der String-Methode ```.split()``` müssen wir das Trennzeichen der Wörter nicht kennen. Außerdem liefert die Funktion ```next_word(s)``` lediglich das erste Wort und den Rest des Strings. Die Methode ```.split()```  liefert eine Liste mit aller Wörter, sofern das Trennzeichen dieser Wörter bekannt ist. Bei gewöhnlichen Texten (Wörter und Leerzeichen als Trennzeichen) empfiehlt sich daher ```.split()``` und ```.join()``` zu benutzen.
## Aufgabe 1 - Pandas
Im gleichen Repository und Ordner wie diese Übung liegt die Datei Spotify-2000.csv
a) Führen sie die benötigten Vorbereitungen aus und laden Sie die csv als Pandas DataFrame.
b) Schreiben Sie eine Funktion, die den DataFrame und Namen eines Artists als Argument erwartet und die Anzahl der Songs dieses Artists zurückgibt. Dank der Filter-Optionen in Pandas ist dies in einer Zeile möglich.

## Aufgabe 2 - Listen
Schreiben Sie nachfolgend zwei Funktionen, die eine Liste mit Zahlen als Parameter entgegennehmen und die größte bzw.
die kleinste Zahl der Liste ermitteln.\  

**Zusatz:** Geben Sie neben der Zahl auch den Index der Liste zurück, an der die Zahl steht.

## Aufgabe 3 - Primzahlen
Schreiben Sie eine Funktion, die eine Zahl n als Eingabe erwartet und eine Liste mit allen Primzahlen, die kleiner
oder gleich n sind, zurückgibt. Falls es keine solche Primzahl gibt, sollte eine leere Liste zurückgegeben werden.   

**Hinweis:** Die kleinste Primzahl ist 2. Um zu prüfen, ob eine gegebene Zahl x eine Primzahl ist, genügt es die
Teilbarkeit durch alle Primzahlen, die kleiner als x sind, zu testen. Falls x nicht durch eine der Primzahlen teilbar
ist, so ist x ebenfalls eine Primzahl.
