
from app import db
from datetime import datetime # Usado para pegar a data de criação/modificação de cada dado

# Configuração do banco de dados para criação de tabela
class Contato (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    data_envio = db.Column (db.DateTime, default=datetime.now())
    nome = db.Column (db.String, nullable=True)
    email = db.Column (db.String, nullable=True)
    assunto = db.Column (db.String, nullable=True)
    mensagem = db.Column (db.String, nullable=True)
    respondido = db.Column (db.Integer, default=0)
    # Botão de envio
