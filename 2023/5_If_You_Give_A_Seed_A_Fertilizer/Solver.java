import java.io.FileInputStream;
import java.util.*;

public class Solver {
    private enum RangeEnum {
        SEED_TO_SOIL, SOIL_TO_FERTILIZER, FERTILIZER_TO_WATER, WATER_TO_LIGHT, LIGHT_TO_TEMPERATURE,
        TEMPERATURE_TO_HUMIDITY, HUMIDITY_TO_LOCATION
    }
    private static final String PATH = "./2023/5_If_You_Give_A_Seed_A_Fertilizer/input/5_If_You_Give_A_Seed_A_Fertilizer.txt";
    private static final String[] STRING_DELIMITERS = {"seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
            "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"};
    private final long[] seeds;
    private final Range seedToSoilRange;
    private final Range soilToFertilizerRange;
    private final Range fertilizerToWaterRange;
    private final Range waterToLightRange;
    private final Range lightToTemperatureRange;
    private final Range temperatureToHumidityRange;
    private final Range humidityToLocationRange;
    public Solver() {
        List<String> lines = getInput();
        this.seeds = initializeSeeds(lines);
        int[] delimiters = getDelimiters(lines);
        this.seedToSoilRange = initializeRange(lines, delimiters[0], delimiters[1]);
        this.soilToFertilizerRange = initializeRange(lines, delimiters[1], delimiters[2]);
        this.fertilizerToWaterRange = initializeRange(lines, delimiters[2], delimiters[3]);
        this.waterToLightRange = initializeRange(lines, delimiters[3], delimiters[4]);
        this.lightToTemperatureRange = initializeRange(lines, delimiters[4], delimiters[5]);
        this.temperatureToHumidityRange = initializeRange(lines, delimiters[5], delimiters[6]);
        this.humidityToLocationRange = initializeRange(lines, delimiters[6], delimiters[7]);
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
    private Range initializeRange(List<String> lines, int startLine, int endLine) {
        Range[] rangeList = new Range[endLine - startLine - 1];
        for (int i = startLine; i < endLine - 1; i++) {
            String[] tmp = lines.get(i + 1).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            rangeList[i - startLine] = new Range(sourceRangeStart, destinationRangeStart, rangeLength);
        }
        return Range.merge(rangeList);
    }
    private long seedToSoil(long seed) {
        return seedToSoilRange.sourceToDestination(seed);
    }
    private long soilToFertilizer(long soil) {
        return soilToFertilizerRange.sourceToDestination(soil);
    }
    private long fertilizerToWater(long fertilizer) {
        return fertilizerToWaterRange.sourceToDestination(fertilizer);
    }
    private long waterToLight(long water) {
        return waterToLightRange.sourceToDestination(water);
    }
    private long lightToTemperature(long light) {
        return lightToTemperatureRange.sourceToDestination(light);
    }
    private long temperatureToHumidity(long temperature) {
        return temperatureToHumidityRange.sourceToDestination(temperature);
    }
    private long humidityToLocation(long humidity) {
        return humidityToLocationRange.sourceToDestination(humidity);
    }
    public long seedToLocation(long seed) {
        long soil = seedToSoil(seed);
        long fertilizer = soilToFertilizer(soil);
        long water = fertilizerToWater(fertilizer);
        long light = waterToLight(water);
        long temperature = lightToTemperature(light);
        long humidity = temperatureToHumidity(temperature);
        long location = humidityToLocation(humidity);
        return location;
    }
    public long[] getLocations() {
        long[] locations = new long[seeds.length];
        for (int i = 0; i < locations.length; i++) {
            locations[i] = seedToLocation(seeds[i]);
        }
        return locations;
    }
}