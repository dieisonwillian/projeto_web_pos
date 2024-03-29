from flask import Flask, render_template, request, redirect, url_for
from valida.login import validalogin

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if validalogin(username,password):
            return redirect(url_for('info', username=username))
        else:
            error = 'Usuário ou senha inválidos'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/info/<username>')
def info(username):
    return render_template('usuarios.html', username=username)
 ##   return f"Bem-vindo, {username}! Seu login foi feito com sucesso."

if __name__ == '__main__':
    app.run(debug=True)