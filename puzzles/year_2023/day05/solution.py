import os
import re
import time

from .demo import build_maps


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(inputs):
    return {
        "seeds": [int(n) for n in re.findall(r"\d+", inputs[0])],
        "maps": build_maps(inputs[1:]),
    }


def solve_part1(inputs):
    seeds = inputs["seeds"]
    maps = inputs["maps"]

    for ranges in maps:
        new_seeds = []
        for seed in seeds:
            mapping_found = False
            for r in ranges:
                if r["source_range_start"] <= seed <= r["source_range_start"] + r["range_length"]:
                    new_seeds.append(seed + (r["destination_range_start"] - r["source_range_start"]))
                    mapping_found = True
                    break

            if not mapping_found:
                new_seeds.append(seed)
        seeds = new_seeds

    return min(seeds)


def _chunkify(lst):
    chunks = []
    for i in range(0, len(lst), 2):
        chunks.append((lst[i], lst[i] + lst[i + 1]))
    return chunks


def solve_part2(inputs):
    # Extract seeds and maps from inputs
    seeds = inputs["seeds"]
    seed_chunks = _chunkify(seeds)
    maps = inputs["maps"]

    # Process each map
    for map_ranges in maps:
        # Initialize a new list for storing transformed seed chunks
        transformed_seed_chunks = []

        # Process each seed chunk
        while seed_chunks:
            chunk_start, chunk_end = seed_chunks.pop()

            overlap_found = False
            # Process each range in the current map
            for map_range in map_ranges:
                # Calculate the overlap between the seed chunk and the source range
                overlap_start = max(chunk_start, map_range["source_range_start"])
                overlap_end = min(chunk_end, map_range["source_range_start"] + map_range["range_length"])

                # If there is an overlap
                if overlap_start < overlap_end:
                    # Transform the overlap according to the range map and add it to the new list
                    transformed_start = overlap_start + (
                        map_range["destination_range_start"] - map_range["source_range_start"]
                    )
                    transformed_end = overlap_end + (
                        map_range["destination_range_start"] - map_range["source_range_start"]
                    )
                    transformed_seed_chunks.append((transformed_start, transformed_end))

                    # If there are parts of the seed chunk that were not part of the overlap, add them back to the seed chunks for further processing
                    if overlap_start > chunk_start:
                        seed_chunks.append((chunk_start, overlap_start))
                    if overlap_end < chunk_end:
                        seed_chunks.append((overlap_end, chunk_end))

                    overlap_found = True
                    break

            if not overlap_found:
                # If the seed chunk does not overlap with any source range, keep it as is
                transformed_seed_chunks.append((chunk_start, chunk_end))

        # Replace the original seed chunks with the transformed seed chunks for the next iteration
        seed_chunks = transformed_seed_chunks

    # Return the smallest transformed seed after all transformations
    return sorted(seed_chunks)[0][0]


def solve(file_name, part=1):
    inputs = read_input(file_name)
    inputs = parse_input(inputs)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    t = time.perf_counter()
    r = solve("input.txt", part=2)
    print(r)
