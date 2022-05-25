# Übung Woche 8

**Anmerkung:**
Dies ist eine Anwendungsaufabe mit zusammenhängenden Teilen, die alle kombiniert werden. 
Lesen Sie sich alle Aufgabenteile durch, bevor Sie beginnen und bedenken Sie, dass der Output einer Funktion der Input der nächsten ist. Deshalb
ist es wichtig darauf zu achten, dass die Reihenfolgen und Datentypen der Outputs genau zusammenpassen. 
Übertragen Sie zuerst die Informationen aus der Aufgabenstellung in den Docstring
und nutzen Sie dies zur Orientierung.

Nutzen Sie die Methoden und Logiken vorheriger Übungen
(bspw. List Comprehensions, min/max finden, etc.) und importieren Sie die Optimierungsfunktion aus diese Order mit der
Logik "from file import funktion".


**Anwendungsziel** dieser Übung ist es für den Iris Datensatz aus fünf Durchläufen die drei besten Cluster zu finden. Schreiben Sie
hierfür eine vereinfachte (nicht optimale aber besser umsetzbare) Version vom K-Means Algorithmus. 
## Aufgabe 0 - Distanzfunktion

Implementieren Sie die in der Vorlesung vorgestellten zwei Distanzmaße als Funktion um die Distanz zwischen zwei Punkten x und y zu berechnen.  

**a)** Euklidische Distanz  
**b)** Manhatten Distanz  


*Hinweis: Nutzen Sie die Möglichkeiten von numpy Rechenoperationen über ganze
Arrays hinweg zu vollführen (Vectorization), wie in VL 4 besprochen wurden. Wenn Sie dies
sinnvoll anwenden, sind die Funktionen in jeweils einer Zeile Code lösbar.*

## Aufgabe 1 - Optimierung
Schreiben Sie eine Funktion, die für den Punkt x eine beliebige Funktion aus dem Distanzfunktion.py Datei nimmt und
aus einem Numpy Array beliebig viele andere Punkte den 1) zu x am nächsten liegenden Punkt y, 2) den Abstand zwischen x
und diesem Punkt y und 3) dessen Index in der Liste der Optionen ausgibt.

*Hinweis: Versuchen Sie diese Aufgabe ohne for-loop zu lösen.*


## Aufgabe 2 - K-Means

Erstellen Sie eine Funktion, die n mal die Schritte auf dem letzten Vorlesungsslide durchläuft 
und das Ergebnis zurückgibt, welches die niedrigste Summe von Distanzen zwischen den Punkten und ihrem nächsten 
Centroiden zurückgibt. Der Output soll eine DataFrame sein, mit einer Reihe pro Punkt
und jeweils 1) die Koordinaten des nächsten der drei Centroiden, 2) der Distanz des Punkten zu diesem und 3) eine Nummer zur Zuordnung
zum Cluster (bei n_clusters = 3 ist das [0,1,2]). Wird dieses DF mit dem ursprünglichen DF gejoint wie im Test Case
vorgeschlagen, können mithilfe der fertigen plot_clusters_3d Funktion im gleichen Order die Cluster visualisiert werden.

Es kann gut sein, dass Sie hier merken, dass vorherige Funktionen umgeschrieben werden müssen.
