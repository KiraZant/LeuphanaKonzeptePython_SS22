"""
Ziel dieser Übung ist es für den Iris Datensatz aus fünf Durchläufen die drei besten Cluster zu finden. Schreiben Sie
hierfür eine vereinfachte (nicht optimale aber besser umsetzbare) Version vom K-Means Algorithmus. Hierzu durchlaufen
wir fünf mal die gleichen Schritte (s. Vorlesungsslides): n_clusters zufällige Punkte als Centroiden wählen. Für jeden
Punk in unserem Datensatz den Centroiden wählen, der laut Euklidischer Distanz (Distanzfunktion) am nächsten ist
(Optimierungsfunktion). Die Distanz aller Punkte zu ihrem Centroiden summieren. Am Ende wollen wir nur wissen, welche
Centroiden aus den fünf Durchläufen die besten waren. Der Output muss eine DataFrame sein mit einer Reihe pro Punkt
mit den Koordinaten des nächsten der drei Centroiden, der Distanz des Punkten zu diesem und eine Nummer zur Zuordnung
zum Cluster (bei n_clusters= 3 ist das [0,1,2). Wird dieses DF mit dem ursprünglichen DF gejoint wie im Test Case
vorgeschrieben, können mithilfe der fertigen plot_clusters_3d Funktion im gleichen Order die Cluster visualisiert werden.

Dies ist eine Anwendungsaufabe mit zusammenhängenden Teilen. Nutzen Sie die Methoden und Logiken vorheriger Übungen
(bspw. List Comprehensions, min/max finden, etc.) und importieren Sie die Optimierungsfunktion aus diese Order mit der
Logik "from file import funktion". Achten Sie darauf, dass der Output einer Funktion der Input der nächsten ist. Deshalb
ist es sehr wichtig darauf zu achten, dass die Reihenfolgen und Datentypen der Outputs genauso sind wie vorgeschrieben.

"""
# Pakete importieren

from sklearn import datasets
# Vorgeschriebene Funktion, die die Ergebnisse plottet
from Plot3D import plot_clusters_3d

def k_means_clustering(data, n_clusters, n_runs):
    """
    """
    pass


# Test Case Iris
# Iris Datensatz laden (und wenn wir plotten wollen, die vierte Dimension entfernen)
dataset = datasets.load_iris().data[:, :3]
# Funktion anwenden um Cluster zu bekommen
funktion_result = k_means_clustering(dataset, 3, 5)
# Mit den ursprünglichen Datenpunkten joinen
results = pd.DataFrame(dataset, columns=['x', 'y', 'z']).join(funktion_result)
# Anschauen
print(results)
#Plotten
plot_clusters_3d(dataset=results, plot_columns=('x', 'y', 'z'), cluster_col='cluster', labels=['C1', 'C2', 'C3'],
                 colors=['r', 'g', 'b'], title='K-Means Clustering')
