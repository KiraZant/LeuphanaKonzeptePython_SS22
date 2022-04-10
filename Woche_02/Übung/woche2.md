# Übung Woche 1

## Aufgabe 1 - Seiteneffekte
In der Datei ```task1.py``` haben wir ein kleines Programm geschrieben.

a) Identifizieren Sie Seiteneffekte der Funktion. Was für Probleme könnten (falls man das Programm erweitert und mit dem
gegebenen Dictionary arbeiten möchte) durch diesen Seiteneffekt auftreten?

b) Ändern Sie die gegebene Funktion, so dass die ungewünschten Seiteneffekte nicht mehr auftreten.

c) Schreiben Sie einen Docstring für die Funktion

## Aufgabe 2 - Erdbeben
In dieser Aufgabe arbeiten Sie mit einem Datensatz über Erdbeben ```earthquake.csv```
(Quelle: https://www.kaggle.com/datasets/usgs/earthquake-database?resource=download). Neben anderen Problemen (z.B. fehlenden Werten) ist eine wichtige Spalte in diesem Datensatz falsch formatiert.

a) Machen Sie sich mit dem Datensatz vertraut (```.info()``` und ```.describe()```). Was fällt Ihnen bezüglich der
Datentypen der Datumsspalte auf?

b) Die Spalte ````Date```` hat leider einen falschen Datentypen. Um die weitere Arbeit zu erleichtern, wollen wir diese 
Spalte zu einer ```datetime``` Spalte umwandeln. Dazu können Sie die Pandas Funktion ``to_datetime`` (Dokumentation: 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) nutzen. Für den Parameter ``format``
müssen Sie für diesen Datensatz ``"%m/%d/%Y"``nutzen.<br>
*Achtung: Sie werden auf einen Fehler stoßen.*

c) In dieser Spalte werden verschiedene Formatierungen für das Datum genutzt. Versuchen Sie zu ermitteln, welche Zeilen 
hier problematisch sind und überführen Sie die betroffenen Zeilen in das ursprüngliche Format.<br>
*Hinweis: Sie könnten beispielsweise mit ```df["Date"].str[:2].unique()``` überprüfen, welche 
verschiedenen Werte es an den ersten beiden Stellen gibt. Was würden Sie hier erwarten?*

d) Versuchen Sie erneut eine ``datetime`` Spalte zu erzeugen. Überprüfen Sie, ob die problematischen Zeilen, die Sie in 
Teil c) ermittelt haben richtig konvertiert wurden. 

## Aufgabe 3 - Morsezeichen
Schreiben Sie eine Funktion, die einen String als Parameter erwartet und diesen String in Morsezeichen übersetzt. 
Zwischen jedem Buchstaben der in Morsecode übersetzt wird, soll ein Leerzeichen eingefügt werden.

Ihre Funktion soll bei der "Übersetzung" alle Satzzeichen (diese können nicht als Morsezeichen dargestellt werden) 
überspringen. Sie können annehmen, dass keine Umlaute oder ähnliches in den Eingabestrings vorkommmen.

Schreiben Sie zusätzlich eine Funktion, die Ihre Funktion mit ```assert``` Statements testet.
Für die Eingabe "Hi 123!" sollte Ihre Funktion folgenden Output erzeugen: ```".... .. .---- ..--- ...--"```

