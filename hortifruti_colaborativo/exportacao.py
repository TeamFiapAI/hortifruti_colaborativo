import json
import os
from db import buscar_todos_produtores, buscar_ofertas, buscar_compradores_filtrados

def exportar_dados_para_json():
    produtores = buscar_todos_produtores()
    compradores = buscar_compradores_filtrados()
    ofertas = buscar_ofertas()

    os.makedirs("relatorios", exist_ok=True)

    with open("relatorios/export_produtores.json", "w", encoding="utf-8") as f:
        json.dump(produtores, f, ensure_ascii=False, indent=4)

    compradores_formatados = [
        {
            "id": c[0],
            "nome": c[1],
            "cpf": c[2],
            "cidade": c[3],
            "contato": c[4]
        }
        for c in compradores
    ]
    with open("relatorios/export_compradores.json", "w", encoding="utf-8") as f:
        json.dump(compradores_formatados, f, ensure_ascii=False, indent=4)

    ofertas_formatadas = [
        {
            "id": o[0],
            "produto": o[1],
            "quantidade": o[2],
            "preco": o[3],
            "data_entrega": o[4],
            "nome_produtor": o[5],
            "cidade_produtor": o[6]
        }
        for o in ofertas
    ]
    with open("relatorios/export_ofertas.json", "w", encoding="utf-8") as f:
        json.dump(ofertas_formatadas, f, ensure_ascii=False, indent=4)

    print("Dados exportados com sucesso para a pasta 'relatorios/'.")


def gerar_relatorio_resumo_json():
    produtores = buscar_todos_produtores()
    compradores = buscar_compradores_filtrados()
    ofertas = buscar_ofertas()

    total_produtores = len(produtores)
    total_compradores = len(compradores)
    total_ofertas = len(ofertas)

    media_preco = 0
    if total_ofertas > 0:
        media_preco = sum(oferta[2] for oferta in ofertas) / total_ofertas

    relatorio = {
        "total_produtores": total_produtores,
        "total_compradores": total_compradores,
        "total_ofertas": total_ofertas,
        "media_preco_ofertas": round(media_preco, 2)
    }

    os.makedirs("relatorios", exist_ok=True)

    with open("relatorios/relatorio_resumo.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=4)

    print("Relatório estatístico salvo como relatorios/relatorio_resumo.json.")
