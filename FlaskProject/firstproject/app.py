from flask import Flask, request, render_template, Response, send_from_directory, session
import os
import uuid
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
        return render_template('success.html', username=username)
    
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
        os.mkdir('downloads')
    filename = f'{uuid.uuid4()}.txt'
    file_path = os.path.join('downloads', filename)
    print(file_path)
    file.save(file_path)
    return render_template('download.html', filename=file_path)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename)

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
        return render_template('index.html', message=f"no session")

@app.route('/clearsession')
def clearsession():
    session.clear()
    return render_template('index.html', message=f"session cleared")


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8018, debug=True)