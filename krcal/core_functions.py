import numpy as np
import tables as tb
import pandas as pd

import matplotlib.pyplot as plt

from typing import TypeVar
Number = TypeVar('Number', int, float)

from typing import List, Tuple

from   invisible_cities.icaro.hst_functions  import labels

from   invisible_cities.core.core_functions import loc_elem_1d
from   invisible_cities.core.core_functions import weighted_mean_and_std
from .  kr_types import GaussPar


def mean_and_std(x : np.array, range : Tuple[Number])->Tuple[Number]:
    """Computes mean and std for an array within a range"""
    x1 = loc_elem_1d(x, find_nearest(x,range[0]))
    x2 = loc_elem_1d(x, find_nearest(x,range[1]))
    xmin = min(x1, x2)
    xmax = max(x1, x2)

    mu, std = weighted_mean_and_std(x[xmin:xmax], np.ones(len(x[xmin:xmax])))
    return mu, std


def gaussian_parameters(x : np.array, range : Tuple[Number])->GaussPar:
    mu, std = mean_and_std(x, range)
    amp     = (2 * np.pi)**0.5 * std 
    return GaussPar(mu = mu, std = std, amp = amp)


def find_nearest(array : np.array, value : Number)->Number:
    """Return the array element nearest to value"""
    idx = (np.abs(array-value)).argmin()
    return array[idx]


def divide_np_arrays(num : np.array, denom : np.array) -> np.array:
    """Safe division of two arrays"""
    assert len(num) == len(denom)
    ok    = denom > 0
    ratio = np.zeros(len(denom))
    np.divide(num, denom, out=ratio, where=ok)
    return ratio
