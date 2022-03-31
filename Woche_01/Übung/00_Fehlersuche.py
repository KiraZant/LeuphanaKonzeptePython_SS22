"""Unter einem Wort verstehen wir im Folgenden jede endliche Folge von Buchstaben des deutschen Alphabets der Länge
≥1. Je zwei Wörter in einer Zeichenfolge werden durch eine nicht-leere, endliche Folge von Zeichen, die nicht zu
diesen Buchstaben gehören getrennt. Die Funktion next_word(s) soll, angewendet auf einen String s, einen Tupel (word,
rest) zurückgeben, wobei word das erste Wort in s ist und rest die Zeichenfolge ist, die in s auf word folgt.

Beispiel: next_word('Python macht Spaß') # -> word = 'Python', rest = ' macht Spaß'.

Falls s kein Wort enthält, gibt die Funktion das Tupel (None, "") zurück. Die folgenden Definitionen enthalten einen
syntaktischen Fehler, einen semantischen Fehler und einen Fehler, der bei vielen (auch kurzen) Eingaben zur Laufzeit
auftritt. Bei Eingaben mit sehr langen Wörtern gibt es einen weiteren Laufzeitfehler, der hier aber nicht behandelt
werden soll. Fehler sind also in genau 3 Zeilen zu finden.

#Aufgabe: Finden und korrigieren Sie die Fehler!

Bemerkung: Im Gegensatz zu der String-Methode .split() müssen wir das Trennzeichen der Wörter nicht kennen. Außerdem
liefert die Funktion next_word(s) lediglich das erste Wort und den Rest des Strings. Die Methode .split() liefert
eine Liste mit aller Wörter, sofern das Trennzeichen dieser Wörter bekannt ist. Bei gewöhnlichen Texten (Wörter und
Leerzeichen als Trennzeichen) empfiehlt sich daher .split() und .join() zu benutzen. """

LETTERS = ("abcdefghijklmnopqrstuvwxyz"
"ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜäöüß")

LETTERS = ("abcdefghijklmnopqrstuvwxyz"
"ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜäöüß")

def _next_word_helper(s):
    """Hilfsfunktion für next_word."""
    if not s:
        return None, s
    if s[0] not in LETTERS:
        return None, s
    word = s[0]
    word_rest, s_rest = _next_word_helper(s[1:])
    if word_rest:
        word = word_rest
    return word, s_rest


def next_word(s):
    """Gibt das erste Wort eines Strings s und den Rest davon zurück."""
    while s[0] not in LETTERS
        s = s[1:]
    return _next_word_helper(s)


print(next_word('Python macht Spaß')) #word = 'Python', rest = ' macht Spaß'.