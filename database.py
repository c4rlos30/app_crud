from pymongo import MongoClient #pymongo es el controlador de python para MongoDB, permite que aplicaciones en python puedan interactuar sobre bases de datos MongoDB
import certifi #Certifi se utiliza con PyMongo para asegurar conexiones a bases de datos MongoDB a través de TLS/SSL

MONGO_URI = 'mongodb+srv://c4RL0S:304BR1L@cluster0.vvzbeud.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
ca=certifi.where()

#función para conectarnos a la base de datos
def dbconnection():
    try:
        cliente = MongoClient(MONGO_URI, tlsCAFile=ca)
        db=cliente["dbb_products_app"] # creación de base de datos en caso de que no exista
    except ConnectionError:
        print('Error de conexión con la bdd') #excepcion en caso de error 
    return db