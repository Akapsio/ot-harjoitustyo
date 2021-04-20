package pasianssi;

import java.util.ArrayDeque;

public class FieldStack {
    ArrayDeque<Card> FieldStack;
    
    public FieldStack() {
        this.FieldStack = new ArrayDeque<>();
    }
    
    public void addCard(Card card, FieldStack fieldStack) {
        ArrayDeque<Card> stack = fieldStack.StackAsDeque();
        Card comparable = stack.getLast();
        if (card.getColor() != comparable.getColor()) {
            if (card.getValue() == comparable.getValue() + 1) {
                stack.addLast(card);
                this.FieldStack = stack;
            }
        }
    }
    
    public ArrayDeque<Card> StackAsDeque() {
        return this.FieldStack;
    }
}
