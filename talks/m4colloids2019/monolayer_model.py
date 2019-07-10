import numpy as np
import refnx
from refnx.analysis import possibly_create_parameter, Parameters
from refnx.reflect import Component
import toolbox as tb
import matplotlib.pyplot as plt


class Monolayer(Component):
    """
    The class to describe a two-layer model for the lipid monolayer.

    Parameters
    ----------
    bs: float, array_like
        The scattering lengths for the head and tail components
    name: string
        A name for the monolayer
    """

    def __init__(self, surfactant, subphase):
        super(Monolayer, self).__init__()
        print('######')
        bs = get_surfactant_scattering(surfactant)
        self.name = "{}_monolayer_at_air/{}".format(surfactant, subphase)

        if isinstance(bs[0], complex):
            self.b_real_h = possibly_create_parameter(
                bs[0].real, "{} - b_real_head".format(self.name)
            )
            self.b_imag_h = possibly_create_parameter(
                bs[0].imag, "{} - b_imag_head".format(self.name)
            )
        else:
            self.b_real_h = possibly_create_parameter(
                bs[0], "{} - b_real_head".format(self.name)
            )
            self.b_imag_h = possibly_create_parameter(
                0, "{} - b_imag_head".format(self.name)
            )
        if isinstance(bs[1], complex):
            self.b_real_t = possibly_create_parameter(
                bs[1].real, "{} - b_real_tail".format(self.name)
            )
            self.b_imag_t = possibly_create_parameter(
                bs[1].imag, "{} - b_imag_tail".format(self.name)
            )
        else:
            self.b_real_t = possibly_create_parameter(
                bs[1], "{} - b_real_tail".format(self.name)
            )
            self.b_imag_t = possibly_create_parameter(
                0, "{} - b_imag_tail".format(self.name)
            )
        print('######')
        volumes = get_volumes(surfactant)
        self.mol_vol_h = possibly_create_parameter(
            volumes[0], "{} - molecular_volume_head".format(self.name)
        )
        self.mol_vol_t = possibly_create_parameter(
            volumes[1], "{} - molecular_volume_tail".format(self.name)
        )


        self.thick_h = possibly_create_parameter(
            100, "{} - thickness_head".format(self.name)
        )
        self.thick_t = possibly_create_parameter(
            100, "{} - thickness_tail".format(self.name)
        )
        print('######')
        self.rho_s = get_subphase_sld(subphase)
        self.phi_h = possibly_create_parameter(0.5, "{} - solvation_head".format(self.name))
        self.phi_t = possibly_create_parameter(0, "{} - solvation_tail".format(self.name))

        self.rough_h_t = possibly_create_parameter(
            3.3, "{} - roughness_head_tail".format(self.name)
        )
        self.rough_t_a = possibly_create_parameter(
            3.3, "{} - roughness_tail_air".format(self.name)
        )
        self.rough_w_h = possibly_create_parameter(
            3.3, "{} - roughness_tail_air".format(self.name)
        )

        self.reverse_monolayer = False

    def set_roughness(self, values, vary, upper_bounds=None, lower_bounds=None):
        if len(values) == 1:
            self.rough_t_a.setp(values[0], vary=vary, bounds=(lower_bounds[0], upper_bounds[0]))
            self.rough_h_t.constraint = self.rough_t_a
            self.rough_w_h.constraint = self.rough_t_a
        elif len(values) == 3:
            self.rough_t_a.setp(values[0], vary=vary[0], bounds=(lower_bounds[0], upper_bounds[0]))
            self.rough_h_t.setp(values[1], vary=vary[1], bounds=(lower_bounds[1], upper_bounds[1]))
            self.rough_w_h.setp(values[2], vary=vary[2], bounds=(lower_bounds[2], upper_bounds[2]))

    def slabs(self, structure=None):
        """
        Returns
        -------
        slab_model = array of np.ndarray
            Slab representation of monolayer made up of two layers
        """
        layers = np.zeros((4, 5))

        layers[1, 0] = self.thick_t
        layers[1, 1] = self.b_real_t * 1e6 / self.mol_vol_t
        layers[1, 2] = self.b_imag_t * 1e6 / self.mol_vol_t
        layers[1, 3] = self.rough_t_a
        layers[1, 4] = self.phi_t

        layers[2, 0] = self.thick_h
        layers[2, 1] = self.b_real_h * 1e6 / self.mol_vol_h
        layers[2, 2] = self.b_imag_h * 1e6 / self.mol_vol_h
        layers[2, 3] = self.rough_h_t
        layers[2, 4] = self.phi_h

        layers[0, 0] = 0
        layers[0, 1] = 0
        layers[0, 2] = 0
        layers[0, 3] = 0
        layers[0, 4] = 0

        layers[3, 0] = 0
        layers[3, 1] = self.rho_s.real
        layers[3, 2] = self.rho_s.imag
        layers[3, 3] = self.rough_w_h
        layers[3, 4] = 0

        if self.reverse_monolayer:
            layers = np.flipud(layers)
            layers[:, 3] = layers[::-1, 3]

        return layers

    @property
    def parameters(self):
        p = Parameters(name=self.name)
        p.extend(
            [
                self.thick_h,
                self.thick_t,
                self.mol_vol_h,
                self.mol_vol_t,
                self.rough_h_t,
                self.rough_t_a,
                self.phi_h,
                self.phi_t,
                self.rough_w_h
            ]
        )
        return p

    def logp(self):
        if self.phi_h >= 1 or self.phi_h < 0:
            return -np.inf
        if self.phi_t >= 1 or self.phi_t < 0:
            return -np.inf
        return 0

def plot(objective, rq4=False, save_location=None):
    fig = plt.figure()
    ax = plt.subplot()
    if rq4:
        plt.errorbar(objective.data.x, objective.data.y*objective.data.x**4, yerr=objective.data.y_err*objective.data.x**4,
                     marker='o', ls='', label='Experiment')
        y = objective.model(objective.data.x)*objective.data.x**4
        plt.plot(objective.data.x, y, label='Model')
        ax.set_ylabel('$R(q)q^4$/Å$^{-4}$')
    else:
        plt.errorbar(objective.data.x, objective.data.y, yerr=objective.data.y_err,
                     marker='o', ls='', label='Experiment')
        y = objective.model(objective.data.x)
        plt.plot(objective.data.x, y, label='Model')
        ax.set_ylabel('$R(q)$')
    ax.set_yscale('log')
    ax.set_xlabel('$q$/Å$^{-1}$')
    plt.legend(loc='upper right')
    if save_location != None:
        if save_location[:-3] == 'png':
            plt.savefig(save_location, dpi=600)
        else:
            plt.savefig(save_location)
    return fig, ax

def run_analysis(model, data, seed):
    model_data = refnx.reflect.ReflectModel(model)
    model_data.scale.setp(vary=True, bounds=(0.005, 10))
    model_data.bkg.setp(data.y[-1], vary=True, bounds=(data.y[-1]/10., data.y[-1]*10.))
    objective = refnx.analysis.Objective(model_data, data, transform=refnx.analysis.Transform("YX4"))
    fitter = refnx.analysis.CurveFitter(objective)
    np.random.seed(seed)
    res = fitter.fit("differential_evolution", target='nlpost')
    print(objective)
    return objective

surf_dict = {'dppc': [{"C": 10, "H": 18, "O": 8, "N": 1, "P": 1},
                      {"C": 15 * 2, "H": 15 * 4 + 2}],
             'dmpc': [{"C": 10, "H": 18, "O": 8, "N": 1, "P": 1},
                      {"C": 13 * 2, "H": 13 * 4 + 2}]}

def get_surfactant_scattering(surfactant):
    if surfactant in surf_dict:
        print("{} was found in our library of surfactants. The head group consists of:".format(surfactant))
        for i in surf_dict[surfactant][0]:
            print("- {}: {} atoms".format(i, surf_dict[surfactant][0][i]))
        print("The tail group consists of:")
        for i in surf_dict[surfactant][1]:
            print("- {}: {} atoms".format(i, surf_dict[surfactant][1][i]))
    bs = []
    bs.append(tb.get_scattering_length(surf_dict[surfactant][0]))
    bs.append(tb.get_scattering_length(surf_dict[surfactant][1]))
    print("Therefore, the total scattering length of the head is {:.2e} Å and of the tail is {:.2e} Å.".format(bs[0], bs[1]))
    return bs

sub_dict = {'h2o': 9.469-0.032j}

def get_subphase_sld(subphase):
    if subphase in sub_dict:
        print("{} was found in our subphse library. The SLD of {} is {}e-6 Å.".format(subphase, subphase, sub_dict[subphase]))
    return sub_dict[subphase]

vol_dict = {'dppc': [320.9, 966.4, "10.1016/S0006-3495(98)77563-0"],
            'dmpc': [320.9, 851.5, "10.1016/S0006-3495(98)77563-0"]}

def get_volumes(surfactant):
    if surfactant in vol_dict:
        print("The {} head volume will be taken as {} Å^3.".format(surfactant, vol_dict[surfactant][0]))
        print("The {} tail volume will be taken as {} Å^3.".format(surfactant, vol_dict[surfactant][1]))
        print("These head and tail values were taken from DOI: {} (please cite this reference if these values are used).".format(vol_dict[surfactant][2]))
    return vol_dict[surfactant][:2]
