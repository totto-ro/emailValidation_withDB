from email_app.config.MySQLConnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash


class Email:
    db = "email_db"
    def __init__(self, id, email, created_at, updated_at):
        self.id = id
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def add_info( cls, data ):
        query = "INSERT into emails ( email ) VALUES (%(email)s);"
        result = connectToMySQL(cls.db).query_db( query,data )
        return result

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)

        emails = []
        for element in results: #la validacion de si un email ya existe puede hacerse aquí?
            emails.append( Email( element['id'], element['email'], element['created_at'], element['updated_at'] ) )
        return emails

    @classmethod
    def destroy( cls, emailID ):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        data = {
            "id" : emailID
        }
        result = connectToMySQL( cls.db ).query_db( query, data )
        return result


    @staticmethod
    def is_valid( email ):
        is_valid = True
        query = "SELECT* FROM emails WHERE email = %(email)s;"
        email = {
            "email": email
        }
        result = connectToMySQL( Email.db ).query_db( query, email )
        print(result)
        print('helloooo')

        if len( result ) >= 1: #find out if already there is an email 
            flash( "Email already taken." )
            is_valid = False
        if not EMAIL_REGEX.match( email ):
            flash( "Invalid Email!!!" )
            is_valid = False
        return is_valid

