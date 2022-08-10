import unittest
from context import *

class TestIntervalos(unittest.TestCase):

    def setUp(self):
        self.intervalo_a1 = IntervaloAbierto(2, 6)
        self.intervalo_c1 = IntervaloCerrado(2, 6)
        self.intervalo_sa1 = IntervaloSemiAbierto(2, 6)

    def test01_assert_limites(self):
        lim_inf, lim_sup = 2, 6
        self.assertEqual(self.intervalo_a1.lim_inf, lim_inf)
        self.assertEqual(self.intervalo_c1.lim_inf, lim_inf)
        self.assertEqual(self.intervalo_sa1.lim_inf, lim_inf)
        self.assertEqual(self.intervalo_a1.lim_sup, lim_sup)
        self.assertEqual(self.intervalo_c1.lim_sup, lim_sup)
        self.assertEqual(self.intervalo_sa1.lim_sup, lim_sup)

    def test02_assert_ancho(self):
        ancho = 4
        self.assertEqual(self.intervalo_a1.ancho, ancho)
        self.assertEqual(self.intervalo_c1.ancho, ancho)
        self.assertEqual(self.intervalo_sa1.ancho, ancho)

    def test03_assert_punto_medio(self):
        punto_medio = 4
        self.assertEqual(self.intervalo_a1.punto_medio, punto_medio)
        self.assertEqual(self.intervalo_c1.punto_medio, punto_medio)
        self.assertEqual(self.intervalo_sa1.punto_medio, punto_medio)

    def test04_assert_dentro_del_intervalo(self):
        self.assertTrue(self.intervalo_a1, 3)
        self.assertTrue(self.intervalo_c1, 3)
        self.assertTrue(self.intervalo_sa1, 3)
        self.assertTrue(self.intervalo_a1, 4)
        self.assertTrue(self.intervalo_c1, 4)
        self.assertTrue(self.intervalo_sa1, 4)
        self.assertTrue(self.intervalo_a1, 5.5)
        self.assertTrue(self.intervalo_c1, 5.5)
        self.assertTrue(self.intervalo_sa1, 5.5)

    def test05_assert_fuera_del_intervalo(self):
        self.assertFalse(self.intervalo_a1.está_dentro_del_intervalo_el_número(2))
        self.assertFalse(self.intervalo_a1.está_dentro_del_intervalo_el_número(6))
        self.assertFalse(self.intervalo_c1.está_dentro_del_intervalo_el_número(0))
        self.assertFalse(self.intervalo_c1.está_dentro_del_intervalo_el_número(7))
        self.assertFalse(self.intervalo_sa1.está_dentro_del_intervalo_el_número(2))
        self.assertFalse(self.intervalo_sa1.está_dentro_del_intervalo_el_número(7))

    def test06_eval_repr(self):
        intervalo_a2 = eval(repr(self.intervalo_a1))
        self.assertEqual(intervalo_a2, self.intervalo_a1)
        self.assertNotEqual(intervalo_a2, self.intervalo_c1)
        self.assertNotEqual(intervalo_a2, self.intervalo_sa1)

    def test07_eq_intervalos(self):
        self.assertFalse(self.intervalo_a1 == self.intervalo_c1)
        self.assertFalse(self.intervalo_a1 == self.intervalo_sa1)
        self.assertFalse(self.intervalo_c1 == self.intervalo_sa1)

if __name__ == "__main__":
    unittest.main() 