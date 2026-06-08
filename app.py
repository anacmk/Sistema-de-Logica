from flask import Flask, render_template, request

app = Flask(__name__)

def binario_para_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        if digito == '1':
            decimal += 2 ** potencia
        elif digito != '0':
            return "Erro: use apenas 0 e 1"
        potencia += 1
    return decimal

def tabela_verdade(a, b):
    a = int(a)
    b = int(b)
    return {
        "and": int(a and b),
        "or":  int(a or b),
        "not": int(not a)
    }

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sistema", methods=["GET", "POST"])
def index():
    resultado_decimal = None
    resultado_logica = None

    if request.method == "POST":
        acao = request.form.get("acao")
        if acao == "converter":
            numero = request.form.get("binario", "").strip()
            if numero:
                resultado_decimal = binario_para_decimal(numero)
        elif acao == "gerar":
            valor_a = request.form.get("a", "0")
            valor_b = request.form.get("b", "0")
            resultado_logica = tabela_verdade(valor_a, valor_b)

    return render_template(
        "index.html",
        resultado_decimal=resultado_decimal,
        resultado_logica=resultado_logica
    )

if __name__ == "__main__":
    app.run(debug=True)