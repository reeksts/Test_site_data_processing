import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import datetime
from math import ceil, floor


class FrostDepthPlot:
    def __init__(self,
                 files_and_dates,
                 temp_on_plots=True,
                 titles_on_plots=False,
                 save_figure=True,
                 show_figure=False):
        self.files_and_dates = files_and_dates
        self.start_date = files_and_dates.start_date
        self.end_date = files_and_dates.end_date
        self.zero_date = files_and_dates.zero_date
        self.temp_on_plots = temp_on_plots
        self.titles_on_plots = titles_on_plots
        self.save_figure = save_figure
        self.show_figure = show_figure

    def plot_frost_depth(self,
                         section_name,
                         save_name,
                         frost_front,
                         thaw_front,
                         interface_list,
                         layer_names):
        # initializer:
        fig, ax = plt.subplots(figsize=(12, 6))

        # plot data:
        ax.plot_date(self.files_and_dates.FDdata['date'],
                     self.files_and_dates.FDdata[frost_front],
                     label='frost front',
                     marker=None,
                     linestyle='solid',
                     linewidth=2)
        ax.plot_date(self.files_and_dates.FDdata['date'],
                     self.files_and_dates.FDdata[thaw_front],
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
        print(layer_thickness_list)

        # add text to plot:
        for i in range(len(layer_thickness_list)):
            if layer_thickness_list[i] <= 0.11:
                ax.text(self.zero_date + datetime.timedelta(self.files_and_dates.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025),
                        layer_names[i][0],
                        fontsize=6,
                        color='black',
                        weight='bold')
                print('executed')
            else:
                ax.text(self.zero_date + datetime.timedelta(self.files_and_dates.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025 - 0.05),
                        layer_names[i][0],
                        fontsize=6,
                        color='black',
                        weight='bold')
                ax.text(self.zero_date + datetime.timedelta(self.files_and_dates.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025 + 0.05),
                        layer_names[i][1],
                        fontsize=6,
                        color='black',
                        weight='bold')
        ax.text(self.zero_date + datetime.timedelta(self.files_and_dates.days * 0.25 * 0.10),
                (interface_list[-1] + 0.2),
                layer_names[-1][0], fontsize=6, color='black', weight='bold')

        # configuration:
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
        ax.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)
        for j in ['top', 'bottom', 'left', 'right']:
            ax.spines[j].set_linewidth(1.5)

        ax.legend(loc="lower right", bbox_to_anchor=(0.7, 0, 0.3, 0.3))
        if self.titles_on_plots:
            ax.set_title('random', fontweight='bold', fontsize=12)
        ax.set_ylabel('Depth, m', size=10)
        ax.invert_yaxis()
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        ax.set_xlim(self.files_and_dates.zero_date, self.files_and_dates.end_date)
        ax.plot([self.files_and_dates.start_date, self.files_and_dates.start_date],
                [0, 4],
                color='black',
                linestyle='solid',
                linewidth=1.5)
        ax.set_xticks(self.files_and_dates.date_list)
        ax.set_ylim([4, 0])
        ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4.0])

        # temperature on plots
        if self.temp_on_plots == True:
            ax2 = ax.twinx()
            ax2.plot_date(self.files_and_dates.ATdata['date'],
                          self.files_and_dates.ATdata['avg'],
                          label='air temperature',
                          marker=None,
                          color='black',
                          linestyle='solid',
                          linewidth=2)
            ax2.plot([self.files_and_dates.start_date, self.files_and_dates.end_date], [0, 0], linestyle='solid', color='black', linewidth=1)
            ax2.set_xlim(self.files_and_dates.zero_date, self.files_and_dates.end_date)
            ax2.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
            ax2.set_xticks(self.files_and_dates.date_list)
            ylim, yticks = self.generate_yaxis_sec_ticks()
            ax2.set_ylim(ylim)
            ax2.set_yticks(yticks)
            ax2.set_ylabel('Temperature, °C', size=10)
            ax2.yaxis.set_label_coords(1.05, 0.22)
            ax2.legend(loc="lower right", bbox_to_anchor=(0.55, 0, 0.3, 0.2))
            ax2.fill_between(self.files_and_dates.ATdata['date'],
                             self.files_and_dates.ATdata['avg'],
                             where=self.files_and_dates.boolean_list,
                             color='cornflowerblue',
                             interpolate=True)
            ax2.tick_params(direction='in', width=1.5)

        # save show options:
        if self.save_figure:
            fig.savefig('out\\' + save_name, dpi=300, bbox_inches='tight')

        if self.show_figure:
            plt.show()

        plt.close(fig)

    def generate_yaxis_sec_ticks(self):
        def roundup_max(val):
            return int(ceil(val / 5) * 5)

        def rounddown_min(val):
            return int(floor(val / 5) * 5)

        min_value = rounddown_min(min(self.files_and_dates.ATdata['avg']))
        max_value = roundup_max(max(self.files_and_dates.ATdata['avg']))
        diff = max_value - min_value
        step_size = 5

        ylim = [min_value, diff+max_value]
        yticks = np.arange(min_value, max_value+step_size, step_size)

        return ylim, yticks
