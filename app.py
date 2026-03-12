from flask import Flask, render_template, request, redirect
import mysql.connector
from model.cadastro import enviar_dados 
from model.cadastro import retornar_dados
from model.cadastro import excluir_dados

app = Flask(__name__)

# nao sei se precisa disso
@app.route("/index", methods=["GET"])
@app.route("/")

def pg_index():
    return render_template("index.html")

#rota para qrequisitos
@app.route("/requisitos")
def pg_requisitos():
    dados = retornar_dados()
    return render_template("requisitos.html", dados = dados)

@app.route("/cadastro/post", methods=["POST"])
def api_enviar():
    descricao = request.form.get("descricao")
    nivel = request.form.get("nivel")
    valor = request.form.get("valor")
    situacao = request.form.get("situacao")
    enviar_dados(descricao, nivel, valor, situacao)
    return redirect("/requisitos")

@app.route("/cadastro/deletar/<id>")
def api_excluir_musica(id):
    excluir_dados(id)
    return redirect("/requisitos")
    

if __name__ == "__main__":
    app.run(debug=True)