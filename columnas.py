from abc import ABCMeta, abstractmethod
from tabulate import tabulate

class ColumnaIterable:

    def __init__(self, columna) -> None:
        self.__datos = columna.datos
        self._current_index = 0
        self._class_size = len(self.__datos)

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self._class_size:
            item = self.__datos[self._current_index]
            self._current_index += 1
            return item
        raise StopIteration

class Columna(metaclass=ABCMeta):

    def __init__(self, datos_iniciales: list, nombre: str) -> None:
        self.__nombre = nombre
        self.__datos = []
        self._completar(datos_iniciales)

    @abstractmethod
    def _completar(self, datos_iniciales: list) -> None:
        pass

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def datos(self) -> list:
        return self.__datos

    @datos.setter
    def datos(self, datos) -> None:
        self.__datos = datos

    def append(self, dato) -> None:
        self.__datos.append(dato)

    def __len__(self) -> int:
        return len(self.__datos)

    def __iter__(self):
        return ColumnaIterable(self)

    def __eq__(self, __columna) -> bool:
        if type(__columna) == type(self):
            return self.datos == __columna.datos
        return False

    def __str__(self) -> str:
        return tabulate(
            {self.nombre: self.datos},
            headers = "keys",
            tablefmt = "fancy_grid",
            showindex = False,
            stralign = "center",
            numalign = "center"
        )

class Variables(Columna):

    def __init__(self, datos_iniciales: list, nombre = "x") -> None:
        super().__init__(datos_iniciales, nombre)
    
    def _completar(self, datos_iniciales: list) -> None:
        self.datos = datos_iniciales.copy()

class Frecuencias(Variables):

    def __init__(self, datos_iniciales: list, nombre = "f") -> None:
        super().__init__(datos_iniciales, nombre)

class Intervalos(Variables):

    def __init__(self, datos_iniciales: list, nombre = "Intervalos") -> None:
        super().__init__(datos_iniciales, nombre)

class PuntosMedios(Columna):

    def __init__(self, intervalos: Intervalos, nombre = "m") -> None:
        super().__init__(intervalos, nombre)

    def _completar(self, intervalos) -> None:
        self.datos = list(map(lambda intervalo: intervalo.punto_medio, intervalos))

class FrecuenciasRelativas(Columna):

    def __init__(self, frecuencias: Frecuencias, nombre = "fr") -> None:
        super().__init__(frecuencias.datos, nombre)

    def _completar(self, frecuencias: list) -> None:
        total = sum(frecuencias)
        self.datos = list(map(lambda x: x / total, frecuencias))

class FrecuenciasAcumuladas(Columna):

    def __init__(self, frecuencias: Frecuencias, nombre = "F") -> None:
        super().__init__(frecuencias, nombre)

    def _completar(self, frecuencias) -> None:
        suma_temp = 0.0
        for frecuencia in frecuencias:
            suma_temp += frecuencia
            self.datos.append(suma_temp)

class FrecuenciasRelativasAcumuladas(FrecuenciasAcumuladas):

    def __init__(self, frecuencias: FrecuenciasRelativas, nombre = "Fr") -> None:
        super().__init__(frecuencias.datos, nombre)

if __name__ == "__main__":
    print(Variables([1, 2, 3, 4, 5]))
    for dato in Variables([1, 2, 3, 4, 5]):
        print(dato, end=' ')
    print(FrecuenciasAcumuladas(Frecuencias([1, 2, 3, 4, 5])))
    help(Frecuencias)