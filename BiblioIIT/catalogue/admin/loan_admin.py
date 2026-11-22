from django.contrib import admin
from ..models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "member", "borrowed_on", "due_date", "returned_on")
    list_filter = ("borrowed_on", "due_date", "returned_on")
    search_fields = ("book__title", "member__full_name", "member__email")
