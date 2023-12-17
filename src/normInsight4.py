import yaml
import pandas as pd
import os
from tqdm import tqdm

from textblob import TextBlob
from textblob.sentiments import PatternAnalyzer

dir = os.path.dirname(os.path.abspath(__file__))

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

dataDir = dir + config['data']['dataDir']
plotDir = dataDir + config['data']['plotDir']
normDir = dataDir + config['data']['normDir']

dfTweet = pd.read_csv(normDir + config['data']['normTweet'],low_memory=False)

authorSentScore = {}

for i,row in tqdm(dfTweet.iterrows(),total=dfTweet.shape[0]):
    sentScore = TextBlob(row['content'],analyzer=PatternAnalyzer()).sentiment
    if row['AuthorId'] not in authorSentScore.keys():
        authorSentScore[row['AuthorId']] = {'polarity': 0, 'subjectivity': 0}
    authorSentScore[row['AuthorId']]['polarity'] = (authorSentScore[row['AuthorId']]['polarity'] + sentScore[0])/2
    authorSentScore[row['AuthorId']]['subjectivity'] = (authorSentScore[row['AuthorId']]['subjectivity'] + sentScore[1])/2

df = pd.DataFrame(columns=['AuthorId', 'Polarity','Subjectivity'],dtype=float)

for k,v in tqdm(authorSentScore.items()):
    df.loc[len(df)] = [k,v['polarity'],v['subjectivity']]

df.to_csv(dataDir + config['data']['resultDir'] + '/insight4.csv',index=False)