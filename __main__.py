import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# matplotlib.use("TkAgg")

from data_generator import DataGenerator


test_file = 'test0.csv'

DataGenerator().generate_data(
    test_file,
    10000
)

df = pd.read_csv(
    test_file,
    parse_dates=['timestamp']
)

df['log_d'] = np.log10(df['duration'])
max_d = np.max(df['log_d'])

bins = [-np.inf]
bin_labels = []

p = 1
p0 = 0
for r in range(32):
    bins.append(p)
    bin_labels.append(f'2^{p0}')
    p0 += 1
    p *= 2

bins.append(np.inf)
bin_labels.append('max')

df['bin'] = pd.cut(
    df['size'], 
    bins=bins, 
    labels=bin_labels, 
    right=False, 
    include_lowest=True
)

dfs = []
dfs_labels = ['']

for bin_label in bin_labels:
    df0 = df.loc[lambda df: df['bin'] == bin_label]
    if len(df0) > 0:
        dfs.append(df0['log_d'])
        dfs_labels.append(bin_label)

# print(dfs) 

# fig = plt.figure(1, figsize=(5, 5))
# fig.patch.set_facecolor((0.1, 0.1, 0.1, 1))

# ax = df.plot.scatter(
#     x='size',
#     y='duration',
#     c=[[0,0,0,0.2]],
#     s=2
# )

#plt.show()

# plt.savefig('/home/neil/clients/tno/dev/python/datamanip/datamanip000/scatter.png')

fig, ax = plt.subplots()
ax.box(dfs)

ax.set_title('Duration x Size')
ax.set_xlabel('Size')
ax.set_ylabel('log10 Duration')
ax.set_xticks(np.arange(0,len(dfs_labels),1), minor=False, fontsize=6)
ax.set_xticklabels(dfs_labels, fontsize=6)
ax.set_yticks(np.arange(1,max_d,1), minor=False, fontsize=6)

# plt.show()

plt.savefig('/home/neil/clients/tno/dev/python/datamanip/datamanip000/violin.png')