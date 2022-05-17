# Übungsblatt #7

## Aufgabe 1

Der folgende Pseudocode beschreibt den *Insertion Sort*-Algorithmus, der als Eingabe ein Array *A* der Länge *n* verwendet.
Der Befehl ```swap(A[pos], A[pos-1])``` bedeutet, dass die Elemente ```A[pos]``` und ```A[pos-1]``` getauscht werden. <br>
**In dieser Aufgabe müssen Sie keinen Code implementieren.**

```
Algorithmus INSERTIONSORT(A[0,...,n-1]):

for i=0 to n-2 do
    pos = i + 1
    while pos > 0 and A[pos] < A[pos-1] do
        swap(A[pos], A[pos-1])
        pos = pos - 1
```

a) Angenommen *Insertion Sort* läuft auf der Eingabe ```A = [27, 8, 19, 5, 23, 12]```. Geben Sie *A* nach dem Ende jeder 
Iteration der for-Schleife an.

b) Geben Sie die Worst-Case Laufzeit von *Insertion Sort* als Funktion von *n* an. Erklären Sie Ihre Antwort.

## Aufgabe 2

Für zwei Listen *A_1* und *A_2* von Zahlen sind alle Zahlen gesucht, die sowohl in *A_1* als auch in *A_2* vorkommen. Sie können annehmen, dass keine Zahl mehrfach in einer der beiden Listen steht.<br>
Beispiel:

```
A_1 = [1, 2, 3, 4, 7]
A_2 = [-1, 0, 4, 7, 10]
==> [4, 7]
```
a) Programmieren Sie einen naiven Algorithmus für dieses Problem und bestimmen Sie dessen Laufzeit in Abhängigkeit von 
den Listengrößen *|A_1|* und *|A_2|*. Dieser Algorithmus soll auch für *nicht-sortierte* Listen funktionieren.<br>
*Bemerkung: Mit *|A_1|* bzw. *|A_2|* ist die Anzahl der Elemente in der Liste *A_1* bzw. *A_2* gemeint.*

b) Programmieren Sie einen Algorithmus, der dieses Problem in Zeit *O(|A_1|+|A_2|)* löst, falls die beiden Listen 
bereits sortiert sind. Begründen Sie die lineare Laufzeit. 

## Aufgabe 3

a) Implementieren Sie die Sortieralgorithmen *Merge Sort*. 

b) Messen Sie die Laufzeit des Sortieralgorithmus für verschiedene Eingabegrößen *n = 100, 200, ..., 5000*. Die 
Eingabe-Liste mit Länge *n* soll aus zufälligen Integerwerten bestehen. 

## Aufgabe 4

Erinnern Sie sich an die Fibonacci Zahlen aus der Vorlesung/Übung. Analysieren Sie Worstcase-Laufzeit von 
```fibonacci(n)``` und ```fibonacci_topdown(n)```.

```
memo_table = [0] * (n+1)

def fibonacci_topdown(n):
  if not memo_table[n]:
    if n==1 or n==2:
      memo_table[n] = 1
    else:
      memo_table[n] = fib_topdown(n-1) + fib_topdown(n-2)
  return memo_table[n]
  

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```