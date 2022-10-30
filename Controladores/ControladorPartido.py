from Modelos.modeloPartido import ModeloPartido
from Repositorio.RepositorioPartido import RepositorioPartido



class ControladorPartido():
    def __init__(self):
        print("Creando Controlador Partido")
        self.repositorioPartido = RepositorioPartido()

    def createPartido(self, infoPartido):
        print("Creando el candidato....")
        nuevopartido = ModeloPartido(infoPartido)
        print("estudiante a crear en base de datos: ", nuevopartido.__dict__)
        self.repositorioPartido.save(nuevopartido)
        return True

    def showidPartido(self, id):
        print("Mostrando un Partido con id ", id)
        partido=ModeloPartido(self.repositorioPartido.findById(id))
        return partido.__dict__

    def showallPartido(self):
        print("Mostrando las partido de la base de datos ")
        return self.repositorioPartido.findAll()

    def updatePartido(self,infoPartido):
        partidoactual = ModeloPartido(self.repositorioPartido.findById((infoPartido["infoPartido"])))
        print("Actualizando Partido con id ", partidoactual)
        partidoactual.nombre= infoPartido["nombre"]
        partidoactual.lema = infoPartido["lema"]
        self.repositorioPartido.save(partidoactual)
        return True

    def deletePartido(self, id):
        print("Elimiando Mesa con id ", id)
        self.repositorioPartido.delete(id)
        return True

