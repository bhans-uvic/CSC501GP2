import yaml
import pandas as pd
import os

dir = os.path.dirname(os.path.abspath(__file__))

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

dataDir = dir + config['data']['dataDir']
rawDir = dataDir + config['data']['rawDir']
combinedDfDir = dataDir + config['data']['combinedDfDir']
normDir = dataDir + config['data']['normDir']
plotDir = dataDir + config['data']['plotDir']
resultDir = dataDir + config['data']['resultDir']

if not os.path.exists(dataDir):
    os.makedirs(dataDir) 

if not os.path.exists(rawDir):
    os.makedirs(rawDir)

if not os.path.exists(combinedDfDir):
    os.makedirs(combinedDfDir) 

if not os.path.exists(normDir):
    os.makedirs(normDir)

if not os.path.exists(plotDir):
    os.makedirs(plotDir)

if not os.path.exists(resultDir):
    os.makedirs(resultDir)

mergedDf = None

for f in os.listdir(rawDir):
    df = pd.read_csv(rawDir + '/' + f,low_memory=False)
    print('****************************',f,'****************************')
    print(df.info())
    print(df.describe())
    print('*********************************************************************')
    if mergedDf is None:
        mergedDf = df
    else:
        mergedDf = pd.concat([mergedDf,df],ignore_index=True)

mergedDf.to_csv(dataDir + config['data']['combinedDfDir'] + config['data']['combinedFName'],index=False)

print('****************************MergedDf****************************')
print(mergedDf.info())
print(mergedDf.describe())
print(mergedDf.isnull().sum())
print(mergedDf.account_type.value_counts())
print('*********************************************************************')