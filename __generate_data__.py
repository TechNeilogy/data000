from math import floor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm

np.random.seed()

size = 5000

servers = [
    ['a', 100,  50],
    ['b', 200,  50],
    ['c', 400, 100],
    ['d', 250, 250],
]

loads = [
    [1,    0],
    [2,    0],
    [4,    0],
    [8,   20],
    [16, 100],
]

for server in servers:
    for load in loads:

        mean = server[1] + 5 * load[0]
        std = server[2] + load[1]

        df = pd.DataFrame(
            {
                'y': np.random.normal(mean, std, size),
                's': [server[0]]*size,
                't': [str(load[0])]*size
            }
        ).loc[
            lambda df: df['y'] >= 0.0
        ]

        print(f'{server[0]} {load[0]}: {floor(df["y"].mean())} {floor(df["y"].std())}')

        df.to_csv(
            f'./data/output/{server[0]}/df_{load[0]}.csv',
            index = False
        )
