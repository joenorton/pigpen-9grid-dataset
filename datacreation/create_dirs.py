import os

for each_directory in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA']:
    os.makedirs("train/" + each_directory)
    os.makedirs("test/" + each_directory)
    os.makedirs("validation/" + each_directory)