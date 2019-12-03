import numpy as np
import pandas as pd

class GeoFilter:
    def __init__(self, city, src_lat, src_lon, dest_lat, dest_lon, diameter=0.5, width=0.3):
        self.city = city.replace(' ', '')
        self.start_lat = src_lat
        self.start_long = src_lon
        self.end_lat = dest_lat
        self.end_long = dest_lon
        self.diameter = diameter
        self.width = width


    def geo_filter(self, row):
        ave_lat = (self.start_lat + self.end_lat) / 2
        mile_long = 1 / (69.172 * np.cos(np.radians(ave_lat)))
        mile_latlong_ave = (1 / 69.172 + mile_long) / 2
        in_range = False
        degree_diameter = self.diameter * mile_latlong_ave
        if (((row['latitude'] - self.start_lat) ** 2 + (row['longitude'] - self.start_long) ** 2 - degree_diameter ** 2) < 0):
            in_range = True
        elif (((row['latitude']- self.end_lat) ** 2 + (row['longitude'] - self.end_long) ** 2 - degree_diameter ** 2) < 0):
            in_range = True
        theta = np.arctan2(self.end_lat - self.start_lat, self.end_long - self.start_long)
        rect_angle = np.pi / 2 - abs(theta)
        degree_width = self.width * mile_latlong_ave
        dx = np.cos(rect_angle) * degree_width
        dy = np.sin(rect_angle) * degree_width
        contour = []
        contour.append([self.start_long + dx, self.start_lat + dy])
        contour.append([self.start_long - dx, self.start_lat - dy])
        contour.append([self.end_long + dx, self.end_lat + dy])
        contour.append([self.end_long - dx, self.end_lat - dy])
        contour_array = np.array(contour)
        contour_array[:, 0] = contour_array[:, 0] - row['longitude']
        contour_array[:, 1] = contour_array[:, 1] - row['latitude']
        contour_flag = contour_array.max(axis=0) * contour_array.min(axis=0)
        if (contour_flag[0] < 0 and contour_flag[1] < 0):
            in_range = True
        return in_range

    def get_best_algorithm(self):
        algos = pd.read_csv(self.city+'-cv-algos.csv')
        return algos['algo'][0]

    def filter_data(self):
        merged_df = pd.read_csv(self.city + '-recommendations-' + self.get_best_algorithm() + '-filtered.csv')
        bools = merged_df.apply(self.geo_filter, axis=1)
        merged_df = merged_df[bools]
        return merged_df

    def filter_by_user(self, user_id):
        filtered = self.filter_data()
        filtered = filtered[filtered['user_id'] == user_id]
        return filtered[['user_id', 'restaurant_id', 'recommended_rating','latitude','longitude']]

def main():
    start_lat = 36.090671
    start_long = -115.179614
    end_lat = 36.131742
    end_long = -115.180300
    diameter = 0.5
    width = 0.3
    gf = GeoFilter('Las Vegas', start_lat, start_long, end_lat, end_long)
    df = gf.filter_by_user('U4INQZOPSUaj8hMjLlZ3KA')
    print(df)

if __name__ == '__main__':
    main()