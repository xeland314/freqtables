from tabulate import tabulate
from math import sqrt, pow
from intervalos import *

class FreqTable(object):

    # Headers
    INTERVALOS = "Intervalos"
    PUNTOS_MEDIOS = "m"
    FRECUENCIAS = "f"
    FRECUENCIAS_RELATIVAS = "fr"
    FRECUENCIAS_ACUMULADAS = "F"
    FRECUENCIAS_RELATIVAS_ACUMULADAS = "Fr"

    def __init__(self, rangos: list, frecuencias: list) -> None:
        self.__tabla = {}   # Template
        self.__tabla[self.INTERVALOS] = rangos
        self.__calcular_puntos_medios()
        self.__tabla[self.FRECUENCIAS] = frecuencias
        self.__completar_tabla()
        self.__calcular_medidas_estadísticas()
    
    def __completar_tabla(self) -> None:
        self.__total_frecuencias = sum(self.frecuencias)
        self.__calcular_frecuencias_acumuladas()
        self.__calcular_frecuencias_relativas()
        self.__calcular_frecuencias_relativas_acumuladas()

    def __calcular_puntos_medios(self) -> None:
        puntos_medios = []
        for intervalo in self.intervalos:
            puntos_medios.append(intervalo.punto_medio)
        self.__tabla[self.PUNTOS_MEDIOS] = puntos_medios

    def __calcular_frecuencias_acumuladas(self) -> None:
        frecuencias_acumuladas = []
        sumatoria = 0
        for frecuencia in self.frecuencias:
            sumatoria += frecuencia
            frecuencias_acumuladas.append(sumatoria)
        self.__tabla[self.FRECUENCIAS_ACUMULADAS] = frecuencias_acumuladas

    def __calcular_frecuencias_relativas(self) -> None:
        frecuencias_relativas = list(map(
            lambda f: f / self.__total_frecuencias,
            self.frecuencias
        ))
        self.__tabla[self.FRECUENCIAS_RELATIVAS] = frecuencias_relativas

    def __calcular_frecuencias_relativas_acumuladas(self) -> None:
        frecuencias_acumuladas = []
        sumatoria = 0
        for frecuencia in self.frecuencias_relativas:
            sumatoria += frecuencia
            frecuencias_acumuladas.append(sumatoria)
        self.__tabla[self.FRECUENCIAS_RELATIVAS_ACUMULADAS] = frecuencias_acumuladas

    def __calcular_medidas_estadísticas(self) -> None:
        self.__calcular_media()
        self.__calcular_varianza()

    def __calcular_media(self) -> None:
        sumatoria = 0
        for fr, pm in zip(self.frecuencias_relativas, self.puntos_medios):
            sumatoria += fr * pm
        self.__media = sumatoria

    def __calcular_varianza(self) -> None:
        sumatoria = 0
        for frecuencia, punto_medio in zip(self.frecuencias, self.puntos_medios):
            sumatoria += frecuencia * pow(punto_medio - self.media, 2)
        self.__varianza = sumatoria / (self.__total_frecuencias - 1)
        self.__desviacion_estandar = sqrt(self.var)

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
        return self.__media
    
    @property
    def var(self) -> float:
        return self.__varianza

    @property
    def std(self) -> float:
        return self.__desviacion_estandar
    
    @staticmethod
    def crear_intervalos(lim_inf, n, ancho):
        rangos = []
        rango = IntervaloCerrado(lim_inf, lim_inf + float(ancho))
        rangos.append(rango)
        lim_inf += ancho
        for _ in range(n - 1):
            rango = IntervaloSemiAbierto(lim_inf, lim_inf + float(ancho))
            rangos.append(rango)
            lim_inf += ancho
        return rangos

    def __str__(self) -> str:
        return tabulate(
            self.__tabla,
            headers = "keys",
            tablefmt = "fancy_grid",
            showindex = True,
            stralign = "center",
            numalign = "center"
        )

def main():
    #rangos = crear_rangos(0,32,4)
    #frecuencias = [47,32,25,20,12,5,4,5]
    rangos = FreqTable.crear_intervalos(26.5,7,9)
    frecuencias = [18, 8, 15, 14, 25, 21, 19]
    tabla = FreqTable(rangos,frecuencias)
    print(tabla)
    tabla.print_resumen()

if __name__ == "__main__":
    main() 