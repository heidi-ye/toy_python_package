import pandas as pd

def aMean(a):
    """
    Returns the mean of the row.

    Parameters
    ----------
    a : pandas.core.series.Series
      A pandas series.

    Returns
    -------
    numpy.float64
      A float of the series mean.

    Examples
    --------
    >>> from toy_python_package import toy_python_package
    >>> a = pd.Series([1,1])
    >>> toy_python_package.aMean(a)
    1.0
    """
    return a.mean(axis = 0)
