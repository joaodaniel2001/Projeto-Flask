
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask (__name__)

# Definindo o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Definindo as váriaveis de banco de dados
db = SQLAlchemy (app)
migrate = Migrate (app, db)

from app.views import homepage
from app.models import Contato