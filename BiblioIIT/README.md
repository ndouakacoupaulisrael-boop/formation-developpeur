# BiblioIIT — gestion de bibliothèque

Application web Django pour consulter un catalogue et gérer les emprunts.

## Prérequis
- Python 3.12 ou plus récent (Python 3.13 convient)
- Git (facultatif pour le lancement, recommandé pour le versionnement)

## Installation sous Windows (PowerShell)

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py check
python manage.py makemigrations catalogue
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvre ensuite http://127.0.0.1:8000/ et l'administration sur http://127.0.0.1:8000/admin/.

Si PowerShell bloque l'activation, exécute temporairement dans ce terminal :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Fonctionnalités de cette première version
- Tableau de bord avec statistiques
- Catalogue, recherche et fiche d'un livre
- Gestion des livres et des lecteurs dans l'administration Django
- Création d'un emprunt avec vérification du stock disponible
- Liste des emprunts et enregistrement d'un retour

## Architecture
- `config/` : configuration générale et URL du projet
- `catalogue/models/` : modèles Livre, Lecteur et Emprunt
- `catalogue/views/` : contrôleurs (fonctions de vues Django)
- `catalogue/admin/` : configuration de l'administration
- `catalogue/forms/` : formulaires
- `catalogue/templates/` : gabarits HTML
- `catalogue/urls.py` : URL propres à l'application

## Commandes utiles

```powershell
python manage.py makemigrations catalogue
python manage.py migrate
python manage.py runserver
python manage.py check
```

La base SQLite (`db.sqlite3`) est créée localement par Django. Ne partage jamais le mot de passe du superutilisateur ni le fichier `.env` s'il en existe un.
