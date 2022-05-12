# Übungsblatt #6

## Aufgabe 1

Die folgende Funktion berechnet für eine gegebene positive, ganze Dezimalzahl (n) die entsprechende Binärdarstellung. 
Wie Sie sehen können, ist dies eine iterative Funktion.
```
def dec_to_bin_iter(n):

    if n == 0:
        return "0"

    bin_num = ""
    while n > 0:
        bin_num = str(n%2) + bin_num
        n = n // 2

    return bin_num
```

Schreiben Sie nun eine rekursive Funktion, die die Binärdarstellung einer natürlichen Zahl als String zurückgibt. 
Überlegen Sie sich zusätzlich Testfälle für ihre rekursive Funktion


## Aufgabe 2

Palindrome sind Wörter, welche vor- und rückwärts gelesen dasselbe Wort ergeben. Beispiele für Palindrome sind "Rentner", "Anna" oder "Naan". Die Groß- und Kleinschreibung der Buchstaben spielt hierbei keine Rolle. 

Schreiben Sie eine rekursive Funktion, die ein Wort als Eingabe erwartet und überprüft, ob dieses Wort ein Palindrom ist. Die Rückgabe der Funktion soll ein Boolean-Wert sein.

## Aufgabe 3

Sehen Sie sich die Datei `binary_searchtree.py` im Vorlesungsordner an und verstehen Sie die Implementierung. Nutzen Sie,
falls notwendig, den Debugger. Versuchen Sie den Schritt vom Suchen eines Knotens zum Einfügen eines Knotens genau zu 
verstehen.

## Aufgabe 4 (Fortgeschritten)
In diesem Problem verwenden wir Tupel und Dictionaries für rekursive Memoisierung. 

Dieses Problem wird **Gitterwege** genannt. An jedem Punkt des Gitters gibt es nur zwei mögliche Züge: nach unten und nach rechts. Ausgehend von der linken oberen Ecke eines 2x2-Gitters, gibt es genau 6 Wege in die rechte untere Ecke!

![alt text](https://alphacentauri32.files.wordpress.com/2012/06/problem_15.jpg)

**a)** Schreiben Sie zunächst eine rekursive (nicht memoisierte) Funktion, um die Anzahl der Pfade von der linken oberen Ecke eines (n x m) Gitters (n Zeilen und m Spalten) bis zur rechten unteren Ecke zu berechnen.

*Zur Kontrolle*: \\
Für m=n=2 -> Rückgabewert: 6 \\
Für m=n=6 -> Rückgabewert: 924 \\
Für hohe (n, m) braucht die Berechnung ohne Memoisierung viel zu lange.

**b)** Die Art und Weise, wie der obige Code aufgebaut ist, führt zu vielen wiederholten Aufrufen von gleichen Funktionen. Wenn Sie z.B. am oberen Ende eines 20x20-Rasters beginnen und dann nach unten und rechts gehen, dann rufen Sie die Funktion für ein 19x19-Raster auf. Dasselbe gilt, wenn Sie nach rechts und dann nach unten gehen. An dieser Stelle kommt die Memoisierung ins Spiel. Die Ausgabe der Funktion wird beim ersten Aufruf in einem Dictionary gespeichert, sodass ab dem zweiten Aufruf sofort der Wert aus dem Dictionary zurückgegeben wird, damit wir Aufrufe nicht zweimal machen. 

Die Schlüssel-Wert Paare des Dictionarys sind also $(n,m)$-Tupel mit dazugehöriger Ausgabe. Stellen Sie sicher, dass Sie zu Beginn der Funktionsausführung überprüfen, ob das Tupel $(n,m)$ im Memoization Dictionary vorhanden ist.

*Zur Kontrolle*: \\
Für m=n=2 -> Rückgabewert: 6 \\
Für m=n=6 -> Rückgabewert: 924 \\
Für m=n=20 -> Rückgabewert: 137846528820 \\
Für m=n=40 -> Rückgabewert: 107507208733336176461620 \\
Durch Memoisierung ist die Berechnung jetzt auch für hohe (m, n) schnell durchführbar.

