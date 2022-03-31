"""
Im Datensatz spotify.csv fällt auf, dass die Spalte 'Length (Duration)' durch den Aufruf  df.describe()
nicht angezeigt wird. Dies liegt daran, dass diese Methode nur numerische Werte zeigt.
"""

#  a) Führen sie die benötigten Vorbereitungen aus und laden Sie die csv als Pandas DataFrame mit dem Namen df.


#b) Schreiben Sie eine Funktion, die den DataFrame und Namen eines Artists als Argument erwartet und die Anzahl der
#   Songs dieses Artists zurückgibt. Dank der Filter-Optionen in Pandas ist dies in einer Zeile möglich.

def artists_len(df, artist):
    pass


print(artists_len(df, 'Foo Fighters'))  # 9
print(artists_len(df, 'Nirvana'))  # 11
print(artists_len(df, 'The Killers'))  # 3
