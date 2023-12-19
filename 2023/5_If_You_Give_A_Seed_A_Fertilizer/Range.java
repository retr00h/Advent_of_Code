import java.util.Arrays;

public class Range implements Comparable<Range>{
    private final long sourceRangeStart;
    private final long destinationRangeStart;
    private final long rangeLength;
    private final long sourceRangeEnd;
    private final long offset;
    public Range(long sourceRangeStart, long destinationRangeStart, long rangeLength) {
        this.sourceRangeStart = sourceRangeStart;
        this.destinationRangeStart = destinationRangeStart;
        this.rangeLength = rangeLength;
        this.sourceRangeEnd = sourceRangeStart + rangeLength;
        this.offset = destinationRangeStart - sourceRangeStart;
    }
        public long sourceToDestination(long source) {
        if (source >= sourceRangeStart && source <= sourceRangeEnd) {
            source += offset;
        }
        return source;
    }
    @Override
    public int compareTo(Range other) {
        return Long.compare(this.sourceRangeStart, other.sourceRangeStart);
    }
//    public static Range merge(Range[] ranges) {
//        if (ranges.length == 1) return ranges[0];
//        Arrays.sort(ranges);
//        long totalLength = 0;
//        for (Range r : ranges) totalLength += r.rangeLength;
//        return new Range(ranges[0].sourceRangeStart, ranges[0].destinationRangeStart, totalLength);
//    }
    @Override
    public String toString() {
        return "Range{" +
                "sourceRangeStart=" + sourceRangeStart +
                ", destinationRangeStart=" + destinationRangeStart +
                ", rangeLength=" + rangeLength +
                '}';
    }
    public boolean containsSource(long source) {
        return source >= sourceRangeStart && source <= sourceRangeEnd;
    }

}

