# 🌱 Hortifruti Colaborativo

Plataforma de Mercado e Logística Colaborativa para Hortifrúti Familiar

Sistema em Python que auxilia **pequenos produtores rurais** no cadastro e gerenciamento de suas ofertas de produtos hortifrutigranjeiros, permitindo também o **cadastro de compradores** e a **visualização filtrada de ofertas**.

Este projeto simula o backend de uma futura Agrotech voltada para agricultura familiar e economia regional.

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

✅ Persistência de dados em banco Oracle:  
- Todas as informações são salvas e consultadas diretamente no banco de dados, sem uso de arquivos locais  

---

## 📁 Estrutura do Projeto

hortifruti_colaborativo/
├── main.py          # Menu principal do sistema (CLI)
├── cadastro.py      # Cadastro de produtores e suas ofertas
├── compradores.py   # Cadastro e filtros de compradores
├── gerenciamento.py # Listagem, edição, exclusão e filtros de produtores e ofertas
├── db.py            # Conexão e acesso ao banco de dados Oracle
├── utils.py         # Validações de dados (CPF, telefone, datas, etc.)
└── config.json      # Configurações de conexão com o banco Oracle

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12+  
- Interface via linha de comando (CLI)  
- Módulo `oracledb` para integração com banco de dados Oracle  
- Programação modular (separação por responsabilidade)  
- Validações personalizadas para CPF, telefone, datas e valores numéricos