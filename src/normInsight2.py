import yaml
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dir = os.path.dirname(os.path.abspath(__file__))

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

dataDir = dir + config['data']['dataDir']
plotDir = dataDir + config['data']['plotDir']
normDir = dataDir + config['data']['normDir']

dfAuthor = pd.read_csv(normDir + config['data']['normAuthor'])
dfAuthor['Id'] = dfAuthor['Id'].astype('object')
dfTweet = pd.read_csv(normDir + config['data']['normTweet'],low_memory=False)
dfTweet['AuthorId'] = dfTweet['AuthorId'].astype('object')

accountTypeCount = dfAuthor.accountType.value_counts()
print(accountTypeCount)

mergedDf = pd.merge(dfTweet,dfAuthor,left_on='AuthorId',right_on='Id',how='inner')
groupedDf = mergedDf.groupby('accountType')['retweet'].sum().reset_index()
groupedDf['authors'] = groupedDf['accountType'].map(accountTypeCount)
    
print(groupedDf.head)
print(groupedDf.info())
print(groupedDf.describe())

groupedDf.to_csv(dataDir + config['data']['resultDir'] + '/insight2.csv',index=False)

accTypeGroups = [list(groupedDf['accountType'].unique())[i:i + 5] for i in range(0, 19, 5)]
barWidth = 0.35
barOffsets = np.arange(len(accTypeGroups)) * (2 * barWidth + 0.5)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes = axes.flatten()

for idx, accountTypes in enumerate(accTypeGroups):
    filteredDf = groupedDf[groupedDf['accountType'].isin(accountTypes)]
    
    combined_df = filteredDf.melt(id_vars='accountType', value_vars=['authors', 'retweet'], var_name='Metric', value_name='Count')

    sns.barplot(x='accountType', y='Count', hue='Metric', data=combined_df,
                ax=axes[idx], estimator=sum, palette='Set2', alpha=0.7, saturation=0.8, order=accountTypes)

    for p in axes[idx].patches:
        x = p.get_x() + p.get_width() / 2.
        
        y = p.get_height()
        axes[idx].annotate(f'{y:.0f}', (x, y), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points', fontsize=8)

    axes[idx].set_xlabel('Account Types')
    axes[idx].set_ylabel('Count')
    axes[idx].legend()

    axes[idx].tick_params(axis='x', which='major', pad=10)
    axes[idx].tick_params(axis='y', which='major', pad=8)
    
    sns.despine()

plt.subplots_adjust(wspace=0.4, hspace=0.5)
plt.tight_layout(pad=3.0)
plt.savefig(plotDir + '/Insight2Barplot.png',dpi=300)



