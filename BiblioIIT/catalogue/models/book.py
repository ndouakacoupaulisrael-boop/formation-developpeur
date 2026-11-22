from django.db import models
from django.db.models import F, Q


class Book(models.Model):
    title = models.CharField("Titre", max_length=180)
    author = models.CharField("Auteur", max_length=150)
    isbn = models.CharField("ISBN", max_length=20, unique=True, blank=True, null=True)
    category = models.CharField("Catégorie", max_length=80, blank=True)
    description = models.TextField("Description", blank=True)
    publication_year = models.PositiveSmallIntegerField("Année de publication", null=True, blank=True)
    total_copies = models.PositiveIntegerField("Nombre d'exemplaires", default=1)
    available_copies = models.PositiveIntegerField("Exemplaires disponibles", default=1)
    created_at = models.DateTimeField("Ajouté le", auto_now_add=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        constraints = [
            models.CheckConstraint(
                condition=Q(available_copies__lte=F("total_copies")),
                name="available_copies_not_above_total",
            )
        ]

    def __str__(self):
        return f"{self.title} — {self.author}"
