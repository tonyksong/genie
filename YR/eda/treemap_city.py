import squarify
import matplotlib.pyplot as plt
import pandas as pd

business = pd.read_csv('../business.csv')
filter_state = business['state'].str.contains('AZ')

business = business[filter_state]

cities = business.groupby('city')
city_cnt = cities['business_id'].count()
print(city_cnt['Phoenix'])

city_cnt.sort_values(ascending=False,inplace=True)

squarify.plot(sizes= city_cnt[0:15].values, label= city_cnt[0:15].index, alpha=0.9)

plt.axis('off')
plt.tight_layout()
plt.savefig('business_city_treemap_az.png')
plt.clf()

business = pd.read_csv('../business.csv')
filter_state = business['state'].str.contains('NV')

business = business[filter_state]

cities = business.groupby('city')
city_cnt = cities['business_id'].count()
print(city_cnt['Las Vegas'])

city_cnt.sort_values(ascending=False,inplace=True)

squarify.plot(sizes= city_cnt[0:15].values, label= city_cnt[0:15].index, alpha=0.9)

plt.axis('off')
plt.tight_layout()
plt.savefig('business_city_treemap_nv.png')
