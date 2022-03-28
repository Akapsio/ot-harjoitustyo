import unittest
from src.maksukortti import Maksukortti
from src.kassapaate import Kassapaate

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)
        self.kassa = Kassapaate()
        maksu = 1000

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)
    
    def test_luotu_kassa_on_maaritelty_oikein(self):
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)
        self.assertEqual(int(self.kassa.edulliset), 0)
        self.assertEqual(int(self.kassa.maukkaat), 0)

    def test_edullisen_osto_kasvattaa_edullisten_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(1000)
        self.assertEqual(int(self.kassa.edulliset), 1)

    def test_edullisen_lounaan_ostosta_palautuu_oikea_vaihtoraha(self):
        self.assertEqual(int(self.kassa.syo_edullisesti_kateisella(1000)), 760)

    def test_edullisen_lounaan_osto_kateisella_kasvattaa_kassassa_olevaa_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(1000)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100240)

    def test_edullisen_lounaan_osto_ei_onnistu_liian_vahalla_rahalla(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(int(self.kassa.edulliset), 0)
        self.assertEqual(int(self.kassa.syo_edullisesti_kateisella(200)), 200)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)

    def test_maukkaan_osto_kateisella_kasvattaa_edullisten_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(1000)
        self.assertEqual(int(self.kassa.maukkaat), 1)

    def test_maukkaan_lounaan_ostosta_palautuu_oikea_vaihtoraha(self):
        self.assertEqual(int(self.kassa.syo_maukkaasti_kateisella(1000)), 600)

    def test_maukkaan_lounaan_osto_kasvattaa_kassassa_olevaa_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(1000)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100400)

    def test_maukkaan_lounaan_osto_ei_onnistu_liian_vahalla_rahalla(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(int(self.kassa.maukkaat), 0)
        self.assertEqual(int(self.kassa.syo_maukkaasti_kateisella(200)), 200)
        self.assertEqual(int(self.kassa.kassassa_rahaa), 100000)
    
    def test_edullisen_lounaan_osto_onnistuu_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 7.6")
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_edullisen_lounaan_osto_kortilla_kasvattaa_myytyjen_maaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullisen_lounaan_osto_ei_vie_saldoa_negatiiviseksi_eika_kasvata_myytyjen_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)

    def test_maukkaan_lounaan_osto_ei_vie_saldoa_negatiiviseksi_eika_kasvata_myytyjen_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
        self.assertEqual(self.kassa.maukkaat, 2)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)

    def test_korttiosto_ei_muuta_kassassa_olevaa_rahamaaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_lataaminen_kerryttaa_kassaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1010)
        self.assertEqual(self.kassa.kassassa_rahaa, 101010)
        self.assertEqual(str(self.kortti), "saldo: 20.1")

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(str(self.kortti), "saldo: 10.0")

    def test_kortin_saldo_ei_mene_negatiiviseksi(self):
        self.kortti.ota_rahaa(1001)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
        self.assertEqual(self.kortti.ota_rahaa(1001), False)