from flask import Flask,request,jsonify
from billboar_db2 import db, Billboards
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base,sessionmaker
Base = declarative_base()
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)#create session active

#Init app
app =Flask(__name__)
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind = engine)#create session active




#Database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///databases///movies.db' 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db.init_app(app)

#to indicate an endpoint
@app.route("/")
def hello_world():
    return "Hi everyone to Movies GT"

#path parameter
@app.route('/billboard')
def showMovies():
    try:
        q = Session.query(Billboards)
        return q
        
    except Exception:
        print("[SERVER]: Error")
        return jsonify({"msg": "Ha ocurrido un error"}),500
    return "<h1>Success</h1>"
    
    """
   
    return{
        "movie_id": request.form[Billboard.id],
        "tittle": request.form[Billboard.title],
        "url_img": request.form[Billboard.url_img],
        "clasification": request.form[Billboard.clasification],
        "id_function": request.form[Billboard.id_function],
        "date-time":request.form[Billboard.date_time]

    }
     """
    



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