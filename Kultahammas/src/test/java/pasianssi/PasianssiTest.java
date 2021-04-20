package pasianssi;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

public class PasianssiTest {

    Deck deck;

    @Test
    public void DeckSizeIs52() {
        assertThat(deck.getDeck().size(), is(equalTo(52)));
    }

    @Test
    public void CardsAreNotLostWhenShuffled() {
        deck.shuffleDeck();
        assertThat(deck.getDeck().size(), is(equalTo(52)));
    }

    @Before
    public void setUp() {
        deck = new Deck();
    }

    public PasianssiTest() {
    }

    @BeforeClass
    public static void setUpClass() {
    }

    @AfterClass
    public static void tearDownClass() {
    }

    @After
    public void tearDown() {
    }

    // TODO add test methods here.
    // The methods must be annotated with annotation @Test. For example:
    //
    // @Test
    // public void hello() {}
}
