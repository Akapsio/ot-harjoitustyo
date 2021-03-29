package com.mycompany.unicafe;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author osvald
 */
public class KassapaateTest {
    
    Kassapaate kassa;
    
    public KassapaateTest() {
        
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
        kassa = new Kassapaate();
    }
    
    @Test
    public void rahamaaraJaMyydytLounaatAlussaOk() {
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
    }
    
    @Test
    public void edullisetAlussaOk() {
        assertThat(kassa.edullisiaLounaitaMyyty(), is(equalTo(0)));
    }
    
    @Test
    public void maukkaatAlussaOk() {
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(equalTo(0)));
    }
    
    @Test
    public void edullisenLounaanOstoKateisellaToimii() {
        int vaihtoraha = kassa.syoEdullisesti(200);
        assertThat(vaihtoraha, is(equalTo(200)));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(equalTo(0)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
        vaihtoraha = kassa.syoEdullisesti(1000);
        assertThat(vaihtoraha, is(equalTo(1000-240)));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(equalTo(1)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100240)));
    }
    
    @Test
    public void maukkaanLounaanOstoKateisellaToimii() {
        int vaihtoraha = kassa.syoMaukkaasti(200);
        assertThat(vaihtoraha, is(equalTo(200)));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(equalTo(0)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
        vaihtoraha = kassa.syoMaukkaasti(1000);
        assertThat(vaihtoraha, is(equalTo(1000-400)));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(equalTo(1)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100400)));
    }
    
    @Test
    public void edullisenLounaanOstoKortillaToimii() {
        Maksukortti kortti = new Maksukortti(1000);
        boolean toimiko = kassa.syoEdullisesti(kortti);
        assertThat(toimiko, is(true));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(equalTo(1)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
    }
    
    @Test
    public void edullisenLounaanOstoEiToimiJosEiTarpeeksiRahaa() {
        Maksukortti kortti = new Maksukortti(0);
        boolean toimiko = kassa.syoEdullisesti(kortti);
        assertThat(toimiko, is(false));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(equalTo(0)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
    }
    
    @Test
    public void maukkaanLounaanOstoKortillaToimii() {
        Maksukortti kortti = new Maksukortti(1000);
        boolean toimiko = kassa.syoMaukkaasti(kortti);
        assertThat(toimiko, is(true));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(equalTo(1)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
    }
    
    @Test
    public void maukkaanLounaanOstoEiToimiJosEiTarpeeksiRahaa() {
        Maksukortti kortti = new Maksukortti(0);
        boolean toimiko = kassa.syoMaukkaasti(kortti);
        assertThat(toimiko, is(false));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(equalTo(0)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
    }
    
    @Test
    public void kortilleLadattaessaKortinSaldoMuuttuuJaKassaanTuleeRahaa() {
        Maksukortti kortti = new Maksukortti(0);
        kassa.lataaRahaaKortille(kortti, 100);
        assertThat(kortti.saldo(), is(equalTo(100)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100100)));
    }
    
    @Test
    public void kortilleEiVoiLadataNegatiivistaSummaa() {
        Maksukortti kortti = new Maksukortti(0);
        kassa.lataaRahaaKortille(kortti, -1);
        assertThat(kortti.saldo(), is(equalTo(0)));
        assertThat(kassa.kassassaRahaa(), is(equalTo(100000)));
    }
    // TODO add test methods here.
    // The methods must be annotated with annotation @Test. For example:
    //
    // @Test
    // public void hello() {}
}
