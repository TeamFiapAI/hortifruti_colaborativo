
import json
import os
from utils import validar_cpf, validar_telefone

CAMINHO_ARQUIVO = "data/compradores.json"

def carregar_dados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def cadastrar_comprador():
    comprador = {}
    comprador['nome'] = input("Nome do comprador: ").strip()
    comprador['cpf'] = validar_cpf(input("CPF: ").strip())
    comprador['cidade'] = input("Cidade: ").strip()
    comprador['contato'] = validar_telefone(input("Telefone (12 dígitos): ").strip())

    dados = carregar_dados()
    dados.append(comprador)
    salvar_dados(dados)
    print("\n✅ Comprador cadastrado com sucesso!")

def listar_compradores_filtrados():
    dados = carregar_dados()
    if not dados:
        print("\nNenhum comprador cadastrado.")
        return

    cidade_filtro = input("Filtrar por cidade (ou Enter para ignorar): ").strip().lower()
    nome_filtro = input("Filtrar por nome (ou Enter para ignorar): ").strip().lower()

    print("\n=== Compradores Cadastrados ===")
    for comprador in dados:
        if cidade_filtro and cidade_filtro not in comprador['cidade'].lower():
            continue
        if nome_filtro and nome_filtro not in comprador['nome'].lower():
            continue
        print(f"- {comprador['nome']} | CPF: {comprador['cpf']} | {comprador['cidade']} | Contato: {comprador['contato']}")
