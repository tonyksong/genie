import numpy as np
import pandas as pd
import json

import time



class PrepareData:
    def __init__(self, filters):
        self.filters = filters

    def extract_business_data(self, filters):
        business = pd.read_csv('business.csv')
        filter_city = business['city'].str.contains(filters['city'])
        filter_restaurants = business['categories'].str.contains('Restaurants')
        filter_food = business['categories'].str.contains('Food')
        food_restaurants_city = business[filter_city & filter_restaurants & filter_food]
        food_restaurants_city.to_csv(self.filters['city'].replace(' ','')+'-restaurant.csv')
        return food_restaurants_city

    def extract_business_list(self, city):
        food_restaurants_city = pd.read_csv(city+'-restaurant.csv')
        business_list = food_restaurants_city['business_id'].tolist()
        return business_list

    def reduce_review_data(self, business_list, city):
        reviews_df = pd.read_csv('review.csv')
        reviews_df.dropna(subset=['business_id', 'user_id'], how='any', inplace=True)
        reviews_df = reviews_df[reviews_df['business_id'].isin(business_list)]
        reviews_df = reviews_df[reviews_df.groupby('user_id').user_id.transform(len) > 1]
        reviews_df.to_csv(city+'-reviews-business.csv')
        return reviews_df

    def extract_user_list(self, city):
        reviews_df = pd.read_csv(city+'-reviews-business.csv')
        return reviews_df['user_id'].tolist()

    def reduce_user_data(self,user_list, city):
        user_df = pd.read_csv('user.csv')
        user_df.dropna(subset=['user_id'], how='any', inplace=True)
        user_df = user_df[user_df['user_id'].isin(user_list)]
        user_df.to_csv(city + '-users-business.csv')
        return user_df

    def merge_reviews_user_business(self, city):
        reviews_df = pd.read_csv(city + '-reviews-business.csv')
        user_filtered = pd.read_csv(city + '-users-business.csv')
        reviews_user_df = pd.merge(reviews_df, user_filtered, how='inner', on='user_id')
        reviews_user_df_keys = reviews_user_df[['user_id', 'review_id', 'business_id', 'stars']]
        reviews_user_df_keys.to_csv(city+'-reviews-user-business.csv')
        return reviews_user_df_keys

    def process_data(self):
        self.extract_business_data(self.filters)
        business_list = self.extract_business_list(self.filters['city'].replace(' ', ''))
        self.reduce_review_data(business_list, self.filters['city'].replace(' ', ''))
        user_list = self.extract_user_list(self.filters['city'].replace(' ', ''))
        self.reduce_user_data(user_list, self.filters['city'].replace(' ', ''))
        self.merge_reviews_user_business(self.filters['city'].replace(' ', ''))


def main():
    filters = {'city': 'Las Vegas'}
    prep = PrepareData(filters)
    start = time.time()
    prep.process_data()
    end = time.time()

    print("Time Taken for total processing of data :: "+str(end-start))

if __name__ == '__main__':
    main()


