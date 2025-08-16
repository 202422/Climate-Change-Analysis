from googletrans import Translator
import pandas as pd

# Copier la table reçue de Power Query dans df
df = dataset.copy()

translator = Translator()

def traduire_texte(text):
    try:
        # La traduction peut échouer sur des valeurs vides ou non-string
        if not isinstance(text, str) or text.strip() == "":
            return text
        # Traduire de l'anglais vers le français
        traduction = translator.translate(text, src='en', dest='fr')
        return traduction.text
    except Exception as e:
        # En cas d'erreur, renvoyer le texte original
        return text

# Appliquer la traduction sur la colonne 'Definition'
df['Definition'] = df['Definition'].apply(traduire_texte)

