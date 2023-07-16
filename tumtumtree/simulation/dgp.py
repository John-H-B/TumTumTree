import numpy as np
import pandas as pd
import inspect

from tumtumtree.utils.input_cleaning import get_continuous_parameter,\
    get_bounded_continuous_parameter, get_discrete_parameter

"""
GENERATE SHOULD RETURN EITHER A PANDAS DATAFRAME OR A NUMPY DATA FRAME
THESE SHOULD ALWAYS HAS THE SAME NUMBER OF COLUMNS
"""


class BaseDataGeneratingProcess():
    simulation_object_type = 'DataGeneratingProcess'

    def __init__(self, **kwargs):
        self.stored_kwargs = dict(**kwargs)
        self.check_all_and_only_expected_kwargs_available()
        self.reset(**self.stored_kwargs)

    def check_all_and_only_expected_kwargs_available(self):
        expected = self.expected_kwargs()
        stored = set(self.stored_kwargs.keys())
        assert expected.symmetric_difference(stored) == {'self'}, f"""
        expected {expected},
        received {stored},
        difference {expected.symmetric_difference(stored)},
        should be exactly {{'self'}}"""

    def expected_kwargs(self):
        expected_arguments = set(inspect.getfullargspec(self.reset).args)
        return expected_arguments

    def generate(self, simulator=None):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError


class TwoArmNormal(BaseDataGeneratingProcess):

    def generate(self, simulator=None):
        sample_1 = np.random.normal(self.mu1, self.sigma1, self.size1)
        sample_2 = np.random.normal(self.mu2, self.sigma2, self.size2)

        df1 = pd.DataFrame({'arm': 1,'value': sample_1})
        df2 = pd.DataFrame({'arm': 2, 'value': sample_2})

        return_data = pd.concat((df1,df2),axis=0)
        print(return_data)

    def reset(self, mu1, mu2, sigma1, sigma2, size1, size2):
        self.mu1 = get_continuous_parameter(mu1)
        self.mu2 = get_continuous_parameter(mu2)
        self.sigma1 = get_bounded_continuous_parameter(sigma1, gte_bound=0)
        self.sigma2 = get_bounded_continuous_parameter(sigma2, gte_bound=0)
        self.size1 = get_discrete_parameter(size1)
        self.size2 = get_discrete_parameter(size2)

