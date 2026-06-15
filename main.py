

def enlistar_csv(nombre_archivo):
    lista = []
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    archivo.readline() # Saltar encabezado
    for linea in archivo: #leemos linea por linea
        linea_limpia = linea.strip()
        nombre, poblacion, superficie, continente = linea_limpia.split(',') #desempaquetamos la linea
        pais = {
            'nombre' : nombre,
            'poblacion' : poblacion,
            'superficie' : superficie,
            'continente' : continente,
        }
        lista.append(pais)
    archivo.close()
    
    return lista

#PRUEBA
lista_paises = enlistar_csv('TPI2\TPI_2_programacion\paises.csv') # QUITAR
for i in lista_paises: print(i) # QUITAR

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
                print(f'Datos actuales: \nPais: {nombre_encontrado}')
                print(f'Continente: {continente_encontrado}')
                print(f'1. Poblacion: {poblacion_encontrada}')
                print(f'2. Superficie: {superficie_encontrada}')
                print('============================')
                
                while True:
                    try:
                        dato_a_cambiar = int(input('Ingrese el numero del dato que quisiera cambiar (1/2).'))
                        print('============================')
                        
                        if dato_a_cambiar in(1,2):
                            break
                        
                        else:
                            print('Error. Ingrese una opcion valida.')
                    except ValueError:
                        print('Error. Ingrese un numero valido.')
                        continue
                    
                    
                if dato_a_cambiar == 1:
                    print('A Continuacion ingrese el nuevo valor de la Poblacion.')
                    while True:
                        try:
                            nuevo_valor = int(input('Nuevo valor: '))
                            print('============================')
                            poblacion_encontrada = nuevo_valor
                            print(f'Se a actualizado la poblacion en {nombre_encontrado}')
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
                            print(f'Se a actualizado la superficie en {nombre_encontrado}')
                            break
                        except:
                            print('Error. Ingrese un numero valido.')
                        
                else:
                    print('Error. Ingrese un numero valido.')
                
                #Actualizo datos.
                pais['poblacion'] = poblacion_encontrada
                pais['superficie'] = superficie_encontrada
        if encontrado == False:
            print('No se encuentra un pais con ese nombre.')
            print('============================')

def filtrar_paises(lista_paises):
    while True:
        encontrado = False
        print('Filtrar paises por:')
        print('1. Continente')
        print('2. Rango de población')
        print('3. Rango de superficie')
        print('============================')
        
        while True:
            try:
                opcion = int(input('Opcion: '))
                
                if opcion in(1,2,3):
                    break
                
                else:
                    print('Error. Ingrese una opcion valida.')
                    print('============================')
                
            except ValueError:
                print('Error. Ingrese un numero valido.')
                print('============================')
                continue
        
        if opcion == 1:
            while True:
                print('A continuacion ingrese el nombre del continente.')
                continente = input('Continente: ')
                print('============================')
                contador_paises = 0
                for pais in lista_paises:
                    if pais['continente'] == continente:
                        encontrado = True
                        contador_paises =  contador_paises + 1
                        nombre_encontrado = pais['nombre']
                        continente_encontrado = pais['continente']
                        poblacion_encontrada = pais['poblacion']
                        superficie_encontrada = pais['superficie']
                        print(f'Pais: {nombre_encontrado}')
                        print(f'Continente: {continente_encontrado}')
                        print(f'Poblacion: {poblacion_encontrada}')
                        print(f'Superficie: {superficie_encontrada}')
                        print('============================')
                if contador_paises > 0:
                    print(f'Se han encontrado un total de {contador_paises} paises.')
                    print('============================')
                    return
                if encontrado == False:
                    print('No se ha encontrado pais con ese continente.')
                    print('============================')
                    continue
        
        elif opcion == 2:
            print('A continuacion debera ingresar 2 valores para el rango de poblacion.')
        
            while True:
                try:
                    minimo = int(input('Poblacion minima: '))
                    break
                except ValueError:
                    print('Error. Ingrese un numero valido.')
                    print('============================')
                
            while True:
                try:
                    maximo = int(input('Poblacion maxima: '))
                    break
                except ValueError:
                    print('Error. Ingrese un numero valido.')
                    print('============================')
                    
            
            
            contador_paises = 0
            for pais in lista_paises:
                if pais['poblacion'] >= minimo and pais['poblacion'] <= maximo:
                    
                    contador_paises = contador_paises + 1
                    
                    print(f"Pais: {pais['nombre']}")
                    print(f"Continente: {pais['continente']}")
                    print(f"Poblacion: {pais['poblacion']}")
                    print(f"Superficie: {pais['superficie']}")
                    print('============================')
            
            if contador_paises > 0:
                print(f'Se han encontrado un total de {contador_paises} paises.')
                return
            else:
                print('No se encontraron paises en ese rango.')
                continue
        
        elif opcion == 3:
            print('A continuacion debera ingresar 2 valores para el rango de superficie.')
            
            while True:
                try:
                    minimo = int(input('Superficie minima: '))
                    break
                except ValueError:
                    print('Error. Ingrese un numero valido.')
                    print('============================')
                
            while True:
                try:
                    maximo = int(input('Superficie maxima: '))
                    break
                except ValueError:
                    print('Error. Ingrese un numero valido.')
                    print('============================')
            
            
            contador_paises = 0
            for pais in lista_paises:
                if pais['superficie'] >= minimo and pais['superficie'] <= maximo:
                    
                    contador_paises = contador_paises + 1
                    
                    print(f"Pais: {pais['nombre']}")
                    print(f"Continente: {pais['continente']}")
                    print(f"Poblacion: {pais['poblacion']}")
                    print(f"Superficie: {pais['superficie']}")
                    print('============================')
            
            if contador_paises > 0:
                print(f'Se han encontrado un total de {contador_paises} paises.')
                print('============================')
                return
            else:
                print('No se encontraron paises en ese rango.')
                print('============================')
                continue

def mostrar_estadisticas(lista_paises):
    menor_poblacion = 9999999999
    mayor_poblacion = 0
    
    suma_poblacion = 0
    suma_superficie = 0
    
    c_america = 0
    c_europa = 0
    c_asia = 0
    c_africa = 0
    c_oceania = 0
    for pais in lista_paises:
        if pais['poblacion'] > mayor_poblacion:
            mayor_poblacion = pais['poblacion']
            pais_mayor_poblacion = pais['nombre']
        
        if pais['poblacion'] < menor_poblacion:
            menor_poblacion = pais['poblacion']
            pais_menor_poblacion = pais['nombre']
        
        suma_poblacion = suma_poblacion + pais['poblacion']
        suma_superficie = suma_superficie + pais['superficie']
        
        
        if pais['continente'] == 'America':
            c_america = c_america + 1
        elif pais['continente'] == 'Europa':
            c_europa = c_europa + 1
        elif pais['continente'] == 'Asia':
            c_asia = c_asia + 1
        elif pais['continente'] == 'Africa':
            c_africa = c_africa + 1
        elif pais['continente'] == 'Oceania':
            c_oceania = c_oceania + 1

    promedio_poblacion = suma_poblacion / len(lista_paises)
    promedio_superficie = suma_superficie / len(lista_paises)
    
    print('Pais con mayor poblacion:')
    print(pais_mayor_poblacion)
    print('============================')
    
    print('Pais con menor poblacion:')
    print(pais_menor_poblacion)
    print('============================')
    
    print('Promedio de poblacion:')
    print(f'{promedio_poblacion:.2f}')
    print('============================')
    
    print('Promedio de superficie:')
    print(f'{promedio_superficie:.2f}')
    print('============================')
    
    print('Cantidad de paises por continente:')
    print('America:',c_america)
    print('Europa:',c_europa)
    print('Asia:',c_asia)
    print('Africa:',c_africa)
    print('Oceania:',c_oceania)

