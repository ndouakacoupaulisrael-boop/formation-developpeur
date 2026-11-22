from decimal import Decimal
from pathlib import Path

from .service import DEFAULT_DATA, basket_totals, cheapest_by_product, load_prices, price_alerts


def _money(value: Decimal) -> str:
    return f"{value.quantize(Decimal('0.01'))} FCFA"


def display_report(path: Path = DEFAULT_DATA) -> None:
    prices = load_prices(path)
    best_offers = cheapest_by_product(prices)
    totals = basket_totals(prices)
    alerts = price_alerts(prices)

    print("\n=== COMPARATEUR DE PRIX ===")
    print(f"Données chargées : {len(prices)} offres\n")
    print("MEILLEURE OFFRE PAR PRODUIT")
    for product, offer in sorted(best_offers.items()):
        print(f"  • {product:<18} {offer.store:<14} {_money(offer.amount)}")

    print("\nTOTAL PAR BOUTIQUE")
    for store, total in sorted(totals.items(), key=lambda item: item[1]):
        print(f"  • {store:<18} {_money(total)}")
    if totals:
        winner = min(totals, key=totals.get)
        print(f"\nBoutique au total le plus bas : {winner} ({_money(totals[winner])})")

    print("\nALERTES (écart supérieur à 8 % du meilleur prix)")
    if not alerts:
        print("  Aucune alerte.")
    else:
        for offer, percent in alerts:
            print(f"  ! {offer.product} chez {offer.store} : +{percent.quantize(Decimal('0.1'))} %")
    print("\nAnalyse terminée.\n")


def main() -> None:
    try:
        display_report()
    except (OSError, ValueError) as error:
        print(f"Erreur : {error}")
        raise SystemExit(1) from error
