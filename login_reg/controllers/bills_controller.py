from flask import redirect, request, render_template
from login_reg import app
from login_reg.models.bills import Bill


# Creando una ruta para crear un nuevo vuelo
@app.route('/bills/new', methods=['POST'])
def new_bill():
    # request.form = {
    #         self.total_seats = 3
    #
    #         self.created_at = data['created_at']
    #         self.updated_at = data['updated_at']
    #         self.user_id = 20
    # }

    formulario = {
        "total_price": 0,
        "user_id": request.form['user_id'],
    }

    id = Bill.save(formulario)

    formularioGet = {
        "id": id,
    }

    bill = Bill.get_by_id(formularioGet)

    return render_template('purchase_seats.html', bill=bill, flight_id=request.form['flight_id'])


# Creando una ruta para consultar facturas por id
@app.route('/bills/<int:id>', methods=['GET'])
def find_bill_by_id(id):
    formulario = {
        "id": int(id)
    }

    bill = Bill.get_by_id(formulario)

    return redirect('/dashboard')