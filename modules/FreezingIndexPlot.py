import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

class FreezingIndexPlot:
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

    def plot_freezing_index(self):
        fig, ax = plt.subplots(figsize=(12, 6))

        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
        ax.tick_params(axis='both', direction='in', width=1, right=True, top=True)
        for j in ['top', 'bottom', 'left', 'right']:
            ax.spines[j].set_linewidth(1)

        ax.plot_date(self.file.FIdata['date'],
                       self.file.FIdata['FIcum'],
                       label='FI cumulative',
                       marker=None,
                       linestyle='dashed',
                       linewidth=2.5,
                       color='black')
        ax.plot_date(self.file.FIdata['date'],
                       self.file.FIdata['FInet'],
                       label='FI net',
                       marker=None,
                       linestyle='solid',
                       linewidth=2.5,
                       color='black')
        ax.plot_date(self.file.FIdata['date'],
                       self.file.FIdata['TIcum'],
                       label='TI cumulative',
                       marker=None,
                       linestyle='dotted',
                       linewidth=2.5,
                       color='black')
        ax.plot([self.file.start_date, self.file.date_list[-1]], [0, 0], color='black', linestyle='solid', linewidth=1)

        ax.legend(loc="upper left", bbox_to_anchor=(0, 0.7, 0.3, 0.3))
        ax.set_ylabel('Frost/Thaw Index [°C hours]', size=10)
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        ax.set_xlim(self.file.start_date, self.file.end_date)
        ax.set_xticks(self.file.date_list)
        ax.set_ylim([-5000, 5000])
        ax.set_yticks(range(-4000, 5000, 1000))

        if self.titles_on_plots == True:
            ax.set_title('Freezing Index', fontweight='bold', fontsize=12)

        if self.save_figure == True:
            fig.savefig('out/freezing_index', dpi=300, bbox_inches='tight')

        if self.show_figure == True:
            plt.show()

        plt.close()