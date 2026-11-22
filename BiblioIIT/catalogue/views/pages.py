from django.shortcuts import render
from ..models import Book, Member, Loan


def home(request):
    context = {
        "book_count": Book.objects.count(),
        "member_count": Member.objects.count(),
        "active_loan_count": Loan.objects.filter(returned_on__isnull=True).count(),
        "recent_books": Book.objects.all()[:5],
    }
    return render(request, "catalogue/home.html", context)
