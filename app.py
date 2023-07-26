from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask_tutorial'

mysql = MySQL(app)
CORS(app)


@app.get('/desserts')
def get_des():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from desserts")
    data = cur.fetchall()
    cur.close()
    # return jsonify(data)
    u = []
    for v in data:
        u.append({
            'sno': v[0],
            'name': v[1],
            'flavour': v[2]
        })
    return jsonify(u)


# @app.route('/desserts', methods=['POST'])
# def add_user():
#     name = request.json['name']
#     flavour = request.json['flavour']
#     cur = mysql.connection.cursor()
#     cur.execute("INSERT INTO desserts (name, flavour) VALUES (%s, %s)", (name, flavour))
#     mysql.connection.commit()
#     cur.close()
#     return jsonify({'message': 'User created successfully'})


@app.route('/desserts', methods=['POST'])
def add_dessert():
    name = request.json['name']
    flavour = request.json['flavour']
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO desserts (name, flavour) VALUES (%s, %s)", (name, flavour))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'dessert added successfully'})


@app.route('/desserts/<int:sno>', methods=['PUT'])
def update_dessert(sno):
    name = request.json['name']
    flavour = request.json['flavour']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE desserts SET name = %s , flavour = %s WHERE sno = %s",
                (name, flavour, sno))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'dessert updated successfully'})


@app.route('/desserts/<int:sno>', methods=['DELETE'])
def delete_dessert(sno):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM desserts WHERE sno = %s", (sno,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'dessert deleted successfully'})


if __name__ == "__main__":
    app.run(debug=True)
