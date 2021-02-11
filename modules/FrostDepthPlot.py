import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import datetime


class FrostDepthPlot:
    def __init__(self,
                 file,
                 temp_on_plots=True,
                 titles_on_plots=False,
                 save_figure=True,
                 show_figure=False):
        self.file = file
        self.temp_on_plots = temp_on_plots
        self.titles_on_plots = titles_on_plots
        self.save_figure = save_figure
        self.show_figure = show_figure

    def plot_frost_depth(self,
                         frost_front,
                         thaw_front,
                         interaface_list,
                         layer_names,
                         layer_thick,
                         title,
                         save_name):
        # initializer:
        fig, ax = plt.subplots(figsize=(12, 6))

        # plot data:
        ax.plot_date(self.file.FDdata['date'],
                     self.file.FDdata[frost_front],
                     label='frost front',
                     marker=None,
                     linestyle='solid',
                     linewidth=2)
        ax.plot_date(self.file.FDdata['date'],
                     self.file.FDdata[thaw_front],
                     label='thaw front',
                     marker=None,
                     c='firebrick',
                     linestyle='solid',
                     linewidth=2)

        for interface in interaface_list[:-1]:
            ax.plot([self.file.start_date, self.file.end_date], [interface, interface], color="black", linestyle='--', linewidth=1)
            ax.plot([self.file.zero_date, self.file.start_date], [interface, interface], color="black", linestyle='solid', linewidth=1)
        last_interface = interaface_list[-1]
        ax.plot([self.file.start_date, self.file.end_date],
                [last_interface - 0.025,
                 last_interface - 0.025],
                color="black",
                linestyle='--',
                linewidth=1)
        ax.plot([self.file.zero_date, self.file.start_date],
                [(last_interface - 0.025),
                 (last_interface - 0.025)],
                color="black",
                linestyle='solid',
                linewidth=1)

        # add text to plot:
        cumsum_list = np.concatenate((np.array([0]), np.cumsum(layer_thick)), axis=0)
        for i in range(len(layer_names)-1):
            if layer_thick[i] <= 0.1:
                ax.text(self.file.zero_date + datetime.timedelta(self.file.days * 0.25 * 0.10),
                        (cumsum_list[i] + layer_thick[i] / 2 + 0.025),
                        layer_names[i][0], fontsize=6, color='black', weight='bold')
            else:
                ax.text(self.file.zero_date + datetime.timedelta(self.file.days * 0.25 * 0.10),
                        (cumsum_list[i] + layer_thick[i] / 2 + 0.025 - 0.05),
                        layer_names[i][0], fontsize=6, color='black', weight='bold')
                ax.text(self.file.zero_date + datetime.timedelta(self.file.days * 0.25 * 0.10),
                        (cumsum_list[i] + layer_thick[i] / 2 + 0.025 + 0.05),
                        layer_names[i][1], fontsize=6, color='black', weight='bold')
        ax.text(self.file.zero_date + datetime.timedelta(self.file.days * 0.25 * 0.10),
                (cumsum_list[-2] + layer_thick[-1] / 2 + 0.025),
                layer_names[-1][0], fontsize=6, color='black', weight='bold')

        # configuration:
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
        ax.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)
        for j in ['top', 'bottom', 'left', 'right']:
            ax.spines[j].set_linewidth(1.5)

        ax.legend(loc="lower right", bbox_to_anchor=(0.7, 0, 0.3, 0.3))
        if self.titles_on_plots == True:
            ax.set_title(title, fontweight='bold', fontsize=12)
        ax.set_ylabel('Depth, m', size=10)
        ax.invert_yaxis()
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        ax.set_xlim(self.file.zero_date, self.file.end_date)
        ax.plot([self.file.start_date, self.file.start_date], [0, 4], color='black', linestyle='solid', linewidth=1.5)
        ax.set_xticks(self.file.date_list)
        ax.set_ylim([4, 0])
        ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4.0])

        # temperature on plots
        if self.temp_on_plots == True:
            ax2 = ax.twinx()
            ax2.plot_date(self.file.ATdata['date'], self.file.ATdata['avg'], label='air temperature', marker=None, color='black',
                          linestyle='solid', linewidth=2)
            ax2.plot([self.file.start_date, self.file.end_date], [0, 0], linestyle='solid', color='black', linewidth=1)
            ax2.set_xlim(self.file.zero_date, self.file.end_date)
            ax2.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
            ax2.set_xticks(self.file.date_list)
            ax2.set_ylim([-14, 40])
            ax2.set_yticks(range(-14, 12, 2))
            ax2.set_ylabel('Temperature, °C', size=10)
            ax2.yaxis.set_label_coords(1.05, 0.22)
            ax2.legend(loc="lower right", bbox_to_anchor=(0.55, 0, 0.3, 0.2))
            ax2.fill_between(self.file.ATdata['date'],
                             self.file.ATdata['avg'],
                             where=self.file.boolean_list,
                             color='cornflowerblue',
                             interpolate=True)
            ax2.tick_params(direction='in', width=1.5)

        # save show options:
        if self.save_figure:
            fig.savefig(save_name, dpi=300, bbox_inches='tight')

        if self.show_figure:
            plt.show()

        plt.close(fig)