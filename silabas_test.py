import unittest
from silabas import Silabeador

class grupoVocalTest(unittest.TestCase):
    def test_grupo_vocal_sencillo(self):
        self.assertEqual(Silabeador().silabeo('cadena'), ['ca','de','na'])
        self.assertEqual(Silabeador().silabeo('enano'), ['e','na','no'])
        self.assertEqual(Silabeador().silabeo('altar'), ['al','tar'])
        self.assertEqual(Silabeador().silabeo('calentar'), ['ca','len','tar'])

    def test_grupo_vocal_diptongo(self):
        self.assertEqual(Silabeador().silabeo('camión'), ['ca','mión'])
        self.assertEqual(Silabeador().silabeo('pingüino'), ['pin','güi','no'])
        self.assertEqual(Silabeador().silabeo('baile'), ['bai','le'])
        self.assertEqual(Silabeador().silabeo('aire'), ['ai','re'])
        self.assertEqual(Silabeador().silabeo('caucho'), ['cau','cho'])
        self.assertEqual(Silabeador().silabeo('ambiguo'), ['am','bi','guo'])

    def test_grupo_vocal_triptongo(self):
        self.assertEqual(Silabeador().silabeo('biauricular'), ['biau','ri','cu','lar'])
        self.assertEqual(Silabeador().silabeo('semiautomatico'), ['se','miau','to','ma','ti','co'])
        self.assertEqual(Silabeador().silabeo('miau'), ['miau'])

    def test_grupo_vocal_hiato(self):
        self.assertEqual(Silabeador().silabeo('teorema'), ['te','o','re','ma'])
        self.assertEqual(Silabeador().silabeo('baúl'), ['ba','úl'])

    def test_grupo_vocal_excepcion_y(self):
        self.assertEqual(Silabeador().silabeo('Paraguay'), ['Pa','ra','guay'])
        self.assertEqual(Silabeador().silabeo('fluye'), ['flu','ye'])        
        self.assertEqual(Silabeador().silabeo('soy'), ['soy'])

    def test_grupo_vocal_excepcion_in(self):
        self.assertEqual(Silabeador().silabeo('inacción'), ['in','ac','ción'])
        self.assertEqual(Silabeador().silabeo('inadmisible'), ['in','ad','mi','si','ble'])        

if __name__ == '__main__':
    unittest.main()