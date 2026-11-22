from django.db import models
from .book import Book
from .member import Member


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="loans", verbose_name="Livre")
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="loans", verbose_name="Lecteur")
    borrowed_on = models.DateField("Date d'emprunt", auto_now_add=True)
    due_date = models.DateField("Date de retour prévue")
    returned_on = models.DateField("Date de retour effective", null=True, blank=True)

    class Meta:
        ordering = ["-borrowed_on"]
        verbose_name = "Emprunt"
        verbose_name_plural = "Emprunts"

    def __str__(self):
        return f"{self.book.title} — {self.member.full_name}"

    @property
    def is_returned(self):
        return self.returned_on is not None
