from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.home, name="home"),
    path("livres/", views.book_list, name="books"),
    path("livres/<int:pk>/", views.book_detail, name="book_detail"),
    path("emprunts/", views.loan_list, name="loans"),
    path("emprunts/nouveau/", views.loan_create, name="loan_create"),
    path("emprunts/<int:pk>/retour/", views.loan_return, name="loan_return"),
]
