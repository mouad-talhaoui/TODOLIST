from flask import Flask, redirect,render_template, request, flash, url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todolist'
 
mysql = MySQL(app)
 
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM tasks")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', tasks=data )

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        description = request.form['description']
        state = request.form['state']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (description, state) VALUES (%s, %s)", (description, state))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<int:id_data>', methods = ['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/view/<int:id_data>',methods=['GET'])
def view(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT  id, description, state FROM tasks where id=%s", (id_data,))
    data = cur.fetchall()
    cur.close()
    print("data",data)
    return render_template('update.html', task=data )


@app.route('/update/<int:id_data>',methods=['POST'])
def update(id_data):

    if request.method == 'POST':
        id_data = request.form['id']
        description = request.form['description']
        state = request.form['state']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE tasks
               SET description=%s, state=%s
               WHERE id=%s
            """, (description, state, id_data))
        mysql.connection.commit()
        return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)