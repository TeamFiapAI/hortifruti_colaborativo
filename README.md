# hortifruti_colaborativo
Plataforma de Mercado e Logística Colaborativa para Hortifrúti Familiar
# 🌱 Hortifruti Colaborativo

Sistema em Python para ajudar **pequenos produtores rurais** a cadastrar e gerenciar suas ofertas de produtos hortifrutigranjeiros, permitindo também o **cadastro de compradores** e a **visualização filtrada de ofertas**.

Este projeto simula o backend de uma futura Agrotech, voltada para agricultura familiar e economia regional.

---

## 📌 Funcionalidades

✅ Cadastro de produtores com:
- Nome, CPF, cidade, telefone (com validação)
- Registro de múltiplas ofertas (produto, quantidade, preço, data de entrega)

✅ Cadastro de compradores com:
- Nome, CPF, cidade e telefone

✅ Gerenciamento completo de produtores:
- Listar, editar e excluir

✅ Visualização de ofertas:
- Com e sem filtros (por produto, cidade e preço)

✅ Visualização de compradores:
- Com filtros por nome e cidade

---

## 💻 Estrutura do Projeto

hortifruti_colaborativo/ │ ├── main.py # Menu principal do sistema (CLI) ├── cadastro.py # Cadastro de produtores e suas ofertas ├── compradores.py # Cadastro e filtros de compradores ├── gerenciamento.py # Listagem, edição, exclusão e filtros de produtores e ofertas ├── utils.py # Validações e persistência de dados │ ├── data/ │ ├── produtores.json # Dados dos produtores │ ├── compradores.json # Dados dos compradores │ └── configuracoes.json # Reservado para configurações futuras

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12+
- CLI (linha de comando)
- Estruturas de dados: listas, dicionários, JSON
- Organização modular por arquivos
- Validações manuais de CPF, telefone, datas e números

---


