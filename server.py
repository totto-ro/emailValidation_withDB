from flask import Flask
from email_app import app
from email_app.controllers import emails_controller


if __name__ == "__main__":
    app.run( debug = True )