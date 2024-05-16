from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = sqlite3.connect('bintech.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        conn.close()

        users = [{'id': row[0], 'email': row[1], 'username':row[2]} for row in data]
        return render_template('users.html', users=users)
    except sqlite3.Error as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')