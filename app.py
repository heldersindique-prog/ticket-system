from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import init_db, criar_ticket, listar_tickets, fechar_ticket, get_ticket, estatisticas

app = Flask(__name__)

@app.route('/')
def index():
    tickets = listar_tickets()
    stats = estatisticas()
    return render_template('index.html', tickets=tickets, stats=stats)

@app.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        categoria = request.form['categoria']
        criar_ticket(titulo, descricao, categoria)
        return redirect(url_for('index'))
    return render_template('novo.html')

@app.route('/ticket/<int:ticket_id>')
def ver_ticket(ticket_id):
    ticket = get_ticket(ticket_id)
    return render_template('ticket.html', ticket=ticket)

@app.route('/fechar/<int:ticket_id>', methods=['POST'])
def fechar(ticket_id):
    resolucao = request.form['resolucao']
    fechar_ticket(ticket_id, resolucao)
    return redirect(url_for('index'))

@app.route('/api/stats')
def api_stats():
    return jsonify(estatisticas())

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
