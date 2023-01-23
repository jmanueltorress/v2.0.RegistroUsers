from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import config
from flask_mysqldb import MySQL

# from models.entities import modelUser 
# from models.entities import User

app = Flask(__name__)
db=MySQL(app)

#from datetime import datetime
#app=Flask(__name__)
app = Flask(__name__, template_folder='/home/juanmanuelts/Escritorio/ProyectoSABES/src/templates'
,static_folder='/home/juanmanuelts/Escritorio/ProyectoSABES/src/static')


@app.route('/')
def index():
    return redirect(url_for('login'))
    #CONFIG SYS TO DB
@app.route('/login', methods=['GET', 'POST'])  #rute to templates
def login():
    if request.method=='POST':
        print(request.form['matricula'])
        print(request.form['password'])
        # user=User(0,request.form['matricula'],request.form['password'])
        # logged_user=modelUser.login(db,user)
        

        return render_template('/auth/login.html')
    else:
         return render_template('/auth/login.html')

         #'return '<h1>Hello world</h1> '

@app.route('/signin')  
def signin():
    return render_template('/auth/signin.html')
@app.route('/panel')  
def panel():
    return render_template('/auth/panel.html')
@app.route('/sistAdmin')  
def sistAdmin():
    return render_template('/auth/sistAdmin.html')


# @app.route('/login', methods=['POST', 'GET'])  
# def login():
#     print('Ya entre a LOGEAR')
#     if request.method=='POST':
#         matricula=request.form['matricula']
#         password=request.form['password']
#        # user=User(0,request.form['matricula'], request.form['in-pass'], None)
#         print(matricula)


#Main to run app
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run() 