from flask import render_template, redirect, session, request, flash
from login_reg import app
from login_reg.models.fligths import Fligth


# Creando una ruta para crear un nuevo vuelo
@app.route('/fligths/new', methods=['POST'])
def new_fligth():
    # request.form = {
    #         self.departure_date = 20-10-2022
    #         self.departure_hour = 06:00
    #         self.departure_place = "Medellin"
    #         self.destiny_place = "Cartagena"
    #         self.total_seats = 60
    #         self.created_at = data['created_at']
    #         self.updated_at = data['updated_at']
    # }

    formulario = {
        "departure_date": request.form['departure_date'],
        "departure_hour": request.form['departure_hour'],
        "departure_place": request.form['departure_place'],
        "destiny_place": request.form['destiny_place'],
        "total_seats": request.form['total_seats'],
    }

    id = Fligth.save(formulario)  # Guardando a mi usuario y recibo el ID del nuevo registro

    return redirect('/dashboard')


# Creando una ruta para consultar vuelos por id
@app.route('/fligths/<int:id>', methods=['GET'])
def find_fligth_by_id(id):
    formulario = {
        "id": int(id)
    }

    fligth = Fligth.get_by_id(formulario)

    date = str(fligth.departure_date)[0:10]
    anio = date[0:4]
    mes = date[5:7]
    dia = date[8:]
    date = dia + "/" + mes + "/" + anio
    fligth.departure_date = date

    hour = str(fligth.departure_hour)[11:16]
    fligth.departure_hour = hour

    # Hay que cambiar la pagina que se renderiza
    return render_template("render_flight.html", fligth=fligth)


# Creando una ruta para consultar vuelos por id
@app.route('/fligths', methods=['GET'])
def find_all():

    fligths = Fligth.get_all()

    # Hay que cambiar la pagina que renderiza
    return redirect('/dashboard')
