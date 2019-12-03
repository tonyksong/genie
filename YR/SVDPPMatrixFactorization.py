
from surprise import SVDpp
from Classifier import Classifier

class SVDPPMatrixFactorization(Classifier):

    def __init__(self):
        super().__init__("svdpp", SVDpp, {'n_factors': [50,100,150],'n_epochs': [20,30], 'lr_all': [0.005,0.01],'reg_all':[0.02,0.1]})
        best_params = super().tune()
        print(best_params)
        self.algo = SVDpp(n_factors=best_params['n_factors'], n_epochs=best_params['n_epochs'],
                        lr_all=best_params['lr_all'], reg_all=best_params['reg_all'])

def main():
    algo = SVDPPMatrixFactorization()
    algo.process()


if __name__ == '__main__':
    main()







