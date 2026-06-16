# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**
Tecnicatura Universitaria en Programación — UTN

---

## Integrantes

| Nombre | GitHub |
|--------|--------|
| Benjamín Provera Rocha | [@Benjaa635](https://github.com/Benjaa635) |
| Tomás Rocco D'Ambrosio | [@dambro182](https://github.com/dambro182) |

---

## Tutores

| Nombre | Comisión |
|--------|----------|
| Sofía Elizabeth Fernández | C14 |
| Flor Camila Gubiotti | C19 |

---

## Descripción

Sistema de gestión de información sobre países desarrollado en Python 3.
Permite cargar datos desde un archivo CSV y realizar operaciones de consulta,
filtrado, ordenamiento y estadísticas a través de un menú interactivo en consola.

---

## Estructura del proyecto

```
TPI_2_programacion/
│
├── main.py          # Código fuente principal
├── paises.csv       # Dataset base de países
└── README.md        # Este archivo
```

---

## Instrucciones de uso

### Requisitos
- Python 3.x instalado
- El archivo `paises.csv` debe estar en la misma carpeta que `main.py`

### Ejecutar el programa
```bash
python main.py
```

### Formato del CSV
El archivo `paises.csv` debe tener el siguiente formato:
```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Japon,125800000,377975,Asia
Brasil,213993437,8515767,America
Alemania,83149300,357022,Europa
```

---

## Menú de opciones

```
============================
   GESTIÓN DE PAÍSES
============================
1. Agregar país
2. Buscar país
3. Actualizar datos de un país
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
0. Salir
============================
```

---

## Funcionalidades

### 1. Agregar país
Solicita nombre, población, superficie y continente. Valida que ningún campo esté vacío y que los tipos de datos sean correctos. Guarda el nuevo país en el CSV.

**Ejemplo:**
```
Nombre del país: Uruguay
Población: 3500000
Superficie (km²): 176215
Continente: America
→ País "Uruguay" agregado correctamente.
```

### 2. Buscar país
Busca por coincidencia parcial o exacta sin distinción de mayúsculas.

**Ejemplo:**
```
Ingrese el nombre o parte del nombre a buscar: ar
→ Encuentra: Argentina, Qatar, Bulgaria...
```

### 3. Actualizar datos
Permite modificar la población o la superficie de un país existente.

**Ejemplo:**
```
Nombre exacto del país: Argentina
1. Población : 45376763
2. Superficie: 2780400 km²
¿Qué dato desea actualizar? (1/2): 1
Nueva población: 46000000
→ Población de "Argentina" actualizada a 46000000.
```

### 4. Filtrar países
Filtra por:
- **Continente:** muestra todos los países de ese continente.
- **Rango de población:** muestra países cuya población esté entre un mínimo y un máximo.
- **Rango de superficie:** igual pero por superficie en km².

**Ejemplo:**
```
Opción: 2 (Rango de población)
Población mínima: 10000000
Población máxima: 50000000
→ Muestra todos los países en ese rango.
```

### 5. Ordenar países
Ordena por nombre, población o superficie, en orden ascendente o descendente. Utiliza el algoritmo **Bubble Sort**.

**Ejemplo:**
```
Opción: 2 (Población)
Orden (ASC / DESC): desc
→ Lista ordenada de mayor a menor población.
```

### 6. Mostrar estadísticas
Calcula y muestra:
- País con mayor y menor población
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente

**Ejemplo de salida:**
```
País con mayor población : China (1,400,000,000)
País con menor población : Vaticano (800)
Promedio de población    : 45,230,000.00
Promedio de superficie   : 512,300.00 km²
Cantidad de países por continente:
  America: 5
  Europa: 4
  Asia: 6
```

---

## Validaciones implementadas

- Campos vacíos no permitidos en ninguna entrada
- Nombres de países y continentes sin números ni símbolos
- Población y superficie deben ser números enteros mayores a 0
- Opciones de menú con control de errores (`ValueError`)
- Manejo de archivo CSV no encontrado
- Líneas con formato incorrecto en el CSV son ignoradas con advertencia

---

## Links

- Repositorio: [github.com/Benjaa635/TPI_2_programacion](https://github.com/Benjaa635/TPI_2_programacion)
- Video demostración: _(agregar link aquí)_
- Documentación PDF: _(agregar link aquí)_

---

## Tecnologías utilizadas

- Python 3.x
- Archivos CSV (lectura y escritura nativa)
- Estructuras: listas, diccionarios, funciones
- Algoritmo de ordenamiento: Bubble Sort
