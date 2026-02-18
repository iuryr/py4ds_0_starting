from tqdm import tqdm
from time import sleep

from Loading import ft_tqdm

# for elem in tqdm(range(333)):
#     # print("something")
#     sleep(0.5)
# print()

for elem in ft_tqdm(range(333)):
    sleep(0.005)


