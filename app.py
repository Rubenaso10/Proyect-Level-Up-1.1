from flask import Flask

app =Flask(__name__)

#to indicate an endpoint
@app.route("/")
def hello_world():
    return "Hi everyone to Movies GT"



"""    
@app.route('/edad/<int:edad_persona>')
def verificar_edad(edad_persona):
    if edad_persona >= 18:
        return "Es un adulto"
    else:
        return "No es un adulto"

@app.route('/saludo',methods=['POST'])
def saludar():
    return "Saludos a todos desde el POST"

@app.route('/users',methods=['POST'])
def registrar():
    return{
        "metodo": request.method,
        "nombre": request.form["nombre"],
        "edad": request.form["edad"]
    }

@app.errorhandler(404)
def not_found(error):
    return "uppss este endpoint no existe"
"""