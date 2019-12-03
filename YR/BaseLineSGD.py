from surprise import BaselineOnly
from Classifier import Classifier

class BaseLineSGD(Classifier):

    def __init__(self):
        options = {
            'method': 'sgd',
            'learning_rate': .0005
        }
        super().__init__("bsdg", BaselineOnly, param_grid={
            'bsl_options': {'method': ['sgd'], 'learning_rate': [0.000146, 0.00025, 0.0005]}})
        best_params = super().tune()
        print(best_params)
        self.algo = BaselineOnly(bsl_options=best_params['bsl_options'])

def main():
    algo = BaseLineSGD()
    algo.process()

if __name__ == '__main__':
    main()