package pasianssi;

import java.util.ArrayDeque;

public class AceStack {

    ArrayDeque<Card> AceStack;

    public AceStack() {
        this.AceStack = new ArrayDeque<>();
    }

    public void addCard(Card card) {
        if (this.AceStack.isEmpty() && card.getValue() == 1) {
            this.AceStack.add(card);
        } else {
            if (AceStack.getLast().getValue() == card.getValue() - 1) {
                AceStack.add(card);
            }
        }
    }
}
