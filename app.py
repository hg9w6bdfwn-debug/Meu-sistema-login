from flask import Flask, render_template_string, request

app = Flask(__name__)

def carregar_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/')
def home():
    return render_template_string(carregar_html(), erro=None)

@app.route('/login', methods=['POST'])
def login():
    usuario_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')
    
    # Credenciais de teste
    if usuario_digitado == "admin" and senha_digitada == "1234":
        return """
        <body style="font-family:sans-serif; text-align:center; padding-top:50px; background:#f2f2f7;">
            <h1 style="color:#34c759;">✓ Sucesso!</h1>
            <p>Conectado ao back-end em Python funcionando!</p>
            <a href="/">Voltar para o Login</a>
        </body>
        """
    else:
        return render_template_string(carregar_html(), erro="Usuário ou senha incorretos!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
