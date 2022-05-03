# Übungsblatt #5

## Aufgabe 1 (Leuphana Kurse)

### Grundlegende Klasse

Im Folgenden werden wir eine Klasse erstellen, die die Kurse der Leuphana repräsentiert! Ein Kurs wird drei Attribute haben: eine Lehrkraft (z.B. Prof. Musterfrau), einen Kurscode (wie "32622000") und einen Titel (wie "Mikroökonomische Theorie I").

**a)** Erstellen Sie die Klasse LeuphanaCourse. Welche Informationen erhalten Sie durch die drei Print-Statements? Sie können davon ausgehen, dass alle Argumente der init-Methode Strings sind. 


Wir erzeugen eine Instanz der Klasse, indem wir das Klassenobjekt instanziieren und einige Argumente liefern. 

**b)** Erstellen Sie den oben beschriebenen Kurs "Mikroökonomische Theorie I". Drucken Sie die drei Attribute der Instanz ```micro_theory``` aus.


### Vererbung

**c)** Nun wollen wir eine ```LeuphanaEconCourse``` Klasse erstellen, die einen zusätzlichen Parameter ```recorded``` (d.h. ob der Kurs aufgenommen wird) nimmt, der standardmäßig auf ```False``` gesetzt ist, sowie einen zusätzlichen Parameter ```german```, der standardmäßig auf ```True``` gesetzt ist. 
<br>
Sie können hier die [super()-Methode](https://realpython.com/python-super/#super-in-single-inheritance) benutzen. Die Methode ```super()``` erlaubt es Ihnen Methoden der Eltern-/Oberklasse aufzurufen. In diesem Fall wird mit 
```
class Subclass(Superclass):
    def __init__(self, param1, ..., paramn):
        super().__init__(param1, ..., paramn)
```
die ```__init__()```-Methode der Superklasse aufgerufen. Der Methode übergeben Sie die passenden Parameter für die Superklasse und müssen *nicht* erneut den Parameter ```self``` übergeben.


Können Sie erkennen, was die Methode ```mro()``` zurückgibt?

**d)** Instanziieren Sie die neue Klasse mit dem Kurs "37811000 - Spieltheorie", welcher aufgenommen wird und auf deutsch stattfindet. 


**e)** Lesen Sie die folgenden Aussagen durch und versuchen Sie, die Ergebnisse vorherzusagen. 
```
a = LeuphanaCourse("Prof. Musterfrau", "33027000", "Statistics")
b = LeuphanaEconCourse("Prof. Musterfrau", "33028000", "Advanced Statistics", recorded=True)
c = LeuphanaEconCourse("Prof. Mustermsnn", "33029000", "Econometrics", recorded=True, german=False)

print(type(a)) # ->
print(isinstance(a, LeuphanaCourse)) # ->
print(isinstance(b, LeuphanaCourse)) # ->
print(isinstance(c, LeuphanaCourse)) # ->
print(isinstance(a, LeuphanaEconCourse)) # ->
print(issubclass(LeuphanaCourse, LeuphanaEconCourse)) # ->
print(type(a) == type(b)) # ->
print(type(b) == type(c)) # ->
print(a == b) # ->
print(b == c) # -> 
```


### Voraussetzungen implementieren - Fortgeschritten

**g)** Nun werden wir uns auf den ```LeuphanaEconCourse``` konzentrieren. Wir wollen Funktionalität implementieren, um festzustellen, ob ein Wirtschaftskurs Voraussetzung für einen anderen ist.

Wir gehen davon aus, dass die Reihenfolge der Kurse durch den numerischen Kurscode bestimmt wird. Wenn die Zahl an der 5. Stelle geringer ist, muss der Kurs davor belegt werden, zum Beispiel ````33027000```` vor ```33026000```. Alle anderen Zahlen (außer die 5.Stelle) muss gleich sein. 

Nach der Implementierung sollte man Folgendes sehen: 
```
micro_1 = LeuphanaCourse("Prof. Mustermann", "3302500", "Mikroökonomik I")
micro_2 = LeuphanaEconCourse("Prof. Mustermann", "3302600", "Mikroökonomik II")
macro_1 = LeuphanaEconCourse("Prof. Musterfrau", "3303500", "Makroökonomik I")
macro_2 = LeuphanaEconCourse("Prof. Musterfrau", "3303600", "Makroökonomik II")

micro_1 < micro_2 # -> True
micro_1 < macro_2 # -> False
```

Um dies zu erreichen, müssen Sie eine magische Methode ```___lt___``` implementieren, die Funktionalität hinzufügt, um festzustellen, ob ein Kurs Voraussetzung für einen anderen Kurs ist. 

Zusätzlich sollten Sie eine ```__eq__```-Methode für ```LeuphanaCourse``` implementieren. Zwei Klassen sind gleichwertig, wenn sie dasselbe Institut sind und denselben Kurscode haben; der Titel spielt hier keine Rolle. 