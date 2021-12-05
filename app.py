from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/locataires")
def locataires():
    conn = get_db_connection()
    locataire_list = conn.execute('SELECT * FROM locataire').fetchall()
    conn.close()
    return render_template('locataires.html', locataires=locataire_list)


@app.route("/voitures")
def voitures():
    conn = get_db_connection()
    voiture_list = conn.execute('SELECT * FROM voiture').fetchall()
    conn.close()
    return render_template('voitures.html', voitures=voiture_list)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
