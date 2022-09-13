from flask import render_template, redirect, session, request, flash
from login_reg import app
from login_reg.models.seats import Seat


# Creando una ruta para crear un nuevo vuelo
@app.route('/seats/new', methods=['POST'])
def new_seat():
    # request.form = {
    #         self.seat_number = 30
    #         self.seat_price = 100000
    #         self.created_at = data['created_at']
    #         self.updated_at = data['updated_at']
    #         self.user_id = 2
    #         self.fligth_id = 3
    #         self.bill_id = 5
    # }

    formulario = {
        "seat_number": request.form['seat_number'],
        "seat_price": request.form['seat_price'],
        "user_id": request.form['user_id'],
        "fligth_id": request.form['fligth_id'],
        "bill_id": request.form['bill_id'],
    }
    Seat.save(formulario)  # Guardando a mi usuario y recibo el ID del nuevo registro
    return redirect('/dashboard')


# Creando una ruta para consultar asientos por id
@app.route('/seats/<int:id>', methods=['GET'])
def find_seat_by_id(id):
    formulario = {
        "id": int(id)
    }

    seat = Seat.get_by_id(formulario)

    return redirect('/dashboard')