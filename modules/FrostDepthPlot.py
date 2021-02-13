import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import datetime
from math import ceil, floor
from modules.FigureFormatting import FigureFormatting


class FrostDepthPlot:
    def __init__(self, dfs):
        self.dfs = dfs
        self.start_date = dfs.start_date
        self.end_date = dfs.end_date
        self.zero_date = dfs.zero_date

    def plot_frost_depth(self,
                         formatter,
                         section_name,
                         save_name,
                         frost_front,
                         thaw_front,
                         interface_list,
                         layer_names,
                         title=False,
                         twinx=True,
                         save_fig=False,
                         show_fig=True):
        # initializer:
        fig, ax = plt.subplots(figsize=formatter['figsize'])
        plt.tight_layout()

        # plot data:
        ax.plot_date(self.dfs.FDdata['date'],
                     self.dfs.FDdata[frost_front],
                     label='frost front',
                     marker=None,
                     linestyle='solid',
                     linewidth=2)
        ax.plot_date(self.dfs.FDdata['date'],
                     self.dfs.FDdata[thaw_front],
                     label='thaw front',
                     marker=None,
                     c='firebrick',
                     linestyle='solid',
                     linewidth=2)

        layer_thickness_list = np.ediff1d(interface_list)
        for interface in interface_list:
            ax.plot([self.start_date, self.end_date],
                    [interface, interface],
                    color="black",
                    linestyle='--',
                    linewidth=1)
            ax.plot([self.zero_date, self.start_date],
                    [interface, interface],
                    color="black",
                    linestyle='solid',
                    linewidth=1)
        ax.plot([self.dfs.start_date, self.dfs.start_date],
                [0, 4],
                color='black',
                linestyle='solid',
                linewidth=1.5)

        # add text to plot:
        for i in range(len(layer_thickness_list)):
            if layer_thickness_list[i] <= 0.11:
                ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025),
                        layer_names[i][0],
                        fontsize=formatter['text_size'],
                        color='black',
                        weight='bold')
                print('executed')
            else:
                ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025 - 0.05),
                        layer_names[i][0],
                        fontsize=formatter['text_size'],
                        color='black',
                        weight='bold')
                ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025 + 0.05),
                        layer_names[i][1],
                        fontsize=formatter['text_size'],
                        color='black',
                        weight='bold')
        ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                (interface_list[-1] + 0.2),
                layer_names[-1][0],
                fontsize=formatter['text_size'],
                color='black',
                weight='bold')

        # PRE-CONFIGURATION (has to be executed before the twinx plot):
        # legend:
        legend = ax.legend(loc='lower right',
                           fontsize=formatter['legend_size'],
                           handlelength=formatter['legend_length'])
        legend.get_frame().set_linewidth(formatter['legend_frame_width'])
        legend.get_frame().set_edgecolor(formatter['legend_edge_color'])
        legend.remove()

        # temperature on plots
        if twinx:
            # initializer:
            ax_twin = ax.twinx()

            # plot data:
            ax_twin.plot_date(self.dfs.ATdata['date'],
                          self.dfs.ATdata['avg'],
                          label='air temperature',
                          marker=None,
                          color='black',
                          linestyle='solid',
                          linewidth=2)
            ax_twin.plot([self.dfs.start_date, self.dfs.end_date],
                         [0, 0],
                         linestyle='solid',
                         color='black',
                         linewidth=1)
            ax_twin.fill_between(self.dfs.ATdata['date'],
                                 self.dfs.ATdata['avg'],
                                 where=self.dfs.boolean_list,
                                 color='cornflowerblue',
                                 interpolate=True)

            # TWINX CONFIGURATION
            # legend:
            legend2 = ax_twin.legend(loc='lower left',
                                     fontsize=formatter['legend_size'],
                                     handlelength=formatter['legend_length'])
            legend2.get_frame().set_linewidth(formatter['legend_frame_width'])
            legend2.get_frame().set_edgecolor(formatter['legend_edge_color'])
            ax_twin.add_artist(legend)
                        # ax_twin.legend(loc="lower right", bbox_to_anchor=(0.55, 0, 0.3, 0.2))  ?????

            # ticks:
            ylim_twin, yticks_twin = self.generate_yaxis_twin_ticks()
            ax_twin.set_ylim(ylim_twin)
            ax_twin.set_yticks(yticks_twin)
            ax_twin.legend(loc="lower right", bbox_to_anchor=(0.55, 0, 0.3, 0.2))
            ax_twin.tick_params(direction='in', width=1.5)
            ax.tick_params(axis='both', direction='in', width=formatter['tick_width'], top=True,
                           labelsize=formatter['tick_size'], length=formatter['tick_length'])

            # label:
            ax_twin.set_ylabel('Temperature, °C', size=formatter['label_size'])
            ax_twin.yaxis.set_label_coords(1.05, 0.22)

            # spines:
            for spine in ['top', 'bottom', 'left', 'right']:
                ax_twin.spines[spine].set_visible(False)

        else:
            ax.add_artist(legend)
            ax.tick_params(axis='both', direction='in', width=formatter['tick_width'], right=True, top=True,
                           labelsize=formatter['tick_size'], length=formatter['tick_length'])

        # MAIN CONFIGURATION:
        # ticks:
        #ax.invert_yaxis()
        ax.set_xlim(self.dfs.zero_date, self.dfs.end_date)
        ax.set_xticks(self.dfs.date_list)
        ax.set_ylim([0, 4])
        ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4.0])
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        plt.setp(ax.get_xticklabels(), rotation=formatter['tick_rotation'], ha='right')

        # spines:
        for spine in ['top', 'bottom', 'left', 'right']:
            ax.spines[spine].set_linewidth(formatter['spine_width'])

        # title:
        if title:
            ax.set_title(section_name)

        # save show options:
        if save_fig:
            fig.savefig('out\\' + save_name, dpi=300, bbox_inches='tight')

        if show_fig:
            plt.show()

        plt.close(fig)

    def generate_yaxis_twin_ticks(self):
        def roundup_max(val):
            return int(ceil(val / 5) * 5)

        def rounddown_min(val):
            return int(floor(val / 5) * 5)

        min_value = rounddown_min(min(self.dfs.ATdata['avg']))
        max_value = roundup_max(max(self.dfs.ATdata['avg']))
        diff = max_value - min_value
        step_size = 5

        ylim = [min_value, diff+max_value]
        yticks = np.arange(min_value, max_value+step_size, step_size)

        return ylim, yticks
