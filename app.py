from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():                                 # A rota define a função que será chamada quando a URL raiz for acessada
    return "Hello, World!"

@app.route("/about")
def about():
    return "Pagina Sobre"                # Retorna uma mensagem para a rota /about

if __name__ == "__main__":                  # Verifica se o script está sendo executado diretamente
    app.run(debug=True)                          # Executa o aplicativo Flask com o modo de depuração ativado
