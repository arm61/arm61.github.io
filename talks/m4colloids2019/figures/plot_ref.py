import matplotlib.pyplot as plt
import numpy as np

type = ['monolayer', 'bilayer', 'floating_bilayer']
type_nice = ['Monolayer', 'Bilayer', 'Floating bilayer']

for e, i in enumerate(type):
    x, y = np.loadtxt('{}.txt'.format(i))
    fig = plt.figure(figsize=(5,3))
    ax = fig.add_subplot(111)
    ax.spines['bottom'].set_color('#888888')
    ax.spines['top'].set_color('#888888')
    ax.spines['left'].set_color('#888888')
    ax.spines['right'].set_color('#888888')
    ax.xaxis.label.set_color('#888888')
    ax.yaxis.label.set_color('#888888')
    ax.tick_params(axis='x', colors='#888888')
    ax.tick_params(axis='y', colors='#888888')
    plt.plot(x, y, 'o', c='#2e94c4')
    plt.xlabel('$q$/Å')
    plt.ylabel('log[$R(q)q^4$]')
    plt.title('{}'.format(type_nice[e]), c='#888888')
    plt.tight_layout()
    plt.savefig('{}.png'.format(i), dpi=600)
