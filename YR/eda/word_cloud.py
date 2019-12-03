import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from wordcloud import WordCloud, STOPWORDS


business = pd.read_csv('../business.csv')
filter_city = business['city'].str.contains('Las Vegas')
filter_restaurants = business['categories'].str.contains('Restaurants')
filter_food = business['categories'].str.contains('Food')
print(filter_city)
filter_city = filter_city.fillna(method='ffill')
business = business[filter_city & filter_restaurants &filter_food]


plt.figure(figsize=(12,10))

wordcloud = WordCloud(background_color='white',
                          width=1500,
                      stopwords = STOPWORDS,
                          height=1200
                         ).generate(str(business['name']))


plt.imshow(wordcloud)
plt.axis('off');

plt.savefig('wc.png')