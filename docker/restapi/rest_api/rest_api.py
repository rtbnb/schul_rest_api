from flask import Flask, request, render_template
import mysql.connector as cn

app = Flask(__name__)


def get_connection():
    try:
        connection = cn.connect(host='172.20.0.4',
                                database='rest_api_db',
                                user='root',
                                password='root')
        return connection

    except cn.Error as err:
        print("Error while connecting to MySQL\n", err)


def insert_data(vorname, nachname):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO rest_api_data (vorname, nachname) VALUES (\'{vorname}\', \'{nachname}\')")
    connection.commit()
    result = cursor.fetchall()
    return result


def get_all_data():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("select * from rest_api_data")
    result = cursor.fetchall()

    data_list = []

    for row in result:
        data_list.append({'vorname': row[0], 'nachname': row[1]})
    return data_list


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/all_data', methods=['GET'])
def get_person():
    data_list = get_all_data()

    return render_template("alle_daten.html", data_list=data_list)


@app.route('/add_data', methods=['POST'])
def post_person():
    if not request.form['vorname'] or not request.form['nachname']:
        return render_template("index.html")

    insert_data(request.form['vorname'], request.form['nachname'])

    return render_template("daten_hinzugefuegt.html")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
