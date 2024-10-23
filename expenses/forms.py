from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'total_amount']

class SplitForm(forms.Form):
    SPLIT_METHODS = [
        ('equal', 'Equal Split'),
        ('percentage', 'Percentage Split'),
        ('exact', 'Exact Amounts'),
    ]
    
    method = forms.ChoiceField(choices=SPLIT_METHODS)
    amounts = forms.CharField(widget=forms.Textarea, help_text="Enter amounts or percentages for each user")
