from datetime import date
from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from ..forms import LoanForm
from ..models import Loan, Book


def loan_list(request):
    loans = Loan.objects.select_related("book", "member").all()
    return render(request, "catalogue/loan_list.html", {"loans": loans})


def loan_create(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                selected_book = form.cleaned_data["book"]
                book = Book.objects.select_for_update().get(pk=selected_book.pk)
                if book.available_copies < 1:
                    form.add_error("book", "Ce livre n'est plus disponible.")
                else:
                    book.available_copies -= 1
                    book.save(update_fields=["available_copies"])
                    loan = form.save(commit=False)
                    loan.book = book
                    loan.save()
                    messages.success(request, "Emprunt enregistré avec succès.")
                    return redirect("catalogue:loans")
    else:
        form = LoanForm()
    return render(request, "catalogue/loan_form.html", {"form": form})


@require_POST
def loan_return(request, pk):
    with transaction.atomic():
        loan = get_object_or_404(Loan.objects.select_for_update().select_related("book"), pk=pk)
        if loan.returned_on is None:
            loan.returned_on = date.today()
            loan.save(update_fields=["returned_on"])
            book = Book.objects.select_for_update().get(pk=loan.book_id)
            book.available_copies = min(book.available_copies + 1, book.total_copies)
            book.save(update_fields=["available_copies"])
            messages.success(request, "Retour du livre enregistré.")
        else:
            messages.info(request, "Cet emprunt est déjà clôturé.")
    return redirect("catalogue:loans")
