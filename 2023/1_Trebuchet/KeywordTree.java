public class KeywordTree {
    private final Node root;
    private char nextLabel = 1;

    public KeywordTree() {
        this.root = new Node(Character.MIN_VALUE, false);
    }

    public void addWord(String w) {
        if (nextLabel == 1) {
            Node n = root;
            for (char c : w.toCharArray()) {
                n = n.addChild(c, false);
            }
            n.addChild(this.nextLabel++, true);
        } else {

        }
    }
}
