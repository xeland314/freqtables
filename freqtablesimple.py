from tabulate import tabulate
from collections import Counter

class TablaVacía(Exception):

    def __init__(self) -> None:
        super().__init__("Entrada de datos vacía.")

class FreqTableSimple(object):

    """
    FreqTableSimple: Tabla de frecuencias simple

    Args:
        x: Variables.
        f: Frecuencias de cada cada variable.
    Results:
        F: Frecuencias acumuladas.
        fr: Frecuencias relativas de cada variable.
        Fr: Frecuancias relativas acumuladas.
    Example:
    ╒════╤═════╤═════╤═════╤══════╤══════╕
    │    │  x  │  f  │  F  │  fr  │  Fr  │
    ╞════╪═════╪═════╪═════╪══════╪══════╡
    │ 0  │  A  │  3  │  3  │ 0.3  │ 0.3  │
    ├────┼─────┼─────┼─────┼──────┼──────┤
    │ 1  │  B  │  6  │  9  │ 0.6  │ 0.9  │
    ├────┼─────┼─────┼─────┼──────┼──────┤
    │ 2  │  C  │  1  │ 10  │ 0.1  │  1   │
    ╘════╧═════╧═════╧═════╧══════╧══════╛
    """
    __tabla = {  # Template de la tabla
        "x": [],
        "f": [], "F": [],
        "fr": [], "Fr": []
    }
    __total_frecuencias = 0
    __cantidad_de_variables = 0

    def __init__(self, datos) -> None:
        # Verificar que haya datos en la entrada:
        if len(datos) == 0:
            raise TablaVacía()
        # Verificar el tipo de dato de entrda:
        if isinstance(datos, (list, tuple)):
            self.__inicializar_tabla_de_list(datos)
        elif isinstance(datos, dict):
            self.__inicializar_tabla_de_dict(datos)
        else:
            raise NotImplementedError()

    def __inicializar_tabla_de_list(self, datos) -> None:
        """
        Esta función transforma una lista o tupla
        en un Counter() iterando cada uno de sus elementos.
        """
        self.__datos = Counter()
        for x in datos:
            self.__datos[x] += 1
        self.__completar_tabla()

    def __inicializar_tabla_de_dict(self, datos: dict) -> None:
        """
        Inicializa el Counter() con un diccionario.
        """
        self.__datos = Counter(datos)
        self.__completar_tabla()

    def __completar_tabla(self) -> None:
        """
        Se completan las todas las columnas de la tabla
        en self.__tabla.
        """
        # Columna de variables:
        self.__tabla["x"] = list(self.datos.keys())
        # Columna de frecuencias:
        self.__tabla["f"] = list(self.datos.values())
        # Número de datos:
        self.__cantidad_de_variables = len(self.__tabla["x"])
        self.__total_frecuencias = sum(self.__tabla["f"])
        # Columna de frecuencias relativas:
        self.__tabla["fr"] = list(map(
            lambda x: x / self.__total_frecuencias, self.__tabla["f"]
        ))
        # Columna de frecuencias acumuladas:
        suma_f = 0.0
        columna_F = []
        for frecuencia in self.__tabla["f"]:
            suma_f += frecuencia
            columna_F.append(suma_f)
        self.__tabla["F"] = columna_F
        # Columna de frecuencias acumuladas relativas:
        columna_Fr = []
        columna_Fr = list(map(
            lambda x: x / self.__total_frecuencias, self.__tabla["F"] 
        ))
        self.__tabla["Fr"] = columna_Fr

    @property
    def datos(self) -> dict:
        return self.__datos

    @property
    def variables(self) -> list:
        return self.__tabla["x"]

    @property
    def frecuencias(self) -> list:
        return self.__tabla["f"]

    @property
    def frecuencias_relativas(self) -> list:
        return self.__tabla["fr"]

    @property
    def frecuencias_acumuladas(self) -> list:
        return self.__tabla["F"]

    @property
    def frecuencias_relativas_acumuladas(self) -> list:
        return self.__tabla["Fr"]

    @property
    def cantidad_de_variables(self) -> int:
        return self.__cantidad_de_variables

    @property
    def total_frecuencias(self) -> float:
        return self.__total_frecuencias

    @staticmethod
    def print_example() -> None:
        tabla1 = FreqTableSimple([
            'A', 'A', 'A', 'B', 'B',
            'B', 'B', 'B', 'B', 'C',

        ])
        print(tabla1)

    def __str__(self) -> str:
        return tabulate(
            self.__tabla,
            headers = "keys",
            tablefmt="fancy_grid",
            showindex=True,
            stralign="center",
            numalign="center"
        )

if __name__ == "__main__":
    help(FreqTableSimple)
    FreqTableSimple.print_example()
