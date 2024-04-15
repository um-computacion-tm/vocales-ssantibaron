import unittest

def contar_vocales(mi_string):
    resultado = {}
    for letra in mi_string:
        if letra in "aeiou":
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
        if letra in "AEIOU":
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
        if letra in "áéíóú":
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado

class TestContarVocales(unittest.TestCase):

    def test_nada(self):
        resultado = contar_vocales("zzz")
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales("cas")
        self.assertEqual(resultado, {"a":1})

    def test_contar_aa(self):
        resultado = contar_vocales("casa")
        self.assertEqual(resultado, {"a":2})

    def test_contar_bese(self):
        resultado = contar_vocales("bese")
        self.assertEqual(resultado, {"e":2})

    def test_contar_besa(self):
        resultado = contar_vocales("besa")
        self.assertEqual(resultado, {"e":1, "a":1})

    def test_contar_casanova(self):
        resultado = contar_vocales("casanova")
        self.assertEqual(resultado, {"a":3,"o":1})

    def test_contar_CASANOVA(self):
        resultado = contar_vocales("CASANOVA")
        self.assertEqual(resultado, {"A":3,"O":1})

    def test_contar_fué(self):
        resultado = contar_vocales("fué")
        self.assertEqual(resultado, {"u":1,"é":1})

    def test_contar_cAnCión(self):
        resultado = contar_vocales("cAnCión")
        self.assertEqual(resultado, {"A":1,"i":1,"ó":1})
    
    def test_contar_miércoles(self):
        resultado = contar_vocales("miércoles")
        self.assertEqual(resultado, {"i":1,"é":1,"o":1,"e":1})

unittest.main()

#while(True):
#    palabra = input("Ingrese palabra: ")
#    print(contar_vocales(palabra))