#!/usr/bin/env python
# Probability model
#   Posterior: (1-dimensional) Bernoulli
# Variational model
#   Likelihood: Mean-field Bernoulli
import numpy as np
import tensorflow as tf

import blackbox as bb
from blackbox.dists import bernoulli_log_prob
from blackbox.likelihoods import MFBernoulli

class Bernoulli:
    """
    p(x, z) = p(z) = p(z | x) = Bernoulli(z; p)
    """
    def __init__(self, p):
        self.p = p
        self.num_vars = len(p.shape)

    def log_prob(self, zs):
        log_prior = bernoulli_log_prob(zs[:, 0], p)
        return log_prior

np.random.seed(42)
tf.set_random_seed(42)

p = np.array([0.6])
model = Bernoulli(p)
q = MFBernoulli(model.num_vars)

inference = bb.VI(model, q, n_minibatch=100)
inference.run()