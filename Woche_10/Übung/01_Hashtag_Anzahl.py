# Finden Sie heraus, welche 15 Hashtags am häufigsten genutzt wurden und erstellen Sie ein Bar Plot
# in der die Häufigkeiten dargestellt sind.

# a) Laden Sie einen der noch nicht gesäuberten Datensätze und schauen Sie sich den Text vs. die
# 'hashtags'-Spalte an. Sie werden feststellen, dass in deer automatisch generierten Spalte viele # fehlen.

# b) Nutzen Sie das angegebene re pattern, welches nach # sucht um alle Hashtags in eine extra Spalte zu ziehen

pattern = r'#(\w+)'

# c) Mit list-comprehensions können Sie alle Hashtags in eine Liste übertragen (Tipp: Googlen Sie "flatten list python")

# d) Zählen Sie die Häufigkeit der einzelnen Hashtags
# Tipp: Sie können dies mit einer Dictionary Comprehension und der .count() Funktion für Listen lösen

# e) Erstellen Sie ein Barplot mit den Häufigkeiten der 15 meistgenutzten Wörter
