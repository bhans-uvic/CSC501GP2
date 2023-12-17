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

dfTweet = pd.read_csv(normDir + config['data']['normTweet'],low_memory=False)

dfTweet['publishDate'] = pd.to_datetime(dfTweet['publishDate'])

# Extract year, month, day, and hour
dfTweet['Year'] = dfTweet['publishDate'].dt.year
dfTweet['Month'] = dfTweet['publishDate'].dt.month
dfTweet['Day'] = dfTweet['publishDate'].dt.day
dfTweet['Hour'] = dfTweet['publishDate'].dt.hour
dfTweet['Date'] = dfTweet['publishDate'].dt.date

# Calculate yearly tweet count
yearly_tweet_count = dfTweet['Year'].value_counts().sort_index()

# Most frequent day, hour, and month
most_frequent_day = dfTweet['Day'].mode().values[0]
most_frequent_hour = dfTweet['Hour'].mode().values[0]
most_frequent_month = dfTweet['Month'].mode().values[0]
most_frequent_date = dfTweet['Date'].mode().values[0]

print("Yearly Tweet Count:")
print(yearly_tweet_count)
print("\nMost Frequent Day for Publishing:", most_frequent_day)
print("Most Frequent Hour for Publishing:", most_frequent_hour)
print("Most Frequent Month for Publishing:", most_frequent_month)
print("Most Frequent Date for Publishing Tweets:", most_frequent_date)

plt.figure(figsize=(10, 6))
ax = sns.countplot(data=dfTweet, x='Year')
plt.title('Yearly Tweet Count')
plt.xlabel('Year')
plt.ylabel('Tweet Count')

# Annotate counts on each bar
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', xytext=(0, 5), textcoords='offset points')

sns.despine()

plt.tight_layout(pad=3.0)

plt.savefig(plotDir + '/Insight3Countplot.png',dpi=300)