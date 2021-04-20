package pasianssi;

import java.util.*;

public class Deck {
    ArrayList<Card> cards;
    
    public Deck() {
        this.cards = new ArrayList<>();
        for (int i = 0; i <= 3; i++) {
            for (int j = 1; j <= 13; j++) {
                cards.add(new Card(i, j));
            }
        }
    }
    
    public ArrayList<Card> getDeck() {
        return this.cards;
    }
    
    public void shuffleDeck() {
        Random random = new Random();
        ArrayList<Card> newDeck = new ArrayList<>();
        for (int i = 52; i > 0; i--) {
            int card = random.nextInt(i);
            newDeck.add(cards.get(card));
            cards.remove(card);
        }
        this.cards = newDeck;
    }
}
