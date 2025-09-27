# Climate-Change-Analysis
The goal of this project is to visualize the trends of various climate change indicators, identify the factors that influence them, and propose decisions to combat climate change. To achieve this, I used Excel files, Power Query, Power BI, DAX, and other tools.

## Repository architecture

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
```

### Power Query Transformation

* Modified column headers and their names.
* Renamed tables.
* Removed duplicates.
* Checked values before changing the data type of each column:

  * Deleted empty rows in the three tables.
  * Replaced `".."` in **Country.Capital** with `"Aggregates"`.
  * Replaced `"Not Classified"` in **Country.Loan Category** with `null`.
  * Kept only the rows in the **Scale** and **Decimals** columns (in the *Indicator* and *Data* tables) that do not contain `"Text"`.
  * Replaced `".."` with `null` in the year columns and converted them to numeric type.
* Unpivoted the year columns in the **Data** table.
* Executed a Python script to translate the definitions in the **Indicator** table.
* Executed a Python script to fill missing values in the **Data** table with the average of each indicator.
* Converted the **Value** column in the **Data** table to **Decimal** type using the **US** locale settings.
