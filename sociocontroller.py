from socio import socio
class sociocontroller:
    def __init__(self):
        self.listasocios={}
        self.productos={'naranja':5,'platano':10,'manzana':3}
    def addsocio(self,socio):
        if socio.getIdsocio() not in self.listasocios:
            if socio.getDni() not in self.listasocios:
                self.listasocios[socio.getIdsocio()] = socio
                return True
        return False        
    def borrarsocio(self,id_socio):
        if id in self.listasocios:
            del self.listasocios[id_socio]
            return True
        return False
    def listar(self):
        return self.listasocios
    def registrarsocio(self,id_socio,nombre,kilos):
        if id_socio in self.listasocios:
            if nombre in self.productos:
                self.listasocios[id_socio].setRegistro(nombre,kilos)
                return True
            return False    
        return False        
    def lisrarproductos(self):
        for key in self.productos:
            print (key, ":", self.productos[key])

    def actualizasaldo(self,id_socio):
        saldo=0.0
        if id_socio in self.listasocios:
            for clave,valor in self.listasocios[id_socio].getregistro().items():
                saldo+= self.productos[clave] * float(valor)

            self.listasocios[id_socio].actualizaSaldo(saldo)
            self.listasocios[id_socio].delRegistros()
            return True

        return False           
    def fichaSocio(self,id_socio):
        socio=""
        if id_socio in self.listasocios:
            for clave,valor in self.listasocios.items():
                socio = ("Id_socio: "+valor.getIdsocio()+"tDni: "+valor.getDni()+"Nombre: "+valor.getNombre()+"Apellidos: "+valor.getApellido()+"fecha: "+str(valor.getFecha())+"Saldo: "+str( "{:10.2f}".format(valor.getSaldo()))+"Registros Pendientes: "+str(valor.getregistro()))

        return socio    