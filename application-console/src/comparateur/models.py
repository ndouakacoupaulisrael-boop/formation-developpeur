from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Price:
    product: str
    store: str
    amount: Decimal

    def __post_init__(self) -> None:
        if not self.product.strip() or not self.store.strip():
            raise ValueError("Le produit et la boutique sont obligatoires.")
        if self.amount <= 0:
            raise ValueError("Le prix doit être strictement positif.")
