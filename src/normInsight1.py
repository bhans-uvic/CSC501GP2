import yaml
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

dir = os.path.dirname(os.path.abspath(__file__))

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

dataDir = dir + config['data']['dataDir']
plotDir = dataDir + config['data']['plotDir']
normDir = dataDir + config['data']['normDir']

dfAuthor = pd.read_csv(normDir + config['data']['normAuthor'])
print(dfAuthor[['followers','updates']].describe())
correlation = dfAuthor['updates'].corr(dfAuthor['followers'])
print(f"Correlation between updates and followers: {correlation}")

plt.figure(figsize=(12, 8))
sns.scatterplot(x='followers', y='updates', data=dfAuthor)
sns.despine()

plt.ylabel('Updates',labelpad=20,fontsize=14)
plt.xlabel('Followers',labelpad=20,fontsize=14)

plt.suptitle('Scatter Plot of Updates vs Followers', x=0.9, y=0.8, fontsize=20, ha='right')
plt.savefig(plotDir + '/insight1Scatter.png',dpi=300)
