package com.mycompany.unicafe;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(10);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }

    @Test
    public void saldoAlussaOikein() {
        System.out.println(kortti.toString());
	assertThat(kortti.toString(), is(equalTo("saldo: 0.10")));
    }
    
    @Test
    public void rahanLataaminenKasvattaSaldoaOikein() {
        kortti.lataaRahaa(10);
        assertThat(kortti.toString(), is(equalTo("saldo: 0.20")));
    }
    
    @Test
    public void rahanOttaminenToimiiOikein() {
        boolean toimiko = kortti.otaRahaa(10);
        assertThat(kortti.toString(), is(equalTo("saldo: 0.0")));
        assertThat(toimiko, is(true));
    }
    
    @Test 
    public void saldoEiMeneNegatiiviseksi() {
        boolean toimiko = kortti.otaRahaa(20);
        assertThat(kortti.toString(), is(equalTo("saldo: 0.10")));
        assertThat(toimiko, is(false));
    }
}
