from flask import render_template, redirect, session, request, flash
from login_reg import app
from login_reg.models.bills import Bill


# Creando una ruta para crear un nuevo vuelo
@app.route('/bills/new', methods=['POST'])
def new_bill():
    # request.form = {
    #         self.total_price = 100000
    #         self.created_at = data['created_at']
    #         self.updated_at = data['updated_at']
    #         self.user_id = 20
    # }

    formulario = {
        "total_price": request.form['departure_date'],
        "user_id": request.form['user_id'],
    }

    Bill.save(formulario)

    return redirect('/dashboard')


# Creando una ruta para consultar facturas por id
@app.route('/bills/<int:id>', methods=['GET'])
def find_bill_by_id(id):
    formulario = {
        "id": int(id)
    }

    bill = Bill.get_by_id(formulario)

    return redirect('/dashboard')