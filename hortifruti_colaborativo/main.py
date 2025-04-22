from cadastro import cadastrar_produtor
from gerenciamento import listar_produtores, editar_produtor, excluir_produtor, listar_ofertas, listar_ofertas_filtradas
from compradores import cadastrar_comprador, listar_compradores_filtrados
from exportacao import exportar_dados_para_json, gerar_relatorio_resumo_json
from db import executar_ddl


def exibir_menu():
    print("\n=== Sistema Hortifruti Colaborativo ===")
    print("1. Cadastrar produtor e oferta")
    print("2. Listar produtores")
    print("3. Editar produtor")
    print("4. Excluir produtor")
    print("5. Listar ofertas")
    print("6. Listar ofertas com filtros")
    print("7. Cadastrar comprador")
    print("8. Listar compradores com filtros")
    print("9. Exportar dados para JSON")
    print("10. Gerar relatório estatístico (JSON)")
    print("11. Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produtor()
        elif opcao == "2":
            listar_produtores()
        elif opcao == "3":
            editar_produtor()
        elif opcao == "4":
            excluir_produtor()
        elif opcao == "5":
            listar_ofertas()
        elif opcao == "6":
            listar_ofertas_filtradas()
        elif opcao == "7":
            cadastrar_comprador()
        elif opcao == "8":
            listar_compradores_filtrados()
        elif opcao == "9":
            exportar_dados_para_json()
        elif opcao == "10":
            gerar_relatorio_resumo_json()
        elif opcao == "11":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    try:
        executar_ddl()
        main()
    except Exception as e:
        print(f"\n Ocorreu um erro inesperado: {e}")
