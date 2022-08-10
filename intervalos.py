from abc import ABCMeta, abstractmethod

class Rango(metaclass=ABCMeta):

    """
    Representa un rango de valores
    como base para crear intervalos.
    """

    def __init__(self, lim_inf, lim_sup):
        self.__lim_inf: float = lim_inf
        self.__lim_sup: float = lim_sup

    @property
    def lim_inf(self) -> float:
        return self.__lim_inf

    @property
    def lim_sup(self) -> float:
        return self.__lim_sup

    @property
    def punto_medio(self) -> float:
        return (self.lim_inf + self.lim_sup) / 2

    @property
    def ancho(self) -> float:
        return self.lim_sup - self.lim_inf

    @abstractmethod
    def está_dentro_del_intervalo_el_número(self):
        ...

class IntervaloAbierto(Rango):

    def __init__(self, lim_inf, lim_sup):
        super().__init__(lim_inf, lim_sup)

    def está_dentro_del_intervalo_el_número(self, numero) -> bool:
        return (numero > self.lim_inf) and (numero < self.lim_sup)

    def __str__(self) -> str:
        return f"({self.lim_inf}-{self.lim_sup})"

    def __eq__(self, other) -> bool:
        if type(other) is IntervaloAbierto:
            return self.lim_inf == other.lim_inf and self.lim_sup == other.lim_sup
        return False

    def __repr__(self) -> str:
        return f"IntervaloAbierto({self.lim_inf}, {self.lim_sup})"

class IntervaloCerrado(Rango):

    def __init__(self, lim_inf, lim_sup):
        super().__init__(lim_inf, lim_sup)

    def está_dentro_del_intervalo_el_número(self, numero) -> bool:
        return (numero >= self.lim_inf) and (numero <= self.lim_sup)

    def __str__(self) -> str:
        return f"[{self.lim_inf}-{self.lim_sup}]"

    def __repr__(self) -> str:
        return f"IntervaloCerrado({self.lim_inf}, {self.lim_sup})"
    
    def __eq__(self, other) -> bool:
        if type(other) is IntervaloCerrado:
            return self.lim_inf == other.lim_inf and self.lim_sup == other.lim_sup
        return False

class IntervaloSemiAbierto(Rango):

    def __init__(self, lim_inf, lim_sup):
        super().__init__(lim_inf, lim_sup)

    def está_dentro_del_intervalo_el_número(self, numero) -> bool:
        return (numero > self.lim_inf) and (numero <= self.lim_sup)

    def __str__(self) -> str:
        return f"]{self.lim_inf}-{self.lim_sup}]"

    def __repr__(self) -> str:
        return f"IntervaloSemiAbierto({self.lim_inf}, {self.lim_sup})"

    def __eq__(self, other) -> bool:
        if type(other) is IntervaloSemiAbierto:
            return self.lim_inf == other.lim_inf and self.lim_sup == other.lim_sup
        return False
