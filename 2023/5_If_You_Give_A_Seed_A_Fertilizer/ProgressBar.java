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
    private double timeLeft = .0;
    private final long startTime = System.currentTimeMillis();
    private long lastPrint = 0;
    public ProgressBar(int currentStep, int totalSteps) {
        this.currentStep = currentStep;
        this.totalSteps = totalSteps;
    }
    public void stepCompleted() {
        long now = System.currentTimeMillis();
        if (times.isEmpty()) times.add(now - startTime);
        else times.add(System.currentTimeMillis() - now);
        this.currentStep++;
        this.updateAverageStepTimeAndTimeLeft();
    }
    private void updateAverageStepTimeAndTimeLeft() {
        averageStepTime = times.stream().mapToLong(Long::longValue).average().getAsDouble();
        long percentage = 10 * currentStep / totalSteps;
        timeLeft = (10 - percentage) * averageStepTime / 1000;
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
        double elapsedTime = (System.currentTimeMillis() - startTime) / 1000.0;
        sb.append(" ").append(formatTime(elapsedTime));
//        if (!times.isEmpty()) {
//                    sb.append(" - ")
//                    .append(formatTime(averageStepTime / 1000.0))
//                    .append("/iteration on average");
//        }
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
        if (time < 0) time = 0;
        long minutes = (long) (time / 60);
        long seconds = (long) (time % 60);
        return pad(minutes) + ":" + pad(seconds);
    }
    private String pad(long n) {
        if (n < 10) return "0" + n;
        return "" + n;
    }
}
