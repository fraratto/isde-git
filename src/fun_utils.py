from pandas import read_csv
import numpy as np


def load_data(filename):
    """
    Load data from a csv file

    Parameters
    ----------
    filename : string
        Filename to be loaded.

    Returns
    -------
    X : ndarray
        the data matrix.

    y : ndarray
        the labels of each sample.
    """
    data = read_csv(filename)
    z = np.array(data)
    y = z[:, 0]
    X =
    return X, y


def split_data(x, y, tr_fraction=0.5):
       pass


def predict(x, centroids):
    dist = euclidean_distances(x, centroids, squared=True)
    y_pred = np.argmin(dist, axis=1)
    return y_preddef predict(x, centroids):
    dist = euclidean_distances(x, centroids, squared=True)
    y_pred = np.argmin(dist, axis=1)
    return y_pred
