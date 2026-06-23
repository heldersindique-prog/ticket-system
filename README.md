# HelderLab - Sistema de Tickets Help Desk

Sistema web de gestao de tickets de suporte IT, desenvolvido em Python/Flask com interface grafica completa.

## Funcionalidades

- Criacao de tickets com titulo, categoria e descricao
- Classificacao automatica de prioridade por categoria
- Painel com contadores em tempo real
- Fila de tickets com estado e historico completo
- Fecho de tickets com registo de resolucao
- API REST para estatisticas em JSON

## Tecnologias

- Python 3.12 / Flask / Gunicorn
- SQLite
- HTML/CSS/JS

## Categorias e Prioridades

Rede e Acesso: P1 Critico
Hardware e Software: P2 Alto
Impressora: P3 Normal

## Instalacao

git clone https://github.com/heldersindique-prog/ticket-system
cd ticket-system
python3 -m venv venv
source venv/bin/activate
pip install flask gunicorn
python3 app.py

Aceder em http://localhost:5000

## Estrutura

app.py - Backend Flask e rotas
models.py - Base de dados SQLite
templates/index.html - Painel principal
templates/novo.html - Formulario de novo ticket
templates/ticket.html - Detalhe do ticket

## Autor

Helder Sindique - github.com/heldersindique-prog
