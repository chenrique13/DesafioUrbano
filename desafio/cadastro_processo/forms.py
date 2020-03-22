from django import forms

from .models import cadProcesso

class cadForm(forms.ModelForm):
    class Meta:
        model = cadProcesso
        fields = ('nome','cliente')
# ,'arquivo'