def parse_map(map_lines):
    result = []
    for line in map_lines:
        if (
            line.strip()
            and not line.startswith("seed-to-soil map:")
            and not line.startswith("soil-to-fertilizer map:")
            and not line.startswith("fertilizer-to-water map:")
        ):
            destination_range_start, source_range_start, range_length = [int(value) for value in line.split()]
            result.append(
                {
                    "destination_range_start": destination_range_start,
                    "source_range_start": source_range_start,
                    "range_length": range_length,
                }
            )
    return result


def build_maps(lines):
    seed_to_soil_start = lines.index("seed-to-soil map:") + 1
    soil_to_fertilizer_start = lines.index("soil-to-fertilizer map:") + 1
    fertilizer_to_water_start = lines.index("fertilizer-to-water map:") + 1
    water_to_light_start = lines.index("water-to-light map:") + 1
    light_to_temperature_start = lines.index("light-to-temperature map:") + 1
    temperature_to_humidity_start = lines.index("temperature-to-humidity map:") + 1
    humidity_to_location_start = lines.index("humidity-to-location map:") + 1
    seed_to_soil_map = parse_map(lines[seed_to_soil_start : soil_to_fertilizer_start - 1])
    soil_to_fertilizer_map = parse_map(lines[soil_to_fertilizer_start : fertilizer_to_water_start - 1])
    fertilizer_to_water_map = parse_map(lines[fertilizer_to_water_start : water_to_light_start - 1])
    water_to_light_map = parse_map(lines[water_to_light_start : light_to_temperature_start - 1])
    light_to_temperature_map = parse_map(lines[light_to_temperature_start : temperature_to_humidity_start - 1])
    temperature_to_humidity_map = parse_map(lines[temperature_to_humidity_start : humidity_to_location_start - 1])
    humidity_to_location_map = parse_map(lines[humidity_to_location_start:])

    return [
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
    ]
