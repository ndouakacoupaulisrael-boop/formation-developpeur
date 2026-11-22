import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable

from .models import Price

ALERT_THRESHOLD = Decimal("0.08")
DEFAULT_DATA = Path(__file__).resolve().parents[2] / "data" / "produits.csv"


def load_prices(path: Path = DEFAULT_DATA) -> list[Price]:
    """Charge et valide les prix depuis un fichier CSV UTF-8."""
    if not path.exists():
        raise FileNotFoundError(f"Fichier de données introuvable : {path}")
    prices: list[Price] = []
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = {"produit", "boutique", "prix"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError("Le CSV doit contenir les colonnes produit,boutique,prix.")
        for line_number, row in enumerate(reader, start=2):
            try:
                amount = Decimal((row["prix"] or "").strip().replace(",", "."))
                prices.append(Price((row["produit"] or "").strip(), (row["boutique"] or "").strip(), amount))
            except (InvalidOperation, ValueError, AttributeError) as exc:
                raise ValueError(f"Donnée invalide à la ligne {line_number}.") from exc
    if not prices:
        raise ValueError("Le fichier CSV ne contient aucun prix.")
    return prices


def cheapest_by_product(prices: Iterable[Price]) -> dict[str, Price]:
    """Retourne l'offre la moins chère pour chaque produit (parcours linéaire)."""
    cheapest: dict[str, Price] = {}
    for price in prices:
        current = cheapest.get(price.product)
        if current is None or price.amount < current.amount:
            cheapest[price.product] = price
    return cheapest


def basket_totals(prices: Iterable[Price]) -> dict[str, Decimal]:
    """Additionne les prix de chaque boutique pour les produits qu'elle propose."""
    totals: dict[str, Decimal] = defaultdict(Decimal)
    for price in prices:
        totals[price.store] += price.amount
    return dict(totals)


def price_alerts(prices: Iterable[Price], threshold: Decimal = ALERT_THRESHOLD) -> list[tuple[Price, Decimal]]:
    """Signale les prix strictement supérieurs au meilleur prix de plus que le seuil."""
    materialized = list(prices)
    cheapest = cheapest_by_product(materialized)
    alerts: list[tuple[Price, Decimal]] = []
    for price in materialized:
        best = cheapest[price.product].amount
        if price.amount > best * (Decimal("1") + threshold):
            difference = (price.amount - best) / best * Decimal("100")
            alerts.append((price, difference))
    return alerts
