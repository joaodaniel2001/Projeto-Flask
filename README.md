# Projeto FLASK

## Pasta **.venv**

<p> 1. Instalação da pasta <b>.venv</b></p>

<pre><code>python -m venv .venv</code></pre>
<br>

<p> 2. Ativação no terminal</p>

<ul>
    <li>Abra o <b>Command Prompt</b></li>
    <li>Reabra o Terminal</li>
    <li>Digite o comando:</li>
</ul>

<pre><code>.venv\Scripts\activate</code></pre><br>

## Biblioteca Flask

<ul><li>Instalando a Biblioteca Flask:</li></ul>
<pre><code>pip install flask</code></pre>

<ul><li>Flask SQLAlchemy & Flask Migrate:</li></ul>
<pre><code>pip install Flask-SQLAlchemy Flask-Migrate</code></pre>

<ul><li>Flask-WTF:</li></ul>
<pre><code>pip install Flask-WTF</code></pre><br>

## Comandos

<ul><li>Inicializar a pasta de <b>migrações</b>:</li></ul>
<pre><code>flask db init</code></pre><br>

<ul><li>Cria uma migração com uma nova <b>mensagem</b>:</li></ul>
<pre><code>flask db migrate -m "mensagem"</code></pre><br>

<ul><li>Aplica as migrações ao <b>banco de dados</b>:</li></ul>
<pre><code>flask db upgrade</code></pre><br>

## Estrutura básica

<ul><li>Crie uma arquivo <b>main.py</b> e escreva:</li></ul>

<pre><code>
from flask import flask

app = flask (__name__)
@app.route ('/')
def homepage ():
    return 'Minha primeira página Flask

if __name__ = '__main__':
    app.run (debug=true)

</code></pre>

<ul><li>Inicie o código, e no <b>terminal</b>, copie o código <b>http</b> e cole no navegador que seu código flask funcionará:</li></ul>
<pre><code><ul><li>Running on http://127.0.0.1:5000</li></ul></pre></code>

