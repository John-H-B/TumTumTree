"""
This file is just used to structure what I hope that the project will be able to do
"""

## Both of these import pythons work
import tumtumtree.simulation as ts
from tumtumtree.simulation import metrics
from tumtumtree.simulation import dists

# Conditions
conditions = ts.conditions.NullConditions()

# Data generating process
dgp = ts.dgp.TwoArmed(  # For if we set the mean and sd of the arms as known
    arms=(
        ts.dists.Normal(mu=0,
                        sigma=1,
                        size = 5),
        ts.dists.Normal(mu=0.5,
                        sigma = 1,
                        size = 5),
    ),
)

# Analyst
analyst = ts.analyst.AsymptoticExpectedValue()

# Stopping
stopping_rule = ts.stopping.StepLimit(steps=10)

# decisions rules
decision_rule = ts.decisions.AlphaThreshold(alpha=0.05)

# Metrics. Storing whether significance was reached and if arm 1 was greater than arm 2
metric1 = ts.metrics.SignificanceReached('significance',decision_rule)
metric2 = ts.metrics.Chosen('chosen',decision_rule)
metric3 = ts.metrics.Mean('mean',[0], [1], [0,1]) # Gets the mean value of arm 1, arm 2, and all data
metrics = ts.metrics.Metrics([metric1, metric2, metric3]) # Produces a 5-vector of metrics for each simulation run



simulator = ts.simulator.Simulator(
    conditions,
    dgp,
    analyst,
    stopping_rule,
    decision_rule,
    metrics
)

results = simulator.simulate(100) # returns a 100 by 5 pandas array

results = ts.optimiser.Optimise(
    simulator=simulator,
    num_simulations = 100, # interpreted as 100 each for method = 'observe'
    params = {
        'stopping_rule.steps': [5,10,20],
        'dgp.arms[1].mu': [0.5,1,2]
    },
    param_parse_method = 'cross', # would do
    method='observe' # only gathers the data and stores it
)

print(results.data) # would return a (3*3*100)x(5+1+1+1) df. The 5 is the number of metrics.
# The 1s are each the simulation number, the parameter value for stopping rule, and the mu value for the treatment arm