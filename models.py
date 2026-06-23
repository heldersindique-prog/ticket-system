import sqlite3
from datetime import datetime

DB = "tickets.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            categoria TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            estado TEXT DEFAULT 'Aberto',
            criado_em TEXT NOT NULL,
            fechado_em TEXT,
            resolucao TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_ticket(titulo, descricao, categoria):
    prioridades = {
        "rede": "P1 - Critico",
        "acesso": "P1 - Critico",
        "hardware": "P2 - Alto",
        "software": "P2 - Alto",
        "impressora": "P3 - Normal"
    }
    prioridade = prioridades.get(categoria.lower(), "P3 - Normal")
    criado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        INSERT INTO tickets (titulo, descricao, categoria, prioridade, criado_em)
        VALUES (?, ?, ?, ?, ?)
    ''', (titulo, descricao, categoria, prioridade, criado_em))
    conn.commit()
    ticket_id = c.lastrowid
    conn.close()
    return ticket_id

def listar_tickets(estado=None):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    if estado:
        c.execute('SELECT * FROM tickets WHERE estado = ? ORDER BY id DESC', (estado,))
    else:
        c.execute('SELECT * FROM tickets ORDER BY id DESC')
    tickets = [dict(row) for row in c.fetchall()]
    conn.close()
    return tickets

def fechar_ticket(ticket_id, resolucao):
    fechado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        UPDATE tickets SET estado = 'Fechado', fechado_em = ?, resolucao = ?
        WHERE id = ?
    ''', (fechado_em, resolucao, ticket_id))
    conn.commit()
    conn.close()

def get_ticket(ticket_id):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def estatisticas():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM tickets')
    total = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM tickets WHERE estado = "Aberto"')
    abertos = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM tickets WHERE estado = "Fechado"')
    fechados = c.fetchone()[0]
    c.execute('SELECT categoria, COUNT(*) FROM tickets GROUP BY categoria')
    por_categoria = dict(c.fetchall())
    c.execute('SELECT prioridade, COUNT(*) FROM tickets GROUP BY prioridade')
    por_prioridade = dict(c.fetchall())
    conn.close()
    return {
        "total": total,
        "abertos": abertos,
        "fechados": fechados,
        "por_categoria": por_categoria,
        "por_prioridade": por_prioridade
    }
