/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pasianssi;

/**
 *
 * @author osvald
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Deck d = new Deck();
        for (int i = 0 ; i < 52 ; i++) {
            System.out.println(d.getDeck().get(i));
            
        }
        
        d.shuffleDeck();
        for (int i = 0 ; i < 52 ; i++) {
            System.out.println(d.getDeck().get(i));
            
        }
    }
    
}
