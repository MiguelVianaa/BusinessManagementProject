from django import forms
from ..models import setor

class SetorForm(forms.ModelForm):
    class Meta:
        model = setor
        fields = ['nome', 'descricao']