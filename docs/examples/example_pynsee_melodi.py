# %% [markdown]
# # Utilisation des fonctions melodi de pynsee

# %% [markdown]
# ## I. Installer, désinstaller un module python depuis un dépôt GitHub
# 
# Pour installer le module pynsee depuis un dépôt GitHub, exécuter dans le terminal la ligne suivante : pip install git+https://github.com/Mathieu-David/pynsee.git@MELODI.
# 
# Si vous voulez le désinstaller, exécuter dans un terminal la commande suivante : pip uninstall pynsee
# 
# Pour avoir la liste des modules installées en python, exécuter dans un terminal la commande suivante : pip list
# 
# Pour exécuter dans un terminal : appuyer sur la touche "Entrée".

# %% [markdown]
# ## II. Charger le module pynsee

# %%
# Charger l'intégralité du module pynsee
import pynsee

# %% [markdown]
# ## III. Listes des fonction melodi

# %%
# Charger le module inspect pour l'introspection des objets
import inspect

# Extraction et affichage de toutes les fonctions du sous-module melodi
fonctions_melodi = [
    nom for nom, obj in inspect.getmembers(pynsee.melodi, inspect.isfunction)
]

# Afficher la liste des fonctions du sous-module melodi
print("Fonctions du sous-module melodi :")
for f in sorted(fonctions_melodi):
    print(f"- {f}")

# %% [markdown]
# ## IV. Aides des fonctions melodi de pynsee

# %%
# Aides de toutes les fonctions du sous-module melodi
help(pynsee.melodi)

# %% [markdown]
# ## V. Exemples d'utilisation des fonctions
# 
# ### V.a Fonction get_all_data : 
# 
# #### V.a.1 Aide de get_all_data : 

# %%
# Aide de la fonction get_all_data du sous-module melodi
help(pynsee.get_all_data)

# %% [markdown]
# #### V.a.2 Exemple d'utilisation de la fonction get_all_data :
# 
# Exemple 1 : 

# %%
# Tuple contenant les données et les métadonnées pour le jeu de données "DS_TICM_PRATIQUES"
tuple=pynsee.get_all_data("DS_TICM_PRATIQUES")

# Jeu de données pour le DS : "DS_TICM_PRATIQUES"
data = tuple[0]
data.info()
data.head()


# %%
# Métadonnées pour le DS : "DS_TICM_PRATIQUES"
metadata = tuple[1]
metadata.info()
metadata.head()

# %% [markdown]
# Exemple 2 : 

# %%
# Tuple contenant les données et les métadonnées pour le jeu de données "DS_FILOSOFI_CC"
tuple=pynsee.get_all_data("DS_FILOSOFI_CC")

#data
data = tuple[0]
data.info()
data.head()

# %%
# Métadonnées pour le DS : "DS_FILOSOFI_CC"
metadata = tuple[1]
metadata.info()
metadata.head()

# %% [markdown]
# ### V.b Fonction get_catalog : 
# 
# #### V.b.1 Aide de get_catalog :

# %%
# Aide de la fonction get_catalog du sous-module melodi
help(pynsee.get_catalog)

# %% [markdown]
# #### V.b.2 Exemples d'utilisation de la fonction get_catalog :
# 
# Exemple 1 :

# %%
# Extraction et affichage du catalogue des jeux de données disponibles dans le catalogue Melodi
catalogue_melodi = pynsee.get_catalog()
catalogue_melodi.head()

# %% [markdown]
# Exemple 2 :

# %%
# Extraction et affichage du catalogue des jeux de données disponibles dans le catalogue Melodi en anglais
catalogue_melodi = pynsee.get_catalog(lang="en")
catalogue_melodi.head()

# %% [markdown]
# ### V.c Fonction get_data : 
# 
# #### V.c.1 Aide de get_data :

# %%
# Aide de la fonction get_data du sous-module melodi
help(pynsee.get_data)

# %% [markdown]
# #### V.c.2 Exemples d'utilisation de la fonction get_data :
# 
# Exemple 1 :

# %%
# Extraction et affichage des données pour le jeu de données "DS_POPULATIONS_REFERENCE" en sélectionnant la mesure "PMUN" et le territoire "FRANCE-F"
data=pynsee.get_data("https://api.insee.fr/melodi/data/DS_POPULATIONS_REFERENCE?POPREF_MEASURE=PMUN&GEO=FRANCE-F")

data.info()
data.head()

# %% [markdown]
# Exemple 2 :

# %%
# Extraction et affichage des données pour le jeu de données "DS_RP_MENAGES_PRINC_IRIS" en sélectionnant la mesure "POP", le statut conjugal "_T", la taille du ménage "_T" et l'âge "Y_GE15"
data=pynsee.get_data("https://api.insee.fr/melodi/data/DS_RP_MENAGES_PRINC_IRIS?RP_MEASURE=POP&CIVIL_STATUS=_T&NOC=_T&AGE=Y_GE15")

data.info()
data.head()

# %% [markdown]
# ### V.d Fonction get_file : 
# 
# #### V.d.1 Aide de get_file :

# %%
# Aide de la fonction get_file du sous-module melodi
help(pynsee.get_file)

# %% [markdown]
# #### V.d.2 Exemples d'utilisation de la fonction get_file :
# 
# Exemple 1 : xlsx qui s'appelle BPE_SPORT_LOISIR_CULTURE_FR et associé au jeu de données DS_BPE

# %%
# Télécharger le fichier excel qui s'appelle "BPE_SPORT_LOISIR_CULTURE_FR" du jeu de données "DS_BPE" et le sauvegarder sous le nom "BPE_SPORT_LOISIR_CULTURE_FR.xlsx"
pynsee.get_file(ds_name = "DS_BPE",
             file_name = "BPE_SPORT_LOISIR_CULTURE_FR",
             download_file_name = "BPE_SPORT_LOISIR_CULTURE_FR.xlsx")

# %% [markdown]
# Exemple 2 : 

# %%
# Télécharger le fichier CSV associé au DS "DS_FILOSOFI_SAGE_LOG_TP_NIVVIE", qui s'appelle "DS_FILOSOFI_SAGE_LOG_TP_NIVVIE_2023_CSV_FR" et le sauvegarder sous le nom "DS_FILOSOFI_SAGE_LOG_TP_NIVVIE_CSV_FR.zip" qui contient un fichier de data et un fichier de metadata
# Le fichier de data corrspond à l'ensemble de la base de données et le fichier de metadata correspond à la description des variables et des modalités
pynsee.get_file(ds_name = "DS_FILOSOFI_SAGE_LOG_TP_NIVVIE",
             file_name = "DS_FILOSOFI_SAGE_LOG_TP_NIVVIE_2023_CSV_FR",
             download_file_name = "DS_FILOSOFI_SAGE_LOG_TP_NIVVIE_CSV_FR.zip")

# %% [markdown]
# Exemple 3 : parquet

# %%
# Télécharger le fichier parquet associé au DS "DS_RP_TD_POPULATION_AGECOUPLECIVILSEX_PRINC" et le sauvegarder sous le nom "DS_RP_TD_POPULATION_AGECOUPLECIVILSEX_PRINC.parquet"
# Le fichier parquet correspond à l'ensemble de la base de données
pynsee.get_file(ds_name = "DS_RP_TD_POPULATION_AGECOUPLECIVILSEX_PRINC")

# %% [markdown]
# ### V.e Fonction get_local_data : 
# 
# #### V.e.1 Aide de get_local_data :

# %%
# Aide de la fonction get_local_data du sous-module melodi
help(pynsee.get_local_data)

# %% [markdown]
# #### V.e.2 Exemples d'utilisation de la fonction get_local_data :
# 
# Exemple 1 :

# %%
# Extraction et affichage des données pour le jeu de données "DS_POPULATIONS_REFERENCE" en sélectionnant la région 53 (REG="53", Bretagne)
data=pynsee.get_local_data(

      ds_name = "DS_POPULATIONS_REFERENCE",

      geo = "53",

      geo_object = "REG")

# Infos et 5 premières lignes du jeu de données
data.info()
data.head()

# %% [markdown]
# Exemple 2 :

# %%
# Extraction et affichage des données pour le jeu de données "DS_POPULATIONS_REFERENCE" en sélectionnant le code commune 44109 (Nantes) et la mesure "PMUN"
data=pynsee.get_local_data(

      ds_name = "DS_POPULATIONS_REFERENCE",

      geo = "44109",

      geo_object = "COM",
      
      query_filter = "POPREF_MEASURE=PMUN")

# Infos et 5 premières lignes du jeu de données
data.info()
data.head()

# %% [markdown]
# ### V.f Fonction get_local_data_by_com : 
# 
# #### V.f.1 Aide de get_local_data_com :

# %%
# Aide de la fonction get_local_data_by_com du sous-module melodi
help(pynsee.get_local_data_by_com)

# %% [markdown]
# #### V.f.2 Exemples d'utilisation de la fonction get_local_data_com :
# 
# Exemple 1 :

# %%
# Extraction et affichage des données pour le jeu de données "DS_POPULATIONS_REFERENCE" en sélectionnant les communes de la région 53 (REG="53", Bretagne)
data=pynsee.get_local_data_by_com(

      ds_name = "DS_POPULATIONS_REFERENCE",

      geo = "53",

      geo_object = "REG")

# Infos et 5 premières lignes du jeu de données
data.info()
data.head()

# %% [markdown]
# Exemple 2 :

# %%
# Extraction et affichage des données pour le jeu de données "DS_POPULATIONS_REFERENCE" en sélectionnant les communes du département 44 (DEP="44", Loire-Atlantique) et l'indicateur "PMUN" (population municipale)

data=pynsee.get_local_data_by_com(

      ds_name = "DS_POPULATIONS_REFERENCE",

      geo = "44",

      geo_object = "DEP",
      
      query_filter = "POPREF_MEASURE=PMUN")

# Infos et 5 premières lignes du jeu de données
data.info()
data.head()

# %% [markdown]
# ### V.g Fonction get_metadata : 
# 
# #### V.g.1 Aide de get_metadata : 

# %%
# Aide de la fonction get_metadata du sous-module melodi
help(pynsee.get_metadata)

# %% [markdown]
# #### V.g.2 Exemples d'utilisation de la fonction get_metadata :
# 
# Exemple 1 : 

# %%
# Extraction et affichage des métadonnées pour le jeu de données "DS_POPULATIONS_REFERENCE"
metadata=pynsee.get_metadata(ds_name = "DS_POPULATIONS_REFERENCE")

# %% [markdown]
# Exemple 2 :

# %%
# Extraction et affichage des métadonnées pour le jeu de données "DS_SRCV_PMS"
metadata=pynsee.get_metadata(ds_name = "DS_SRCV_PMS")


# %% [markdown]
# 

# %% [markdown]
# ### V.h Fonction get_range : 
# 
# #### V.h.1 Aide de get_range :

# %%
# Aide de la fonction get_range du sous-module melodi
help(pynsee.get_range)

# %% [markdown]
# #### V.h.2 Exemples d'utilisation de la fonction get_range :
# 
# Exemple 1 :

# %%
# Extraction et affichage des variables\modalités pour le jeu de données "DS_FILOSOFI_CC"
data=pynsee.get_range("DS_FILOSOFI_CC")

data.info()
data.head()

# %% [markdown]
# Exemple 2 :

# %%
# Extraction et affichage des variables\modalités pour le jeu de données "DS_FILOSOFI_CC" en anglais
data=pynsee.get_range("DS_FILOSOFI_CC",lang="en")

data.info()
data.head()

# %% [markdown]
# ### V.i Fonction get_range_geo : 
# 
# #### V.i.1 Aide de get_range_geo :

# %%
# Aide de la fonction get_range_geo du sous-module melodi
help(pynsee.get_range_geo)

# %% [markdown]
# #### V.i.2 Exemples d'utilisation de la fonction get_range_geo :
# 
# Exemple 1 :

# %%
# Extraction et affichage des zones géographiques pour le jeu de données "DS_RP_MENAGES_PRINC_IRIS"
data=pynsee.get_range_geo("DS_RP_MENAGES_PRINC_IRIS")

data.info()
data.head()

# %% [markdown]
# Exemple 2 :

# %%
# Extraction et affichage des zones géographiques pour le jeu de données "DS_RP_MENAGES_PRINC_IRIS" en anglais
data=pynsee.get_range_geo("DS_RP_MENAGES_PRINC_IRIS",lang="en")

data.info()
data.head()

# %% [markdown]
# ## VI. Utilisation du module polars qui ressemble à du dplyr

# %%
# Importer le module polars que l'on a installé avec la commande "pip install polars" dans le terminal de VSCode
# pl est un alias pour le module polars, qui est une bibliothèque de manipulation de données en Python. Il fournit des structures de données et des fonctions pour travailler avec des tableaux de données, similaires à pandas, mais avec des performances améliorées pour les grands ensembles de données.
import polars as pl

# %% [markdown]
# ### VI.a Importer un jeu de données

# %%
# Extraction du jeu de données "DS_RP_MENAGES_PRINC_IRIS" en sélectionnant la mesure "POP" ou "ONEPERS", le statut conjugal "_T", et l'âge "Y_GE15" avec la fonction get_data du sous-module melodi
POP_IRIS=pynsee.get_data("https://api.insee.fr/melodi/data/DS_RP_MENAGES_PRINC_IRIS?RP_MEASURE=POP&RP_MEASURE=ONEPERS&CIVIL_STATUS=_T&AGE=Y_GE15")

# %% [markdown]
# ### VI.b Filtrer des données

# %%
# Convertir le dataframe pandas en dataframe polars, obligatoire pour utiliser les méthodes/fonctions polars
POP_IRIS=pl.from_pandas(POP_IRIS)

# Filtrer la table POP_IRIS pour garder uniquement la population totale (RP_MEASURE=POP)
POP_IRIS=POP_IRIS.filter(pl.col("RP_MEASURE")=="POP")

# Quelques méthodes dataframe polars

## 5 premières et dernières lignes du dataframe POP_IRIS
POP_IRIS.head(5)
POP_IRIS.tail(5)

## Nombre de lignes et de colonnes du dataframe POP_IRIS
POP_IRIS.shape

## Affiche le type de chaque colonne du dataframe POP_IRIS
POP_IRIS.schema

## Description statistique des colonnes du dataframe POP_IRIS
POP_IRIS.describe()

# %% [markdown]
# ### VI.c Sélectionner des colonnes et renommer une variable

# %%
# Sélectionner les colonnes "TIME_PERIOD", "GEO_OBJECT", "GEO", "LAB_IRIS" et "OBS_VALUE" du dataframe POP_IRIS et renommer la colonne "OBS_VALUE" en "POP_IRIS"
POP_IRIS=POP_IRIS.select("TIME_PERIOD","GEO_OBJECT","GEO","LAB_IRIS","OBS_VALUE").rename({"OBS_VALUE":"POP_IRIS"})  

# %% [markdown]
# ### VI.d Fusion de table

# %%
# Importer les données pour avoir le nombre de personnes ayant un diplôme de niveau Bac+5 ou plus par IRIS
DIPLO_BAC_PLUS_5_OU_PLUS=pynsee.get_data("https://api.insee.fr/melodi/data/DS_RP_DIPLOMES_PRINC_IRIS?SEX=_T&EDUC=700_RP")

# Transformer le dataframe pandas en dataframe polars pour pouvoir utiliser les méthodes/fonctions polars
DIPLO_BAC_PLUS_5_OU_PLUS=pl.from_pandas(DIPLO_BAC_PLUS_5_OU_PLUS)

# Sélectionner uniquement les colonnes d'intérêt dans le dataframe DIPLO_BAC_PLUS_5_OU_PLUS
DIPLO_BAC_PLUS_5_OU_PLUS=DIPLO_BAC_PLUS_5_OU_PLUS.select("TIME_PERIOD","GEO_OBJECT","GEO","LAB_IRIS","OBS_VALUE").rename({"OBS_VALUE":"POP_DIPLO_BAC_PLUS_5_OU_PLUS"})

# Fusionner les deux dataframes POP_IRIS et DIPLO_BAC_PLUS_5_OU_PLUS sur les colonnes TIME_PERIOD, GEO_OBJECT, GEO et LAB_IRIS
POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS=POP_IRIS.join(DIPLO_BAC_PLUS_5_OU_PLUS, on=["TIME_PERIOD","GEO_OBJECT","GEO","LAB_IRIS"], how="inner")

# %% [markdown]
# ### VI.e Créer\modifier une colonne

# %%
# Calculer le pourcentage de personnes ayant un diplôme de niveau Bac+5 ou plus par IRIS et arrondir le résultat à 2 décimales
POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS = (
    POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS
    .filter(pl.col("POP_IRIS") != 0) # Filtrer les lignes où la population totale (POP_IRIS) est différente de zéro pour éviter la division par zéro
    .with_columns(
        (
            pl.col("POP_DIPLO_BAC_PLUS_5_OU_PLUS")
            / pl.col("POP_IRIS")
            * 100 # Calculer le pourcentage de personnes ayant un diplôme de niveau Bac+5 ou plus par IRIS
        )
        .round(2) # Arrondir le résultat à 2 décimales
        .alias("POURCENTAGE_DIPLO_BAC_PLUS_5_OU_PLUS") # Nommer la nouvelle colonne "POURCENTAGE_DIPLO_BAC_PLUS_5_OU_PLUS"
    )
)

# %% [markdown]
# ### VI.f Calculer des indicateurs par groupe, calculer la part de personnes par département qui a un bac + 5 ou plus
# 

# %%
# Calculer le pourcentage de personnes ayant un diplôme de niveau Bac+5 ou plus par département et arrondir le résultat à 2 décimales
POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS_DEP = (
    POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS
    .with_columns(
        # Créer une nouvelle colonne "DEP" qui contient le code du département à partir de la colonne "GEO"
        DEP=pl.when(
            pl.col("GEO").str.starts_with("97") # Pour les départements d'outre-mer (ex: 971, 972, 973, 974, 976)
            | pl.col("GEO").str.starts_with("98")
        )
        .then(
            pl.col("GEO").str.slice(0, 3) # 3 premiers caractères pour l'outre-mer (ex: 971, 975, ...)
        )  
        .otherwise(
            pl.col("GEO").str.slice(0, 2) # 2 premiers caractères pour la métropole (ex: 75, 69)
        ),
    )
    .group_by("DEP") # Grouper par département
    .agg(POP_DEP=pl.col("POP_IRIS").sum(), # Somme population par département, création de la colonne POP_DEP
         DIPLO_DEP=pl.col("POP_DIPLO_BAC_PLUS_5_OU_PLUS").sum()) # Somme bac + 5 ou plus par département, création de la colonne DIPLO_DEP

    .with_columns(
        (
            pl.col("DIPLO_DEP")
            / pl.col("POP_DEP")
            * 100 # Calculer le pourcentage de personnes ayant un diplôme de niveau Bac+5 ou plus par département
        )
        .round(2) # Arrondir le résultat à 2 décimales
        .alias("POURCENTAGE_DIPLO_BAC_PLUS_5_OU_PLUS_DEP") # Nommer la nouvelle colonne "POURCENTAGE_DIPLO_BAC_PLUS_5_OU_PLUS_DEP"
    )
    .sort(by=["POURCENTAGE_DIPLO_BAC_PLUS_5_OU_PLUS_DEP"], descending=[True]))# Trier de manière décroissante par le pourcentage de personnes ayant un diplôme de niveau Bac+5 ou plus par département

# %% [markdown]
# ### VI.g Trier une table

# %%
# Trier POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS par pourcentage décroissant de personnes ayant un diplôme de niveau Bac+5 ou plus
POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS = POP_IRIS_DIPLO_BAC_PLUS_5_OU_PLUS.sort(by=["POURCENTAGE_DIPLO_BAC_PLUS_5_OU_PLUS"], descending=[True])


