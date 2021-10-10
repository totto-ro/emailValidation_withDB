from flask import render_template, redirect, request
from email_app import app
from email_app.models.Email import Email

@app.route('/', methods=['GET'])         
def index():
    return render_template("index.html")

@app.route( '/create/email', methods=['POST'] )
def add_info():

    email = request.form['email']

    if Email.is_valid( email ):
        newEmail = Email ( email )
        result = Email.add_info
        Email.add_info( newEmail )
        print( result )
        return redirect ( '/result' )
    else:
        print( "Something went wrong" )
        return redirect ( '/' )

        

@app.route( '/result' )
def results():
    email = Email.get_all()
    return render_template( 'result.html', emails = email )

@app.route( "/destroy/<int:id>",  methods=['GET'])
def destroy (id):
    emailID = id
    Email.destroy( emailID )
    return redirect ( '/result' )

