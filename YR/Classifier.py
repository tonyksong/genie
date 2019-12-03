import numpy as np
import pandas as pd


from surprise.model_selection import train_test_split
from surprise import Reader, Dataset
from surprise import accuracy
from surprise.model_selection import GridSearchCV


class Classifier:
    def __init__(self, name, algo, param_grid, city='Las Vegas'):
        self.name = name
        self.algo = algo
        self.param_grid = param_grid
        self.city = city.replace(' ','')

    def split_data(self,percent):
        reviews_user_business = pd.read_csv(self.city+'-reviews-user-business.csv')
        req_data = reviews_user_business[['user_id', 'business_id', 'stars']]
        reader = Reader(rating_scale=(1.0, 5.0))
        self.data = Dataset.load_from_df(req_data, reader)
        self.tr, self.te = train_test_split(self.data, test_size=percent)


    def train(self, train):
        self.algo.fit(train)

    def test(self, test):
        self.predictions = self.algo.test(test)

    def accuracy_rmse(self):
        return accuracy.rmse(self.predictions)

    def predict(self, user_id, restaurant_id):
        return self.algo.predict(uid=user_id, iid=restaurant_id, clip=True)


    def persist_prediction(self):
        recommendations = pd.DataFrame(columns=['user_id', 'restaurant_id', 'actual_rating', 'recommended_rating'])

        for prediction in self.predictions:
            recommendations = recommendations.append(
                {'user_id': prediction.uid, 'restaurant_id': prediction.iid, 'actual_rating': prediction.r_ui,
                 'recommended_rating': prediction.est}, ignore_index=True)
        recommendations.to_csv(self.city+'-recommendations-'+self.name+'.csv')

    def tune(self):
        self.split_data(0.25)
        print('algo')
        print(self.algo)
        res = not self.param_grid
        if res:
            return {}
        gs = GridSearchCV(self.algo, self.param_grid, measures=['rmse'], cv=2)
        gs.fit(self.data)
        params = gs.best_params['rmse']
        return params

    def process(self):
        self.train(self.tr)
        self.test(self.te)
        print(self.accuracy_rmse())
        self.persist_prediction()





