from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'login'
mysql.init_app(app)

@app.route('/')
def index():
    conexion = mysql.connect()
    print(conexion)
    return render_template('sitio/login-crear-inicio.html')

@app.route('/login-contraseña')
def login_contraseña():
    return render_template('sitio/login-contraseña.html')

@app.route('/login-creacion')
def login_creacion():
    return render_template('sitio/login-creacion.html')

@app.route('/login-recuperar-exito')
def login_recuperar_exito():
    return render_template('sitio/login-recuperar-exito.html')

@app.route('/login-recuperar')
def login_recuperar():
    return render_template('sitio/login-recuperar.html')

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/sitio/login-recuperar', methods=['POST'] )
def recibir_datos():
    name = request.form['txtUser']
    password = request.form['txtPass']

    sql = "INSERT INTO `user/pass` (`Id`, `User`, `Password`) VALUES (NULL, %s, %s);"
    datos = (name,password)

    conexion = mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    print(f"hola {name} tu password es {password}")
    return redirect('/login-recuperar')

if __name__ == '__main__':
    app.run(debug=True)