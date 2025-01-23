from django.core.exceptions import ValidationError

def validate_cpf(value):
    cpf=''.join([char for char in value if char.isdigit()])
    if len(cpf)!=11:
        raise ValidationError('CPF Invalido')
    if cpf==cpf[0]*11:
        raise ValidationError('CPF Invalido')