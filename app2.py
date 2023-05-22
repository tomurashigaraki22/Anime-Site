from flask import Flask, render_template, jsonify, request
import sqlite3

app2 = Flask(__name__)
app2.debug = True

@app2.route('/')
def home():
    return render_template('signup.html')

@app2.route('/signups', methods=['POST', 'GET'])  # Corrected method to 'POST'
def signup():
    conn = sqlite3.connect('userxpass.db')
    cursor = conn.cursor()
    username = request.args.get('username')
    password = request.args.get('password')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
    conn.commit()
    conn.close()
    return render_template('signup.html')

if __name__ == '__main__':
    app2.run()
