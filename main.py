import pandas as pd
import matplotlib.pyplot as plt

print("Début de l'analyse des ventes...")

# 1. Lecture dynamique du fichier CSV
fichier_cible = input("📂 Quel fichier CSV voulez-vous analyser ? (ex: ventes.csv) : ")

try:
    df = pd.read_csv(fichier_cible)
    print(f"✅ Fichier '{fichier_cible}' chargé avec succès !")
except FileNotFoundError:
    print(f"❌ Erreur : Le fichier '{fichier_cible}' est introuvable. Vérifiez le nom.")
    exit() # On arrête l'exécution proprement

# 2. Calculez le Chiffre d'Affaires Brut (Prix * Quantité)
# Pandas multiplie les deux colonnes ligne par ligne automatiquement
df['CA_Brut'] = df['Prix'] * df['Quantite']

# 3. Appliquez les remises (en pourcentage) pour obtenir le CA Net
# Formule : CA Brut * (1 - (Remise / 100))
df['CA_Net'] = df['CA_Brut'] * (1 - (df['Remise'] / 100))

# 4. Calculez le montant de la TVA (20%) sur le CA Net
df['TVA'] = df['CA_Net'] * 0.20

# 5. On affiche le tableau dans le terminal pour vérifier
print("\nVoici le tableau avec les nouveaux calculs :")
print(df)

# --- NOUVEAU CODE À AJOUTER ---

# 5. Affichez le CA Total de l'entreprise 
# La fonction sum() additionne simplement toute la colonne
ca_total = df['CA_Net'].sum()
print("\n=== RÉSULTATS GLOBAUX ===")
print(f"Le Chiffre d'Affaires Total Net est de : {ca_total}")

# 6. Identifiez l'ID du produit star 
# idxmax() trouve le numéro de la ligne qui a le plus grand CA Net
ligne_max = df['CA_Net'].idxmax()
# loc permet de récupérer la valeur de la colonne 'ID' à cette ligne précise
meilleur_id = df.loc[ligne_max, 'ID']
print(f"Le produit star (meilleur CA Net) est l'ID numéro : {meilleur_id}")

# ------------------------------
# 6. Exportez un fichier resultats_final.csv avec toutes les colonnes
df.to_csv('resultats_final.csv', index=False)

print("\nAnalyse terminée ! Le fichier resultats_final.csv est créé.")


print("\nGénération du graphique en cours...")

# On crée un graphique en barres (ID du produit en X, CA Net en Y)
df.plot(kind='bar', x='ID', y='CA_Net', color='skyblue', legend=False)

# On ajoute des jolis titres
plt.title("Chiffre d'Affaires Net par Produit")
plt.xlabel("ID du Produit")
plt.ylabel("CA Net (en €)")
plt.xticks(rotation=0) # Pour garder les ID à l'horizontale

# On affiche la fenêtre avec le graphique
plt.show()