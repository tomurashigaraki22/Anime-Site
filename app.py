from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
app.debug = True

conn = sqlite3.connect('userxpass.db')

@app.route('/')
def home():
    return render_template('signin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Connect to the SQLite database
        username = request.args.get('username')
        password = request.args.get('password')
        conn = sqlite3.connect('userxpass.db')
        cursor = conn.cursor()
        print("Test 2 passed")

        # Execute a SELECT query to check if the username and password match
        cursor.execute('''SELECT * FROM users WHERE username=? AND password=?''', (username, password))
        user = cursor.fetchone()
        print("Test3 passed")

        conn.close()
        print("Test4 passed")

        if user:
            # Authentication successful
            response = {'status': 'success', 'message': 'Login successful'}
        else:
            # Authentication failed
            response = {'status': 'failed', 'message': 'Login Failed'}
        return jsonify(response)

    return render_template('signin.html')

if __name__ == '__main__':
    app.run()

