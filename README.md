# An Text Analysis of Andres Manuel Lopez Obrador’s Speeches

This repository proposes to analyze the text of the speeches, conferences and interviews of the current president of Mexico, and has an educational aim, there are no purposes of political interest in this document, you are free to interpret the data in your own way. I personally think that formalize this type of practices helps us to follow up on the political promises of the presidents of Latin America and could help us to make decisions in advance for our countries, however, what I intend to do is to show you a basic flow of text analysis using Python, visualize aggregated data and get insight at every step. Enjoy it.

![image](https://user-images.githubusercontent.com/8701464/133873297-7d7d7a2d-27db-4f51-8a44-218dd8a457b1.png)

# Data source

The official AMLO website has a stenographic version of each speech, It is the punctual and faithful transcription about what was expressed verbally, we will take this URL for the experiments.

https://lopezobrador.org.mx/

# Web scraping with Python

Today AMLO’s site is grouping the speeches into 667sections, and this number grows weekly, each section has a group of speeches by date, my scrapping technique is targeting each element of a group, which represents the speech, check the image below:

![image](https://user-images.githubusercontent.com/8701464/133873399-d09562a9-9356-4d78-b598-9afe2987f589.png)

![image](https://user-images.githubusercontent.com/8701464/133873404-343d836b-337c-46af-a585-67659ee67c0b.png)

# Let’s start looking for insight
**The amlo_analysis.ipynb** notebook contains all the analysis code, here we will explain each step taken and interpretation of each visualization.


## Reading the .csv file generated in the previous step
Here we can see the speeches described for each box of each url with its dates, and this is what I want.

 ```python
 df = pd.read_csv('C:/Users/ramse/Downloads/amlo_speechs.csv')
columns = ['id_speech', 'date','title','url','content']
df = df[columns]
df['content'] = df['title'] + ' ' +  df['content']
df = df[df['content'].notna()]
df
```








