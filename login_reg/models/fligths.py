from login_reg.config.mysqlconnection import connectToMySQL
from flask import flash  # mandar mensajes a la plantilla
import re  # Importamos expresiones regulares

# crear una expresión regular para verificar que tengamos el email con formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Expresion regular para una contraseña que tenga 1 digito, 1 minuscula, 1 mayuscula y 1 caracter especial
PASSWORD_REGEX = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$')


class Fligth:

    def __init__(self, data):
        self.id = data['id']
        self.departure_date = data['departure_date']
        self.departure_hour = data['departure_hour']
        self.departure_place = data['departure_place']
        self.destiny_place = data['destiny_place']
        self.total_seats = data['total_seats']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO fligths(departure_date, departure_hour, departure_place, destiny_place, total_seats) VALUES (%(departure_date)s, %(departure_hour)s, %(departure_place)s, %(destiny_place)s, %(total_seats)s)"
        result = connectToMySQL('finalGrupal').query_db(query, formulario)  # 1 - Insert recibe id
        return result  # result = Identificador del nuevo registro

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM fligths WHERE id = %(id)s"
        result = connectToMySQL('finalGrupal').query_db(query, formulario)  # Select recibe lista
        fligth = cls(result[0])
        return fligth

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM fligths"
        results = connectToMySQL('finalGrupal').query_db(query)  # Select recibe lista
        fligths = []
        for result in results:
            fligth = cls(result)
            fligths.append(fligth)
        return fligths
