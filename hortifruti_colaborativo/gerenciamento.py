from db import (
    buscar_todos_produtores,
    buscar_produtor_por_id,
    atualizar_produtor,
    deletar_produtor,
    buscar_ofertas,
    buscar_ofertas_filtradas
)
from utils import validar_telefone, validar_cpf


def listar_produtores():
    produtores = buscar_todos_produtores()
    if not produtores:
        print("\nNenhum produtor cadastrado ainda.")
        return []

    print("\n=== Lista de Produtores Cadastrados ===")
    for idx, (produtor_id, nome, cidade) in enumerate(produtores, start=1):
        print(f"{idx}. {nome} - {cidade}")
    return produtores


def editar_produtor():
    produtores = listar_produtores()
    if not produtores:
        return

    try:
        escolha = int(input("\nDigite o número do produtor que deseja editar: ")) - 1
        if escolha < 0 or escolha >= len(produtores):
            print("Escolha inválida.")
            return
        produtor_id = produtores[escolha][0]
    except ValueError:
        print("Entrada inválida.")
        return

    produtor = buscar_produtor_por_id(produtor_id)
    if not produtor:
        print("Produtor não encontrado.")
        return

    nome, cpf_cnpj, cidade, contato = produtor

    novo_nome = input(f"Novo nome ({nome}): ").strip() or nome
    novo_cpf = input(f"Novo CPF ({cpf_cnpj}): ").strip() or cpf_cnpj
    nova_cidade = input(f"Nova cidade ({cidade}): ").strip() or cidade
    novo_contato = input(f"Novo contato ({contato}): ").strip() or contato

    atualizar_produtor(produtor_id, novo_nome, novo_cpf, nova_cidade, novo_contato)
    print("✅ Produtor atualizado com sucesso.")


def excluir_produtor():
    produtores = listar_produtores()
    if not produtores:
        return

    try:
        escolha = int(input("\nDigite o número do produtor que deseja excluir: ")) - 1
        if escolha < 0 or escolha >= len(produtores):
            print("Escolha inválida.")
            return
        produtor_id = produtores[escolha][0]
    except ValueError:
        print("Entrada inválida.")
        return

    deletar_produtor(produtor_id)
    print("✅ Produtor e suas ofertas foram removidos com sucesso.")


def listar_ofertas():
    ofertas = buscar_ofertas()
    if not ofertas:
        print("\nNenhuma oferta cadastrada.")
        return

    print("\n=== Ofertas Cadastradas ===")
    for produto, quantidade, preco, data_entrega, nome_produtor, cidade in ofertas:
        print(f"- {produto} | {quantidade} kg | R$ {preco:.2f}/kg | Entrega: {data_entrega} | Produtor: {nome_produtor} ({cidade})")


def listar_ofertas_filtradas():
    cidade_filtro = input("Filtrar por cidade (ou Enter para ignorar): ").strip().lower()
    produto_filtro = input("Filtrar por produto (ou Enter para ignorar): ").strip().lower()
    preco_max_input = input("Filtrar por preço máximo (ou Enter para ignorar): ").strip()

    try:
        preco_max = float(preco_max_input) if preco_max_input else None
    except ValueError:
        print("Preço máximo inválido. Ignorando filtro de preço.")
        preco_max = None

    ofertas = buscar_ofertas_filtradas(cidade_filtro, produto_filtro, preco_max)
    if not ofertas:
        print("Nenhuma oferta encontrada com os filtros fornecidos.")
        return

    print("\n=== Ofertas Filtradas ===")
    for produto, quantidade, preco, data_entrega, nome_produtor, cidade in ofertas:
        print(f"- {produto} | {quantidade} kg | R$ {preco:.2f}/kg | Entrega: {data_entrega} | Produtor: {nome_produtor} ({cidade})")
