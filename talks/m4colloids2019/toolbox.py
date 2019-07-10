import periodictable as pt
from refnx.dataset import ReflectDataset
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set("talk", palette='colorblind')

def get_scattering_length(component):
    scattering_length = 0 + 0j
    import scipy.constants as const

    cre = const.physical_constants["classical electron radius"][0]
    for key in component:
        scattering_length += np.multiply(pt.elements.symbol(key).xray.scattering_factors(energy=12)[0], cre * component[key])
        scattering_length += (np.multiply(pt.elements.symbol(key).xray.scattering_factors(energy=12)[1], cre * component[key]) * 1j)
    return scattering_length * 1e10

def experimental_data(experiment_number, run_number, rq4=False):
    data = ReflectDataset('{}/{}.dat'.format(experiment_number, run_number))
    fig = plt.figure()
    ax = plt.subplot()
    if rq4:
        plt.errorbar(data.x, data.y*data.x**4, yerr=data.y_err*data.x**4,
                     marker='o', ls='', label='{}.dat'.format(run_number))
        ax.set_ylabel('$R(q)q^4$')
    else:
        plt.errorbar(data.x, data.y, yerr=data.y_err,
                     marker='o', ls='', label='{}.dat'.format(run_number))
        ax.set_ylabel('$R(q)$')
    ax.set_yscale('log')
    ax.set_xlabel('$q$/Å')
    plt.legend(loc='upper right')
    return fig, data
