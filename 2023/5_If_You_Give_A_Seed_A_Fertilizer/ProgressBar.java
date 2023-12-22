import java.util.ArrayList;
import java.util.List;

public class ProgressBar extends Thread {
    private static final char[] ANIMATION_CHARACTERS = {'\\','|','/','-'};
    private static int animationCounter = 0;
    private final long totalSteps;
    private final long startTime = System.currentTimeMillis();
    private final List<Long> times = new ArrayList<Long>();
    private long currentStep;
    private long lastPrint = 0;
    private boolean terminate = false;
    public ProgressBar(long currentStep, long totalSteps) {
        this.currentStep = currentStep;
        this.totalSteps = totalSteps;
        new Thread(this).start();
    }
    public ProgressBar(long totalSteps) {
        this.currentStep = 0;
        this.totalSteps = totalSteps;
        new Thread(this).start();
    }
    public synchronized void completeStep() {
        long now = System.currentTimeMillis();
        if (times.isEmpty()) times.add(now - startTime);
        else times.add(System.currentTimeMillis() - now);
        currentStep++;
//        updateAverageStepTimeAndTimeLeft();
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
            print(false, false);
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
    public synchronized void end() {
        print(true, true);
        terminate = true;
    }
}