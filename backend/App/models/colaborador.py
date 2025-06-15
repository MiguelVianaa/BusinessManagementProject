from django.utils import timezone
from django.db import models
from ..validators import colaborador_validators as validators
from ..models import Empresa
from ..models import Cargo
from ..models import Setor


class Colaborador(models.Model):
    nome = models.CharField(max_length=100, validators=[validators.valida_nome])
    idade = models.PositiveIntegerField(validators=[validators.valida_idade])
    genero = models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')])
    telefone = models.CharField(max_length=15, validators=[validators.valida_telefone])
    email = models.EmailField(unique=True, validators=[validators.valida_email])

    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'colaboradores'
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()