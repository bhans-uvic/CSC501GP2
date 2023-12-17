import yaml
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

dir = os.path.dirname(os.path.abspath(__file__))

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

dataDir = dir + config['data']['dataDir']
resDir = dataDir + config['data']['resultDir']
plotDir = dataDir + config['data']['plotDir']

df = pd.read_csv(resDir + '/insight4.csv')

bin_width = 0.1
bins = np.arange(min(df['Polarity']), max(df['Polarity']) + bin_width, bin_width)

plt.figure(figsize=(12, 8))
sns.histplot(data = df,x='Polarity', bins=bins, kde=False,  palette = 'Spectral')  

plt.xlabel('Polarity',labelpad=20,fontsize=14)
plt.ylabel('User Frequency',labelpad=20,fontsize=14)
#plt.title('Insight1',fontsize=20)

plt.xticks(np.arange(-1.1,1.1,0.1))

for i in range(len(bins) - 1):
    count = np.sum((df['Polarity'] >= bins[i]) & (df['Polarity'] <= bins[i+1]))
    plt.text((bins[i] + bins[i + 1]) / 2, count, str(count), ha='center', va='bottom')

sns.despine(top=True)
plt.suptitle('Insight4 Polarity', x=0.8, y=0.8, fontsize=20, ha='right')
plt.savefig(plotDir + '/insight4PolarityHist.png',dpi=300)