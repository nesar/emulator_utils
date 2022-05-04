"""
split.py
========
Hold out routines

"""

from sklearn.model_selection import train_test_split

__all__ = ("random_holdout", "nonrandom_holdout", )



def random_holdout(input_data, output_data, split_fraction):
    """
    Used for train-test splitting of data. The datapoints are randomly selection. 
    TO-DO: fix random seed?

    Parameters
    ----------
    input_data: float
        insert explanation
    output_data: float
        insert explanation
    split_fraction: float
        insert explanation

    Returns
    -------
    train_data: float
        insert explanation
    test_data: float
        insert explanation
    train_target: float
        insert explanation
    test_target: float
        insert explanation

    """

    train_data, test_data, train_target, test_target = train_test_split(input_data, output_data, test_size=split_fraction, random_state=1)
    return train_data, test_data, train_target, test_target

def nonrandom_holdout():
    """
    Non-random holdouts. Currently not implemented

    """
    return NotImplemented




