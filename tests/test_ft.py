import unittest
from context import *

class TestTablasDeFrecuencias(unittest.TestCase):
    
    def setUp(self):
        intervalos1 = crear_lista_intervalos(8, 0, 4)
        frecuencias1 = [47, 32, 25, 20, 12, 5, 4, 5]
        intervalos2 = crear_lista_intervalos(7, 26.5, 9)
        frecuencias2 = [18, 8, 15, 14, 25, 21, 19]
        self.tabla1 = FreqTable(intervalos1, frecuencias1)
        self.tabla2 = FreqTable(intervalos2, frecuencias2)

    def test01_assert_puntos_medios(self):
        puntos_medios1 = [2, 6, 10, 14, 18, 22, 26, 30]
        puntos_medios2 = [31, 40, 49, 58, 67, 76, 85]
        self.assertListEqual(self.tabla1.puntos_medios, puntos_medios1)
        self.assertListEqual(self.tabla2.puntos_medios, puntos_medios2)

    def test02_assert_frecuencias_acumuladas(self):
        frecuencias_acumuladas1 = [47, 79, 104, 124, 136, 141, 145, 150]
        frecuencias_acumuladas2 = [18, 26, 41, 55, 80, 101, 120]
        self.assertListEqual(self.tabla1.frecuencias_acumuladas, frecuencias_acumuladas1)
        self.assertListEqual(self.tabla2.frecuencias_acumuladas, frecuencias_acumuladas2)

    def test03_assert_frecuencias_relativas(self):
        frecuencias_relativas1 = [
            47/150, 16/75, 1/6, 2/15, 2/25, 1/30, 2/75, 1/30
        ]
        frecuencias_relativas2 = [
            3/20, 1/15, 1/8, 7/60, 5/24, 7/40, 19/120
        ]
        self.assertListEqual(
            self.tabla1.frecuencias_relativas, frecuencias_relativas1
        )
        self.assertListEqual(
            self.tabla2.frecuencias_relativas, frecuencias_relativas2
        )

    def test04_assert_f_relativas_acumuladas(self):
        frecuencias_acumuladas1 = [
            47/150, 79/150, 52/75, 62/75, 68/75, 141/150, 29/30, 1.0
        ]
        frecuencias_acumuladas2 = [
            3/20, 13/60, 41/120, 11/24, 2/3, 101/120, 1.0
        ]
        for fra1, fra2 in zip(frecuencias_acumuladas1, self.tabla1.frecuencias_relativas_acumuladas):
            self.assertAlmostEqual(fra1, fra2)
        for fra1, fra2 in zip(frecuencias_acumuladas2, self.tabla2.frecuencias_relativas_acumuladas):
            self.assertAlmostEqual(fra1, fra2)

    def test05_assert_medias_varianzas(self):
        media1, media2 = 9.306666666666666, 60.925
        var1, var2 = 55.569753914988816, 324.22121848739494
        self.assertAlmostEqual(self.tabla1.media, media1)
        self.assertAlmostEqual(self.tabla2.media, media2)
        self.assertAlmostEqual(self.tabla1.var, var1)
        self.assertAlmostEqual(self.tabla2.var, var2)

if __name__ == "__main__":
    unittest.main()