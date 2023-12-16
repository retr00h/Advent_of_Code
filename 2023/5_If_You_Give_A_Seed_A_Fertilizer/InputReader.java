import java.io.FileInputStream;
import java.util.*;

public class InputReader {

    public static final String PATH = "./2023/5_If_You_Give_A_Seed_A_Fertilizer/input/5_If_You_Give_A_Seed_A_Fertilizer.txt";
    private static final List<String> lines = new ArrayList<String>();
    private static long[] seeds;
    private static final Map<Long, Long> seedsToSoilMap = new HashMap<Long, Long>();
    private static final Map<Long, Long> soilToFertilizerMap = new HashMap<Long, Long>();
    private static final Map<Long, Long> fertilizerToWaterMap = new HashMap<Long, Long>();
    private static final Map<Long, Long> waterToLightMap = new HashMap<Long, Long>();
    private static final Map<Long, Long> lightToTemperatureMap = new HashMap<Long, Long>();
    private static final Map<Long, Long> temperatureToHumidityMap = new HashMap<Long, Long>();
    private static final Map<Long, Long> humidityToLocationMap = new HashMap<Long, Long>();
    public static List<String> getInput() {
        if (lines.isEmpty()) {
            String line;
            try {
                Scanner sc = new Scanner(new FileInputStream(PATH));
                while (sc.hasNextLine()) {
                    line = sc.nextLine();
                    if (!line.isEmpty()) {
                        lines.add(line);
                    }
                }
            } catch (Exception ignored) {}
        }
        return lines;
    }
    public static long[] getSeeds() {
        if (lines.isEmpty()) getInput();
        if (seeds == null) {
            String[] tmp = lines.get(0).split("\\s+");
            tmp = Arrays.copyOfRange(tmp, 1, tmp.length);
            seeds = Arrays.stream(tmp).mapToLong(Long::parseLong).toArray();
        }
        return seeds;
    }
    public static Map<Long, Long> getSeedsToSoilMap() {
        if (seeds == null) getSeeds();
        if (seedsToSoilMap.isEmpty()) {
            int idx = 0;
            while (!lines.get(idx++).equals("seed-to-soil map:"));
            while(!lines.get(idx).equals("soil-to-fertilizer map:")) {
                String[] tmp = lines.get(idx).split("\\s+");
                long destinationRangeStart = Long.parseLong(tmp[0]);
                long sourceRangeStart = Long.parseLong(tmp[1]);
                long rangeLength = Long.parseLong(tmp[2]);
                for (long i = 0; i < rangeLength; i++) {
                    seedsToSoilMap.put(sourceRangeStart + i, destinationRangeStart + i);
                }
                idx++;
            }
        }
        return seedsToSoilMap;
    }
    public static long getSeedToSoil(long seed) {
        if (seedsToSoilMap.isEmpty()) getSeedsToSoilMap();
        if (!seedsToSoilMap.containsKey(seed)) return seed;
        return seedsToSoilMap.get(seed);
    }
    public static Map<Long, Long> getSoilToFertilizerMap() {
        if (seedsToSoilMap.isEmpty()) getSeedsToSoilMap();
        int idx = 0;
        while (!lines.get(idx++).equals("soil-to-fertilizer map:"));
        while(!lines.get(idx).equals("fertilizer-to-water map:")) {
            String[] tmp = lines.get(idx).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            for (long i = 0; i < rangeLength; i++) {
                soilToFertilizerMap.put(sourceRangeStart + i, destinationRangeStart + i);
            }
            idx++;
        }
        return soilToFertilizerMap;
    }
    public static long getSoilToFertilizer(long soil) {
        if (soilToFertilizerMap.isEmpty()) getSoilToFertilizerMap();
        if (!soilToFertilizerMap.containsKey(soil)) return soil;
        return soilToFertilizerMap.get(soil);
    }
    public static Map<Long, Long> getFertilizerToWaterMap() {
        if (soilToFertilizerMap.isEmpty()) getSoilToFertilizerMap();
        int idx = 0;
        while (!lines.get(idx++).equals("fertilizer-to-water map:"));
        while (!lines.get(idx).equals("water-to-light map:")) {
            String[] tmp = lines.get(idx).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            for (long i = 0; i < rangeLength; i++) {
                fertilizerToWaterMap.put(sourceRangeStart + i, destinationRangeStart + i);
            }
            idx++;
        }
        return fertilizerToWaterMap;
    }
    public static long getFertilizerToWater(long fertilizer) {
        if (fertilizerToWaterMap.isEmpty()) getFertilizerToWaterMap();
        if (!fertilizerToWaterMap.containsKey(fertilizer)) return fertilizer;
        return fertilizerToWaterMap.get(fertilizer);
    }
    public static Map<Long, Long> getWaterToLightMap() {
        if (fertilizerToWaterMap.isEmpty()) getFertilizerToWaterMap();
        int idx = 0;
        while (!lines.get(idx++).equals("water-to-light map:"));
        while (!lines.get(idx).equals("light-to-temperature map:")) {
            String[] tmp = lines.get(idx).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            for (long i = 0; i < rangeLength; i++) {
                waterToLightMap.put(sourceRangeStart + i, destinationRangeStart + i);
            }
            idx++;
        }
        return waterToLightMap;
    }
    public static long getWaterToLight(long water) {
        if (waterToLightMap.isEmpty()) getWaterToLightMap();
        if (!waterToLightMap.containsKey(water)) return water;
        return waterToLightMap.get(water);
    }
    public static Map<Long, Long> getLightToTemperatureMap() {
        if (waterToLightMap.isEmpty()) getWaterToLightMap();
        int idx = 0;
        while (!lines.get(idx++).equals("light-to-temperature map:"));
        while (!lines.get(idx).equals("temperature-to-humidity map:")) {
            String[] tmp = lines.get(idx).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            for (long i = 0; i < rangeLength; i++) {
                lightToTemperatureMap.put(sourceRangeStart + i, destinationRangeStart + i);
            }
            idx++;
        }
        return lightToTemperatureMap;
    }
    public static long getLightToTemperature(long light) {
        if (lightToTemperatureMap.isEmpty()) getLightToTemperatureMap();
        if (!lightToTemperatureMap.containsKey(light)) return light;
        return lightToTemperatureMap.get(light);
    }
    public static Map<Long, Long> getTemperatureToHumidityMap() {
        if (lightToTemperatureMap.isEmpty()) getLightToTemperatureMap();
        int idx = 0;
        while (!lines.get(idx++).equals("temperature-to-humidity map:"));
        while (!lines.get(idx).equals("humidity-to-location map:")) {
            String[] tmp = lines.get(idx).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            for (long i = 0; i < rangeLength; i++) {
                temperatureToHumidityMap.put(sourceRangeStart + i, destinationRangeStart + i);
            }
            idx++;
        }
        return temperatureToHumidityMap;
    }
    public static long getTemperatureToHumidity(long temperature) {
        if (temperatureToHumidityMap.isEmpty()) getTemperatureToHumidityMap();
        if (!temperatureToHumidityMap.containsKey(temperature)) return temperature;
        return temperatureToHumidityMap.get(temperature);
    }
    public static Map<Long, Long> getHumidityToLocationMap() {
        if (temperatureToHumidityMap.isEmpty()) getTemperatureToHumidityMap();
        int idx = 0;
        while (!lines.get(idx++).equals("humidity-to-location map:"));
        while (idx < lines.size()) {
            String[] tmp = lines.get(idx).split("\\s+");
            long destinationRangeStart = Long.parseLong(tmp[0]);
            long sourceRangeStart = Long.parseLong(tmp[1]);
            long rangeLength = Long.parseLong(tmp[2]);
            for (long i = 0; i < rangeLength; i++) {
                humidityToLocationMap.put(sourceRangeStart + i, destinationRangeStart + i);
            }
            idx++;
        }
        return humidityToLocationMap;
    }
    public static long getHumidityToLocation(long humidity) {
        if (humidityToLocationMap.isEmpty()) getHumidityToLocationMap();
        if (!humidityToLocationMap.containsKey(humidity)) return humidity;
        return humidityToLocationMap.get(humidity);
    }

    public static long getSeedToLocation(long seed) {
        long soil = getSeedToSoil(seed);
        long fertilizer = getSoilToFertilizer(soil);
        long water = getFertilizerToWater(fertilizer);
        long light = getWaterToLight(water);
        long temperature = getLightToTemperature(light);
        long humidity = getTemperatureToHumidity(temperature);
        return getHumidityToLocation(humidity);
    }
}