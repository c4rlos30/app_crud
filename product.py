class Product:
    #Constructor de la clase
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    #funcion que nos de la estructura para guardar los datos en la base de datos

    def toDBCollection(self):
        return{
            'name':self.name,
            'price':self.price,
            'quantity':self.quantity
        }