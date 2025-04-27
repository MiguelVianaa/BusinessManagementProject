import re
from django.core.exceptions import ValidationError

def valida_nome(nome):
    if not nome:
        raise ValidationError('O nome é obrigatório!')
    if len(nome) < 3:
        raise ValidationError('O nome deve ter pelo menos 3 caracteres!')
    if len(nome) > 100:
        raise ValidationError('O nome deve ter no máximo 100 caracteres!')
    if len(nome.strip().split()) < 2:
        raise ValidationError('Informe o nome completo!')
    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\s]+", nome):
        raise ValidationError('Nome inválido!')

def valida_razao_social(razao_social):
    if not razao_social:
        ValidationError('A razão social é obrigatório!')
    if len(razao_social) < 3:
        raise ValidationError('A razão social deve ter pelo menos 3 caracteres!')
    if len(razao_social) > 100:
        raise ValidationError('A razão social deve ter no máximo 100 caracteres!')
    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ0-9\s]*$', razao_social):
        raise ValidationError('A razão social contém caracteres especiais inválidos!')

def valida_cnpj(cnpj):
    if not cnpj:
        raise ValidationError('O CNPJ é obrigatório!')
    if len(cnpj) != 14:
        raise ValidationError('CNPJ deve ter 14 dígitos!')
    if len(set(cnpj)) == 1:
        raise ValidationError('CNPJ inválido!')

def valida_inscricao_estadual(inscricao_estadual):
    inscricao = str(inscricao_estadual)
    if len(inscricao) < 10:
        raise ValidationError('A inscrição estadual deve ter no mínimo 10 caracteres!')
    if len(inscricao) > 20:
        raise ValidationError('A inscrição estadual deve ter no máximo 20 caracteres!')
    if len(set(inscricao)) == 1:
        raise ValidationError('A inscrição estadual não pode conter apenas números repetidos!')