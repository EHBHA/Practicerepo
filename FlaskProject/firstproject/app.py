from flask import Flask, abort, request, render_template, Response, send_from_directory, session, make_response, jsonify, flash
import os
import uuid
from werkzeug.utils import secure_filename
import mimetypes
app = Flask(__name__, template_folder="templates")
app.secret_key="12iwuhdwiewiddiwd"

@app.route("/")
def hello():
    myvalue = "bharat"
    mylist = [1,2,3,4,5]
    return render_template('index.html', myvalue=myvalue, mylist=mylist)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 
    else:
        username = request.form['username']
        password = request.form['password']
        # return render_template('success.html', username=username)
        flash("login success")
        return render_template('index.html', message='')
    
@app.route("/file_upload", methods=['GET','POST'])
def filehandle():
    file = request.files['file']
    return file.read().decode()

@app.route("/download_file", methods=['GET', 'POST'])
def downloadfile():
    file = request.files['file']
    response = Response(
        file,
        mimetype='text/plain',
        headers={
            'Content-Disposition':'attachment; filename=lkb.txt'
        }
    )
    return response

@app.route("/download_file_two", methods=['POST'])
def download_file_two():
    file = request.files['file']
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    filename = f'{uuid.uuid4()}.txt'
    filename = secure_filename(filename)
    file_path = os.path.join('downloads', filename)
    print(file_path)
    file.save(file_path)
    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    filename = secure_filename(filename)
    
    mime_type, _ = mimetypes.guess_type(filename)
    print(f"Serving file with MIME type: {mime_type}")
    return send_from_directory('downloads', filename, download_name="result.txt", as_attachment=True, mimetype=mime_type)

@app.route("/handlepost", methods=['POST'])
def hanlde_post():
    greeting=request.json['greeting']
    name=request.json['name']
    with open('file.txt', 'w') as file:
        file.write(f'{greeting}, {name}')

    return jsonify({'message': 'message written in file'})

@app.route('/setsession')
def setsession():
    session['name']='abcd'
    session['ho']='qwerty'
    return render_template('index.html', message="session created")

@app.route('/getsession')
def getsession():
    if 'name' in session.keys() and 'ho' in session.keys():
        name=session['name']
        ho=session['ho']
        return render_template('index.html', message=f"name: {name}, ho: {ho}")
    else:
        return render_template('index.html', message="no session")

@app.route('/clearsession')
def clearsession():
    session.clear()
    # session.pop('name')  # clear individual fields
    return render_template('index.html', message="session cleared")


@app.route("/setcookie")
def setcookie():
    response = make_response(render_template('index.html', message='cookie set'))
    response.set_cookie('cookiename', 'cookievalue')
    return response

@app.route("/getcookie")
def getcookie():
    cookieval = request.cookies.get('cookiename')
    if cookieval:
        return render_template('index.html', message=f'cookie value is: {cookieval}')
    else:
        return render_template('index.html', message='cookie not found')


@app.route('/removecookie')
def removecookie():
    response = make_response(render_template('index.html', message='cookie removed'))
    response.set_cookie('cookiename', expires=0)
    return response


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8018, debug=True)