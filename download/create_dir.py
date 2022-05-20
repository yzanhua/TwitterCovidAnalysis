import os

for i in range(48):
    os.makedirs("data/seg{:02d}".format(i))
