from datetime import date, timedelta
from django import forms
from ..models import Loan, Book


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["book", "member", "due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["book"].queryset = Book.objects.filter(available_copies__gt=0)
        self.fields["due_date"].initial = date.today() + timedelta(days=14)
