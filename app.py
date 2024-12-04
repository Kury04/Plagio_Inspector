from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Ruta para el formulario de inicio de sesión
@app.route('/')
def index():
    return render_template('pc/login.html')

# Ruta para manejar el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Verifica las credenciales (en este ejemplo, usuario: admin, contraseña: password)
    if username == 'admin' and password == 'password':
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    else:
        return render_template('pc/login.html', message='Nombre de usuario o contraseña incorrectos')

# Ruta para el panel de control después del inicio de sesión exitoso
@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return render_template('pc/dashboard.html')
    else:
        return redirect(url_for('pc/index.html'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('pc/index.html'))

if __name__ == '__main__':
    app.run(debug=True)
