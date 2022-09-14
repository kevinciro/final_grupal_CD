from flask import render_template, redirect, session, request, flash  # importaciones de módulos de flask
from login_reg import app

# importamos modelos de User
from login_reg.models.users import User

# Importando BCrypt (encriptar)
from flask_bcrypt import Bcrypt

from login_reg.models.fligths import Fligth

bcrypt = Bcrypt(app)  # inicializando instancia de Bcrypt


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/render_register', methods=['GET'])
def render_register():
    return render_template("register.html")


@app.route('/render_profile', methods=['GET'])
def render_profile():
    return render_template("profile.html")


# Creando una ruta para /register
@app.route('/register', methods=['POST'])
def register():
    # request.form = {
    #   "first_name": "Elena",
    #   "last_name": "De Troya",
    #   "email": "elena@cd.com",
    #   "password": "123456",
    # }

    if not User.valida_usuario(request.form):
        return redirect('/render_register')

    pwd = bcrypt.generate_password_hash(request.form['password'])  # Me encripta el password

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "age": request.form['age'],
        "dni": request.form['dni'],
        "password": pwd
    }



    id = User.save(formulario)  # Guardando a mi usuario y recibo el ID del nuevo registro
    session['usuario_id'] = id  # Guardando en sesion el identificador
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:  # si user=False
        flash("E-mail no encontrado", 'login')
        return redirect('/')

    # Comparando la contraseña encriptada con la contraseña del LOGIN
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Password incorrecto", 'login')
        return redirect('/')

    session['usuario_id'] = user.id

    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)

    fligths = Fligth.get_all()
    formatoFecha(fligths)
    formatoHora(fligths)

    return render_template('dashboard.html', user=user, fligths=fligths)


@app.route('/logout')
def logout():
    session.clear()  # Elimine la sesión
    return redirect('/')


def formatoFecha(fligths):
    for fligth in fligths:
        date = str(fligth.departure_date)[0:10]
        anio = date[0:4]
        mes = date[5:7]
        dia = date[8:]
        date = dia+"/"+mes+"/"+anio
        fligth.departure_date = date


def formatoHora(fligths):
    for fligth in fligths:
        hour = str(fligth.departure_hour)[11:16]
        fligth.departure_hour = hour
