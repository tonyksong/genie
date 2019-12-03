
from surprise import SlopeOne
from Classifier import Classifier

class SlopeOneMatrixFactorization(Classifier):

    def __init__(self):
        super().__init__("slope", SlopeOne, param_grid={})
        best_params = super().tune()
        print(best_params)
        res = not best_params
        if res:
            self.algo = SlopeOne()

def main():
    algo = SlopeOneMatrixFactorization()
    algo.process()


if __name__ == '__main__':
    main()







