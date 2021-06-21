from cgitb import html

from flask import Flask, render_template, request, session, url_for, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = "123456789"

app.config["MYSQL_Host"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Harshal@2708"
app.config["MYSQL_DB"] = "login"

db = MySQL(app)


@app.route('/', methods={'GET', 'POST'})
def index():
    if request.method == 'POST':
        if 'email' in request.form and 'Password' in request.form:
            email = request.form['email']
            password = request.form['Password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM account WHERE email=%s AND Password=%s", (email, password))
            info = cursor.fetchone()

            print(info)
            if info is not None:
                if info['email'] == email and info['Password'] == password:
                    session['loginsucces'] = True
                    return redirect(url_for('bot'))
                    # return "Login Success"
            else:
              return """<html><body><h1>Login Unsuccessful.please Register</h1></body></html>"""




    return render_template('login.html')


@app.route('/new', methods={'GET', 'POST'})
def new_user():
    if request.method == 'POST':
        if "one" in request.form and "two" in request.form and "three" in request.form:
            name = request.form['one']
            email = request.form['two']
            password = request.form['three']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO login.account (Name,email,Password) VALUES (%s,%s,%s)", (name, email, password))
            db.connection.commit()
            return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/new/chatbot')
def bot():
    if session.get('loginsucces', None)== True:
        return render_template('bot.html')


if __name__ == "__main__":
    app.run(debug=True, port=1000)
