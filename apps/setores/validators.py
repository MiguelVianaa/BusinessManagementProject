from django.core.exceptions import ValidationError

def valida_nome_setor(nome):
    if not nome:
        raise ValidationError('O nome do setor é obrigatório!')
    if not nome or nome.isspace():
        raise ValidationError('O nome do setor não pode estar vazio!')
    if len(nome) < 3:
        raise ValidationError('O nome do setor deve ter pelo menos 3 caracteres!')
    if len(nome) > 100:
        raise ValidationError('O nome do setor deve ter no máximo 100 caracteres!')

def valida_descricao(descricao):
    if not descricao:
        raise ValidationError('A descrição é obrigatória!')
    if not descricao or descricao.isspace():
        raise ValidationError('A descrição não pode estar vazia!')
    if len(descricao) > 100:
        raise ValidationError('A descrição deve ter no máximo 100 caracteres!')
