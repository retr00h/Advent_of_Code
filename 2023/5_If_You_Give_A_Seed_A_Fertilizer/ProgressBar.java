import java.util.ArrayList;
import java.util.List;

public class ProgressBar extends Thread {
    private static final char[] ANIMATION_CHARACTERS = {'\\','|','/','-'};
    private static int animationCounter = 0;
    private final long totalSteps;
    private final long startTime = System.currentTimeMillis();
    private long currentStep;
    private long lastPrint = 0;
    private double toSubtract = 0;
    private double timeLeft = 0.0;
    private boolean terminate = false;
    public ProgressBar(long totalSteps) {
        this.currentStep = 0;
        this.totalSteps = totalSteps;
        new Thread(this).start();
    }
    public synchronized void completeStep() {
        timeLeft = (System.currentTimeMillis() - startTime) * (totalSteps - ++currentStep) / 1000.0;
    }
    private synchronized void print(boolean endLine, boolean force) {
        if (force || System.currentTimeMillis() >= lastPrint + 500) {
            lastPrint = System.currentTimeMillis();
            System.out.print(getString());
        }
        if (endLine) System.out.print("\n");
    }
    private synchronized String getString() {
        StringBuilder sb = new StringBuilder("[");
        long percentage = 10 * currentStep / totalSteps;
        for (int i = 0; i < 10; i++) {
            if (percentage == i) {
                sb.append(getAnim());
            } else {
                if (i < percentage) {
                    sb.append("=");
                }
                else sb.append(" ");
            }
        }
        sb.append("]");
        double elapsedTime = (System.currentTimeMillis() - startTime) / 1000.0;
        sb.append(" ").append(formatTime(elapsedTime));
        sb.append(" - ").append(formatTime(timeLeft - toSubtract));
        sb.append(" - ").append(formatIts(currentStep / elapsedTime)).append(" it/s");
        sb.append('\r');
        return String.valueOf(sb);
    }
    private String formatTime(double time) {
        if (time < 0) time = 0;
        long minutes = (long) (time / 60);
        long seconds = (long) (time % 60);
        return pad(minutes) + ":" + pad(seconds);
    }
    private String pad(long n) {
        if (n < 10) return "0" + n;
        return "" + n;
    }
    private String formatIts(double its) {
        return String.format("%.2f", its);
    }
    private synchronized char getAnim() {
        return ANIMATION_CHARACTERS[animationCounter++ % ANIMATION_CHARACTERS.length];
    }
    @Override
    public synchronized void start() {
        super.start();
        print(false, false);
    }
    @Override
    public void run() {
        super.run();
        while (!terminate) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ignored) {}
            toSubtract += 0.1;
            print(false, false);
        }
    }
    public synchronized void end() {
        print(true, true);
        terminate = true;
    }
}