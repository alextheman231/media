def get_ranges(text: list[str]) -> list[tuple[int, int]]:
    block_sizes = [len(block.split("\n")) for block in text]

    ranges = []
    start = 0

    for size in block_sizes:
        ranges.append((start, start + size))
        start += size

    return ranges
