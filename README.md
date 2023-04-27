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
esta será nuestra base de datos(por ahora almacena login y password)
-En el login/user/pass

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
