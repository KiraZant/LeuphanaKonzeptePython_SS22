"""Dieser Code demonstriert kurz wie Exception Handling funktioniert.
Wir haben in errors_ex.py Runtime Errors kennengelernt. Nun wollen wir diese durch
Try-Except Statements abfangen.
"""

# ZeroDivisionError aus errors_ex.py


def division(x, y):

    # Die Anweisung im Try-Block wird zuerst ausgefuehrt
    try:
        print(x/y)
    except ZeroDivisionError: # Falls dieser Fehler auftritt wird die Anweisung ausgefuehrt
        print("Division durch 0 nicht moeglich!")

    # Falls ein anderer Fehler auftritt, erhalten wir wie gewohnt eine Fehlermeldung



division(2., 4.)
division(2, 0)
