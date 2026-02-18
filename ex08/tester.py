from tqdm import tqdm
from time import sleep

from Loading import ft_tqdm

for elem in ft_tqdm(range(333, 0, -1)):
    sleep(0.005)
print()

for elem in tqdm(range(333,0, -1)):
    # print("something")
    sleep(0.005)
print()



