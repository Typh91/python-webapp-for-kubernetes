from flask import Flask, render_template
import mysql.connector
import configparser

app = Flask(__name__)

@app.route('/')
def index():
    data = get_data_from_mysql()
    return render_template('example.html', data=data)

def read_properties():
    config = configparser.ConfigParser()
    config.read('database.properties')
    db_host = config['MySQL']['db.host']
    db_database = config['MySQL']['db.database']
    db_user = config['MySQL']['db.username']
    db_pass = config['MySQL']['db.password']
    return [db_host, db_database, db_user, db_pass]

def get_data_from_mysql():
    rows = []
    db_data = read_properties()
    mysqlConnection = mysql.connector.connect(
        host=db_data[0],
        database=db_data[1],
        user=db_data[2],
        password=db_data[3]
    )
    cursor = mysqlConnection.cursor()
    cursor.execute("SELECT * FROM datos")
    result = cursor.fetchall()
    for i in result:
        rows.append(i)

    return rows

if __name__ == "__main__":
    app.run()