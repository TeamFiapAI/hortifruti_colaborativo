
import json
import os
from datetime import datetime

def validar_float(valor):
    try:
        return float(valor)
    except ValueError:
        print("Valor inválido. Use ponto para casas decimais. Tente novamente.")
        return validar_float(input("Digite novamente: "))

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return data_str
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")
        return validar_data(input("Digite novamente: "))

def validar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))
    if len(telefone) not in [12, 13]:
        print("Telefone inválido. Deve conter 12 ou 13 dígitos (DDI + DDD + número).")
        return validar_telefone(input("Digite novamente: "))
    return telefone

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        print("CPF inválido. Deve conter 11 dígitos.")
        return validar_cpf(input("Digite novamente: "))
    return cpf
