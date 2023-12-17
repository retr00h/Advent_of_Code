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

    public static Range merge(Range[] ranges) {
        if (ranges.length == 1) return ranges[0];
        Arrays.sort(ranges);
        long totalLength = 0;
        for (Range r : ranges) totalLength += r.rangeLength;
        return new Range(ranges[0].sourceRangeStart, ranges[0].destinationRangeStart, totalLength);
    }
    
    @Override
    public String toString() {
        return "Range{" +
                "sourceRangeStart=" + sourceRangeStart +
                ", destinationRangeStart=" + destinationRangeStart +
                ", rangeLength=" + rangeLength +
                '}';
    }

//    public static void main(String[] args) {
////        50 98 2
////        52 50 48
////        destStart srcStart length
//        Range r1 = new Range(98,20,2);
//        Range r2 = new Range(50,52,48);
//        Range[] rlist = {r1, r2};
//        Arrays.sort(rlist);
//        System.out.println(Arrays.toString(rlist));
//        Range newRange = Range.merge(rlist);
//        System.out.println(newRange);
//        System.out.println(newRange.sourceToDestination(79) == 81);
//        System.out.println(newRange.sourceToDestination(14) == 14);
//        System.out.println(newRange.sourceToDestination(55) == 57);
//        System.out.println(newRange.sourceToDestination(13) == 13);
//
////        - Seed number 79 corresponds to soil number 81.
////        - Seed number 14 corresponds to soil number 14.
////        - Seed number 55 corresponds to soil number 57.
////        - Seed number 13 corresponds to soil number 13.
////        System.out.println(r.getDestinationFromSource(53));
//    }
}

