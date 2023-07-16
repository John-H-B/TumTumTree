import numpy as np
CONTINUOUS_PARAMETER_TYPES = (float, np.floating)
DISCRETE_PARAMETER_TYPES = (int)

def get_continuous_parameter(parameter):
    parameter = _get_parameter(parameter, accepted_types=CONTINUOUS_PARAMETER_TYPES)
    return parameter

def get_discrete_parameter(parameter):
    parameter = _get_parameter(parameter, accepted_types=DISCRETE_PARAMETER_TYPES)
    return parameter

def ensure_within_bounds(parameter, gte_bound=None, gt_bound=None, lte_bound=None, lt_bound=None):
    if gte_bound is not None:
        assert parameter >= gte_bound
    if gt_bound is not None:
        assert parameter > gt_bound
    if lte_bound is not None:
        assert parameter <= lte_bound
    if lt_bound is not None:
        assert parameter < lt_bound
def get_bounded_continuous_parameter(parameter, gte_bound=None, gt_bound=None, lte_bound=None, lt_bound=None):
    parameter = float(_get_parameter(parameter, accepted_types=CONTINUOUS_PARAMETER_TYPES))
    ensure_within_bounds(parameter, gte_bound, gt_bound, lte_bound, lt_bound)
    return parameter

def get_bounded_discrete_parameter(parameter, gte_bound=None, gt_bound=None, lte_bound=None, lt_bound=None):
    parameter = int(_get_parameter(parameter, accepted_types=DISCRETE_PARAMETER_TYPES))
    ensure_within_bounds(parameter, gte_bound, gt_bound, lte_bound, lt_bound)
    return parameter

def _get_parameter(parameter, accepted_types):
    condition1 = (type(accepted_types) == tuple) and all([(type(x) == type) for x in accepted_types])
    condition2 = (type(accepted_types) == type)
    assert condition1 or condition2

    if hasattr(parameter, 'rvs'):
        parameter = parameter.rvs()
    if isinstance(parameter, accepted_types):
        return parameter #Ensure that np.float converted to float
    else:
        raise TypeError(f'Parameter must be of a type in {accepted_types} '
                        f'or a scipy frozen distribution capable of generating them')