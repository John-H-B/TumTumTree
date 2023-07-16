import numpy as np

from tumtumtree.utils.input_cleaning import get_continuous_parameter,\
    get_bounded_continuous_parameter, get_discrete_parameter

class BayesianTwoArmNormal():
    def __init__(self, **kwargs):
        self.stored_kwargs = dict(**kwargs)
        self.reset(**self.stored_kwargs)
    def generate(self, simulator=None):

        sample_1 = np.random.normal(self.mu1, self.sigma1, self.size1)


        return_data = sample_1
        print(return_data)

    def reset(self, mu1, mu2, sigma1, sigma2, size1 = 5, size2 = 5):
        self.mu1 = get_continuous_parameter(mu1)
        self.mu2 = get_continuous_parameter(mu2)
        self.sigma1 = get_bounded_continuous_parameter(sigma1, gte_bound=0)
        self.sigma2 = get_bounded_continuous_parameter(sigma2, gte_bound=0)
        self.size1 = get_discrete_parameter(size1)
        self.size1 = get_discrete_parameter(size2)

