# Comparateur de marché — application console Python

Application console d'analyse de prix issue de fichiers CSV. Elle compare plusieurs boutiques, calcule le total des prix par boutique et signale les offres dont le prix dépasse de plus de 8 % le meilleur prix du même produit.

## Prérequis
- Python 3.10 ou supérieur
- Aucune dépendance externe (bibliothèque standard uniquement)

## Lancer le programme
Depuis le dossier `application-console` :

```bash
# Windows PowerShell
$env:PYTHONPATH = "src"
python -m comparateur

# Linux / macOS
PYTHONPATH=src python -m comparateur
```

Le fichier d'entrée est `data/produits.csv`. Colonnes requises : `produit`, `boutique`, `prix`. Les prix sont exprimés en FCFA et utilisent le point décimal.

## Exécuter les tests

```bash
# Windows PowerShell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v

# Linux / macOS
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Architecture

```text
application-console/
├── data/produits.csv
├── src/comparateur/
│   ├── __main__.py       # Point d'entrée
│   ├── cli.py            # Présentation console
│   ├── models.py         # Entité Price et validation
│   └── service.py        # Lecture CSV et règles métier
├── tests/test_service.py
├── .github/workflows/tests.yml
├── pyproject.toml
└── README.md
```

## Algorithmes et complexité
- `cheapest_by_product` utilise un dictionnaire : parcours en O(n) en moyenne pour n offres.
- `basket_totals` effectue aussi un parcours en O(n).
- `price_alerts` calcule d'abord les meilleurs prix puis parcourt les offres : O(n) en moyenne.

## Règle d'alerte
Une offre est signalée lorsque `prix > meilleur_prix × 1,08`. Le meilleur prix lui-même n'est pas signalé.

## Travail en équipe
Voir `TEAM.md` pour répartir les rôles, noter les membres, les décisions et les contributions. Chaque membre doit travailler sur une branche et proposer une Pull Request avant intégration.

## Versionnement conseillé

```bash
git checkout -b feature/nom-fonctionnalite
git add .
git commit -m "feat: ajouter ..."
git push -u origin feature/nom-fonctionnalite
```

Ne jamais versionner un environnement virtuel, des secrets ou des données personnelles.
