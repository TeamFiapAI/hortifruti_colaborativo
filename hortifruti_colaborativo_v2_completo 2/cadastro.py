
import json
import os
from utils import validar_float, validar_data, validar_telefone, validar_cpf, salvar_json

CAMINHO_ARQUIVO = "data/produtores.json"

def cadastrar_produtor():
    produtor = {}
    produtor['nome'] = input("Nome do produtor: ").strip()
    produtor['cpf_cnpj'] = validar_cpf(input("CPF (11 dígitos): ").strip())
    produtor['cidade'] = input("Cidade: ").strip()
    produtor['contato'] = validar_telefone(input("Telefone ou WhatsApp (12 dígitos): ").strip())

    ofertas = []
    while True:
        print("\nCadastro de Oferta:")
        produto = input("Nome do produto: ").strip()
        quantidade = validar_float(input("Quantidade disponível (kg): "))
        preco = validar_float(input("Preço sugerido (R$/kg): "))
        data_entrega = validar_data(input("Data disponível para entrega (DD/MM/AAAA): "))

        oferta = {
            "produto": (produto, "kg"),  # tupla com nome e unidade
            "quantidade": quantidade,
            "preco": preco,
            "data_entrega": data_entrega
        }

        ofertas.append(oferta)

        continuar = input("Deseja adicionar outra oferta? (s/n): ").lower()
        if continuar != 's':
            break

    produtor['ofertas'] = ofertas
    salvar_json(CAMINHO_ARQUIVO, produtor)
    print("\n✅ Cadastro salvo com sucesso!")
