# Counts total number of Nikon and Fuji raws in photo folder
# https://stackoverflow.com/questions/1320731/count-number-of-files-with-certain-extension-in-python
# original idea

import os
total = 0

for dirpath, dirnames, filenames in os.walk("D:\!!!! Potatoes"):
    for file in filenames:
        if file.endswith(".NEF"):
            total += 1
        elif file.endswith(".RAF"):
            total += 1

print("You have taken")
print(total)
print("photographs")
