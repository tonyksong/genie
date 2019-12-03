import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

business = pd.read_csv('../business.csv')
filter_city = business['city'].str.contains('Las Vegas')
print(filter_city)
filter_city = filter_city.fillna(method='ffill')
business = business[filter_city]
print(business['categories'].head())
bcats = business['categories']

bcats = bcats[bcats.apply(type)==str]

business_cats=';'.join(bcats)
print(business_cats)
cats=pd.DataFrame(business_cats.split(';'),columns=['category'])
cats_ser = cats.category.value_counts()


cats_df = pd.DataFrame(cats_ser)
cats_df.reset_index(inplace=True)
print(cats_df)


plt.figure(figsize=(12,12))
f = sns.barplot( x= 'category',y = 'index' , data = cats_df.iloc[0:50])
f.set_ylabel('Category')
f.set_xlabel('Number of businesses');
plt.xticks(rotation=90)
plt.savefig('business_cat.png')