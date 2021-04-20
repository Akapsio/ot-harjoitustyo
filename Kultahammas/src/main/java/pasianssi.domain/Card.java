package pasianssi;

public class Card {
    private int suitOrdinal;
    private int value;
    private boolean isRed;
    private boolean visible;
    
    public Card(int ordinal, int value) {
        this.suitOrdinal = ordinal;
        this.value = value;
        if (ordinal < 2) {
            isRed = false;
        } else {
            isRed = true;
        }
        visible = false;
    }
    
    public int getOrdinal() {
        return this.suitOrdinal;
    }
    
    public int getValue() {
        return this.value;
    }
    
    public boolean getColor() {
        return this.isRed;
    }
    // Method returns the suit as String. Not sure if necessary.
    
    public String suitToString(int ordinal) {
        if (ordinal == Suit.CLUB.ordinal()) { 
            return "CLUB";
        }
        if (ordinal == Suit.SPADE.ordinal()) {
            return "SPADE";
        }
        if (ordinal == Suit.DIAMOND.ordinal()) {
            return "DIAMOND";
        }
        if (ordinal == Suit.HEARTS.ordinal()) {
            return "HEARTS";
        }
        return "";
    }
    
    public String toString() {
        return suitToString(this.suitOrdinal) + " " + this.value; 
    }
}
