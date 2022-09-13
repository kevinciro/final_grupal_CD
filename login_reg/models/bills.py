from login_reg.config.mysqlconnection import connectToMySQL
from flask import flash  # mandar mensajes a la plantilla


class Bill:

    def __init__(self, data):
        self.id = data['id']
        self.total_price = data['total_price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dni = data['dni']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO bills(total_price, user_id) VALUES (%(total_price)s, %(user_id)s)"
        result = connectToMySQL('finalGrupal').query_db(query, formulario)  # 1 - Insert recibe id
        return result  # result = Identificador del nuevo registro

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT b.*, u.first_name, u.last_name, u.dni FROM finalGrupal.bills AS b INNER JOIN users AS u ON b.user_id = u.id WHERE id = %(id)s"
        result = connectToMySQL('finalGrupal').query_db(query, formulario)  # Select recibe lista
        bill = cls(result[0])
        return bill
