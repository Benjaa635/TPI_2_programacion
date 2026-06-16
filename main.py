
ARCHIVO_CSV = 'TPI2\TPI_2_programacion\paises.csv'

# ------------------------------------------------------------
# LECTURA DEL CSV
# ------------------------------------------------------------

def enlistar_csv(nombre_archivo):
    """Lee el CSV y devuelve una lista de diccionarios con los datos de cada país."""
    lista = []
    try:
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo "{nombre_archivo}".')
        return lista
    
    archivo.readline()  # Saltar encabezado
    for linea in archivo:
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue
        try:
            nombre, poblacion, superficie, continente = linea_limpia.split(',')
            pais = {
                'nombre'     : nombre,
                'poblacion'  : int(poblacion),
                'superficie' : int(superficie),
                'continente' : continente,
            }
            lista.append(pais)
        except ValueError:
            print(f'Advertencia: línea con formato incorrecto ignorada -> {linea_limpia}')
    archivo.close()
    return lista


# ------------------------------------------------------------
# GUARDAR EN CSV  (reescribe el archivo completo)
# ------------------------------------------------------------

def guardar_csv(lista_paises, nombre_archivo):
    """Sobreescribe el CSV con la lista de países actualizada."""
    archivo = open(nombre_archivo, 'w', encoding='utf-8')
    archivo.write('nombre,poblacion,superficie,continente\n')
    for pais in lista_paises:
        linea = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
        archivo.write(linea)
    archivo.close()


# ------------------------------------------------------------
# AGREGAR PAÍS
# ------------------------------------------------------------

def agregar_pais(lista_paises):
    """Solicita los datos de un nuevo país, los valida y los agrega a la lista y al CSV."""
    print('============================')
    print('  AGREGAR PAÍS')
    print('============================')
    
    # Nombre
    while True:
        nombre = input('Nombre del país: ').strip()
        if nombre == '':
            print('Error: el nombre no puede estar vacío.')
        elif not nombre.replace(' ', '').isalpha():
            print('Error: el nombre no puede contener números ni símbolos.')
        else:
            break
    
    # Verificar que no exista ya
    for p in lista_paises:
        if p['nombre'].lower() == nombre.lower():
            print(f'Error: el país "{nombre}" ya existe en la lista.')
            return
    
    # Población
    while True:
        entrada = input('Población: ').strip()
        if entrada == '':
            print('Error: la población no puede estar vacía.')
            continue
        try:
            poblacion = int(entrada)
            if poblacion <= 0:
                print('Error: la población debe ser mayor a 0.')
            else:
                break
        except ValueError:
            print('Error: ingrese un número entero válido.')
    
    # Superficie
    while True:
        entrada = input('Superficie: ').strip()
        if entrada == '':
            print('Error: la superficie no puede estar vacía.')
            continue
        try:
            superficie = int(float(entrada))
            if superficie <= 0:
                print('Error: la superficie debe ser mayor a 0.')
            else:
                break
        except ValueError:
            print('Error: ingrese un número válido.')
    
    # Continente
    while True:
        continente = input('Continente: ').strip()
        if continente == '':
            print('Error: el continente no puede estar vacío.')
        elif not continente.replace(' ', '').isalpha():
            print('Error: el nombre del continente no puede contener números ni símbolos.')
        else:
            break
    
    nuevo_pais = {
        'nombre'     : nombre,
        'poblacion'  : poblacion,
        'superficie' : superficie,
        'continente' : continente,
    }
    lista_paises.append(nuevo_pais)
    guardar_csv(lista_paises, ARCHIVO_CSV)
    print('============================')
    print(f'País "{nombre}" agregado correctamente.')
    print('============================')


# ------------------------------------------------------------
# BUSCAR PAÍS  (coincidencia parcial o exacta)
# ------------------------------------------------------------

def buscar_pais(lista_paises):
    """Busca países cuyo nombre contenga el texto ingresado (sin distinción de mayúsculas)."""
    print('============================')
    print('  BUSCAR PAÍS')
    print('============================')
    termino = input('Ingrese el nombre o parte del nombre a buscar: ').strip()
    if termino == '':
        print('Error: ingrese un término de búsqueda.')
        return
    
    resultados = [p for p in lista_paises if termino.lower() in p['nombre'].lower()]
    
    if not resultados:
        print('No se encontraron coincidencias.')
    else:
        print(f'Se encontraron {len(resultados)} resultado(s):')
        print('============================')
        for pais in resultados:
            mostrar_pais(pais)


# ------------------------------------------------------------
# ACTUALIZAR DATOS
# ------------------------------------------------------------

def actualizar_datos(lista_paises):
    """Permite actualizar la población o la superficie de un país existente."""
    print('============================')
    print('  ACTUALIZAR DATOS')
    print('============================')
    nombre = input('Ingrese el nombre exacto del país a actualizar: ').strip()
    print('============================')
    
    pais_encontrado = None
    for pais in lista_paises:
        if pais['nombre'].lower() == nombre.lower():
            pais_encontrado = pais
            break
    
    if pais_encontrado is None:
        print(f'No se encontró el país "{nombre}".')
        return
    
    print(f'Datos actuales de {pais_encontrado["nombre"]}:')
    print(f'  1. Población : {pais_encontrado["poblacion"]}')
    print(f'  2. Superficie: {pais_encontrado["superficie"]}')
    print('============================')
    
    while True:
        try:
            opcion = int(input('¿Qué dato desea actualizar? (1/2): '))
            if opcion in (1, 2):
                break
            print('Error: ingrese 1 o 2.')
        except ValueError:
            print('Error: ingrese un número válido.')
    
    if opcion == 1:
        while True:
            try:
                nuevo = int(input('Nueva población: '))
                if nuevo <= 0:
                    print('Error: debe ser mayor a 0.')
                else:
                    pais_encontrado['poblacion'] = nuevo
                    break
            except ValueError:
                print('Error: ingrese un número entero válido.')
        print(f'Población de "{pais_encontrado["nombre"]}" actualizada a {nuevo}.')
    else:
        while True:
            try:
                nuevo = int(float(input('Nueva superficie: ')))
                if nuevo <= 0:
                    print('Error: debe ser mayor a 0.')
                else:
                    pais_encontrado['superficie'] = nuevo
                    break
            except ValueError:
                print('Error: ingrese un número válido.')
        print(f'Superficie de "{pais_encontrado["nombre"]}" actualizada a {nuevo}.')
    
    guardar_csv(lista_paises, ARCHIVO_CSV)
    print('============================')


# ------------------------------------------------------------
# FILTRAR PAÍSES
# ------------------------------------------------------------

def filtrar_paises(lista_paises):
    """Filtra la lista de países por continente, rango de población o rango de superficie."""
    print('============================')
    print('  FILTRAR PAÍSES')
    print('============================')
    print('1. Por continente')
    print('2. Por rango de población')
    print('3. Por rango de superficie')
    print('============================')
    
    while True:
        try:
            opcion = int(input('Opción: '))
            if opcion in (1, 2, 3):
                break
            print('Error: ingrese una opción válida (1, 2 o 3).')
        except ValueError:
            print('Error: ingrese un número válido.')
    
    if opcion == 1:
        continente = input('Continente: ').strip()
        resultados = []
        
        for pais in lista_paises:
            if pais['continente'].lower() == continente.lower():
                resultados.append(pais)
    
    elif opcion == 2:
        while True:
            try:
                minimo = int(input('Población mínima: '))
                break
            except ValueError:
                print('Error: ingrese un número entero válido.')
        while True:
            try:
                maximo = int(input('Población máxima: '))
                break
            except ValueError:
                print('Error: ingrese un número entero válido.')
        resultados = [p for p in lista_paises if minimo <= p['poblacion'] <= maximo]
    
    else:
        while True:
            try:
                minimo = int(input('Superficie mínima: '))
                break
            except ValueError:
                print('Error: ingrese un número entero válido.')
        while True:
            try:
                maximo = int(input('Superficie máxima: '))
                break
            except ValueError:
                print('Error: ingrese un número entero válido.')
        resultados = [p for p in lista_paises if minimo <= p['superficie'] <= maximo]
    
    print('============================')
    if not resultados:
        print('No se encontraron países con ese criterio.')
    else:
        print(f'Se encontraron {len(resultados)} país/es:')
        print('============================')
        for pais in resultados:
            mostrar_pais(pais)


# ------------------------------------------------------------
# ORDENAR PAÍSES  (bubble sort manual, sin sorted())
# ------------------------------------------------------------

def ordenar_paises(lista_paises):
    """Ordena la lista de países por nombre, población o superficie (asc o desc) usando bubble sort."""
    print('============================')
    print('  ORDENAR PAÍSES')
    print('============================')
    print('Criterio de ordenamiento:')
    print('1. Nombre')
    print('2. Población')
    print('3. Superficie')
    print('============================')
    
    while True:
        try:
            criterio = int(input('Opción: '))
            if criterio in (1, 2, 3):
                break
            print('Error: ingrese 1, 2 o 3.')
        except ValueError:
            print('Error: ingrese un número válido.')
    
    while True:
        direccion = input('Orden (ASC / DESC): ').strip().lower()
        if direccion in ('asc', 'desc'):
            break
        print('Error: ingrese ASC o DESC.')
    
    # Definir la clave de comparación
    claves = {1: 'nombre', 2: 'poblacion', 3: 'superficie'}
    clave = claves[criterio]
    
    # Copia para no modificar el original en memoria (sí lo modifica, igual que el original)
    n = len(lista_paises)
    for i in range(n):
        for j in range(n - 1 - i):
            a = lista_paises[j][clave]
            b = lista_paises[j + 1][clave]
            # Comparación de strings en minúsculas para que el orden sea insensible a mayúsculas
            if isinstance(a, str):
                a, b = a.lower(), b.lower()
            intercambiar = (a > b) if direccion == 'asc' else (a < b)
            if intercambiar:
                lista_paises[j], lista_paises[j + 1] = lista_paises[j + 1], lista_paises[j]
    
    print('============================')
    print(f'Países ordenados por {clave} ({direccion.upper()}):')
    print('============================')
    for pais in lista_paises:
        mostrar_pais(pais)


# ------------------------------------------------------------
# MOSTRAR ESTADÍSTICAS
# ------------------------------------------------------------

def mostrar_estadisticas(lista_paises):
    """Calcula y muestra estadísticas generales sobre la lista de países."""
    if not lista_paises:
        print('No hay países cargados.')
        return
    
    print('============================')
    print('  ESTADÍSTICAS')
    print('============================')
    
    mayor_poblacion = lista_paises[0]['poblacion']
    menor_poblacion = lista_paises[0]['poblacion']
    pais_mayor = lista_paises[0]['nombre']
    pais_menor = lista_paises[0]['nombre']
    
    suma_poblacion  = 0
    suma_superficie = 0
    conteo = {}
    
    for pais in lista_paises:
        pob = pais['poblacion']
        sup = pais['superficie']
        con = pais['continente']
        
        if pob > mayor_poblacion:
            mayor_poblacion = pob
            pais_mayor = pais['nombre']
        if pob < menor_poblacion:
            menor_poblacion = pob
            pais_menor = pais['nombre']
        
        suma_poblacion  += pob
        suma_superficie += sup
        
        conteo[con] = conteo.get(con, 0) + 1
    
    promedio_poblacion  = suma_poblacion  / len(lista_paises)
    promedio_superficie = suma_superficie / len(lista_paises)
    
    print(f'País con mayor población : {pais_mayor} ({mayor_poblacion:,})')
    print(f'País con menor población : {pais_menor} ({menor_poblacion:,})')
    print(f'Promedio de población    : {promedio_poblacion:,.2f}')
    print(f'Promedio de superficie    : {promedio_superficie:,.2f}')
    print('============================')
    print('Cantidad de países por continente:')
    for continente, cantidad in conteo.items():
        print(f'  {continente}: {cantidad}')
    print('============================')


# ------------------------------------------------------------
# HELPER: mostrar un país
# ------------------------------------------------------------

def mostrar_pais(pais):
    print(f"  Nombre    : {pais['nombre']}")
    print(f"  Población : {pais['poblacion']:,}")
    print(f"  Superficie: {pais['superficie']:,}")
    print(f"  Continente: {pais['continente']}")
    print('  --------------------------')


# ------------------------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------------------------

def menu():
    lista_paises = enlistar_csv(ARCHIVO_CSV)
    
    while True:
        print('\n============================')
        print('   GESTIÓN DE PAÍSES')
        print('============================')
        print('1. Agregar país')
        print('2. Buscar país')
        print('3. Actualizar datos de un país')
        print('4. Filtrar países')
        print('5. Ordenar países')
        print('6. Mostrar estadísticas')
        print('0. Salir')
        print('============================')
        
        try:
            opcion = int(input('Opción: '))
        except ValueError:
            print('Error: ingrese un número válido.')
            continue
        
        if opcion == 1:
            agregar_pais(lista_paises)
        elif opcion == 2:
            buscar_pais(lista_paises)
        elif opcion == 3:
            actualizar_datos(lista_paises)
        elif opcion == 4:
            filtrar_paises(lista_paises)
        elif opcion == 5:
            ordenar_paises(lista_paises)
        elif opcion == 6:
            mostrar_estadisticas(lista_paises)
        elif opcion == 0:
            print('¡Hasta luego!')
            break
        else:
            print('Error: opción no válida.')


# ------------------------------------------------------------
# PUNTO DE ENTRADA
# ------------------------------------------------------------

if __name__ == '__main__':
    menu()