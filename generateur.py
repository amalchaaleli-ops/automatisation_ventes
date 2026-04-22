import pandas as pd

# 1. On crée nos données manuellement, tout simplement
donnees = {
    'ID': [101, 102, 103, 104, 105],
    'Prix': [15.0, 25.0, 10.0, 120.0, 45.0],
    'Quantite': [3, 2, 5, 1, 4],
    'Remise': [10, 5, 0, 15, 20]
}

# 2. On transforme ça en tableau Pandas
df = pd.DataFrame(donnees)

# 3. On sauvegarde en fichier CSV
df.to_csv('ventes.csv', index=False)

print("C'est bon, le fichier ventes.csv est créé !")