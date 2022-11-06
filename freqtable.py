from abc import ABC, ABCMeta, abstractmethod
from tabulate import tabulate
from math import sqrt, pow
from collections import Counter

from intervalos import *
from columnas import *

class MedidasEstadisticas(ABC):

    def media(self):
        raise NotImplementedError()

    def mediana(self):
        raise NotImplementedError()

    def moda(self):
        raise NotImplementedError()

    def var(self):
        raise NotImplementedError()

    def std(self) -> float:
        return sqrt(self.var())

class TablaBase(metaclass = ABCMeta):
    
    FRECUENCIAS = "f"
    FRECUENCIAS_RELATIVAS = "fr"
    FRECUENCIAS_ACUMULADAS = "F"
    FRECUENCIAS_RELATIVAS_ACUMULADAS = "Fr"

    def __init__(self) -> None:
        self._tabla = {}    # Template tabla: {columna.nombre: columna}

    @abstractmethod
    def _completar_tabla(self) -> None:
        pass

    @property
    def frecuencias(self) -> Frecuencias:
        return self._tabla[self.FRECUENCIAS]

    @property
    def frecuencias_relativas(self) -> FrecuenciasRelativas:
        return self._tabla[self.FRECUENCIAS_RELATIVAS]

    @property
    def frecuencias_acumuladas(self) -> FrecuenciasAcumuladas:
        return self._tabla[self.FRECUENCIAS_ACUMULADAS]

    @property
    def frecuencias_relativas_acumuladas(self) -> FrecuenciasRelativasAcumuladas:
        return self._tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS]

    @property
    def total_frecuencias(self) -> float:
        return sum(self.frecuencias)

    def __str__(self) -> str:
        return tabulate(
            self._tabla,
            headers = "keys",
            tablefmt = "fancy_grid",
            showindex = True,
            stralign = "center",
            numalign = "center"
        )

class TablaVacía(Exception):

    def __init__(self) -> None:
        super().__init__("Entrada de datos vacía.")

class FreqTableSimple(TablaBase, MedidasEstadisticas):

    """
    FreqTableSimple: Tabla de frecuencias simple

    Args:
        x: Variables.
    Results:
        f: Frecuencias de cada cada variable.
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
    VARIABLES = "x"

    def __init__(self, *datos, **kwargs) -> None:
        super().__init__()
        self._datos_brutos = Counter()
        # Normalizar y procesar datos brutos:
        for variable in datos:
            if isinstance(variable, (list, tuple)):
                for x in variable:
                    self._datos_brutos[x] += 1
            elif isinstance(variable, dict):
                self._datos_brutos.update(variable)
            elif isinstance(variable, (int, float, str, object)):
                self._datos_brutos[variable] += 1
            else:
                raise NotImplementedError()
        for variable, valor in kwargs.items():
            if isinstance(valor, int):
                self._datos_brutos[variable] += valor
            elif isinstance(valor, float):
                self._datos_brutos[variable] += int(valor)
            else:
                raise NotImplementedError()
        if len(self._datos_brutos) == 0:
            raise TablaVacía()
        self._completar_tabla()

    def _completar_tabla(self) -> None:
        """ Se completan las todas las columnas
        de la tabla en self._tabla."""
        self._tabla[self.VARIABLES] = \
            Variables(list(self._datos_brutos.keys()), self.VARIABLES)
        self._tabla[self.FRECUENCIAS] = \
            Frecuencias(list(self._datos_brutos.values()), self.FRECUENCIAS)
        self._tabla[self.FRECUENCIAS_ACUMULADAS] = \
            FrecuenciasAcumuladas(self.frecuencias, self.FRECUENCIAS_ACUMULADAS)
        self._tabla[self.FRECUENCIAS_RELATIVAS] = \
            FrecuenciasRelativas(self.frecuencias, self.FRECUENCIAS_RELATIVAS)
        self._tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS] = \
            FrecuenciasRelativasAcumuladas(self.frecuencias_relativas, self.FRECUENCIAS_RELATIVAS_ACUMULADAS)

    @property
    def datos(self) -> Counter:
        return self._datos_brutos

    @property
    def variables(self) -> Variables:
        return self._tabla[self.VARIABLES]

    @property
    def cantidad_de_variables(self) -> int:
        return len(self.variables)

    def media(self) -> float:
        if any(filter(lambda v: not isinstance(v, int, float), self.variables)):
            return self.total_frecuencias / self.cantidad_de_variables
        sumatoria: float = 0
        for frecuencia, variable in zip(self.frecuencias, self.variables):
            sumatoria += frecuencia * variable
        return sumatoria / self.total_frecuencias

    def var(self) -> float:
        sumatoria: float = 0
        if any(filter(lambda v: not isinstance(v, int, float), self.variables)):
            for frecuencia in self.frecuencias:
                sumatoria += pow(frecuencia - self.media, 2)
            return sumatoria / (self.cantidad_de_variables - 1)
        for frecuencia, variable in zip(self.frecuencias, self.variables):
            sumatoria += frecuencia * pow(variable - self.media, 2)
        return sumatoria / (self.total_frecuencias - 1)

    @staticmethod
    def print_example() -> None:
        tabla1 = FreqTableSimple([
            'A', 'A', 'A', 'B', 'B',
            'B', 'B', 'B', 'B', 'C',
        ])
        print(tabla1)

def crear_intervalos(n: int, lim_inf: float, ancho: float) -> list:
    """
    Parámetros:
        - n: Número de intervalos a crear.
        - lim_inf: límite inferior del primer intervalo.
        - ancho: ancho de cada clase; 
            ancho = limite_superior - limite_inferior
    """
    intervalos = []
    intervalos.append(IntervaloCerrado(lim_inf, lim_inf := lim_inf + ancho))
    for _ in range(n - 1):
        intervalos.append(IntervaloSemiAbierto(lim_inf, lim_inf := lim_inf + ancho))
    return intervalos

class FreqTable(TablaBase, MedidasEstadisticas):
    """
    Tabla de frecuencias con intervalos

    Parámetros:
        - intervalos: list
        - frecuencias: list
    """
    INTERVALOS = "intervalos"
    PUNTOS_MEDIOS = "m"

    def __init__(self, intervalos: list, frecuencias: list) -> None:
        super().__init__()
        self._completar_tabla(intervalos, frecuencias)

    def _completar_tabla(self, intervalos: list, frecuencias: list) -> None:
        self._tabla[self.INTERVALOS] = Intervalos(intervalos)
        self._tabla[self.PUNTOS_MEDIOS] = \
            PuntosMedios(self.intervalos, self.PUNTOS_MEDIOS)
        self._tabla[self.FRECUENCIAS] = \
            Frecuencias(frecuencias, self.FRECUENCIAS)
        self._tabla[self.FRECUENCIAS_ACUMULADAS] = \
            FrecuenciasAcumuladas(self.frecuencias, self.FRECUENCIAS_ACUMULADAS)
        self._tabla[self.FRECUENCIAS_RELATIVAS] = \
            FrecuenciasRelativas(self.frecuencias, self.FRECUENCIAS_RELATIVAS)
        self._tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS] = \
            FrecuenciasRelativasAcumuladas(self.frecuencias_relativas, self.FRECUENCIAS_RELATIVAS_ACUMULADAS)

    @property
    def intervalos(self) -> Intervalos:
        return self._tabla[self.INTERVALOS]
    
    @property
    def puntos_medios(self) -> PuntosMedios:
        return self._tabla[self.PUNTOS_MEDIOS]

    def media(self) -> float:
        sumatoria = 0
        for fr, pm in zip(self.frecuencias_relativas, self.puntos_medios):
            sumatoria += fr * pm
        return sumatoria

    def var(self) -> float:
        sumatoria, media = 0, self.media()
        for frecuencia, punto_medio in zip(self.frecuencias, self.puntos_medios):
            sumatoria += frecuencia * pow(punto_medio - media, 2)
        return sumatoria / (self.total_frecuencias - 1)

    def print_resumen(self) -> None:
        info = [
            "Rango:", "Media:", 
            "Varianza:", "Desviación estándar:"]
        rango = IntervaloAbierto(
            self.intervalos[0].lim_inf,
            self.intervalos[-1].lim_sup
        )
        datos = [rango, self.media(), self.var(), self.std()]
        resumen = {"Información": info, "Resultados": datos}
        print(tabulate(resumen, headers = "keys",
            tablefmt="fancy_grid", showindex=True, stralign="right"
        ))

if __name__ == "__main__":
    help(FreqTableSimple)
    FreqTableSimple.print_example()
