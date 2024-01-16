import random
from time import sleep
from tqdm import tqdm

print("hacking.......")
for i in tqdm(range(100), colour="green"):
    sleep(random.uniform(0.01, 0.2))

print('you are hacked (  *  )')


