
from app import app
from flask import render_template

# Rota para inicio do Site
@app.route ('/')
def homepage ():
    usuario = 'João'
    idade = 17

    context = {
        'usuario': usuario,
        'idade': idade
    }

    return render_template('index.html', context=context)

@app.route ('/contato/')
def novapagina ():
    return render_template('contato.html')