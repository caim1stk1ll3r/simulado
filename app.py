from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':

        km = float(request.form.get['km'])
        dias = int(request.form['dias'])
        meio = request.form.get('meio')

        km_mes = km * dias * 4
        emissao = km_mes * meio

    

    return render_template('index.html', km=km, dias=dias, meio=meio)



 



















































if __name__ == '__main__':
    app.run(debug=True)