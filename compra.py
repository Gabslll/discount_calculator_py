from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular_desconto", methods=['GET', 'POST'])
def calcular_desconto():
        produto1_valor = float(request.form['produto1'])

        if produto1_valor >= 200:
            resultado = "Total a pagar com o desconto de 20% é de: R$ {:.2f}".format(produto1_valor * 0.8)
        elif produto1_valor >= 100:
            resultado = "Total a pagar com o desconto de 10% é de: R$ {:.2f}".format(produto1_valor * 0.9)
        else:
            resultado = "Não há desconto aplicável."

        return render_template("resultado.html", resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
