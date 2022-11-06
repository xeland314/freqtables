import unittest
from collections import Counter
from context import *

class TestTablasDeFrecuencias(unittest.TestCase):
    
    def setUp(self):
        self.tabla1 = FreqTableSimple([
            'A', 'A', 'A', 'B', 'B',
            'B', 'B', 'B', 'B', 'C'
        ])
        self.tabla2 = FreqTableSimple({
            'A':3, 'B':6, 'C':1
        })
        self.tabla3 = FreqTableSimple(
            'A', 'A', 'A', 'B', 'B',
            'B', 'B', 'B', 'B', 'C'
        )
        self.tabla4 = FreqTableSimple(
            A = 3, B = 6, C = 1.1
        )
        self.x = Variables(['A', 'B', 'C'])
        self.f = Frecuencias([3, 6, 1])
        self.fr = FrecuenciasRelativas(self.f)
        self.fa = FrecuenciasAcumuladas(self.f)
        self.Fr = FrecuenciasRelativasAcumuladas(self.fr)

    def test01_datos_de_entrada_correctos(self):
        resultado1 = Counter({'A':3, 'B':6, 'C':1})
        self.assertEqual(self.tabla1._datos_brutos, resultado1)
        self.assertEqual(self.tabla2._datos_brutos, resultado1)
        self.assertEqual(self.tabla3._datos_brutos, resultado1)
        self.assertEqual(self.tabla4._datos_brutos, resultado1)

    def test02_tabla_vacia(self):
        with self.assertRaises(TablaVacía):
            self.tablaNoInicializada = FreqTableSimple([])

    def test03_assert_columna_de_variables(self):
        self.assertEqual(self.tabla1.variables, self.x)

    def test04_assert_columna_de_frecuencias(self):
        self.assertEqual(self.tabla1.frecuencias, self.f)

    def test05_assert_columna_de_f_relativas(self):
        self.assertEqual(self.tabla1.frecuencias_relativas, self.fr)

    def test06_assert_columna_de_f_acumuludas(self):
        self.assertEqual(self.tabla1.frecuencias_acumuladas, self.fa)

    def test07_assert_columna_de_f_r_acumuladas(self):
        self.assertEqual(self.tabla1.frecuencias_relativas_acumuladas, self.Fr)

if __name__ == "__main__":
    unittest.main()
