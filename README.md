<h1>CSC 501: Data Models and Algorithms</h1>
<h2>Group Project 2</h2>
</br>
<h3>Introduction</h3>
<p>An exploratory Data Analysis of the Influence and Engagement of Twitter(now X) feeds from a Russian "troll factory," the Internet Research Agency (IRA), that alleged to have deliberately sought to sow political discontent in the US with inflammatory social media content that may have affected the 2016 US presidential election.</p>
</br>
<h3>Data Source</h3>
<a href="https://github.com/fivethirtyeight/russian-troll-tweet">Data</a>
</br>
<h3>Pre-requisites</h3>
<ul>
<li>Python 3.10 or greater</li>
<li>pip as python package manager</li>
</ul>
<h3>Installation</h3>
<ul>
<li>Open terminal and Run `pip install virtualenv` (if you don't already have virtualenv installed)</li>
<li>Create virtualenv groupproject2 by running `python -m virtualenv groupproject2`</li>
<li>`cd /groupproject2`</li>
<li>Clone the repo to your virtualenv folder</li>
<li>Run `source Scripts/activate`</li>
<li>Run `pip install -r requirements.txt`</li>
<li>Run `cd /src`</li>
<li>Run `mkdir data`</li>
<li>Run `cd /data`</li>
<li>Run `mkdir raw`</li>
<li>Copy the data from source above to the /src/data/raw/ dirctory</li>
<li>`cd ..`</li>
</ul>
</br>
<h3>Execute</h3>
<ul>
<li>Execute `python merge.py`</li>
<li>To create normalized tables Execute `python rawToNorm.py`</li>
<li>To get Insight1 Execute `python normInsight1.py`</li>
<li>To get Insight2 Execute `python normInsight2.py`</li>
<li>To get Insight3 Execute `python normInsight3.py`</li>
<li>To get Insight4 Execute `python normInsight4.py`</li>
<li>To get Visual plots for Insight4 Execute `python insight4Visualize.py`</li>
</ul>
</br>
<h3>Contributors</h3>
<ul>
<li>Bhan Singh</li>
<li>Anuinder Sekhon</li>
<li>Vatsala Arora</li>
<li>Mohit Kaushik</li>
<li>Jitendra Palaparty</li>
</ul>
