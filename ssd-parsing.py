import numpy as np

ssd_file = 'gw_test_parse.ssd'
raw_output = 'output_bytes.txt'
output_utf8 = 'output_utf8.txt'

# Read data in from the .ssd file
with open(ssd_file, 'rb') as file:
    data_bytes = file.read()
    raw_from_file = np.frombuffer(data_bytes, dtype=np.int8)

print(raw_from_file)
print(len(raw_from_file))

# Save the raw bytes to a .txt file
with open(raw_output, 'w') as file:
    file.write(str(data_bytes))

# Decode the .ssd data
data_u = str(raw_from_file)[2:-1]
# print(data_u)
print(f'.ssd file length in bytes: {len(raw_from_file)}')

sector_input = raw_from_file  # make a copy
sec_size = 256  # bytes per sector
secs_track = 10  # sectors per track
sectors = [raw_from_file[sec_size * i:sec_size * (i + 1)] for i in range(secs_track)]
cat_blocks = [np.split(sectors[i], int(sec_size / 8)) for i in range(2)]

print(f'Number of sectors: {len(sectors)}')
print(f'Number of bytes in total: {len(raw_from_file)}\n')

vol_title_1 = cat_blocks[0][0]
vol_title_2 = cat_blocks[1][0][0:4]
vol_title = np.concatenate((vol_title_1, vol_title_2), axis=0)

# Properties stored on Sector 1
cycle_num = sectors[1][4]  # TODO convert from BCD to decimal
print(cycle_num)

print(len(cat_blocks))

# Save the decoded output to a .txt file
with open(output_utf8, 'w') as file:
    file.write(data_u)

