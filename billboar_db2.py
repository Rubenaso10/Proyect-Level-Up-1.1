from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Billboards(db.Model):
        id = db.Column(db.Integer, primary_key =True)
        title = db.Column(db.String,nullable=False) 
        url_img = db.Column(db.String,nullable=False) 
        clasification = db.Column(db.String)
        id_function = db.Column(db.Integer,nullable=False)
        date_time = db.Column(db.String,nullable=False)

        def __str__(self):
                return "\ntitle:{}. url_img:{}.clasification:{}.id_function:{}.date_time:{}\n".format(
                        self.title,
                        self.url_img,
                        self.clasification,
                        self.id_function,
                        self.date_time

                )
        
        def serialize(self):
                return{
                        "id":self.id,
                        "title":self.title,
                        "url_img":self.url_img,
                        "clasification":self.clasification,
                        "id_function": self.id_function,
                        "date_time":self.date_time
                }
                