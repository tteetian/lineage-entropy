import pickle
import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def euclidean_distance(coor_1, coor_2):
    return math.sqrt(sum((i - j) ** 2 for i, j in zip(coor_1, coor_2)))


def vector_size(x_displacement, y_displacement):
    return math.sqrt(x_displacement ** 2 + y_displacement ** 2)


conditions = ['WT1', 'WT2', 'J1', 'J2']

total_cell_number = 10 ** 8

state_1_ratio = 0.90
state_2_ratio = 0.05
state_3_ratio = 0.05

state_1_number = state_1_ratio * total_cell_number
state_2_number = state_2_ratio * total_cell_number
state_3_number = state_3_ratio * total_cell_number

normalizing_factor = [total_cell_number, state_1_number, state_2_number, state_3_number] * 20

table = pickle.load(open('20200628_finished_table.pickle', 'rb'))
table_2 = pickle.load(open('20200713_finished_table.pickle', 'rb'))

combined_table = pd.concat([table, table_2], axis=1, sort=False)
combined_table.fillna(0, inplace=True)

sum_table = combined_table.sum(axis=0)
normalized_table = combined_table.div(sum_table)
true_number_table = (normalized_table * normalizing_factor).round()

states = ['s1', 's2', 's3']
states_coords = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

top_right_coord = (1, 1)
top_left_coord = (0, 1)
bottom_left_coord = (0, 0)

all_barcode_list_dict = {}
all_barcode_set_dict = {}

triangle_vertices = np.array([top_right_coord, top_left_coord, bottom_left_coord])

timepoints = ['d0', 'd6', 'd12', 'd18', 'd24']

for condition in conditions:
    all_size_set = set()
    all_barcode_set = set()
    all_barcode_list = []
    all_transition_size_list = []

    for barcode, row in true_number_table.iterrows():
        barcode_dict = {}

        barcode_dict['d0_WT1_all'], barcode_dict['d0_WT1_s1'], barcode_dict['d0_WT1_s2'], barcode_dict[
            'd0_WT1_s3'] = row[0:4]
        barcode_dict['d0_WT2_all'], barcode_dict['d0_WT2_s1'], barcode_dict['d0_WT2_s2'], barcode_dict[
            'd0_WT2_s3'] = row[4:8]
        barcode_dict['d0_J1_all'], barcode_dict['d0_J1_s1'], barcode_dict['d0_J1_s2'], barcode_dict['d0_J1_s3'] = row[
                                                                                                                  8:12]
        barcode_dict['d0_J2_all'], barcode_dict['d0_J2_s1'], barcode_dict['d0_J2_s2'], barcode_dict['d0_J2_s3'] = row[
                                                                                                                  12:16]
        barcode_dict['d6_WT1_all'], barcode_dict['d6_WT1_s1'], barcode_dict['d6_WT1_s2'], barcode_dict[
            'd6_WT1_s3'] = row[16:20]
        barcode_dict['d6_WT2_all'], barcode_dict['d6_WT2_s1'], barcode_dict['d6_WT2_s2'], barcode_dict[
            'd6_WT2_s3'] = row[20:24]
        barcode_dict['d6_J1_all'], barcode_dict['d6_J1_s1'], barcode_dict['d6_J1_s2'], barcode_dict['d6_J1_s3'] = row[
                                                                                                                  24:28]
        barcode_dict['d6_J2_all'], barcode_dict['d6_J2_s1'], barcode_dict['d6_J2_s2'], barcode_dict['d6_J2_s3'] = row[
                                                                                                                  28:32]
        barcode_dict['d24_WT1_all'], barcode_dict['d24_WT1_s1'], barcode_dict['d24_WT1_s2'], barcode_dict[
            'd24_WT1_s3'] = row[32:36]
        barcode_dict['d24_J1_all'], barcode_dict['d24_J1_s1'], barcode_dict['d24_J1_s2'], barcode_dict[
            'd24_J1_s3'] = row[36:40]
        barcode_dict['d12_WT1_all'], barcode_dict['d12_WT1_s1'], barcode_dict['d12_WT1_s2'], barcode_dict[
            'd12_WT1_s3'] = row[40:44]
        barcode_dict['d12_WT2_all'], barcode_dict['d12_WT2_s1'], barcode_dict['d12_WT2_s2'], barcode_dict[
            'd12_WT2_s3'] = row[44:48]
        barcode_dict['d12_J1_all'], barcode_dict['d12_J1_s1'], barcode_dict['d12_J1_s2'], barcode_dict[
            'd12_J1_s3'] = row[48:52]
        barcode_dict['d12_J2_all'], barcode_dict['d12_J2_s1'], barcode_dict['d12_J2_s2'], barcode_dict[
            'd12_J2_s3'] = row[52:56]
        barcode_dict['d18_WT1_all'], barcode_dict['d18_WT1_s1'], barcode_dict['d18_WT1_s2'], barcode_dict[
            'd18_WT1_s3'] = row[56:60]
        barcode_dict['d18_WT2_all'], barcode_dict['d18_WT2_s1'], barcode_dict['d18_WT2_s2'], barcode_dict[
            'd18_WT2_s3'] = row[60:64]
        barcode_dict['d18_J1_all'], barcode_dict['d18_J1_s1'], barcode_dict['d18_J1_s2'], barcode_dict[
            'd18_J1_s3'] = row[64:68]
        barcode_dict['d18_J2_all'], barcode_dict['d18_J2_s1'], barcode_dict['d18_J2_s2'], barcode_dict[
            'd18_J2_s3'] = row[68:72]
        barcode_dict['d24_WT2_all'], barcode_dict['d24_WT2_s1'], barcode_dict['d24_WT2_s2'], barcode_dict[
            'd24_WT2_s3'] = row[72:76]
        barcode_dict['d24_J2_all'], barcode_dict['d24_J2_s1'], barcode_dict['d24_J2_s2'], barcode_dict[
            'd24_J2_s3'] = row[76:80]

        barcode_summary = {'id': barcode, 'ternary_coord': [], 'cartesian_coord': [], 'vector': [], 'size': [],
                           'assigned_state': [], 'transition_amount': [], 'total_transition_amount': 0}

        barcode_size = [sum([barcode_dict[timepoint + '_{}_'.format(condition) + state] for state in states]) for
                        timepoint in timepoints]
        for timepoint in timepoints:
            timepoint_all_present = all(barcode_size)
            timepoint_total = sum([barcode_dict[timepoint + '_{}_'.format(condition) + state] for state in states])
            if timepoint_total > 10:
                ternary_coord = []
                dist = []
                for state in states:
                    ternary_coord.append(barcode_dict[timepoint + '_{}_'.format(condition) + state] / timepoint_total)
                barcode_summary['ternary_coord'].append(ternary_coord)

                cartesian_coord = np.dot(np.array(ternary_coord), triangle_vertices)
                barcode_summary['cartesian_coord'].append(list(cartesian_coord))

                for state_coord in triangle_vertices:
                    dist.append(euclidean_distance(cartesian_coord, state_coord))
                barcode_summary['assigned_state'].append(dist.index(min(dist)))

                barcode_summary['size'].append(timepoint_total)

        if len(barcode_summary['cartesian_coord']) == len(barcode_size):
            for i in range(len(barcode_size) - 1):
                vector = (barcode_summary['cartesian_coord'][i + 1][0] - barcode_summary['cartesian_coord'][i][0],
                          barcode_summary['cartesian_coord'][i + 1][1] - barcode_summary['cartesian_coord'][i][1])
                barcode_summary['vector'].append(vector)
                barcode_summary['transition_amount'].append(vector_size(vector[0], vector[1]))
                barcode_summary['total_transition_amount'] += vector_size(vector[0], vector[1])
            all_transition_size_list.append(barcode_summary['total_transition_amount'])
            for size in barcode_summary['size']:
                all_size_set.add(round(size, 3))
            all_barcode_set.add(barcode)
            all_barcode_list.append(barcode_summary)
    all_barcode_list.sort(reverse=True, key=lambda barcode: barcode['total_transition_amount'])
    all_barcode_list_dict[condition] = all_barcode_list
    all_barcode_set_dict[condition] = all_barcode_set

def motility_super_switcher_histogram_all(all_barcode_list_dict):
    rainbow = cm.get_cmap('rainbow_r', 10)
    rainbow_list = rainbow(range(10))

    for condition in all_barcode_list_dict:
        fig, axs = plt.subplots(1, 4, sharex=True, sharey=True, figsize=[3 * 4.5, 2 * 2])
        all_barcode_list = all_barcode_list_dict[condition]
        all_barcode_list.sort(reverse=True, key=lambda barcode: barcode['total_transition_amount'])
        for transition in range(4):
            fig.suptitle(condition)
            for i in np.arange(0, 1, 0.1):
                ax = axs[transition]
                if transition == 0:
                    ax.set_ylabel('Number of Lineages')
                    ax.set_xlabel('Percent Transition')
                ax.set_title('Day {} to {}'.format(transition * 6, (transition + 1) * 6))
                data = []
                for index, barcode in enumerate(
                        all_barcode_list[round(i * len(all_barcode_list)):round((i + 0.1) * len(all_barcode_list))]):
                    motility = barcode['transition_amount'][transition]
                    data.append(motility)
                data = np.array(data) * 100 / math.sqrt(2)
                ax.hist(data, bins=np.arange(0, 100, 1), alpha=0.4, color=rainbow_list[int(i * 10)])

        axins = inset_axes(axs[3],
                           width="5%",
                           height="100%",
                           loc='lower left',
                           bbox_to_anchor=(1.05, 0., 1, 1),
                           bbox_transform=axs[3].transAxes,
                           borderpad=0,
                           )
        bounds = np.arange(0, 110, 10)
        cmap = matplotlib.cm.rainbow
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
        cbar = matplotlib.colorbar.ColorbarBase(axins, cmap=cmap, norm=norm)
        cbar.set_label("Motility Percentile")
        plt.savefig("MotilityInheritance_RepeatedExperiment_{}.svg".format(condition), format='svg', bbox_inches='tight', dpi=720)
        plt.show()

motility_super_switcher_histogram_all(all_barcode_list_dict)