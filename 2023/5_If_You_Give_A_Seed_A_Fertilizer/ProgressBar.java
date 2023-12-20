import java.util.ArrayList;
import java.util.List;

public class ProgressBar {
    private static char[] ANIMATION_CHARACTERS = {'\\','|','/','-'};
    private static int animationCounter = 0;
    private long currentStep;
    private final long totalSteps;
    private final List<Long> times = new ArrayList<Long>();
    private double averageStepTime = .0;
    private double eta = .0;
    private long lastPrint = 0;
    public ProgressBar(int currentStep, int totalSteps) {
        this.currentStep = currentStep;
        this.totalSteps = totalSteps;
    }
    private void updateAverageStepTime() {
        this.averageStepTime = this.times.stream().mapToLong(Long::longValue).average().getAsDouble();
    }
    public void stepCompleted() {
        this.times.add(System.currentTimeMillis());
        this.currentStep++;
        this.updateAverageStepTime();
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
        sb.append("] (").append(percentage).append(" / ").append(this.totalSteps).append(") ");
        if (!this.times.isEmpty()) {
            double timeLeft = (10 - percentage) * this.averageStepTime;
            sb.append("ETA: ").append(timeLeft).append(" seconds");
        }
        sb.append('\r');
        return String.valueOf(sb);
    }
    public void print(boolean endLine) {
        if (System.currentTimeMillis() >= this.lastPrint + 500) {
            this.lastPrint = System.currentTimeMillis();
            System.out.print(this.getString());
        }
        if (endLine) System.out.print("\n");
    }
}
