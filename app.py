# secure_app.py
from flask import Flask, request, render_template, redirect
import sqlite3
import bcrypt
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Login</h2>
        <form method="POST" action="/login">
            Username: <input type="text" name="username"/><br>
            Password: <input type="password" name="password"/><br>
            <input type="submit" value="Login"/>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    if row and bcrypt.checkpw(password, row[0].encode('utf-8')):
        return f"<h3>Welcome, {username}!</h3>"
    else:
        return "<h3>Login Failed!</h3>"

if __name__ == '__main__':
    app.run(debug=False)  # ✅ Debug mode off
