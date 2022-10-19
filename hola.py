from flask import Flask
#Librerias necesarias para SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

#Definir el motor MariaDb usando el conector MariaDB Connector/Phyton
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://misventas:misventas@localhost:3306/empleadosdb")

Base = declarative_base()

#Modelo de Datos
class Empleado(Base):
	__tablename__ = 'empleados'
	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	nombre = sqlalchemy.Column(sqlalchemy.String(length=30))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

@app.route('/')
def index():
	return '<h1>Hola Mundo</h1>'

@app.route('/user/<nombre>')
def user(nombre):
	return '<h1>Hola %s!</h1>'% nombre

@app.route('/empleado/insertar/<nombre>')
def insertar(nombre):
	emp = Empleado(nombre=nombre)
	session.add(emp)
	session.commit()

	return '<h1> %s registrado en la BD</h1>'% emp.nombre

@app.route('/empleados')
def empleados():
	empleados=session.query(Empleado).all()
	return '<h1>Lista de Empleados</h1>'

if __name__== '__main__':
	app.run(debug=True)
