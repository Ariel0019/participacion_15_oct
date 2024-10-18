from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulación de base de datos de usuarios
users = {
    "user1": generate_password_hash("password1"),

    "ariel": generate_password_hash("ariel"),  # Nueva credencial
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username], password):
        session['username'] = username
        return redirect(url_for('welcome'))
    else:
        flash('Credenciales incorrectas. Intenta de nuevo.')
        return redirect(url_for('home'))

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    username = session['username']
    return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
