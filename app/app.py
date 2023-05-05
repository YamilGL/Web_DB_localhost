from flask import Flask
from flask import render_template, request, redirect ,url_for#acceder a las rutas 
from flaskext.mysql import MySQL #para la conexion a la base de datos
from datetime import datetime 
from flask import send_from_directory #mostrar imagenes

import os #verificar carpetas o crearlas para evitar errores

app = Flask(__name__)
mysql = MySQL()

#datos para requerir la conexion a la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost' #cambia si tenemos una direccion mysql
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' #no tiene password
app.config['MYSQL_DATABASE_DB'] = 'web'#nombre a la base de datos que estamos ingresando
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('sitio/inicio.html')

#para retornar la imagen y mostarla en pantalla
@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/temp_img'),imagen)

#seccion de productos
@app.route('/index_muestra_de_productos')
def index_productos():
    
    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `productos`")
    
    recepcion = cursor.fetchall()

    conexion.commit()
    return render_template('sitio/index_muestra_de_productos.html',recepcion = recepcion)

@app.route('/carrito')
def carrito():
    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `carrito`")
    
    recepcion = cursor.fetchall()

    conexion.commit()
    return render_template('carrito/index.html',recepcion = recepcion)

@app.route('/carrito/guardar', methods = ['POST'])
def carrito_guardar():
    _id = request.form['txtID']

    conexion = mysql.connect() 
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `productos` WHERE id =%s",(_id))
    product = cursor.fetchall()
    conexion.commit()
    for data in product:
        _nombre = data[1]
        _descripcion = data[2]
        _color = data[3]
        _precio = data[4]
        _imagen = data[5]
        _cantidad = data[6]    

    sql = "INSERT INTO `carrito` (`ID`, `nombre`, `descripcion`, `Color`, `Precio`, `imagen`, `cantidad`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"

    datos =(_nombre,_descripcion,_color,_precio,_imagen,_cantidad)
    
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
   

    return redirect('/index_muestra_de_productos')

@app.route('/carrito/eliminar',methods = ['POST'])
def carrito_eliminar():
    _id = request.form['txtID']

     #eliminar de la base de datos
    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE  FROM `carrito` WHERE id = %s" ,(_id))
    conexion.commit()

    return redirect('/carrito')


#vista de usuario
@app.route('/inicio/usuario/<id>')
def vista_usuario_inicio(id):
    _id = id
    conexion = mysql.connect() 
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `user/pass` WHERE id =%s",(_id))
    user = cursor.fetchall()
    conexion.commit()
    return render_template('sitio/vista_usuario/inicio.html',user = user)


@app.route('/carrito/usuario/<id>')
def vista_usuario_carrito(id):
    _id = id
    conexion = mysql.connect() 
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `user/pass` WHERE id =%s",(_id))
    user = cursor.fetchall()
    conexion.commit()
    return render_template('sitio/vista_usuario/carrito.html', user = user)
@app.route('/productos/usuario/<id>')
def vista_usuario_productos(id):
    _id = id
    conexion = mysql.connect() 
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `user/pass` WHERE id =%s",(_id))
    user = cursor.fetchall()
    conexion.commit()
    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `productos`")
    
    recepcion = cursor.fetchall()

    conexion.commit()
    return render_template('sitio/vista_usuario/index_muestra_de_productos.html',recepcion = recepcion,user = user)

    

@app.route('/login/inicio')
def login_inicio():
    return render_template('login/login-crear-inicio.html')

@app.route('/login/creacion_1')
def login_creacion_1():
    return render_template('/login/login-creacion.html')

@app.route('/login/login-crear-inicio/Save_data', methods = ['POST'])
def login_create_save_data():
    _nombre = request.form['txtName']
    _email = request.form['txtEmail']
    _Password = request.form['txtPass']

    sql = "INSERT INTO `user/pass` (`Id`, `Nombre`, `Email`, `Password`) VALUES (NULL, %s, %s, %s);"
    datos =(_nombre,_email,_Password)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    return redirect('/login/creacion_1')


@app.route('/login/login-crear-inicio/check',methods=['POST'])
def login_check():
    _email = request.form['txtUser']
    _Password = request.form['txtPassword']

    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `user/pass`")
    
    recepcion = cursor.fetchall()

    for data in recepcion:
        if(data[2] == _email and data[3] ==_Password):
            if(data[0] ==1):
                return redirect('/admin')
            else:
                 id = data[0]
                 return redirect(url_for('vista_usuario_inicio', id = id))
        else:
            continue
    return redirect('/login/inicio')
           

    


@app.route('/login/recuperar')
def login_recuperar():
    return render_template('login/login-recuperar.html')




@app.route('/admin')
def admin_index():

    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `user/pass`")
    
    recepcion = cursor.fetchall()

    conexion.commit()
    return render_template('admin/index.html' ,recepcion = recepcion)

@app.route('/admin/ventas')
def admin_ventas():
    return render_template('admin/ventas.html')

@app.route('/admin/productos')
def admin_productos():
    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `productos`")
    
    recepcion = cursor.fetchall()

    conexion.commit()
    return render_template('admin/productos.html', recepcion = recepcion)

@app.route('/admin/pedidos')
def admin_pedidos():
    return render_template('admin/pedidos.html')

@app.route('/admin/crear_user', methods = ['POST'])
def admin_crear_user():
    _nombre = request.form['txtName']
    _email = request.form['txtEmail']
    _Password = request.form['txtPass']

    sql = "INSERT INTO `user/pass` (`Id`, `Nombre`, `Email`, `Password`) VALUES (NULL, %s, %s, %s);"
    datos =(_nombre,_email,_Password)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    return redirect('/admin')

@app.route('/admin/crear_product',methods = ['POST'])
def admin_crear_product():
    _nombre = request.form['txtName']
    _descripcion = request.form['txtDescr']
    _color = request.form['txtColor']
    _precio = request.form['txtPrecio']
    _imagen = request.files['txtImg']
    _cantidad = request.form['txtCant']
    
    tiempo = datetime.now()
    HoraActual= tiempo.strftime('%Y%H%M%S')

    if _imagen.filename !="":
        nuevoNombre = HoraActual+"_"+_imagen.filename
        if not os.path.exists("app/templates/sitio/temp_img/"):
            os.makedirs("app/templates/sitio/temp_img/")
        _imagen.save("app/templates/sitio/temp_img/"+nuevoNombre)

    sql = "INSERT INTO `productos` (`ID`, `nombre`, `descripcion`, `Color`, `Precio`, `imagen`, `cantidad`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"
    datos =(_nombre,_descripcion,_color,_precio,nuevoNombre,_cantidad)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    return redirect('/admin/productos')
@app.route('/admin/borrar_productos', methods=['POST'])
def admin_borrar_product():
    
    _id = request.form['txtID']

    #eliminar imagen de la carpeta
    conexion = mysql.connect() 
    cursor = conexion.cursor()
    cursor.execute("SELECT imagen FROM `productos` WHERE id =%s",(_id))
    _imagen_ = cursor.fetchall()
    conexion.commit
    if os.path.exists("app/templates/sitio/temp_img/"+str(_imagen_[0][0])):
        os.unlink("app/templates/sitio/temp_img/"+str(_imagen_[0][0]))


     #eliminar de la base de datos
    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE  FROM `productos` WHERE id = %s" ,(_id))
    conexion.commit()

    return redirect('/admin/productos')

@app.route('/admin/borrar', methods=['POST'])
def admin_borrar():
    _id = request.form['txtID']
    
    conexion =mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE  FROM `user/pass` WHERE id = %s" ,(_id))
    conexion.commit()

    return redirect('/admin')




if __name__ == '__main__':
    app.run(debug=True)