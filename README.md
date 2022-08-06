# freqtables

Este paquete permite crear tablas de frecuencias simples dado un conjunto de variables con sus respectivas frecuencias. Este conjunto de datos pueder una lista, tuple o un diccionario:

## freqtablesimple

```python
import freqtablesimple as fts

tabla1 = fts.FreqTableSimple([
    'A', 'A', 'A', 'B', 'B',
    'B', 'B', 'B', 'B', 'C'
])
tabla2 = fts.FreqTableSimple({
    'A':3, 'B':6, 'C':1
})
tabla3 = fts.FreqTableSimple(
    'A', 'A', 'A', 'B', 'B',
    'B', 'B', 'B', 'B', 'C'
)
tabla4 = fts.FreqTableSimple(
    A = 3, B = 6, C = 1
)
```

Cualquiera de estas dos formas de inicializar ```FreqTableSimple``` dando como resultado:

```python
>>> print(tabla1)
╒════╤═════╤═════╤═════╤══════╤══════╕
│    │  x  │  f  │  F  │  fr  │  Fr  │
╞════╪═════╪═════╪═════╪══════╪══════╡
│ 0  │  A  │  3  │  3  │ 0.3  │ 0.3  │
├────┼─────┼─────┼─────┼──────┼──────┤
│ 1  │  B  │  6  │  9  │ 0.6  │ 0.9  │
├────┼─────┼─────┼─────┼──────┼──────┤
│ 2  │  C  │  1  │ 10  │ 0.1  │  1   │
╘════╧═════╧═════╧═════╧══════╧══════╛
```

## freqtable

También es posible crear una tabla de frecuencias con intervalos utilizando ```freqtable.py```.
Para esto, hacemos lo siguiente:

```python
import freqtable as ft

# Se crean 8 intervalos desde 0 con ancho de 4:
intervalos = ft.crear_intervalos(8, 0, 4)
frecuencias = [47, 32, 25, 20, 12, 5, 4, 5]
# Se inicializa la tabla con los intervalos y frecuencias:
tabla_con_intervalos = ft.FreqTable(intervalos, frecuencias)
```

Dando como resultado:

```python
>>> print(tabla_con_intervalos)
╒════╤══════════════╤═════╤═════╤═════╤═══════════╤══════════╕
│    │  Intervalos  │  m  │  f  │  F  │    fr     │    Fr    │
╞════╪══════════════╪═════╪═════╪═════╪═══════════╪══════════╡
│ 0  │   [0-4.0]    │  2  │ 47  │ 47  │ 0.313333  │ 0.313333 │
├────┼──────────────┼─────┼─────┼─────┼───────────┼──────────┤
│ 1  │   ]4-8.0]    │  6  │ 32  │ 79  │ 0.213333  │ 0.526667 │
├────┼──────────────┼─────┼─────┼─────┼───────────┼──────────┤
│ 2  │   ]8-12.0]   │ 10  │ 25  │ 104 │ 0.166667  │ 0.693333 │
├────┼──────────────┼─────┼─────┼─────┼───────────┼──────────┤
│ 3  │  ]12-16.0]   │ 14  │ 20  │ 124 │ 0.133333  │ 0.826667 │
├────┼──────────────┼─────┼─────┼─────┼───────────┼──────────┤
│ 4  │  ]16-20.0]   │ 18  │ 12  │ 136 │   0.08    │ 0.906667 │
├────┼──────────────┼─────┼─────┼─────┼───────────┼──────────┤
│ 5  │  ]20-24.0]   │ 22  │  5  │ 141 │ 0.0333333 │   0.94   │
├────┼──────────────┼─────┼─────┼─────┼───────────┼──────────┤
│ 6  │  ]24-28.0]   │ 26  │  4  │ 145 │ 0.0266667 │ 0.966667 │
├────┼──────────────┼─────┼─────┼─────┼───────────┼──────────┤
│ 7  │  ]28-32.0]   │ 30  │  5  │ 150 │ 0.0333333 │    1     │
╘════╧══════════════╧═════╧═════╧═════╧═══════════╧══════════╛
```

## Instalación

Se puede clonar este repositorio:

```bash
git clone https://github.com/xeland314/freqtables
```

Y luego instalar las demás dependencias:

```bash
pip3 install -r requirements.txt
```

<details>
<summary>requirements.txt</summary>

- tabulate==0.8.10

</details>
