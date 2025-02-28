from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

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


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8008, debug=True)