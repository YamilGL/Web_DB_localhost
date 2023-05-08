### Pagina_web_DB_localhost (proceso)

**requerimientos:**
1.-tener instalado xampp
2.- Tener instalado vscode
3.-entorno virtual en vscode (opcional)
4.- librerias instaladas en vscode (flask, flask-mysql)

**Instalacion de xampp**
1.- descarguelo a travéz del url: https://www.apachefriends.org/download.html

**Creacion del entorno virtual en vscode**
1.- abra una terminal y ejecute el siguiente comando:

`$ pip install virtualenv`

2.- dirígase a la carpeta en la cual desea el entorno virtual(desde la terminal)
3.- ejecute el siguiente comando:

`$virtualenv -p python3 env`

**Inicie su entorno virtual**
1.- ejecute 
`$ .\env\Scripts\activate`

**Si ocurre un error al iniciar el entorno virtual ejecute lo siguiente**
`$ Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Instalacion de flask y flask-mysql**
1.-ejecute en la terminal:
`$ pip install flask`
`$ pip install flask-mysql`

**instalacion de librerias a travez de requeriments.txt**
IMPORTANTE: tener la carpeta app y el archivo requeriments en el mismo sitio en el que se encuentra la carpeta env. Quedando

[![example.png](https://i.postimg.cc/3x65gP8N/example.png)](https://postimg.cc/tshMbvVG)

`$ pip install -r .\requeriments.txt`

**Abrir XAMPP-CONTROL PANEL**
Una vez abierto, activar(presionar start) en Apache y MySQL
dirigirse a la url:
http://localhost/phpmyadmin/ 
esta será nuestra base de datos con el nombre de 'web'
**configuracion de localhost/phpmyadmin**
1.-estando dentro de la direccion http://localhost/phpmyadmin/ crear una nueva base de datos con el nombre de 'web'
2.- dentro de esta base de datos llamada 'web'(importante que tenga este nombre) hacer click en la parte superior a 'importar'
3.- seleccion el archivo web.sql e importalo.
[![example-03.png](https://i.postimg.cc/T2q19jZk/example-03.png)](https://postimg.cc/Lh5m4P4f)
Deberia quedar de esta manera

**EJECUTAR LA PAGINA WEB**
IMPORTANTE: Tener activado el entorno virtual 
`$ .\env\Scripts\activate`

Ejecutar el siguiente comando para iniciar el servidor
`$ python .\app\app.py`

Ir a la ruta que aparece en la terminal
[![Example01.png](https://i.postimg.cc/9MsYbY4G/Example01.png)](https://postimg.cc/7GMzY7n6)

**SALIR DEL ENTORNO VIRTUAL**
Ejecute:
`$ deactivate`


para el login como administrador reconoce: admin@gmail.com      pass:admin
el resto de usuarios solo podran acceder a la vista de compras, mientras que el administrador maneja la base de datos
