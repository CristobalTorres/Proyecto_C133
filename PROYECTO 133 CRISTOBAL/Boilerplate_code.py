#Importar el módulo Flask en el proyecto.
from flask import Flask,render_template

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/")

#‘/’ URL está vinculado con la función first_flask.
def home():
    edad="16"
    name="Cristobal"
    img='imgm.jpg'
    return render_template("index.html",v_edad=edad,v_name=name,v_img=img)

@app.route("/madre")

#‘/’ URL está vinculado con la función first_flask.
def home1():
    home1="37"
    name1="Monica"
    img1='o.jpg'
    return render_template("index.html",v_edad=home1,v_name=name1,v_img=img1)

@app.route("/padre")

#‘/’ URL está vinculado con la función first_flask.
def home2():
    home2="36"
    name2="Miguel"
    img2='imgp.jpg'
    return render_template("index.html",v_edad=home2,v_name=name2,v_img=img2)

@app.route("/hermano")

#‘/’ URL está vinculado con la función first_flask.
def home3():
    home3="12"
    name3="Juan"
    img3='imgb.jpg'
    return render_template("index.html",v_edad=home3,v_name=name3,v_img=img3)

#Ejecutamos la app en el servidor local.
app.run(debug=True)
