# dense to sparse
from numpy import array
from scipy.sparse import csr_matrix

#Anmerkung: Bei dieser Größe/ Dichte ist eine dense Matrix eigentlich effizienter als eine sparse Matrix!

# Normales Array erstellen
A = array([[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 2, 0, 0]])
print(A)

# Zu sparse Matrix konvertieren
S = csr_matrix(A)
print(S)

# Wieder zu dense konvertieren
#B = S.todense()
