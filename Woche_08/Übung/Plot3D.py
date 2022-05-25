import matplotlib.pyplot as plt


def plot_clusters_3d(dataset, plot_columns, cluster_col, labels, colors, title=''):
    """
    @param dataset: DataFrame with minimum of three columns for points and cluster reference
    @param plot_columns: The columns with the dimensions for which the points are plotted
    @param cluster_col: The column with the cluster reference nummer
    @param labels: Name for each cluster
    @param colors: Colors to use when plotting different clusters
    @param title: Title to show on top of plot
    """
    # Create figure and add 3d subplots
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)
    axs = fig.add_subplot(1, 1, 1, projection='3d')
    # Scatter points in each subplot using the set attributes
    legend_dict = {}
    x, y, z = plot_columns
    axs.set(xlabel=x, ylabel=y, zlabel=z)
    for i in dataset.index:
        cluster = dataset.loc[i, cluster_col]
        pt = axs.scatter(dataset.loc[i, x], dataset.loc[i, y], dataset.loc[i, z], color=colors[cluster])
        if cluster not in legend_dict:
            legend_dict[cluster] = pt
    axs.legend(legend_dict.values(), labels)
    plt.show()
