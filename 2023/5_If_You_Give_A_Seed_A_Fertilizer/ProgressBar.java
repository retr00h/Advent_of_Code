import java.util.ArrayList;
import java.util.List;

public class ProgressBar {
    private int done;
    private final int total;
    private static final char[] anim = {'\\','|','/','-'};
    private int animCounter = 0;
    private final List<Long> times = new ArrayList<Long>();
    private long lastPrint = 0;
    public ProgressBar(int done, int total) {
        this.done = done;
        this.total = total;
    }
    public void incrementDone() {
        this.done += 1;
    }
    public void addTime(long startTime) {
        times.add(System.currentTimeMillis() - startTime);
    }
    private char getAnim() {
        char c = anim[animCounter++];
        if (animCounter == anim.length) animCounter = 0;
        return c;
    }
    @Override
    public String toString() {
        String s = "[";
        int completed = 10 * done / total;
        for (int i = 0; i < 10; i++) {
            if (completed == i) {
                s += getAnim();
            } else {
                if (i < completed) s += "=";
                else s += " ";
            }
        }
        s += "] (" + done + " / " + total + ") ";
        if (!times.isEmpty()) {
            double avg = ((double) times.stream().mapToLong(Long::longValue).sum()) / times.size() / 1000;
            double timeLeft = (total - done) * avg;
            s += "ETA: " + timeLeft + " seconds";
        }
        s += "\r";
        return s;
    }
    public void print(boolean endLine) {
        if (System.currentTimeMillis() >= lastPrint + 500) {
            lastPrint = System.currentTimeMillis();
            System.out.print(this);
        }
        if (endLine) System.out.print("\n");
    }
}
