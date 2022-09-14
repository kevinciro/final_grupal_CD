from login_reg.config.mysqlconnection import connectToMySQL
from flask import flash  # mandar mensajes a la plantilla


class Seat:

    def __init__(self, data):
        self.id = data['id']
        self.seat_number = data['seat_number']
        self.seat_price = data['seat_price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user_id = data['user_id']
        self.fligth_id = data['fligth_id']
        self.bill_id = data['bill_id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dni = data['dni']

        self.departure_date = data['departure_date']
        self.departure_hour = data['departure_hour']
        self.destiny_place = data['destiny_place']
        self.departure_place = data['departure_place']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO seats(seat_number, seat_price, user_id, fligth_id, bill_id) VALUES (%(seat_number)s, %(seat_price)s, %(user_id)s, %(fligth_id)s, %(bill_id)s);"
        result = connectToMySQL('finalGrupal').query_db(query, formulario)  # 1 - Insert recibe id
        return result  # result = Identificador del nuevo registro

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT s.*, u.first_name, u.last_name, u.dni, f.departure_date, f.departure_hour, f.destiny_place, f.departure_place FROM finalGrupal.seats AS s INNER JOIN users AS u ON s.user_id = u.id INNER JOIN fligths AS f ON s.fligth_id = f.id WHERE id = %(id)s;"
        result = connectToMySQL('finalGrupal').query_db(query, formulario)  # Select recibe lista
        seat = cls(result[0])
        return seat

    @classmethod
    def get_by_user_and_flight(cls, formulario):
        query = "SELECT s.* FROM finalGrupal.seats AS s WHERE user_id = %(user_id)s and fligth_id = %(fligth_id)s;"
        results = connectToMySQL('finalGrupal').query_db(query, formulario)  # Select recibe lista
        seats = []
        for result in results:
            seat = cls(result)
            seats.append(seat)
        return seats
