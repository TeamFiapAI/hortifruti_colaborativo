from utils import validar_cpf, validar_telefone
from db import inserir_comprador, buscar_compradores_filtrados

def cadastrar_comprador():
    print("\n=== Cadastro de Comprador ===")
    nome = input("Nome do comprador: ").strip()
    cpf = validar_cpf(input("CPF: ").strip())
    cidade = input("Cidade: ").strip()
    contato = validar_telefone(input("Telefone (12 dígitos): ").strip())

    inserir_comprador(nome, cpf, cidade, contato)
    print("\n✅ Comprador cadastrado com sucesso!")


def listar_compradores_filtrados():
    print("\n=== Filtro de Compradores ===")
    cidade_filtro = input("Filtrar por cidade (ou Enter para ignorar): ").strip().lower()
    nome_filtro = input("Filtrar por nome (ou Enter para ignorar): ").strip().lower()

    compradores = buscar_compradores_filtrados(cidade_filtro, nome_filtro)
    if not compradores:
        print("\nNenhum comprador encontrado com os filtros fornecidos.")
        return

    print("\n=== Compradores Cadastrados ===")
    for nome, cpf, cidade, contato in compradores:
        print(f"- {nome} | CPF: {cpf} | {cidade} | Contato: {contato}")
