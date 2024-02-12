import java.util.ArrayList;
import java.util.List;

public class Node {
    private final char label;
    private final boolean isEndOfWord;
    private final List<Node> children;

    public Node(char label, boolean isEndOfWord) {
        this.label = label;
        this.isEndOfWord = isEndOfWord;
        this.children = new ArrayList<Node>();
    }

    public char getLabel() {
        return label;
    }

    public boolean isEndOfWord() {
        return isEndOfWord;
    }

    public List<Node> getChildren() {
        return children;
    }

    public Node addChild(Node n) {
        this.children.add(n);
        return this.children.get(this.children.size() - 1);
    }

    public Node addChild(char label, boolean isEndOfWord) {
        this.children.add(new Node(label, isEndOfWord));
        return this.children.get(this.children.size() - 1);
    }
}
