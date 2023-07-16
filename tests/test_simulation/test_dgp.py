from tumtumtree.simulation.dgp import TwoArmNormal
from scipy.stats import norm, binom,halfnorm


dgp = BayesianTwoArmNormal(mu1 = 1.0, mu2 =2.0, sigma1 = 1.0, sigma2=1.0)
dgp.generate()
dgp.generate()
dgp.reset(**dgp.stored_kwargs)
dgp.generate()
dgp.generate()


dgp = BayesianTwoArmNormal(mu1 = norm(0,10), mu2 =2.0, sigma1 = halfnorm(0,1), sigma2=1.0)
dgp.generate()
dgp.generate()
dgp.reset(**dgp.stored_kwargs)
dgp.generate()
dgp.generate()