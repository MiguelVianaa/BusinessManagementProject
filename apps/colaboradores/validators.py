import re
from django.core.exceptions import ValidationError

def valida_nome(nome):
    padrao_nome = re.compile(r'^[A-Za-zÀ-ÿ\s]+$')
    if not nome:
        raise ValidationError('O nome é obrigatório!')
    if not padrao_nome.match(nome):
        raise ValidationError('O nome deve conter apenas letras e espaços!')
    if len(nome.strip()) < 3:
        raise ValidationError('O nome deve ter pelo menos 3 caracteres!')

def valida_idade(idade):
    if not idade:
        raise ValidationError('A idade é obrigatória!')
    if idade < 18:
        raise ValidationError('A idade mínima é 18 anos!')
    if idade > 60:
        raise ValidationError('A idade máxima é 60 anos!')

def valida_telefone(telefone):
    padrao_telefone = re.compile(r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$')
    if not telefone:
        raise ValidationError('O telefone é obrigatório!')
    if not padrao_telefone.match(telefone):
        raise ValidationError('Formato de telefone inválido! Use (99)99999-9999 ou 99999999999')
    if len(telefone.strip()) < 10:
        raise ValidationError('O telefone deve ter pelo menos 10 dígitos!')


def valida_email(email):
    padrao_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not email:
        raise ValidationError('O email é obrigatório!')
    if not padrao_email.match(email):
        raise ValidationError('Email inválido!')
    if len(email) > 254:
        raise ValidationError('O email não pode ter mais que 254 caracteres!')
