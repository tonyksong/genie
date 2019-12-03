import requests
import json
import pandas as pd

# Get Business Id for 3 Restaurants
business_id = ["SeNOJ2zYHziptxLuiRINLg", "vHz2RLtfUMVRPFmd7VBEHA", "I6EDDi4-Eq_XlFghcDCUhw"]

api_key = "pkk5Sz8_qW3g-mVypkri-SLHO2wQQcezChwildvqoZ0Z99RfMmF9xGQgL4OwuKqkmXFqdrkzP4LlR03wbq6h4YNEAZKwSY9ntrsfONCj67FVAvzTFdOFkXNf9OjMXXYx"

def create_viz_csv(business_id, api_key):
    headers = {'Authorization': 'Bearer %s' % api_key}
    name = list()
    website = list()
    price = list()
    review_count = list()
    stars = list()
    categories = list()
    hours = list()  # nested list of hours

    for i in range(len(business_id)):
        # ******************************** Read Business Information ********************************
        url = 'https://api.yelp.com/v3/businesses/' + business_id[i]
        req = requests.get(url, headers=headers)

        # proceed only if the status code is 200
        if req.status_code != 200:
            quit()

        # extract restaurant information from the response
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
        def dayNameFromWeekday(weekday):
            if weekday == 0:
                return "Monday"
            if weekday == 1:
                return "Tuesday"
            if weekday == 2:
                return "Wednesday"
            if weekday == 3:
                return "Thursday"
            if weekday == 4:
                return "Friday"
            if weekday == 5:
                return "Saturday"
            if weekday == 6:
                return "Sunday"
        for v in hours_list1:
            v[0] = dayNameFromWeekday(v[0])
            v[1] = ": " + v[1][:-2] + ':' + v[1][-2:] + " - "
            v[2] = v[2][:-2] + ':' + v[2][-2:]
        hours_list2 = [''.join(i) for i in hours_list1]
        hours.append(hours_list2)   # list of hours

    df1 = pd.DataFrame(list(zip(name, website, price, review_count, stars, categories, hours)),
                       columns =['name', 'website', 'price', 'review_count', 'stars', 'categories', 'hours'])
    df1.to_csv(r'data_viz.csv', index=False)


create_viz_csv(business_id, api_key)
