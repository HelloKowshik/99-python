def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - (3600 * hours) - (60 * minutes)
    return hours, minutes, remaining_seconds


h1, m1, s1 = convert_seconds(5000)
# print(h1, m1, s1)


def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    print(f"file: {filesize} - full: {full_blocks} - partial:{partial_block_remainder}")
    if partial_block_remainder > 0:
        return block_size * (full_blocks + 1)
    return filesize


# print(calculate_storage(1))     # Should be 4096
# print(calculate_storage(4096))  # Should be 4096
# print(calculate_storage(4097))  # Should be 8192
# print(calculate_storage(6000))  # Should be 8192
# print(calculate_storage(8192))
# print(calculate_storage(8193))
print("big" > "small")
