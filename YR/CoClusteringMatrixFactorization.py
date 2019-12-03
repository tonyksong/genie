
from surprise import CoClustering
from Classifier import Classifier

class CoClusteringMatrixFactorization(Classifier):

    def __init__(self):
        super().__init__("cocluster", CoClustering, param_grid={'n_cltr_u':[3,6],'n_cltr_i':[3,6],'n_epochs':[20,25]})
        best_params = super().tune()
        print(best_params)
        self.algo = CoClustering(n_cltr_u=best_params['n_cltr_u'], n_cltr_i=best_params['n_cltr_i'], n_epochs=best_params['n_epochs'])

def main():
    algo = CoClusteringMatrixFactorization()
    algo.process()


if __name__ == '__main__':
    main()
