
from surprise import SVD
from Classifier import Classifier

class ProbabilisticMatrixFactorization(Classifier):

    def __init__(self):
        super().__init__("pmf", SVD, {'n_factors': [50, 100, 150], 'n_epochs': [20, 30], 'lr_all': [0.005, 0.01],
                                      'reg_all': [0.02, 0.1]})
        best_params = super().tune()
        print(best_params)
        self.algo = SVD(n_factors=best_params['n_factors'], n_epochs=best_params['n_epochs'],
                        lr_all=best_params['lr_all'], reg_all=best_params['reg_all'], biased=False)

def main():
    algo = ProbabilisticMatrixFactorization()
    algo.process()


if __name__ == '__main__':
    main()







