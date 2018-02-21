import numpy as np
import matplotlib.pyplot as plt
import pandas
from wordcloud import WordCloud
from wordcloud import STOPWORDS

df = pandas.read_csv('references-with-keywords.csv')
print list(df)
yearseries = df['Year'].value_counts().sort_index() #Pandas series, count different values in columns, and sorts by key

plt.figure()
figYears = yearseries.plot(kind='line')
figYears.set_xlabel("Year")
figYears.set_ylabel("Publications")
plt.show()

plt.figure()
typeseries = df['Document Type'].value_counts()
figType = typeseries.plot(kind='pie')
plt.show()


text  = ""
for index, row in df.iterrows():
	#print row['Index Keywords']
	text = text+" "+str(row['Index Keywords'])


wordcloud = WordCloud(max_font_size=40, background_color="white", max_words=100,stopwords=STOPWORDS.add("nan")).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()



