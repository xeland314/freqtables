from tabulate import tabulate
from math import sqrt, pow
from intervalos import *

def crear_lista_intervalos(n: int, lim_inf: float, ancho: float) -> list:
    """
    Parámetros:
        - n: Número de intervalos a crear.
        - lim_inf: límite inferior del primer intervalo.
        - ancho: ancho de cada clase; 
            ancho = limite_inferior - limite_superior
    """
    intervalos = []
    intervalos.append(IntervaloCerrado(lim_inf, lim_inf := lim_inf + ancho))
    for _ in range(n - 1):
        intervalos.append(IntervaloSemiAbierto(lim_inf, lim_inf := lim_inf + ancho))
    return intervalos

class FreqTable(object):
    """
    Tabla de frecuencias con intervalos

    Parámetros:
        - intervalos: list
        - frecuencias: list
    """
    # Headers
    INTERVALOS = "Intervalos"
    PUNTOS_MEDIOS = "m"
    FRECUENCIAS = "f"
    FRECUENCIAS_RELATIVAS = "fr"
    FRECUENCIAS_ACUMULADAS = "F"
    FRECUENCIAS_RELATIVAS_ACUMULADAS = "Fr"

    def __init__(self, intervalos: list, frecuencias: list) -> None:
        self.__tabla = {}   # { columna: lista_de_valores }
        self.__tabla[self.INTERVALOS] = intervalos
        self.__calcular_puntos_medios()
        self.__tabla[self.FRECUENCIAS] = frecuencias
        self.__total_frecuencias = sum(self.frecuencias)
        self.__calcular_frecuencias_acumuladas()
        self.__calcular_frecuencias_relativas()
        self.__calcular_frecuencias_relativas_acumuladas()

    def __calcular_puntos_medios(self) -> None:
        self.__tabla[self.PUNTOS_MEDIOS]  = list(map(
            lambda intervalo: intervalo.punto_medio, self.intervalos
        ))

    def __calcular_frecuencias_acumuladas(self) -> None:
        frecuencias_acumuladas = []
        sumatoria = 0
        for frecuencia in self.frecuencias:
            sumatoria += frecuencia
            frecuencias_acumuladas.append(sumatoria)
        self.__tabla[self.FRECUENCIAS_ACUMULADAS] = frecuencias_acumuladas

    def __calcular_frecuencias_relativas(self) -> None:
        frecuencias_relativas = list(map(
            lambda f: f / self.__total_frecuencias, self.frecuencias
        ))
        self.__tabla[self.FRECUENCIAS_RELATIVAS] = frecuencias_relativas

    def __calcular_frecuencias_relativas_acumuladas(self) -> None:
        frecuencias_acumuladas = []
        sumatoria = 0
        for frecuencia in self.frecuencias_relativas:
            sumatoria += frecuencia
            frecuencias_acumuladas.append(sumatoria)
        self.__tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS] = frecuencias_acumuladas

    def print_resumen(self) -> None:
        info = [
            "Rango:", "Media:", 
            "Varianza:", "Desviación estándar:"]
        rango = IntervaloAbierto(
            self.intervalos[0].lim_inf,
            self.intervalos[-1].lim_sup
        )
        datos = [rango, self.media, self.var, self.std]
        resumen = {"Información": info, "Resultados": datos}
        print(tabulate(resumen, headers = "keys",
            tablefmt="fancy_grid", showindex=True, stralign="right"
        ))

    @property
    def intervalos(self) -> list:
        return self.__tabla[self.INTERVALOS]

    @property
    def puntos_medios(self) -> list:
        return self.__tabla[self.PUNTOS_MEDIOS]
    
    @property 
    def frecuencias(self) -> list:
        return self.__tabla[self.FRECUENCIAS]

    @property
    def frecuencias_acumuladas(self) -> list:
        return self.__tabla[self.FRECUENCIAS_ACUMULADAS]

    @property 
    def frecuencias_relativas(self) -> list:
        return self.__tabla[self.FRECUENCIAS_RELATIVAS]

    @property
    def frecuencias_relativas_acumuladas(self) -> list:
        return self.__tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS]

    @property
    def total_frecuencias(self) -> float:
        return self.__total_frecuencias

    @property
    def media(self) -> float:
        sumatoria = 0
        for fr, pm in zip(self.frecuencias_relativas, self.puntos_medios):
            sumatoria += fr * pm
        return sumatoria
    
    @property
    def var(self) -> float:
        sumatoria = 0
        for frecuencia, punto_medio in zip(self.frecuencias, self.puntos_medios):
            sumatoria += frecuencia * pow(punto_medio - self.media, 2)
        return sumatoria / (self.__total_frecuencias - 1)

    @property
    def std(self) -> float:
        return sqrt(self.var)

    def __str__(self) -> str:
        return tabulate(
            self.__tabla,
            headers = "keys",
            tablefmt = "fancy_grid",
            showindex = True,
            stralign = "center",
            numalign = "center"
        )
