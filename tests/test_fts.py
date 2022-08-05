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

    def test01_datos_de_entrada_correctos(self):
        resultado1 = Counter({'A':3, 'B':6, 'C':1})
        self.assertEqual(self.tabla1.datos, resultado1)
        self.assertEqual(self.tabla2.datos, resultado1)
        self.assertEqual(self.tabla3.datos, resultado1)
        self.assertEqual(self.tabla4.datos, resultado1)

    def test02_tabla_vacia(self):
        with self.assertRaises(TablaVacía):
            self.tablaNoInicializada = FreqTableSimple([])

    def test03_assert_columna_de_variables(self):
        x = ['A', 'B', 'C']
        self.assertEqual(self.tabla1.variables, x)

    def test04_assert_columna_de_frecuencias(self):
        f = [3, 6, 1]
        self.assertEqual(self.tabla1.frecuencias, f)

    def test05_assert_columna_de_f_relativas(self):
        fr = [0.3, 0.6, 0.1]
        self.assertEqual(self.tabla1.frecuencias_relativas, fr)

    def test06_assert_columna_de_f_acumuludas(self):
        F = [3, 9, 10]
        self.assertEqual(self.tabla1.frecuencias_acumuladas, F)

    def test07_assert_columna_de_f_r_acumuladas(self):
        Fr = [0.3, 0.9, 1.0]
        self.assertEqual(self.tabla1.frecuencias_relativas_acumuladas, Fr)

if __name__ == "__main__":
    unittest.main()
