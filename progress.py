import random

from rich.progress import track
from time import sleep

def do_step(step):
    sleep(random.uniform(0.01, 0.2))

for step in track(range(100), description="loading my preasure..."):
    do_step(step)