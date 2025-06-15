from django.core.exceptions import ValidationError

def valida_nome_cargo(nome_cargo):
    if len(nome_cargo) > 50:
        raise ValidationError('O nome do cargo não pode ter mais que 50 caracteres!')
    if len(nome_cargo.strip()) < 3:
        raise ValidationError('O nome do cargo deve ter pelo menos 3 caracteres!')

def valida_descricao(descricao):
    if len(descricao.strip()) < 3:
        raise ValidationError('A descrição deve ter pelo menos 3 caracteres!')
    if len(descricao) > 300:
        raise ValidationError('A descrição não pode ter mais que 300 caracteres!')
