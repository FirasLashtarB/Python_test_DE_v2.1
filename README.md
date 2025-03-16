# Data Pipeline Project

##  Installation
1. **Cloner le projet ou télécharger l’archive ZIP**
   git clone https://github.com/ton-utilisateur/ton-repo.git
   cd data_pipeline_project
 
2. **Créer un environnement virtuel (recommandé)**
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows

3. **Installer les dépendances**
   pip install -r requirements.txt

---

##  Exécution du pipeline
1. **Assurez-vous que les fichiers de données sont bien placés dans `data/`**.
2. **Lancer le pipeline** :
   python main.py

3. **Le fichier de sortie `output.json` sera généré dans `tests/`**.

##  Tests
- Vous pouvez exécuter les modules individuellement pour vérifier leur bon fonctionnement :
   python -m src.data_loader
   python -m src.data_cleaner
   python -m src.data_processor
   python -m src.output_generator
- Vérifiez que `output.json` contient bien les relations attendues.

---
Question 4: 
## ad-hoc (`adhoc.py`)
Le fichier `adhoc.py` permet d'effectuer des analyses supplémentaires sur les données traitées. Deux fonctionnalités principales sont disponibles :

**Trouver le journal qui mentionne le plus de médicaments différents**
python src/adhoc.py
Affiche le journal ayant le plus grand nombre de médicaments référencés.

**Trouver les médicaments liés à un médicament donné** (dans PubMed uniquement)
python src/adhoc.py --drug "Diphenhydramine"
Renvoie la liste des médicaments mentionnés dans les mêmes journaux que le médicament donné.

---

## Question 6
- Ajout de logs et d’une gestion des erreurs plus robuste.
- Intégration dans un orchestrateur comme Airflow.
-  Modifications à apporter pour gérer de grosses volumétries de données (To/millions de fichiers): 
    * Lecture par batch avec chunksize pour éviter la surcharge mémoire.
    * Utilisation de Spark (PySpark) ou Dask pour un traitement distribué.