from abc import ABC, abstractmethod
from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class MedidasDeTendenciaCentral(object):

    moda: float = 0.0
    mediana: float = 0.0
    media: float = 0.0

    def __str__(self) -> str:
        return ""

@dataclass
class MedidasDeDispersion(object):

    rango: float = 0.0
    rango_intercuartil: float = 0.0
    varianza: float = 0.0
    desviacion_estandar: float = 0.0
    asimetria: float = 0.0
    curtosis: float = 0.0
    coeficiente_de_variacion: float = 0.0
    coeficiente_de_apuntalamiento: float = 0.0

    def __str__(self) -> str:
        return ""

class MedidasDePosicion(object):
    pass
