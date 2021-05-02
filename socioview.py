from socio import socio
from sociocontroller import sociocontroller
from datetime import datetime
con = sociocontroller()
registro = []
while True:
    print("1-Añadir socio")
    print("2-Baja socio")
    print("3-Lisar socio")
    print("4-Registrar socio")
    print("5-Actualizar socio")
    print("6-ficha socio")

    while True:
        try:
            opcion=int(input("Que opcion eliges"))
            break
        except ValueError:
            print("Solo numeros")  

    if opcion == 1:
        id_socio=input("Dime la id del socio")
        dni=input("Dime el dni")
        nombre=input("Dime el nombre") 
        apellido=input("Dime el apellido")
        fecha=datetime.now()
        saldo=0
        soc = socio(id_socio,dni,nombre,apellido,fecha,saldo)
        con.addsocio(soc)
    if opcion == 2:              
        id_socio=input("Dime la id del socio")

    if opcion == 3:
        print("***LISTAR socios***")
        listasocios = con.listar()
        if(len(listasocios)== 0):
            print("Aun no hay socios")
        else: 
            for i in listasocios:
                print("ID_SOCIO",listasocios[i].getIdsocio())
                print("dni",listasocios[i].getDni())
                print("nombre",listasocios[i].getNombre())
                print("Apellido",listasocios[i].getApellido())
                print("Fecha",listasocios[i].getFecha())
                print("saldo",listasocios[i].getSaldo())
          
    if opcion ==4:
        id_socio=input("Dime la id del socio")   
        con.lisrarproductos()
        nombre=input("DIME EL PRODUCTO")
        kilos = int(input("Dime kilos"))
        if con.registrarsocio(id_socio,nombre,kilos)==True:
            print("se ha guardadooo")
        else:
            print("No se ha guardado")     


          


    if opcion ==5:
        id_socio=input("Dime la id del socio") 
        con.lisrarproductos()
        if con.actualizasaldo(id_socio)==True:
            print("Se ha actualizado")

        else:
            print("no se ha actualizado")
    if opcion==6:
        id_socio=input("Introduce el id del socio: ")

        print(con.fichaSocio(id_socio))
