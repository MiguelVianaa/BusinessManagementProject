from django.utils import timezone
from django.db import models
from ..validators import setor_validators as validators

class Setor(models.Model):
    nome = models.CharField(max_length=100, unique=True, validators=[validators.valida_nome_setor])
    descricao = models.CharField(max_length=100, validators=[validators.valida_descricao])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'setores'
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.nome

    def delete(self, *args, **kwargs):
        from ..models import Setor

        Setor.objects.filter(setor=self).update(setor=None)
        self.deleted_at = timezone.now()
        self.save()