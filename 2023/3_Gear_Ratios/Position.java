public class Position {
    private static int lineLength;
    private final int value;
    private final int start;
    private final int end;

    public static void setLineLength(int lineLength) {
        Position.lineLength = lineLength;
    }

    public Position(int value, int start, int end) {
        this.value = value;
        this.start = start;
        this.end = end;
    }

    public int getValue() {
        return value;
    }

    public int getStart() {
        return start;
    }

    public int getEnd() {
        return end;
    }

    public int getRow() {
        return start / Position.lineLength;
    }

    public int getStartCol() {
        return start % Position.lineLength;
    }

    public int getEndCol() {
        return end % Position.lineLength;
    }

    public boolean isNeighbor(int row, int col) {
        if (row == getRow() || row == getRow() - 1 || row == getRow() + 1) {
            return col >= getStartCol() - 1 && col <= getEndCol() + 1;
        }
        return false;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Position position = (Position) o;

        if (start != position.start) return false;
        return end == position.end;
    }
}
