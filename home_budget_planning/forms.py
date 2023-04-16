from django import forms
from .models import Expense, Receipt
from .models import ReceiptCategory, ExpenseCategory
from bootstrap_datepicker_plus.widgets import DatePickerInput

class ReceiptCategoryForm(forms.ModelForm):
    class Meta:
        model = ReceiptCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date', 'category', 'photo', 'recurring', 'last_added']
        widgets = {
            'date': DatePickerInput(format='%Y-%m-%d'), # specify the date format
        }

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['description', 'amount', 'date', 'category', 'photo', 'recurring', 'last_added']
        widgets = {
            'date': DatePickerInput(format='%Y-%m-%d'), # specify the date format
        }

