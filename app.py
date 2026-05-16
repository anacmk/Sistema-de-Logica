from flask import Flask, render_template, request

app = Flask(__name__)

# BINARIO PARA DECIMAL
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


# TABELA VERDADE
def tabela_verdade(a, b):

    a = int(a)
    b = int(b)

    resultado_and = a and b
    resultado_or = a or b
    resultado_not = int(not a)

    return {
        "and": resultado_and,
        "or": resultado_or,
        "not": resultado_not
    }


@app.route("/", methods=["GET", "POST"])
def index():

    resultado_decimal = None
    resultado_logica = None

    if request.method == "POST":

        # BINARIO
        numero = request.form.get("binario")

        if numero:
            resultado_decimal = binario_para_decimal(numero)

        # TABELA VERDADE
        valor_a = request.form.get("a")
        valor_b = request.form.get("b")

        if valor_a != "" and valor_b != "":
            resultado_logica = tabela_verdade(valor_a, valor_b)

    return render_template(
        "index.html",
        resultado_decimal=resultado_decimal,
        resultado_logica=resultado_logica
    )


if __name__ == "__main__":
    app.run(debug=True)