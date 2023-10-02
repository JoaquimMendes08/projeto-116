# importando os módulos da biblioteca flask
from flask import Flask, render_template    

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'

# defina a rota para a página do pai
@app.route("/")
def home(): 
    marca = "Koenigesegg"
    modelo = "Jesko"
    velocidade = "480 km/h"

    return render_template('index.html', marca=marca, modelo=modelo, velocidade=velocidade)

# defina a rota para a página da mãe
@app.route("/divo")
def divo(): 
    marca = "Bugatti"
    modelo = "Divo"
    velocidade =  "380 km/h"

    return render_template('divo.html', marca=marca, modelo=modelo, velocidade=velocidade)

# defina a rota para a página do amigo
@app.route("/senna")
def senna(): 
    marca = "McLaren"
    modelo = "Senna"
    velocidade = "335 km/h"

    return render_template('senna.html', marca=marca, modelo=modelo, velocidade=velocidade)

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
