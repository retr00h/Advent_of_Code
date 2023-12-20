import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;

public class ProgressBar {
    private static char[] ANIMATION_CHARACTERS = {'\\','|','/','-'};
    private static int animationCounter = 0;
    private long currentStep;
    private final long totalSteps;
    private final List<Long> times = new ArrayList<Long>();
    private double averageStepTime = .0;
    private final long startTime = System.currentTimeMillis();
    private long lastPrint = 0;
    public ProgressBar(int currentStep, int totalSteps) {
        this.currentStep = currentStep;
        this.totalSteps = totalSteps;
    }
    public void stepCompleted() {
        long lastTime = System.currentTimeMillis();
        if (times.isEmpty()) times.add(lastTime - startTime);
        else times.add(System.currentTimeMillis() - lastTime);
        this.currentStep++;
        this.updateAverageStepTime();
    }
    private void updateAverageStepTime() {
        averageStepTime = times.stream().mapToLong(Long::longValue).average().getAsDouble();
    }
    private char getAnim() {
        return ANIMATION_CHARACTERS[animationCounter++ % ANIMATION_CHARACTERS.length];
    }
    private String getString() {
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
        if (!times.isEmpty()) {
            double timeLeft = (10 - percentage) * averageStepTime / 1000;
            sb.append(" (").append(formatTime((System.currentTimeMillis() - startTime) / 1000.0))
                    .append(" - ").append(formatTime(timeLeft)).append(")");
        }
        sb.append('\r');
        return String.valueOf(sb);
    }
    public void print(boolean endLine) {
        if (System.currentTimeMillis() >= lastPrint + 500) {
            lastPrint = System.currentTimeMillis();
            System.out.print(getString());
        }
        if (endLine) System.out.print("\n");
    }
    private String formatTime(double time) {
        long minutes = (long) (time / 60);
        long seconds = (long) (time % 60);
        return pad(minutes) + ":" + pad(seconds);
    }
    private String pad(long n) {
        if (n < 10) return "0" + n;
        return "" + n;
    }
}
