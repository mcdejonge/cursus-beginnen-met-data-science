# Code voor het tonen van voorspelde clusters vs echte species.
# Merk op dat het resultaat iedere keer dat je deze code uitvoert anders is 
km_penguins = KMeans(n_clusters = 3)
km_penguins.fit(dfpenguins[['culmen_length_mm', 'flipper_length_mm']])

df_plot = dfpenguins.assign(cluster = km_penguins.labels_)
mapping = {
    'Adelie' : 'o',
    'Gentoo' : 'x',
    'Chinstrap' : '+'
}

for pspecies in df_plot['species'].unique():
    df_species = df_plot[df_plot['species'] == pspecies ]
    plt.scatter(df_species['culmen_length_mm'],
                df_species['flipper_length_mm'],
                c = df_species['cluster'],
                marker = mapping[pspecies])


plt.show()