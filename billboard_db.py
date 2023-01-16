from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,Integer,String,DateTime,create_engine
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()
engine = create_engine("sqlite:///:memory:")

#db= SQLAlchemy()

class Billboard(Base):
        
        __tablename__ = 'movies' #nombre de la tabla

        id = Column(Integer, primary_key =True)
        title = Column(String,nullable=False) 
        url_img = Column(String,nullable=False) 
        clasification = Column(String)
        id_function = Column(Integer,nullable=False)
        date_time = Column(String,nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)#create session active
session1 = Session()

movie1 = Billboard(title="Avatar",url_img="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/313099306_466556672134552_8738886800381528729_n_480x.progressive.jpg?v=1669136451",clasification="B",id_function=1234,date_time="2022-03-15 12:05:57")
movie2 = Billboard(title="Spiderman",url_img="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/301983133_1072845516765536_7607702103270945846_n_500x749.jpg?v=1665071762",clasification="B",id_function=4560,date_time="2021-03-15 12:05:57")
movie3 = Billboard(title="Batman",url_img="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/c6f663c3b042cb061aa74d607183a34c_31928227-8024-4131-bbd8-eb3a67a426ba_500x749.jpg?v=1573587310",clasification="B",id_function=7890,date_time="2023-03-15 12:05:57")
movie4 = Billboard(title="Scream",url_img="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/scream5_500x749.jpg?v=1634919281",clasification="C",id_function=1043,date_time="2023-03-15 12:05:57")
movie5 = Billboard(title="the ring",url_img="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/3bd1695448a5d0e2c9e46e3611c0bb71_7204ebd7-ebb5-444a-b288-64186473335b_500x749.jpg?v=1573654008",clasification="C",id_function=1784,date_time="2022-03-15 12:05:57")

print(movie1.title)

session1.add(movie1)
session1.add(movie2)
session1.add(movie3)
session1.add(movie4)
session1.add(movie5)

session1.commit()