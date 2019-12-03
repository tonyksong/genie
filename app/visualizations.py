import requests
import json
import pandas as pd
#from recommender import Recommender
from GeoFilter import GeoFilter

class Visualizations:
    def __init__(self):
        self.api_key = "p5XJewjpIhpiwegBmHG-dETXNCdQst3XaDxu6iubyTvAWjYGrHoVLQxmcIVfTDRVwLkzujm1M8_8Dz2LhKh8etCa3HzwwAdm4zEFWDcDL-ebocrgJzLJZYWHxWu2XXYx"
        self.weekdays = {}
        self.weekdays[0] = 'Monday'
        self.weekdays[1] = 'Tuesday'
        self.weekdays[2] = 'Wednesday'
        self.weekdays[3] = 'Thursday'
        self.weekdays[4] = 'Friday'
        self.weekdays[5] = 'Saturday'
        self.weekdays[6] = 'Sunday'

    def retrieve_data(self, user_id):
        #recommender = Recommender('Las Vegas')
        #recommendations = recommender.recommend(user_id)
        #business_list = recommendations['restaurant_id'].to_list()
        #business_list = business_list[0:3]

        # read user choice
        user_choice = pd.read_csv('user_choice.csv')
        user = user_choice['UserID'][0]
        start_lat = user_choice['Start_Lat'][0]
        start_long = user_choice['Start_Long'][0]
        end_lat = user_choice['End_Lat'][0]
        end_long = user_choice['End_Long'][0]

        # new geofilter added
        recommender = GeoFilter('Las Vegas', start_lat, start_long, end_lat, end_long)
        recommendations = recommender.filter_by_user(user)
        business_list = recommendations['restaurant_id'].to_list()
        business_list = business_list[0:3]

        # Get Business Id for 3 Restaurants
        # business_id = ["SeNOJ2zYHziptxLuiRINLg", "vHz2RLtfUMVRPFmd7VBEHA", "I6EDDi4-Eq_XlFghcDCUhw"]

        headers = {'Authorization': 'Bearer %s' % self.api_key}
        name = list()
        website = list()
        price = list()
        review_count = list()
        stars = list()
        categories = list()
        hours = list()  # nested list of hours
        longitude = list()
        latitude = list()

        for i in range(len(business_list)):
            url = 'https://api.yelp.com/v3/businesses/' + business_list[i]
            req = requests.get(url, headers=headers)
            if req.status_code != 200:
                quit()
            restaurant = json.loads(req.text)

            name.append(restaurant['name'])
            website.append(restaurant['url'])
            price.append(restaurant['price'])
            review_count.append(restaurant['review_count'])
            stars.append(restaurant['rating'])
            categories.append([i['title'] for i in restaurant['categories']])
            # format business hours
            hours_list = restaurant['hours'][0]['open']
            hours_list1 = [[i['day'], i['start'], i['end']] for i in hours_list]
            for v in hours_list1:
                v[0] = self.weekdays[v[0]]
                v[1] = ": " + v[1][:-2] + ':' + v[1][-2:] + " - "
                v[2] = v[2][:-2] + ':' + v[2][-2:]
            hours_list2 = [''.join(i) for i in hours_list1]
            hours.append(hours_list2)  # list of hours
            latitude.append(restaurant['coordinates']['latitude'])
            longitude.append(restaurant['coordinates']['longitude'])
        df1 = pd.DataFrame(list(zip(name, website, price, review_count, stars, categories, hours, latitude, longitude)),
                           columns=['name', 'website', 'price', 'review_count', 'stars', 'categories', 'hours', 'latitude', 'longitude'])
        df1.to_csv(r'data_viz.csv', index=False)
        df1.to_csv(r'./static/data_viz.csv', index=False)

def main():
    vis = Visualizations()
    vis.retrieve_data('U4INQZOPSUaj8hMjLlZ3KA')

if __name__ == '__main__':
    main()
