from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # Necessário para usar o flash

# Função para calcular o salário completo
def calcular_tudo(salario, gratificacao, inss_percentual, vale_transporte, vale_alimentacao, dias_trabalhados):
    total1 = (salario + gratificacao) - ((salario + gratificacao) * inss_percentual)
    total2 = total1 + dias_trabalhados * (vale_transporte + vale_alimentacao)
    return total2

# Função para calcular apenas os vales
def calcular_vales(vale_transporte, vale_alimentacao, dias_trabalhados):
    total_vales = (vale_transporte + vale_alimentacao) * dias_trabalhados
    return total_vales

# Função para calcular apenas o salário líquido
def calcular_salario_liquido(salario, gratificacao, inss_percentual):
    total1 = (salario + gratificacao) - ((salario + gratificacao) * inss_percentual)
    return total1

# Função para calcular o salário bruto (sem deduções)
def calcular_salario_bruto(salario, gratificacao):
    return salario + gratificacao

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pj')
def pj():
    return render_template('pj.html')

@app.route('/clt', methods=['GET', 'POST'])
def clt():
    if request.method == 'POST':
        try:
            # Coletar os valores dos campos
            salario = request.form.get('salario', '').strip()
            gratificacao = request.form.get('gratificacao', '').strip()
            inss_percentual = request.form.get('inss', '').strip()
            vale_transporte = request.form.get('vale_transporte', '').strip()
            vale_alimentacao = request.form.get('vale_alimentacao', '').strip()
            dias_trabalhados = request.form.get('dias_trabalhados', '').strip()
            operacao = request.form['operacao']

            # Validação dos campos para cada operação
            if operacao == 'calcular_vales':
                if not (vale_transporte and vale_alimentacao and dias_trabalhados):
                    flash("Os campos Vale Transporte, Vale Alimentação e Dias Trabalhados devem estar preenchidos.")
                    return redirect(url_for('clt'))
                total_vales = calcular_vales(float(vale_transporte), float(vale_alimentacao), int(dias_trabalhados))
                resultado = f'Total Vales: R$ {total_vales:.2f}'

            elif operacao == 'calcular_salario_liquido':
                if not (salario and gratificacao and inss_percentual):
                    flash("Os campos Salário, Gratificação e INSS devem estar preenchidos.")
                    return redirect(url_for('clt'))
                total_liquido = calcular_salario_liquido(float(salario), float(gratificacao), float(inss_percentual) / 100)
                resultado = f'Salário Líquido: R$ {total_liquido:.2f}'

            elif operacao == 'calcular_salario_bruto':
                if not (salario and gratificacao):
                    flash("Os campos Salário e Gratificação devem estar preenchidos.")
                    return redirect(url_for('clt'))
                total_bruto = calcular_salario_bruto(float(salario), float(gratificacao))
                resultado = f'Salário Bruto: R$ {total_bruto:.2f}'

            elif operacao == 'calcular_tudo':
                if not (salario and gratificacao and inss_percentual and vale_transporte and vale_alimentacao and dias_trabalhados):
                    flash("Todos os campos devem estar preenchidos para calcular tudo.")
                    return redirect(url_for('clt'))
                total_tudo = calcular_tudo(float(salario), float(gratificacao), float(inss_percentual) / 100, 
                                           float(vale_transporte), float(vale_alimentacao), int(dias_trabalhados))
                resultado = f'Salário Total: R$ {total_tudo:.2f}'

            return render_template('clt.html', resultado=resultado)

        except ValueError:
            flash("Por favor, insira valores válidos.")
            return redirect(url_for('clt'))

    return render_template('clt.html', resultado=None)

if __name__ == '__main__':
    app.run(debug=True)
