from django import forms
from ..models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'razao_social', 'cnpj', 'inscricao_estadual', 'telefone', 'email']