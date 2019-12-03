from surprise import KNNWithMeans
from Classifier import Classifier

class KNNMeans(Classifier):

    def __init__(self):
        options = {'name': 'cosine',
         'shrinkage': 0,  # no shrinkage
         'user_based': False
         }
        super().__init__("knnm", KNNWithMeans, param_grid={'k': [2,3,4], 'min_k': [1,2], 'sim_options':{'name': ['cosine'],
         'shrinkage': [0],  # no shrinkage
         'user_based': [False]
         }})
        best_params = super().tune()
        print(best_params)
        self.algo = KNNWithMeans(k=best_params['k'], min_k=best_params['min_k'], sim_options=best_params['sim_options'])

def main():
    algo = KNNMeans()
    algo.process()

if __name__ == '__main__':
    main()