import random

def gera_cpf():
    def calcula_digito(cpf_parcial):
        soma = 0
        peso = 10
        for digito in cpf_parcial:
            soma += int(digito) * peso
            peso -= 1
        resto = soma % 11
        if resto < 2:
            return '0'
        else:
            return str(11 - resto)
    
    cpf_base = [random.randint(0, 9) for _ in range(9)]
    
    # Calcula o primeiro dígito verificador
    cpf_base.append(calcula_digito(cpf_base))
    
    # Calcula o segundo dígito verificador
    cpf_base.append(calcula_digito(cpf_base))
    
    return ''.join(map(str, cpf_base))

# Gerar um CPF aleatório
cpf_aleatorio = gera_cpf()
print("CPF gerado aleatoriamente:", cpf_aleatorio)
