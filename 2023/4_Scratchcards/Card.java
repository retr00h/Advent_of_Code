import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Card {
    private final HashSet<Integer> winningNumbers = new HashSet<Integer>();
    private final HashSet<Integer> numbers = new HashSet<Integer>();
    private final int id;
    public Card(int id) {
        this.id = id;
    }
    public Card(int id, int[] numbers, int[] winningNumbers) {
        this.id = id;
        for (int n : numbers) this.numbers.add(n);
        for (int n : winningNumbers) this.winningNumbers.add(n);
    }

    public int getId() {
        return id;
    }

    public List<Integer> getNumbersThatAreWinningNumbers() {
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        for (int n : this.numbers) if (this.winningNumbers.contains(n)) numbers.add(n);
        return numbers;
    }
}
