# Generated for the initial BiblioIIT catalogue schema.
from django.db import migrations, models
import django.db.models.deletion
from django.db.models import F, Q


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180, verbose_name="Titre")),
                ("author", models.CharField(max_length=150, verbose_name="Auteur")),
                ("isbn", models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name="ISBN")),
                ("category", models.CharField(blank=True, max_length=80, verbose_name="Catégorie")),
                ("description", models.TextField(blank=True, verbose_name="Description")),
                ("publication_year", models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Année de publication")),
                ("total_copies", models.PositiveIntegerField(default=1, verbose_name="Nombre d'exemplaires")),
                ("available_copies", models.PositiveIntegerField(default=1, verbose_name="Exemplaires disponibles")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Ajouté le")),
            ],
            options={"verbose_name": "Livre", "verbose_name_plural": "Livres", "ordering": ["title"]},
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=160, verbose_name="Nom complet")),
                ("email", models.EmailField(max_length=254, unique=True, verbose_name="Adresse e-mail")),
                ("phone", models.CharField(blank=True, max_length=30, verbose_name="Téléphone")),
                ("student_id", models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name="Matricule")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Inscrit le")),
            ],
            options={"verbose_name": "Lecteur", "verbose_name_plural": "Lecteurs", "ordering": ["full_name"]},
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("borrowed_on", models.DateField(auto_now_add=True, verbose_name="Date d'emprunt")),
                ("due_date", models.DateField(verbose_name="Date de retour prévue")),
                ("returned_on", models.DateField(blank=True, null=True, verbose_name="Date de retour effective")),
                ("book", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="loans", to="catalogue.book", verbose_name="Livre")),
                ("member", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="loans", to="catalogue.member", verbose_name="Lecteur")),
            ],
            options={"verbose_name": "Emprunt", "verbose_name_plural": "Emprunts", "ordering": ["-borrowed_on"]},
        ),
        migrations.AddConstraint(
            model_name="book",
            constraint=models.CheckConstraint(condition=Q(available_copies__lte=F("total_copies")), name="available_copies_not_above_total"),
        ),
    ]
