from flask import Flask, abort, request, render_template, Response, session, make_response, jsonify, flash
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__, template_folder="templates")
bcrypt = Bcrypt()
app.secret_key = "12jksdknsfsnfslfnsflf"

# mysql = MySQL(app)
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=''
# app.config['MYSQL_DB']='user-details'


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        abort(404)
        return
    else:
        username = request.form['username']
        password = request.form['password']

        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM user WHERE username= %s AND password= %s',(username, password, ))
        # user = cursor.fetchone()
        # print(user)
        # if not user:
        #     cursor.execute(
        #         'INSERT INTO user VALUES (NULL, % s, % s)', 
        #               (username, password ))
        #     mysql.connection.commit()
        # user = cursor.fetchone()

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        is_valid = bcrypt.check_password_hash(hashed_password, password)
        flash(f'login success')
        return render_template('home.html', message=username)
    

@app.route('/setsession')
def setsession():
    session['name']='abcd'
    session['ho']='qwerty'
    session['as']='12vfdv'
    session['ds']='34fgeg'
    session['we']='98uefijeni'
    return render_template('home.html', message="session created")

@app.route('/getsession')
def getsession():
    if 'name' in session.keys() and 'ho' in session.keys():
        name=session['name']
        ho=session['ho']
        return render_template('home.html', message=f"name: {name}, ho: {ho}")
    else:
        return render_template('home.html', message="no session")

@app.route('/clearsession')
def clearsession():
    session.clear()
    # session.pop('name')  # clear individual fields
    return render_template('home.html', message="session cleared")


@app.route("/setcookie")
def setcookie():
    response = make_response(render_template('home.html', message='cookie set'))
    response.set_cookie('cookiename', 'cookievalue')
    return response

@app.route("/getcookie")
def getcookie():
    cookieval = request.cookies.get('cookiename')
    if cookieval:
        return render_template('home.html', message=f'cookie value is: {cookieval}')
    else:
        return render_template('home.html', message='cookie not found')


@app.route('/removecookie')
def removecookie():
    response = make_response(render_template('home.html', message='cookie removed'))
    response.set_cookie('cookiename', expires=0)
    return response

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8008, debug=True)


