# A Text Analysis of Andres Manuel Lopez Obrador’s Speeches

### Check the article here:  <a href="https://medium.com/geekculture/an-text-analysis-of-amlo-speeches-864dbdb15e9a">A Text Analysis of Andres Manuel Lopez Obrador’s Speeches</a>

This repository proposes to analyze the text of the speeches, conferences and interviews of the current president of Mexico, and has an educational aim, there are no purposes of political interest in this document, you are free to interpret the data in your own way. I personally think that formalize this type of practices helps us to follow up on the political promises of the presidents of Latin America and could help us to make decisions in advance for our countries, however, what I intend to do is to show you a basic flow of text analysis using Python, visualize aggregated data and get insight at every step.

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

![image](https://user-images.githubusercontent.com/8701464/133873474-facbdc75-f01a-49e6-b0a9-b4ad7acd2852.png)

## Text Preprocessing
- Convert to lowercase
- Remove extra spaces, carriage change and tabs
- Remove punctuation marks and question marks
- Remove stopwords
- Apply Stemming, Lematización and NER

![image](https://user-images.githubusercontent.com/8701464/133873487-4c2fa009-f57c-4c0f-9b5a-17c205108d28.png)

## Let’s delve into the count of words used by AMLO before and during his presidential term

![image](https://user-images.githubusercontent.com/8701464/133873491-a0d81463-24ac-48f4-b747-88c75215cf28.png)

The code above is used to generate the below visualization, there are three colors separating the chart vertically, which are the three periods of AMLO, He began its campaign in 2011, lost against Peña Nieto in December 2012, and he remained active in the mandate of President Peña Nieto, in 2018 he won the Mexican presidential elections and his number of words used per speech increased, as well as the vocabulary used.

![image](https://user-images.githubusercontent.com/8701464/133873501-f99262db-d1ed-44d1-91bb-21df393f7bb3.png)

## Let’s group by Year and Month and visualize the word clouds for each presidential term
This could help us understand what were his plans and priorities over each period before and while his presidential term

![image](https://user-images.githubusercontent.com/8701464/133873506-b3f12be3-5266-4393-8051-8ee62377e46d.png)

### Before Peña Nieto

![image](https://user-images.githubusercontent.com/8701464/133873514-65b1d5a0-b7c5-46f1-acf2-5bd1f78ad4eb.png)

### Peña Nieto’s presidential term

![image](https://user-images.githubusercontent.com/8701464/133873521-35d1d09e-450b-4c25-b5f1-1e0be03e0ecf.png)

### AMLO’s presidential term until September 2021

![image](https://user-images.githubusercontent.com/8701464/133873533-16268c52-8b95-406e-a4c6-6e2f0d94a7ed.png)

Although there are NLP techniques to detect topics, here we will not use these practices because this study involves political terms that are very common in the political environment of each country, in this case I will choose the topics and terms related to the topics manually

- Economy: gasto, remesas, ahorro, economía, finanzas, inflación, salarios, inversión, impuesto, austeridad
- Political institutions: pan, prd, pri, morena, pt
- General institutions: onu, inm, ine, oms, imss, cfe, cndh, inegi, sep, conacyt, insabi, sat, profeco
- Education: maestros,maestras, estudiante, educación, escuela, universidad, beca, reformaeducativa, libros, escuela, primaria, profesores
- Energetic: energética, aceite, gas, pemex, petróleo, gasolina, combustible
- Migration: migración, extranjeros, frontera, centroamericanos, deportaciones, centroamérica
- Alimentation: hambre, alimentación, canastabásica, comida, alimentos, desnutrición, nutrición, comida, pobreza
- Southern federative entities: campeche, chiapas, quintanaroo, tabasco, veracruz, yucatán
- Central federative entities: cdmx, edomex, guerrero, hidalgo, oaxaca, puebla, querétaro, tlaxcala
- North federal entities: aguascalientes, bajacalifornia, bajacaliforniasur, chihuahua, coahuila, colima, durango, guanajuato, guerrero, jalisco, michoacán, morelos, nayarit, nuevoleón, sanluispotosí, sinaloa, sonora, tamaulipas, zacatecas
- Health: bienestar, salud, médico, camas, vacuna, enfermedad, contagio, infección, pandemia, epidemia, covid, hospital, dosis, doctores, enfermeras, paramédicos, enfermeros, hospitalización
- Corruption: ayotzinapa, justicia, corrupción, extorsión, soborno, desaparición, secuestro, narcotráfico, homicidio, anticorrupción
- Political rivals: zedillo, salinas, peñanieto, anaya, meade, fox, calderon, margarita, videgaray, lozoya, chong, yunes
- Political allies: gordillo, buylla, tclouthier, mclouthier, clouthier, aliados, aliado, ebrard, sheinbaum, monreal, gatell, alcocer, mueller
- International people: trump, obama, biden
- Other problems: 4t, indígenas, avión, tren, huachicol, méxico, pueblo
- Countries: venezuela, chile, colombia, bolivia, argentina, cuba, honduras, nicaragua, canada, panama, españa, francia, alemania, china, rusia

Now we will see the frequency of each word by year into each Topic

![image](https://user-images.githubusercontent.com/8701464/133873558-fa631555-edd3-436c-a3ae-c4b0a89e0b9d.png)

![image](https://user-images.githubusercontent.com/8701464/133873561-9e668eb1-0185-46cf-aafc-893be0cda8f9.png)

![image](https://user-images.githubusercontent.com/8701464/133873567-6592dcb7-e49c-4c6f-ad5c-3c93cb0c852a.png)

![image](https://user-images.githubusercontent.com/8701464/133873571-e4d00b36-e8b7-4e01-bfe1-da3b551d4afb.png)

![image](https://user-images.githubusercontent.com/8701464/133873573-21edd133-094f-4748-8e98-395758fa5808.png)

![image](https://user-images.githubusercontent.com/8701464/133873576-35311bfe-fdc9-4141-a5d5-a5a11e892c48.png)

![image](https://user-images.githubusercontent.com/8701464/133873577-df9a3a6c-4fa6-47d1-b512-bd6a9d07214e.png)

## Funny right? let’s dig into other types of insights, observe the evolution of the frequency over time is very important as well

![image](https://user-images.githubusercontent.com/8701464/133873587-218c3bf4-fcf4-40c2-9dbb-7c4580af192b.png)

![image](https://user-images.githubusercontent.com/8701464/133873591-094f7211-467a-4397-9f8d-e7a80e020f7c.png)

Apparently the use of the word “economía” in his speeches before his presidential term had relevance, but the use of this word is stronger in his current presidential term, also take a look at the word “impuesto”

![image](https://user-images.githubusercontent.com/8701464/133873599-815cf6a8-4c6d-46af-8a82-f693c7825bdb.png)

The most mentioned political party before his presidential term was “Morena”, at the same time he mentioned political parties rivals like “PRD” and “PRI”

![image](https://user-images.githubusercontent.com/8701464/133873602-d404a750-b4f6-47e7-900b-9a8c10cfc72d.png)

CFE , IMSS and CNDH the most mentioned words related to general institutions

![image](https://user-images.githubusercontent.com/8701464/133873606-839c0194-9da6-46e5-b59b-c8a283019914.png)

“educación” has always been a word used since the beginning of his campaign, and now in his presidential term “escuela” is the most relevant word related to education.

![image](https://user-images.githubusercontent.com/8701464/133873612-a35e9f65-4641-4cb8-9a31-9c8db6d76a21.png)

During the first years of Peña Nieto’s mandate, AMLO used the words “petróleo” and “energética” for a large period of time.

![image](https://user-images.githubusercontent.com/8701464/133873617-415bf0a9-60a4-42f8-b194-6e605e4fe689.png)

The word “extranjeros” was common from the beginning of his campaign until today, however, lately “migración” and “frontera” appears stronger

![image](https://user-images.githubusercontent.com/8701464/133873625-39c40a51-4f14-4f94-aa65-49187afd92cb.png)

Veracruz and Tabasco

![image](https://user-images.githubusercontent.com/8701464/133873628-176c4022-3277-4eb4-bcb2-98528d857ead.png)

“CDMX” is the most mentioned area in the center of the country, but there is a spiky rebound in the word “oaxaca” the last months of 2019

![image](https://user-images.githubusercontent.com/8701464/133873643-942b2f84-24ab-4be2-86c8-943b80f1eae8.png)

![image](https://user-images.githubusercontent.com/8701464/133873647-5458d743-b6b7-4907-9f80-05636b1675e9.png)

The words “pobreza” and “alimentación” were very common since the beginning of his presidential campaign, and now both stronger

![image](https://user-images.githubusercontent.com/8701464/133873651-ca931fb8-402d-4a41-8c28-ce6491ae75f2.png)

From the last months of 2020 until today, He’s been using the word “vacuna”, It was his priority.

![image](https://user-images.githubusercontent.com/8701464/133873652-9df59fab-7916-4439-b404-7a97cb8e4c41.png)

“corrupción” is one of his favorite words

![image](https://user-images.githubusercontent.com/8701464/133873657-ca012662-74d1-45b1-9848-68e59184855f.png)

From the beginning of his presidential campaign, “Peña nieto” was the target.

![image](https://user-images.githubusercontent.com/8701464/133873660-e4afb407-c2c7-48d6-9692-6d2a939c4f8e.png)

Since the beginning of his presidential term “ebrard” and “sheinbaum” have been his political allies that he has mentioned the most.

![image](https://user-images.githubusercontent.com/8701464/133873664-d645f1d7-622d-4e3d-b157-eb8dcee2a781.png)

“trump” very relevant and now “biden”, the dates make sense.

![image](https://user-images.githubusercontent.com/8701464/133873666-96dced0b-8a80-4af0-a41b-fd381e8b6ed7.png)

His other favorite word is “pueblo” but it is also wor
