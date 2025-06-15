from django import forms
from ..models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'idade', 'genero', 'telefone', 'email', 'empresa', 'cargo', 'setor']