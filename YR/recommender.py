
import pandas as pd
from surprise import Reader, Dataset
from surprise.model_selection import train_test_split

from BaseLineALS import BaseLineALS
from BaseLineSGD import BaseLineSGD
from CoClusteringMatrixFactorization import CoClusteringMatrixFactorization
from CrossValidationMapReduce import CrossValidationMapReduce
from KNNBase import KNNBase
from KNNBasicCosineI import KNNBasicCosineI
from KNNBasicPearson import KNNBasicPearson
from KNNMeans import KNNMeans
from KNNZScore import KNNZScore
from NMFMatrixFactorization import NMFMatrixFactorization
from SVDMatrixFactorization import SVDMatrixFactorization
from SVDPPMatrixFactorization import SVDPPMatrixFactorization
from SlopeOneMatrixFactorization import SlopeOneMatrixFactorization
from ProbabilisticMatrixFactorization import ProbabilisticMatrixFactorization

class Recommender:
    def __init__(self, city):

        self.city = city.replace(' ', '')
        self.cv = CrossValidationMapReduce(self.city, [], init=False)

    def process_recommendations(self):
        reviews_user_business = pd.read_csv(self.city+'-reviews-user-business.csv')
        dat = reviews_user_business[['user_id', 'business_id', 'stars']]
        reader = Reader(rating_scale=(1.0, 5.0))
        data = Dataset.load_from_df(dat, reader)
        train, test = train_test_split(data, test_size=0.25)
        best_algorithm = self.cv.get_best_algo()
        if best_algorithm == 'svd':
            algo = SVDMatrixFactorization()
            algo.process()
        if best_algorithm == 'svdpp':
            algo = SVDPPMatrixFactorization()
            algo.process()
        if best_algorithm == 'bals':
            algo = BaseLineALS()
            algo.process()
        if best_algorithm == 'bsdg':
            algo = BaseLineSGD()
            algo.process()
        if best_algorithm == 'knb':
            algo = KNNBase()
            algo.process()
        if best_algorithm == 'knnm':
            algo = KNNMeans()
            algo.process()
        if best_algorithm == 'knnzs':
            algo = KNNZScore()
            algo.process()
        if best_algorithm == 'knbp':
            algo = KNNBasicPearson()
            algo.process()
        if best_algorithm == 'knbci':
            algo = KNNBasicCosineI()
            algo.process()
        if best_algorithm == 'cocluster':
            algo = CoClusteringMatrixFactorization()
            algo.process()
        if best_algorithm == 'nmf':
            algo = NMFMatrixFactorization()
            algo.process()
        if best_algorithm == 'pmf':
            algo = ProbabilisticMatrixFactorization()
            algo.process()
        if best_algorithm == 'slope':
            algo = SlopeOneMatrixFactorization()
            algo.process()


        recommendations = pd.read_csv(self.city+'-recommendations-'+best_algorithm+'.csv')
        recommendations = recommendations[
            abs(recommendations['actual_rating'] - recommendations['recommended_rating']) < 1.0]
        all_restaurants = pd.read_csv(self.city + '-restaurant.csv')
        merged_df = pd.merge(recommendations, all_restaurants, how='left', left_on='restaurant_id', right_on='business_id')
        merged_df = merged_df[['user_id','restaurant_id','actual_rating','recommended_rating', 'latitude', 'longitude']]
        user_series = merged_df.groupby('user_id').size()
        user_df = pd.DataFrame({'user_id': user_series.index, 'size': user_series.values})
        user_df = user_df[user_df['size'] > 2]
        user_list = user_df['user_id'].tolist()
        merged_df = merged_df[merged_df['user_id'].isin(user_list)]
        merged_df.to_csv(self.city + '-recommendations-' + best_algorithm + '-filtered.csv')

    def recommend(self, user_id):
        best_algorithm = self.cv.get_best_algo()
        recommendations = pd.read_csv(self.city+'-recommendations-'+best_algorithm+'-filtered.csv')
        recommendations = recommendations[recommendations['user_id']==user_id]
        return recommendations[['user_id', 'restaurant_id', 'recommended_rating','latitude','longitude']]

def main():
    recommender = Recommender('Las Vegas')
    recommender.process_recommendations()
    df = recommender.recommend('U4INQZOPSUaj8hMjLlZ3KA')
    print(df)

if __name__ == '__main__':
    main()



