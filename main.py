from conexao import select, deletar, salvar
import requests
from flask import Flask, render_template, request, redirect

app = Flask('Visie')


@app.route('/', methods=['GET'])
def home():
  lista_pessoas = select()
  return render_template('index.html', lista_pessoas = lista_pessoas)

@app.route("/save", methods=['POST'])
def save():
  dados_registro = {
    "nome": request.form['nome'],
    "rg": request.form['rg'],
    "cpf": request.form['cpf'],
    "data_nasc": request.form['data_nasc'],
    "data": request.form['data'],
    "funcao": request.form['funcao']
  }  
  salvar(dados_registro)
  return redirect('/')

@app.route("/delete/<id_pessoa>", methods=['GET'])
def delete(id_pessoa):
  print(id_pessoa)
  deletar(id_pessoa)
  return redirect('/')


if __name__ == "__main__":
  app.run(host='0.0.0.0')