import java.io.FileInputStream;
import java.util.*;

public class Solver {
    private static final String PATH = "./2023/5_If_You_Give_A_Seed_A_Fertilizer/input/5_If_You_Give_A_Seed_A_Fertilizer.txt";
    private static final String[] STRING_DELIMITERS = {"seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
            "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"};
    private final long[] seeds;
    private final Range[] seedToSoilRanges;
    private final Range[] soilToFertilizerRanges;
    private final Range[] fertilizerToWaterRanges;
    private final Range[] waterToLightRanges;
    private final Range[] lightToTemperatureRanges;
    private final Range[] temperatureToHumidityRanges;
    private final Range[] humidityToLocationRanges;
    public Solver() {
        List<String> lines = getInput();
        this.seeds = initializeSeeds(lines);
        int[] delimiters = getDelimiters(lines);
        this.seedToSoilRanges = initializeRange(lines, delimiters[0], delimiters[1]);
        this.soilToFertilizerRanges = initializeRange(lines, delimiters[1], delimiters[2]);
        this.fertilizerToWaterRanges = initializeRange(lines, delimiters[2], delimiters[3]);
        this.waterToLightRanges = initializeRange(lines, delimiters[3], delimiters[4]);
        this.lightToTemperatureRanges = initializeRange(lines, delimiters[4], delimiters[5]);
        this.temperatureToHumidityRanges = initializeRange(lines, delimiters[5], delimiters[6]);
        this.humidityToLocationRanges = initializeRange(lines, delimiters[6], delimiters[7]);
    }
    private List<String> getInput() {
        List<String> lines = new ArrayList<String>();
        String line;
        try {
            Scanner sc = new Scanner(new FileInputStream(PATH));
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                if (!line.isEmpty()) {
                    line = line.replaceAll("\\s+map:", "");
                    lines.add(line);
                }
            }
        } catch (Exception ignored) {}

        return lines;
    }
    private long[] initializeSeeds(List<String> lines) {
        String[] tmp = lines.get(0).split("\\s+");
        tmp = Arrays.copyOfRange(tmp, 1, tmp.length);
        return Arrays.stream(tmp).mapToLong(Long::parseLong).toArray();
    }
    private int[] getDelimiters(List<String> lines) {
        int[] delimiters = new int[STRING_DELIMITERS.length + 1];
        int idx = 0;
        for (int i = 0; i < lines.size(); i++) {
            String tmp = lines.get(i);
            if (idx < STRING_DELIMITERS.length && tmp.equals(STRING_DELIMITERS[idx])) {
                delimiters[idx++] = i;
            }
        }
        delimiters[delimiters.length - 1] = lines.size();
        return delimiters;
    }
    private Range[] initializeRange(List<String> lines, int startLine, int endLine) {
        Range[] rangeList = new Range[endLine - startLine - 1];
        for (int i = startLine; i < endLine - 1; i++) {
            String[] tmp = lines.get(i + 1).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            rangeList[i - startLine] = new Range(sourceRangeStart, destinationRangeStart, rangeLength);
        }
        return rangeList;
    }
    private long sourceToDestination(long source, Range[] ranges) {
        for (Range range : ranges) {
            if (range.containsSource(source)) return range.sourceToDestination(source);
        }
        return source;
    }
    public long seedToLocation(long seed) {
        long soil = sourceToDestination(seed, seedToSoilRanges);
        long fertilizer = sourceToDestination(soil, soilToFertilizerRanges);
        long water = sourceToDestination(fertilizer, fertilizerToWaterRanges);
        long light = sourceToDestination(water, waterToLightRanges);
        long temperature = sourceToDestination(light, lightToTemperatureRanges);
        long humidity = sourceToDestination(temperature, temperatureToHumidityRanges);
        long location = sourceToDestination(humidity, humidityToLocationRanges);
        return location;
    }
    public long[] getLocations() {
        long[] locations = new long[seeds.length];
        for (int i = 0; i < locations.length; i++) {
            locations[i] = seedToLocation(seeds[i]);
        }
        return locations;
    }

    public long getMinLocationWithSeedsAsRanges() {
        long[] lowerBounds = new long[seeds.length / 2];
        long[] lengths = new long[seeds.length / 2];
        long[] upperBounds = new long[seeds.length / 2];
        for (int i = 0; i < seeds.length - 1; i += 2) {
            lowerBounds[i / 2] = seeds[i];
            lengths[i / 2] = seeds[i + 1];
            upperBounds[i / 2] = lowerBounds[i / 2] + lengths[i / 2];
        }

        long minLocation = Long.MAX_VALUE;
        ProgressBar pb = new ProgressBar(lowerBounds.length);
        for (int i = 0; i < lowerBounds.length; i++) {
            for (long seed = lowerBounds[i]; seed <= upperBounds[i]; seed++) {
                long location = seedToLocation(seed);
                if (location < minLocation) minLocation = location;
            }
            pb.completeStep();
        }
        pb.end();
        try {
            pb.join();
        } catch (InterruptedException ignored) {}

        return minLocation;
    }
}