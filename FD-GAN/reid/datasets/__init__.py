from __future__ import absolute_import
import warnings

from .cuhk03 import CUHK03
from .dukemtmc import DukeMTMC
from .market1501 import Market1501


__factory = {
    # print('__factory')
    'cuhk03': CUHK03,
    'market1501': Market1501,
    'dukemtmc': DukeMTMC,
}


def names():
    return sorted(__factory.keys())


def create(name, root, *args, **kwargs):
    """
    Create a dataset instance.

    Parameters
    ----------
    name : str
        The dataset name. Can be one of 'cuhk03',
        'market1501', and 'dukemtmc'.
    root : str
        The path to the dataset directory.
    split_id : int, optional
        The index of data split. Default: 0
    num_val : int or float, optional
        When int, it means the number of validation identities. When float,
        it means the proportion of validation to all the trainval. Default: 100
    download : bool, optional
        If True, will download the dataset. Default: False
    """
    print('========datasets  create==============')
    print(args)
    if name not in __factory:
        print('nononono')
        raise KeyError("Unknown dataset:", name)
    print('=====================')
    # print (__factory[name](root, *args, **kwargs))  
    return __factory[name](root, *args, **kwargs)


def get_dataset(name, root, *args, **kwargs):
    warnings.warn("get_dataset is deprecated. Use create instead.")
    return create(name, root, *args, **kwargs)
