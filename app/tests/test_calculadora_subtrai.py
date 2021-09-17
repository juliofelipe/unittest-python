try:
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
except:
    raise

import unittest

from src.calculadora import subtrai


class TestCalculadoraSubtrai(unittest.TestCase):
    def test_subtrai_5_e_5_deve_retornar_10(self):
        self.assertEqual(subtrai(5, 5), 0)

    def test_subtrai_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(subtrai(-5, 5), -10)

    def test_subtrai_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 0),
            (5, 5, 0),
            (1.5, 1.5, 0),
            (-5, 5, -10),
            (100, 100, 0),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai("11", 0)

    def test_subtrai_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(11, "0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
