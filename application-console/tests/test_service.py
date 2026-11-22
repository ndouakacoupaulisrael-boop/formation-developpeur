import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from comparateur.models import Price
from comparateur.service import basket_totals, cheapest_by_product, load_prices, price_alerts


class ComparatorTests(unittest.TestCase):
    def setUp(self):
        self.prices = [
            Price("Riz", "A", Decimal("100")),
            Price("Riz", "B", Decimal("110")),
            Price("Riz", "C", Decimal("90")),
            Price("Huile", "A", Decimal("50")),
            Price("Huile", "B", Decimal("55")),
            Price("Huile", "C", Decimal("45")),
        ]

    def test_cheapest_offer_per_product(self):
        result = cheapest_by_product(self.prices)
        self.assertEqual(result["Riz"].store, "C")
        self.assertEqual(result["Huile"].amount, Decimal("45"))

    def test_basket_totals(self):
        result = basket_totals(self.prices)
        self.assertEqual(result["A"], Decimal("150"))
        self.assertEqual(result["C"], Decimal("135"))

    def test_alerts_only_above_eight_percent(self):
        result = price_alerts(self.prices)
        self.assertEqual({price.store for price, _ in result}, {"A", "B"})

    def test_load_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text("produit,boutique,prix\nLivre,A,1200\n", encoding="utf-8")
            result = load_prices(path)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].amount, Decimal("1200"))

    def test_reject_non_positive_price(self):
        with self.assertRaises(ValueError):
            Price("Cahier", "A", Decimal("0"))


if __name__ == "__main__":
    unittest.main()
