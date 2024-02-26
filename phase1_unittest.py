'''CREATED BY JAVIER MOYANO SAN BRUNO (100495884) AND
    JORGE MEJIAS DONOSO (100495807), 27-03-2023'''
import unittest
from phase1 import SList2


class Test(unittest.TestCase):

    # setUp is a method which is ran before a test method is executed. This
    # is useful if you need some data (for example) to be present before
    # running a test.
    def setUp(self):

        'Este es el set up del ejercicio 1 del_largest_seq'
        self.l1 = SList2()
        for n in [1, 2, 3, 4, 9]:
            self.l1.addLast(n)

        self.l2 = SList2()
        self.l2.addLast(8)

        self.l3 = SList2()
        for n in [9, 6, 4, 4, 3, 6, 7]:
            self.l3.addLast(n)

        self.l4 = SList2()
        for n in [1, 2, 3, 4, 4, 4, 4]:
            self.l4.addLast(n)

        self.l5 = SList2()
        for n in [2, 2, 2, 2, 4, 5, 6, 6, 6, 6]:
            self.l5.addLast(n)

        self.l6 = SList2()

        self.l7 = SList2()
        for n in [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]:
            self.l7.addLast(n)


        'Este es el set up del ejercicio 2 left_right_shift'
        self.l16 = SList2()
        for n in [1, 2, 3, 4, 3, 3, 3, 5, 6]:
            self.l16.addLast(n)

        self.l17 = SList2()

        self.l18 = SList2()
        for n in [1]:
            self.l18.addLast(n)


        'Este es el set up del ejercicio 3 left_right_shift'
        self.l8 = SList2()
        self.l9 = SList2()
        for n in [1, 2, 3, 4, 5]:
            self.l8.addLast(n)
            self.l9.addLast(n)

        self.l10 = SList2()
        self.l11 = SList2()
        for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]:
            self.l10.addLast(n)
            self.l11.addLast(n)

        self.l12 = SList2()
        self.l13 = SList2()
        self.l14 = SList2()
        for n in [1, 2, 3, 4, 5, 6]:
            self.l12.addLast(n)
            self.l13.addLast(n)
            self.l14.addLast(n)

        self.l15 = SList2()
        for n in [1, 2, 3, 4]:
            self.l15.addLast(n)


    # TEST EJERCICIO 1

    def test1_1(self):
        print("Caso 1: Todos los numeros se repiten solo una vez por lo que "
              "se borra el último")
        l1_1 = SList2()
        for n in [1, 2, 3, 4]:
            l1_1.addLast(n)
        self.l1.del_largest_seq()
        self.assertEqual(str(self.l1), str(l1_1))

    def test1_2(self):
        print("Caso 2: La lsita está vacía ")
        l2_2 = SList2()
        self.l2.del_largest_seq()
        self.assertEqual(str(self.l2), str(l2_2))

    def test1_3(self):
        print("Caso 3: Elimina la secuencia más larga del medio (la de 4s)")
        l3_3 = SList2()
        for n in [9, 6, 3, 6, 7]:
            l3_3.addLast(n)
        self.l3.del_largest_seq()
        self.assertEqual(str(self.l3), str(l3_3))

    def test1_4(self):
        print("Caso 4: borra la secuencia más larga, que es la última")
        l4_4 = SList2()
        for n in [1, 2, 3]:
            l4_4.addLast(n)
        self.l4.del_largest_seq()
        self.assertEqual(str(self.l4), str(l4_4))

    def test1_5(self):
        print("Caso 5: como hay dos secuencias del mismo tamaño (mayor que "
              "uno) borra la última")
        l5_5 = SList2()
        for n in [2, 2, 2, 2, 4, 5]:
            l5_5.addLast(n)
        self.l5.del_largest_seq()
        self.assertEqual(str(self.l5), str(l5_5))

    def test1_6(self):
        print("Caso 6: la lista está vacía por lo que devuelve la frase "
              "-Error: la lista está vacía- y no hace nada")
        l6_6 = SList2()
        self.l6.del_largest_seq()
        self.assertEqual(str(self.l6), str(l6_6))

    def test1_7(self):
        print("Caso 7: todas las secuencias son mayores que uno y son "
              "iguales por lo que se borrará la última")
        l7_7 = SList2()
        for n in [1, 1, 2, 2, 3, 3, 4, 4]:
            l7_7.addLast(n)
        self.l7.del_largest_seq()
        self.assertEqual(str(self.l7), str(l7_7))


    # TEST EJERCICIO 2

    def test2_1(self):
        print("Caso 16: Recibe una secuencia de 9 numeros y tiene que arreglar el loop que se crea en el ultimo")
        l16_16 = SList2()
        for i in [1, 2, 3, 4, 3, 3, 3, 5, 6]:
            l16_16.addLast(i)
        l16_16.create_loop(8)
        l16_16.fix_loop()
        self.assertEqual(str(self.l16), str(l16_16))

    def test2_2(self):
        print("Caso 17: La lista esta vacia")
        l17_17 = SList2()
        l17_17.fix_loop()
        self.assertEqual(str(self.l17), str(l17_17))

    def test2_3(self):
        print("Caso 16: Recibe una secuencia de 1 numero y crea un bucle")
        l18_18 = SList2()
        for i in [1]:
            l18_18.addLast(i)
        l18_18.create_loop(0)
        l18_18.fix_loop()
        self.assertEqual(str(self.l18), str(l18_18))


    # TEST EJERCICIO 3

    def test3_1(self):
        print("Caso 8: Recibe una secuencia y de 5 numeros y tiene que mover "
              "el primero al final")
        l8_8 = SList2()
        for n in [2, 3, 4, 5, 1]:
            l8_8.addLast(n)
        self.l8.left_right_shift(True, 1)
        self.assertEqual(str(self.l8), str(l8_8))

    def test3_2(self):
        print("Caso 9: Recibe una secuencia y de 5 numeros y tiene que mover "
              "el ultimo al principio")
        l9_9 = SList2()
        for n in [5, 1, 2, 3, 4]:
            l9_9.addLast(n)
        self.l9.left_right_shift(False, 1)
        self.assertEqual(str(self.l9), str(l9_9))

    def test3_3(self):
        print("Caso 10: Recibe una secuencia y de 5 numeros y tiene que mover "
              "los x primeros al final (en este caso 3)")
        l10_10 = SList2()
        for n in [4, 5, 6, 7, 8, 9, 0, 1, 1, 2, 3]:
            l10_10.addLast(n)
        self.l10.left_right_shift(True, 3)
        self.assertEqual(str(self.l10), str(l10_10))

    def test3_4(self):
        print("Caso 11: Recibe una secuencia y de 5 numeros y tiene que mover "
              "los x ultimos al principio (en este caso 6)")
        l11_11 = SList2()
        for n in [9, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8]:
            l11_11.addLast(n)
        self.l11.left_right_shift(False, 3)
        self.assertEqual(str(self.l11), str(l11_11))

    def test3_5(self):
        print("Caso 12: Recibe una secuencia de numero y tiene que devolver "
              "la misma pues vamos a mover todos del principio al final")
        l12_12 = SList2()
        for n in [1, 2, 3, 4, 5, 6]:
            l12_12.addLast(n)
        self.l12.left_right_shift(True, 6)
        self.assertEqual(str(self.l12), str(l12_12))

    def test3_6(self):
        print("Caso 13: Recibe una secuencia de numeros y tiene que devolver "
              "la misma pues vamos a mover todos del final al principo")
        l13_13 = SList2()
        for n in [1, 2, 3, 4, 5, 6]:
            l13_13.addLast(n)
        self.l13.left_right_shift(True, 6)
        self.assertEqual(str(self.l13), str(l13_13))

    def test3_7(self):
        print("Caso 14: La n es mayor que el tamaño de la lista,"
              "Error, se imprime la misma lista")
        l14_14 = SList2()
        for n in [1, 2, 3, 4, 5, 6]:
            l14_14.addLast(n)
        self.l14.left_right_shift(True, 15)
        self.assertEqual(str(self.l14), str(l14_14))

    def test3_8(self):
        print("Caso 15: La n es negativa, Error, se imprime la misma lista")
        l15_15 = SList2()
        for n in [1, 2, 3, 4]:
            l15_15.addLast(n)
        self.l15.left_right_shift(True, -6)
        self.assertEqual(str(self.l15), str(l15_15))


if __name__ == "__main__":
    unittest.main()
