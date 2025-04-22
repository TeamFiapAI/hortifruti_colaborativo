from utils import validar_float, validar_data, validar_telefone, validar_cpf
from db import inserir_produtor, inserir_oferta

def cadastrar_produtor():
    print("\n=== Cadastro de Produtor ===")
    nome = input("Nome do produtor: ").strip()
    cpf_cnpj = validar_cpf(input("CPF (11 dígitos): ").strip())
    cidade = input("Cidade: ").strip()
    contato = validar_telefone(input("Telefone ou WhatsApp (12 dígitos): ").strip())

    produtor_id = inserir_produtor(nome, cpf_cnpj, cidade, contato)

    while True:
        print("\nCadastro de Oferta:")
        produto = input("Nome do produto: ").strip()
        quantidade = validar_float(input("Quantidade disponível (kg): "))
        preco = validar_float(input("Preço sugerido (R$/kg): "))
        data_entrega = validar_data(input("Data disponível para entrega (DD/MM/AAAA): "))

        inserir_oferta(produtor_id, produto, quantidade, preco, data_entrega)

        continuar = input("Deseja adicionar outra oferta? (s/n): ").lower()
        if continuar != 's':
            break

    print("\n✅ Cadastro salvo com sucesso!")
