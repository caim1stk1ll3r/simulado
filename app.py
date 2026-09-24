from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        ida = float(request.form.get['ida'])
        volta = float(request.form.get['volta'])
        dias = int(request.form['dias'])
        meio = request.form.get('meio')

        dia = ida + volta 
        km_mes = dia * dias * 4
        emissao = km_mes * fator


    return render_template('index.html', ida=ida, volta=volta, dias=dias, meio=meio)



 



















































if __name__ == '__main__':
    app.run(debug=True)