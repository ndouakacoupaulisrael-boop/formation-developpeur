from django.db import models


class Member(models.Model):
    full_name = models.CharField("Nom complet", max_length=160)
    email = models.EmailField("Adresse e-mail", unique=True)
    phone = models.CharField("Téléphone", max_length=30, blank=True)
    student_id = models.CharField("Matricule", max_length=40, unique=True, blank=True, null=True)
    created_at = models.DateTimeField("Inscrit le", auto_now_add=True)

    class Meta:
        ordering = ["full_name"]
        verbose_name = "Lecteur"
        verbose_name_plural = "Lecteurs"

    def __str__(self):
        return self.full_name
