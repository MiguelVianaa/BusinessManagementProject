from django.utils import timezone
from django.db import models
from . import validators

class Empresa(models.Model):
    nome = models.CharField(max_length=100, unique=True, validators=[validators.valida_nome])
    razao_social = models.CharField(max_length=100, unique=True, validators=[validators.valida_razao_social])
    cnpj = models.CharField(max_length=14, unique=True, validators=[validators.valida_cnpj])
    inscricao_estadual = models.CharField(max_length=20, unique=True, validators=[validators.valida_inscricao_estadual])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    setores = models.ManyToManyField('setores.Setor', through='EmpresaSetor', related_name='empresas')

    class Meta:
        db_table = 'empresas'

    def __str__(self):
        return self.razao_social

    def delete(self, *args, **kwargs):
        from apps.colaboradores.models import Colaborador
        Colaborador.objects.filter(empresa=self).update(empresa=None)
        self.deleted_at = timezone.now()
        self.save()


class EmpresaSetor(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_setores')
    setor = models.ForeignKey('setores.Setor', on_delete=models.CASCADE, related_name='setor_empresas')

    class Meta:
        db_table = 'empresa_setores'
        unique_together = ('empresa', 'setor')