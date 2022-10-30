from Modelos.modeloMesa import ModeloMesa
from Repositorio.RepositorioMesa import RepositorioMesa


class ControladorMesa():

    def __init__(self):
        print("Creando Controlador Mesa")
        self.repositorioMesa = RepositorioMesa()


    def createMesa(self, infoMesa):
        print("Creando el mesa...")
        nuevomesa = ModeloMesa(infoMesa)
        print("mesa a crear en base de datos: ", nuevomesa.__dict__)
        self.repositorioMesa.save(nuevomesa)
        return True

    def showidMesa(self, id):
        print("Mostrando un Mesa con id ", id)
        mesa = ModeloMesa(self.repositorioMesa.findById(id))
        return mesa.__dict__

    def showallMesa(self):
        print("Mostrando las mesas de la base de datos ")
        return self.repositorioMesa.findAll()

    def updateMesa(self, infoMesa):
        mesaactual = ModeloMesa(self.repositorioMesa.findById((infoMesa["infoMesa"])))
        print("Actualizando Mesa con id ", mesaactual)
        mesaactual.numero = infoMesa["numero"]
        mesaactual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        self.repositorioMesa.save(mesaactual)
        return True

    def deleteMesa(self, id):
        print("Elimiando Mesa con id ", id)
        self.repositorioMesa.delete(id)
        return True
