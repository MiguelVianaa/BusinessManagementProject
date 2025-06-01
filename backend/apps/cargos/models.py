from django.utils import timezone
from django.db import models
from . import validators

class Cargo(models.Model):
    nome = models.CharField(max_length=50, unique=True, validators=[validators.valida_nome_cargo])
    descricao = models.CharField(max_length=300, validators=[validators.valida_descricao])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'cargos'

    def __str__(self):
        return self.nome

    def delete(self, *args, **kwargs):
        from apps.colaboradores.models import Colaborador

        Colaborador.objects.filter(cargo=self).update(cargo=None)
        self.deleted_at = timezone.now()
        self.save()