import pandas as pd

# Assurer que la colonne "Années" est bien numérique
dataset['Années'] = pd.to_numeric(dataset['Années'], errors='coerce')

# Liste des années attendues
annees_attendues = list(range(1990, 2012))

# Calcul de la moyenne par (Code Pays, Nom Pays, Code Indicateur, Nom Indicateur)
moyennes = (
    dataset.groupby(['Code Pays', 'Nom Pays', 'Code Indicateur', 'Nom Indicateur'])['Valeur']
    .mean()
    .reset_index()
    .rename(columns={'Valeur': 'Moyenne'})
)

# Préparer la liste pour stocker les lignes manquantes
lignes_a_ajouter = []

for _, row in moyennes.iterrows():
    filtre = (
        (dataset['Code Pays'] == row['Code Pays']) &
        (dataset['Nom Pays'] == row['Nom Pays']) &
        (dataset['Code Indicateur'] == row['Code Indicateur']) &
        (dataset['Nom Indicateur'] == row['Nom Indicateur'])
    )
    annees_existantes = dataset.loc[filtre, 'Années'].unique()
    annees_manquantes = set(annees_attendues) - set(annees_existantes)
    
    for annee in annees_manquantes:
        lignes_a_ajouter.append({
            'Code Pays': row['Code Pays'],
            'Nom Pays': row['Nom Pays'],
            'Code Indicateur': row['Code Indicateur'],
            'Nom Indicateur': row['Nom Indicateur'],
            'Echelle': dataset.loc[filtre, 'Echelle'].iloc[0] if not dataset.loc[filtre, 'Echelle'].empty else None,
            'Décimales': dataset.loc[filtre, 'Décimales'].iloc[0] if not dataset.loc[filtre, 'Décimales'].empty else None,
            'Années': annee,
            'Valeur': row['Moyenne']
        })

# Ajouter les lignes manquantes
dataset = pd.concat([dataset, pd.DataFrame(lignes_a_ajouter)], ignore_index=True)
