
import json
import os

CAMINHO_ARQUIVO = "data/produtores.json"

def carregar_dados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def listar_produtores():
    dados = carregar_dados()
    if not dados:
        print("\nNenhum produtor cadastrado ainda.")
        return
    print("\n=== Lista de Produtores Cadastrados ===")
    for idx, produtor in enumerate(dados, 1):
        print(f"{idx}. {produtor['nome']} - {produtor['cidade']}")

def editar_produtor():
    dados = carregar_dados()
    listar_produtores()
    try:
        escolha = int(input("\nDigite o número do produtor que deseja editar: ")) - 1
        if escolha < 0 or escolha >= len(dados):
            print("Escolha inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    produtor = dados[escolha]
    print(f"Editando produtor: {produtor['nome']}")
    produtor['nome'] = input(f"Novo nome ({produtor['nome']}): ") or produtor['nome']
    produtor['cpf_cnpj'] = input(f"Novo CPF ({produtor['cpf_cnpj']}): ") or produtor['cpf_cnpj']
    produtor['cidade'] = input(f"Nova cidade ({produtor['cidade']}): ") or produtor['cidade']
    produtor['contato'] = input(f"Novo contato ({produtor['contato']}): ") or produtor['contato']

    salvar_dados(dados)
    print("✅ Produtor atualizado com sucesso.")

def excluir_produtor():
    dados = carregar_dados()
    listar_produtores()
    try:
        escolha = int(input("\nDigite o número do produtor que deseja excluir: ")) - 1
        if escolha < 0 or escolha >= len(dados):
            print("Escolha inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    produtor = dados.pop(escolha)
    salvar_dados(dados)
    print(f"✅ Produtor '{produtor['nome']}' removido com sucesso.")

def listar_ofertas():
    dados = carregar_dados()
    print("\n=== Ofertas Cadastradas ===")
    for produtor in dados:
        nome = produtor['nome']
        cidade = produtor['cidade']
        for oferta in produtor.get('ofertas', []):
            print(f"- {oferta['produto']} | {oferta['quantidade']} kg | R$ {oferta['preco']:.2f}/kg | Entrega: {oferta['data_entrega']} | Produtor: {nome} ({cidade})")

def listar_ofertas_filtradas():
    dados = carregar_dados()
    cidade_filtro = input("Filtrar por cidade (ou Enter para ignorar): ").strip().lower()
    produto_filtro = input("Filtrar por produto (ou Enter para ignorar): ").strip().lower()
    preco_max = input("Filtrar por preço máximo (ou Enter para ignorar): ").strip()

    try:
        preco_max = float(preco_max) if preco_max else None
    except ValueError:
        print("Preço máximo inválido. Ignorando filtro de preço.")
        preco_max = None

    print("\n=== Ofertas Filtradas ===")
    for produtor in dados:
        nome = produtor['nome']
        cidade = produtor['cidade']
        if cidade_filtro and cidade_filtro not in cidade.lower():
            continue
        for oferta in produtor.get('ofertas', []):
            if produto_filtro and produto_filtro not in oferta['produto'].lower():
                continue
            if preco_max is not None and oferta['preco'] > preco_max:
                continue
            print(f"- {oferta['produto']} | {oferta['quantidade']} kg | R$ {oferta['preco']:.2f}/kg | Entrega: {oferta['data_entrega']} | Produtor: {nome} ({cidade})")
