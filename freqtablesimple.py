from tabulate import tabulate
from collections import Counter
from math import pow, sqrt

class TablaVacía(Exception):

    def __init__(self) -> None:
        super().__init__("Entrada de datos vacía.")

class FreqTableSimple(object):

    """
    FreqTableSimple: Tabla de frecuencias simple

    Args:
        x: Variables.
        f: Frecuencias de cada cada variable.
    Resultados:
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
    __total_frecuencias: float = 0
    __cantidad_de_variables: int = 0
    # Headers:
    VARIABLES = "x"
    FRECUENCIAS = "f"
    FRECUENCIAS_RELATIVAS = "fr"
    FRECUENCIAS_ACUMULADAS = "F"
    FRECUENCIAS_RELATIVAS_ACUMULADAS = "Fr"

    def __init__(self, *datos, **kdatos) -> None:
        self.__datos_brutos = Counter()
        self.__tabla: dict = {}
        for variable in datos:
            if isinstance(variable, (list, tuple)):
                for x in variable:
                    self.__datos_brutos[x] += 1
            elif isinstance(variable, dict):
                self.__datos_brutos.update(variable)
            elif isinstance(variable, (int, float, str, object)):
                self.__datos_brutos[variable] += 1
            else:
                raise NotImplementedError()
        for variable, valor in kdatos.items():
            if isinstance(valor, int):
                self.__datos_brutos[variable] += valor
            elif isinstance(valor, float):
                self.__datos_brutos[variable] += int(valor)
            else:
                raise NotImplementedError()
        if len(self.__datos_brutos) == 0:
            raise TablaVacía()
        self.__completar_tabla()

    def __completar_tabla(self) -> None:
        """
        Se completan las todas las columnas de la tabla
        en self.__tabla.
        """
        # Columna de variables:
        self.__tabla[self.VARIABLES] = list(self.datos.keys())
        # Columna de frecuencias:
        self.__tabla[self.FRECUENCIAS] = list(self.datos.values())
        # Columna de frecuencias acumuladas:
        suma_f = 0.0
        frecuencias_acumuladas = []
        for frecuencia in self.frecuencias:
            suma_f += frecuencia
            frecuencias_acumuladas.append(suma_f)
        self.__tabla[self.FRECUENCIAS_ACUMULADAS] = frecuencias_acumuladas
        # Número de datos:
        self.__cantidad_de_variables = len(self.variables)
        self.__total_frecuencias = sum(self.frecuencias)
        # Columna de frecuencias relativas:
        self.__tabla[self.FRECUENCIAS_RELATIVAS] = list(map(
            lambda x: x / self.total_frecuencias, self.frecuencias
        ))
        # Columna de frecuencias acumuladas relativas:
        frecuencias_acumuladas = list(map(
            lambda x: x / self.total_frecuencias,
            self.frecuencias_acumuladas 
        ))
        self.__tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS] = frecuencias_acumuladas

    @property
    def datos(self) -> Counter:
        return self.__datos_brutos

    @property
    def variables(self) -> list:
        return self.__tabla[self.VARIABLES]

    @property
    def frecuencias(self) -> list:
        return self.__tabla[self.FRECUENCIAS]

    @property
    def frecuencias_relativas(self) -> list:
        return self.__tabla[self.FRECUENCIAS_RELATIVAS]

    @property
    def frecuencias_acumuladas(self) -> list:
        return self.__tabla[self.FRECUENCIAS_ACUMULADAS]

    @property
    def frecuencias_relativas_acumuladas(self) -> list:
        return self.__tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS]

    @property
    def cantidad_de_variables(self) -> int:
        return self.__cantidad_de_variables

    @property
    def total_frecuencias(self) -> float:
        return self.__total_frecuencias

    @property
    def media(self) -> float:
        if any(filter(lambda v: not isinstance(v, int, float), self.variables)):
            return self.total_frecuencias / self.cantidad_de_variables
        sumatoria: float = 0
        for frecuencia, variable in zip(self.frecuencias, self.variables):
            sumatoria += frecuencia * variable
        return sumatoria / self.total_frecuencias

    @property
    def var(self) -> float:
        sumatoria: float = 0
        if any(filter(lambda v: not isinstance(v, int, float), self.variables)):
            for frecuencia in self.frecuencias:
                sumatoria += pow(frecuencia - self.media, 2)
            return sumatoria / (self.cantidad_de_variables - 1)
        for frecuencia, variable in zip(self.frecuencias, self.variables):
            sumatoria += frecuencia * pow(variable - self.media, 2)
        return sumatoria / (self.total_frecuencias - 1)

    @property
    def std(self) -> float:
        return sqrt(self.var)

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
            tablefmt = "fancy_grid",
            showindex = True,
            stralign = "center",
            numalign = "center"
        )

if __name__ == "__main__":
    help(FreqTableSimple)
    FreqTableSimple.print_example()
