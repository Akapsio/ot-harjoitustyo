
package pasianssi;

public class Main {
    
    public static void main(String[] args) {
        Deck d = new Deck();
        for (int i = 0 ; i < 52 ; i++) {
            System.out.println(d.getDeck().get(i));
            
        }
        
      //d.shuffleDeck();
      //for (int i = 0 ; i < 52 ; i++) {
      //    System.out.println(d.getDeck().get(i));
      //    
      //}
    }
    
}
