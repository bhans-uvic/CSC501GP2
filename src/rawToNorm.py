import yaml
import pandas as pd
import os

dir = os.path.dirname(os.path.abspath(__file__))

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

dataDir = dir + config['data']['dataDir']

df = pd.read_csv(dataDir + config['data']['combinedDfDir'] + config['data']['combinedFName'],low_memory=False)

dfAuthor = pd.DataFrame(columns=['Id','author','following' ,'followers','updates','accountType','accountCategory'])
dfTweet = pd.DataFrame(columns=['Id','content','publishDate' ,'retweet','AuthorId'])

df['publish_date'] = pd.to_datetime(df['publish_date'])
lastTweetDf = df.loc[df.groupby('alt_external_id')['publish_date'].idxmax()]
dfAuthor[['Id','author','following' ,'followers','updates','accountType','accountCategory']] = lastTweetDf[['alt_external_id','author','following' ,'followers','updates','account_type','account_category']]
dfAuthor.to_csv(dataDir + config['data']['normDir'] + config['data']['normAuthor'],index=False)

dfTweet[['Id','content','publishDate' ,'retweet','AuthorId']] = df[['tweet_id','content','publish_date','retweet','alt_external_id']]
dfTweet['publishDate'] = pd.to_datetime(dfTweet['publishDate'])
dfTweet.to_csv(dataDir + config['data']['normDir'] + config['data']['normTweet'],index=False)

for _df,name in [(dfAuthor,'Author'),(dfTweet,'Tweet')]:
    print('\n****************************',name,'***************************************\n')
    print('\t-First 5 Rows')
    print(_df.head())
    print('\t-Info')
    print(_df.info())
    print('\t-Describe')
    print(_df.describe())

print(dfAuthor['Id'].nunique())
print(dfTweet['publishDate'].min(),' to ',dfTweet['publishDate'].max())