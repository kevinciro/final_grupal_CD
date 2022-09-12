from flask_app.config.mysqlconnection import connectToMySQL

import re #Importamos expresiones regulares

#crear una expresión regular para verificar que tengamos el email con formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$')

# DNI_REGEX = re.compile(r'^[\d]{1,3}\.?[\d]{3,3}\.?[\d]{3,3}$')

# La contraseña debe tener al entre 8 y 16 caracteres, al menos un dígito, al menos una minúscula y al menos una mayúscula.
# Detodounpoc0 (contraseña valida) 


#crear una expresion regular para verificar que tengamos el imail con formato correto

from flask import flash, redirect
#flash manda mensajes a la plantilla


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email'] 
        self.age = data['age']
        self.dni = data['dni']
        self.password = data['password'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users(first_name, last_name, email, age, password, dni) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(age)s, %(password)s, %(dni)s)"
        result = connectToMySQL('final').query_db(query, formulario) #1 - Insert recibe id
        print(result)
        return result #result = Identificador del nuevo registro

    @staticmethod
    def valida_usuario(formulario):
        #formulario = {
        #    first_name:    "Elena",
        #    last_name:     "De Troya",
        #    email:         "elena@codingdojo.com",
        #    password:      "password123",
        #confirm_password:      "password123",
        #}
        es_valido = True
        
        #Validar que mi nombre tenga más de 2 caracteres
        if len(formulario['first_name']) < 3:
            flash('Nombre debe de tener al menos 3 caracteres', 'registro')
            es_valido = False
        
        if len(formulario['last_name']) < 3:
            flash('Apellido debe de tener al menos 3 caracteres', 'registro')
            es_valido = False
        
        if len(formulario['age']) < 1: 
            flash('Edad debe de tener al menos 3 caracteres', 'registro')
            es_valido = False

        if len(formulario['dni']) < 3:
            flash('Identificacion debe de tener al menos 3 caracteres', 'registro')
            es_valido = False

        #Valido email con expresiones regulares
        if not EMAIL_REGEX.match(formulario['email']): 
            flash('Email invalido', 'registro')
            es_valido = False


        if len(formulario['password']) < 6:
            flash('Contraseña debe tener al menos 6 caracteres', 'registro')
            es_valido = False
        
        if formulario['password'] != formulario['confirm_password']:
            flash('Contraseñas no coiniciden', 'registro')
            es_valido = False
        
        #Consultar si YA existe el correo
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('final').query_db(query, formulario)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_email(cls, formulario):
        #formulario = {
        #   "email": "elena@cd.com"
        #   "password": "1234"
        #}
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('final').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            #result = [ {first_name: Elena, last_name: De Troya.....} ]
            user = cls(result[0]) #Haciendo una instancia de User -> CON los datos que recibimos de la base de datos
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('final').query_db(query, formulario) #Select recibe lista
        user = cls(result[0])
        return user