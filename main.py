# nombre,poblacion,superficie,continente
#Argentina,45376763,2780400,América

paises = []
pais = {
    'nombre' : 'Argentina',
    'poblacion' : 45376763,
    'superficie' : 2780400,
    'continente' : 'América',
}
paises.append(pais)

def actualizar_datos(lista_paises):
    encontrado = False
    print('Ingrese el nombre del pais sobre el que quiere actualizar los datos.')
    while True:
        nombre = input('Pais: ')
        print('============================')
        for pais in  lista_paises:
            if pais['nombre'] == nombre:
                nombre_encontrado = pais['nombre']
                continente_encontrado = pais['continente']
                poblacion_encontrada = pais['poblacion']
                superficie_encontrada = pais['superficie']
                encontrado = True
                print(f'Datos actuales \nPais: {nombre_encontrado}')
                print(f'Continente: {continente_encontrado}')
                print(f'1. Poblacion: {poblacion_encontrada}')
                print(f'2. Superficie: {superficie_encontrada}')
                print('============================')
                
                while True:
                    try:
                        dato_a_cambiar = int(input('Ingrese el numero del dato que quisiera cambiar (1/2).'))
                        print('============================')
                        break
                    except:
                        print('Error. Ingrese un numero valido.')
                    
                if dato_a_cambiar == 1:
                    print('A Continuacion ingrese el nuevo valor de la Poblacion.')
                    while True:
                        try:
                            nuevo_valor = int(input('Nuevo valor: '))
                            print('============================')
                            poblacion_encontrada = nuevo_valor
                            break
                        except:
                            print('Error. Ingrese un numero valido.')
                        
                elif dato_a_cambiar == 2:
                    print('A Continuacion ingrese el nuevo valor de la Superficie.')
                    while True:
                        try:
                            nuevo_valor = int(input('Nuevo valor: '))
                            print('============================')
                            superficie_encontrada = nuevo_valor
                            break
                        except:
                            print('Error. Ingrese un numero valido.')
                        
                else:
                    print('Error. Ingrese un numero valido.')
                
                #Actualizo datos.
                poblacion_encontrada = pais['poblacion']
                superficie_encontrada = pais['superficie']
        if encontrado == False:
            print('No se encuentra un pais con ese nombre.')
            print('============================')

actualizar_datos(paises)