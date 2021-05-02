class socio:

    def __init__(self,id_socio,dni,nombre,apellido,fecha,saldo):
        self.id_socio=id_socio
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.fecha=fecha
        self.saldo=saldo
        self.registro={}

    def getIdsocio(self):
        return self.id_socio
    def getDni(self):
        return self.dni
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido        
    def getFecha(self):
        return self.fecha
    def getSaldo(self):
        return self.saldo      
    def setsaldo(self,saldo):
        self.saldo = saldo
    def getregistro(self):
        return self.registro
    def setRegistro(self,nombre,kilos):
        if nombre in self.registro:
            self.registro[nombre] += kilos
        else:
            self.registro[nombre] = kilos
    
    def actualizaSaldo(self,saldo):
        self.saldo+=saldo


    def delRegistros(self):
        self.registro={}        
    
        