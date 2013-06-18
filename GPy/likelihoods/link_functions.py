# Copyright (c) 2012, 2013 Ricardo Andrade
# Licensed under the BSD 3-clause license (see LICENSE.txt)


import numpy as np
from scipy import stats
import scipy as sp
import pylab as pb
from ..util.plot import gpplot
from ..util.univariate_Gaussian import std_norm_pdf,std_norm_cdf

class LinkFunction(object):
    """
    Link function class for doing non-Gaussian likelihoods approximation

    :param Y: observed output (Nx1 numpy.darray)
    ..Note:: Y values allowed depend on the likelihood_function used
    """
    def __init__(self):
        pass

class Probit(LinkFunction):
    """
    Probit link function
    """
    def transf(self,mu):
        pass

    def inv_transf(self,f):
        pass

    def log_inv_transf(self,f):
        pass

class Log(LinkFunction):
    """
    Logarithm link function
    """

    def transf(self,mu):
        return np.log(mu)

    def inv_transf(self,f):
        return np.exp(f)

    def log_inv_transf(self,f):
        return f

    def inv_transf_df(sefl,f):
        return np.exp(f)

    def log_inv_transf_df(self,f):
        return 1

    def inv_transf_df(sefl,f):
        return np.exp(f)

    def log_inv_transf_df(self,f):
        return 1



