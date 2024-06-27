from django import forms
from .models import *

class SendForm(forms.ModelForm):
    class Meta:
        model = SendModel
        fields = '__all__'