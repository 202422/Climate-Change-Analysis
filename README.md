# Climate-Change-Analysis
L’objectif de ce projet est de visualiser les tendances de différents indicateurs du changement climatique, d’identifier les facteurs qui les influencent et de proposer des décisions pour lutter contre le changement climatique. Pour y parvenir, j’ai utilisé des fichiers Excel, Power Query, Power BI, DAX, etc.

## Architecture du répertoire

```plaintext
├───Données
│   │   Description_Climate_Change_Dataset.pdf
│   │   
│   ├───Scripts python de Transformation
│   │       Traitement_Valeurs_Manquantes.py
│   │       TraductionDef_Indicateurs.py
│   │
│   ├───Données brutes
│   │       climate_change.xls
│   │
│   └───Données Transformées
│           climate_change_cleaned.xlsx
│
├───PowerBI
│       Climate Change Analysis.pbix
│       Climate Change Nettoyage.pbix
│
├───Rapport
│       Climate Change Analysis.pdf
├───Ressources


### Transformation Power Query

* Modifications des entêtes de colonnes et de leurs noms.
* Modifications des noms des tables.
* Suppression de doublons.
* Vérification des valeurs avant modification du type de chaque colonne :

  * Suppression des lignes vides dans les 3 tables.
  * Remplacement des valeurs `".."` dans **Pays.Capitale** par `"Aggregates"`.
  * Remplacement de `"Not Classified"` dans **Pays.Catégorie de prêt** par `null`.
  * Conserver uniquement les lignes des colonnes **Échelle** et **Décimales** (tables *Indicateur* et *Données*) qui ne contiennent pas `"Text"`.
  * Remplacement de `".."` par `null` dans les années et conversion de leur type en nombre.
* Dépivotage des colonnes années dans la table **Données**.
* Exécution d’un script Python pour traduire les définitions dans la table **Indicateur**.
* Exécution d’un script Python pour compléter les valeurs manquantes dans la table **Données** par la moyenne de chaque indicateur.
* Conversion de la colonne **Valeur** de la table **Données** en type **Décimal** en utilisant les paramètres géographiques des **USA**.
