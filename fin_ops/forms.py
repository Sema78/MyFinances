from django import forms
from django.forms import ModelForm
from .models import FinOperation

class FinOperationForm(ModelForm):
    class Meta:
        model = FinOperation
        # fields = '__all__' - can write if we use all fields
        fields = ('wallet_account', 'op_category', 'is_expanses', 'sum', 'comment')
        