import unittest
from context import *

class TestTablasDeFrecuencias(unittest.TestCase):
    
    def setUp(self):
        self.intervalos1 = crear_intervalos(8, 0, 4)
        self.frecuencias1 = [47, 32, 25, 20, 12, 5, 4, 5]
        self.intervalos2 = crear_intervalos(7, 26.5, 9)
        self.frecuencias2 = [18, 8, 15, 14, 25, 21, 19]
        self.tabla1 = FreqTable(self.intervalos1, self.frecuencias1)
        self.tabla2 = FreqTable(self.intervalos2, self.frecuencias2)

    def test01_assert_puntos_medios(self):
        for pm_calc, pm_test in zip(self.tabla1.puntos_medios, [2, 6, 10, 14, 18, 22, 26, 30]):
            self.assertAlmostEqual(pm_calc, pm_test)
        for pm_calc, pm_test in zip(self.tabla2.puntos_medios, [31, 40, 49, 58, 67, 76, 85]):
            self.assertAlmostEqual(pm_calc, pm_test)

    def test02_assert_frecuencias_acumuladas(self):
        for fa_calc, fa_test in zip(self.tabla1.frecuencias_acumuladas, [47, 79, 104, 124, 136, 141, 145, 150]):
            self.assertAlmostEqual(fa_calc, fa_test)
        for fa_calc, fa_test in zip(self.tabla2.frecuencias_acumuladas, [18, 26, 41, 55, 80, 101, 120]):
            self.assertAlmostEqual(fa_calc, fa_test)

    def test03_assert_frecuencias_relativas(self):
        for fr_calc, fr_test in zip(self.tabla1.frecuencias_relativas, [47/150, 16/75, 1/6, 2/15, 2/25, 1/30, 2/75, 1/30]):
            self.assertAlmostEqual(fr_calc, fr_test)
        for fr_calc, fr_test in zip(self.tabla2.frecuencias_relativas, [3/20, 1/15, 1/8, 7/60, 5/24, 7/40, 19/120]):
            self.assertAlmostEqual(fr_calc, fr_test)

    def test04_assert_f_relativas_acumuladas(self):
        for fra_calc, fra_test in zip(self.tabla1.frecuencias_relativas_acumuladas, [47/150, 79/150, 52/75, 62/75, 68/75, 141/150, 29/30, 1.0]):
            self.assertAlmostEqual(fra_calc, fra_test)
        for fra_calc, fra_test in zip(self.tabla2.frecuencias_relativas_acumuladas, [3/20, 13/60, 41/120, 11/24, 2/3, 101/120, 1.0]):
            self.assertAlmostEqual(fra_calc, fra_test)

    def test05_assert_medias_varianzas(self):
        media1, media2 = 9.306666666666666, 60.925
        var1, var2 = 55.569753914988816, 324.22121848739494
        self.assertAlmostEqual(self.tabla1.media(), media1)
        self.assertAlmostEqual(self.tabla2.media(), media2)
        self.assertAlmostEqual(self.tabla1.var(), var1)
        self.assertAlmostEqual(self.tabla2.var(), var2)

if __name__ == "__main__":
    unittest.main()