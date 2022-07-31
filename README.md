# freqtables

Este paquete permite crear tables de frecuencias simples dado un conjunto de variables con sus respectivas frecuencias. Este conjunto de datos pueder una lista, tuple o un diccionario:

```python
import freqtablesimple as fts

tabla1 = fts.FreqTableSimple([
    'A', 'A', 'A', 'B', 'B',
    'B', 'B', 'B', 'B', 'C'
])
tabla2 = fts.FreqTableSimple({
    'A':3, 'B':6, 'C':1
})
```

Cualquiera de estas dos formas de inicializar ```FreqTableSimple``` da como resultado:

```python
print(tabla1)
>>
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
