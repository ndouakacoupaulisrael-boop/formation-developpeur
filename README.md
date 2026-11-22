# Travaux pratiques — Développement web et Python

Dépôt de travail regroupant les livrables préparés à partir des consignes du cours.

## Contenu

| Dossier / fichier | Livrable | Description |
|---|---|---|
| `index.html`, `style.css`, `script.js`, `cv.html` | Portfolio personnel | Site one-page responsive : introduction, compétences, projets, formation et contact. |
| `application-console/` | Application console en équipe | Comparateur de prix Python, CSV, règles métier, tests unitaires et workflow CI. |
| `BiblioIIT/` | Application web Django | Gestion de catalogue, lecteurs, emprunts et retours, architecture séparée en modèles, vues, formulaires, administration et URL. |

## Démarrage rapide

### Portfolio
Ouvrir `index.html` dans un navigateur. Aucun serveur ni dépendance n'est requis. Le fichier `cv.html` peut être imprimé en PDF depuis le navigateur.

### Application console
Depuis `application-console/` :

```powershell
$env:PYTHONPATH = "src"
python -m comparateur
python -m unittest discover -s tests -v
```

### BiblioIIT (Django)
Depuis `BiblioIIT/` :

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py check
python manage.py makemigrations catalogue
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Avant remise

- Remplacer / compléter les coordonnées manquantes du portfolio (e-mail, téléphone et URL LinkedIn exacts).
- Compléter `application-console/TEAM.md` avec les vrais noms et contributions de l'équipe.
- Exécuter les tests sur la machine de remise et capturer les résultats.
- Vérifier que les fichiers finaux sont bien poussés sur GitHub.
- Ajouter le professeur comme collaborateur du dépôt depuis **Settings → Collaborators → Add people** avec le pseudo `Sedrickgael`.

## Versionnement Git conseillé

```bash
git status
git add .
git commit -m "feat: ajouter les livrables portfolio et applications"
git push
```

Ne jamais committer les mots de passe, jetons d'accès, environnements virtuels ou bases de données personnelles.
