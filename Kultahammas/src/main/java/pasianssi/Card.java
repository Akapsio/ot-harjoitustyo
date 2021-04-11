package pasianssi;

public class Card {
    private int suitOrdinal;
    private int value;
    
    public Card(int ordinal, int value) {
        this.suitOrdinal = ordinal;
        this.value = value;
    }
    
    public int getOrdinal(Card card) {
        return this.suitOrdinal;
    }
    
    public int getValue(Card card) {
        return this.value;
    }
    
    // Method returns the suit as String. Not sure if necessary.
    
    public String suitToString(int ordinal) {
        if (ordinal == Suit.CLUB.ordinal()) return "CLUB";
        if (ordinal == Suit.DIAMOND.ordinal()) return "DIAMOND";
        if (ordinal == Suit.HEARTS.ordinal()) return "HEARTS";
        if (ordinal == Suit.SPADE.ordinal()) return "SPADE";
        return "";
    }
    
    public String toString() {
        if (value > 10) {
            
        }
        return suitToString(this.suitOrdinal) + " " + this.value; 
    }
}
