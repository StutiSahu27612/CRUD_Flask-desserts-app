from flask import Flask
from flask_cors import cross_origin
from flask import request , jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask_tutorial'

mysql = MySQL(app)
cross_origin(app)

@app.get('/desserts')
def get_des():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from desserts")
    data = cur.fetchall()
    cur.close()
    u = []
    for v in data:
        u.append({
            'sno' : v[0],
            'name':v[1],
            'flavour':v[2]
        })
        return u # return jsonify(u)

@app.post('/desserts')
def add_dessert():
    name = request.json['name']
    flavour = request.json['flavour']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO desserts(name , flavour) VALUES (%s , %s)" , (name , flavour))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message' : "addesd"})


@app.put('/desserts/<int:sno>')
def update_Des(sno):
    name = request.json['name']
    flavour = request.json['flavour']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE desserts set name = %s , flavour = %s WHERE sno =%s",(name,flavour,sno) )
    mysql.connection.commit()
    cur.close()
    return jsonify({'message' : "update"})

@app.delete('/desserts/<int:sno>')
def delete_DES(sno):
    cur = mysql.connection.cursor()
    cur.execute("DELETE from desserts where sno = %s", (sno))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message' : "deleted"})


if __main__ == "__name__":
    app.run(debug=True)

