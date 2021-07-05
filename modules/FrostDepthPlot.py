import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import pandas as pd
import datetime
from math import ceil, floor


class FrostDepthPlot:
    def __init__(self, dfs, year_sample):
        self.dfs = dfs
        self.start_date = dfs.start_date
        self.end_date = dfs.end_date
        self.zero_date = dfs.zero_date
        self.year_sample = year_sample
        self.missing_dates = []

        # the following for loop should move to FilesAndDates module
        for missing_period in year_sample['missing_dates']:
            start_date = missing_period['start_date']
            end_date = missing_period['end_date']
            dates = pd.date_range(start_date, end_date)
            for date in dates:
                self.missing_dates.append(date)

    def plot_frost_depth(self,
                         sizer,
                         styler,
                         section_name,
                         save_name,
                         frost_front,
                         thaw_front,
                         interface_list,
                         layer_names,
                         title=False,
                         twinx=True,
                         save_fig=True,
                         show_fig=False):

        # local styler and sizer:
        if styler['name'] == 'light':
            color1 = 'cornflowerblue'
            color2 = 'lightcoral'
            color3 = 'black'  # air temperature line
            color4 = '#dddddd'
            color5 = 'cornflowerblue'  # fill between air temperature
            plotline_width = 1
        else:
            color1 = '#3598FE'
            color2 = '#F29724'
            color3 = '#2B6A6C'  # air temperature line
            color4 = '#404040'
            color5 = '#2B6A6C'  # fill between air temperature
            plotline_width = 1

        # initializer:
        fig, ax = plt.subplots(figsize=sizer['figsize'])
        fig.patch.set_facecolor(styler['facecolor'])
        ax.set_facecolor(styler['axis_color'])
        plt.tight_layout()

        # the following should be placed somewhere else.. or should it?
        plot_periods = []
        flag = False
        period = []
        for date, temp in zip(self.dfs.FDdata['date'], self.dfs.FDdata[frost_front]):
            if temp == 0 and flag is False:
                period.append(date)
                flag = True
            elif temp == 0 or np.isnan(temp) and flag is True:
                period.append(date - pd.Timedelta(days=1))
                plot_periods.append(period)
                if temp == 0:
                    period = [date]
                else:
                    flag = False
                    period = []

        # refactoring the frost period function:
        frost_periods = []
        thaw_periods = []
        f_period_locs = []
        f_period_dates = []

        t_period_locs = []
        t_period_dates = []
        for date, floc, tloc in zip(self.dfs.FDdata['date'],
                                    self.dfs.FDdata[frost_front],
                                    self.dfs.FDdata[thaw_front]):

            if np.isnan(floc) and len(f_period_locs) != 0 and date not in self.missing_dates:
                # This is executed when the end of frost period is reached and it is not terminated by missing date
                f_period_locs.append(f_period_locs[-1])
                f_period_dates.append(date + pd.Timedelta(hours=6))
                frost_periods.append([f_period_locs, f_period_dates])
                f_period_locs = []
                f_period_dates = []
            elif np.isnan(floc) and len(f_period_locs) != 0 and date in self.missing_dates:
                # This is executed when teh end of frost period is reached and it is terminated by a missing date
                frost_periods.append([f_period_locs, f_period_dates])
                f_period_locs = []
                f_period_dates = []

            else:
                # This statement is executed when floc != 0
                if len(f_period_locs) == 0 and (date - pd.Timedelta(days=1)) not in self.missing_dates:
                    # This is executed when a new period starts and there ha snot been a missing date before.
                    # If so then on top of the current dates and floc, a zero and date-1 is added to the list.
                    f_period_locs.append(0)
                    f_period_locs.append(floc)
                    f_period_dates.append(date - pd.Timedelta(days=1))
                    f_period_dates.append(date)

                elif len(f_period_locs) == 0 and (date - pd.Timedelta(days=1)) in self.missing_dates:
                    # This is executed when a new period starts, but there has been a missing dates before.
                    # In this case zero and date-1 is not added.
                    f_period_locs.append(floc)
                    f_period_dates.append(date)

                elif len(f_period_locs) != 0:
                    # This is executed when this value is not the first in the frost period.
                    f_period_locs.append(floc)
                    f_period_dates.append(date)
        for period in frost_periods:
            print(period)

        for period in plot_periods:
            mask = (self.dfs.FDdata['date'] >= period[0]) & (self.dfs.FDdata['date'] <= period[1])
            df = self.dfs.FDdata.loc[mask]

            ax.plot_date(df['date'],
                         df[frost_front],
                         marker=None,
                         color=color1,
                         linestyle='solid',
                         linewidth=plotline_width)


        # plot data:
        ax.plot_date([],
                     [],
                     label='frost front',
                     marker=None,
                     color=color1,
                     linestyle='solid',
                     linewidth=plotline_width)
        ax.plot_date(self.dfs.FDdata['date'],
                     self.dfs.FDdata[thaw_front],
                     label='thaw front',
                     marker=None,
                     color=color2,
                     linestyle='solid',
                     linewidth=plotline_width)

        layer_thickness_list = np.ediff1d(interface_list)
        for interface in interface_list:
            ax.plot([self.start_date, self.end_date],
                    [interface, interface],
                    color=styler['aidline_color'],
                    linestyle='--',
                    linewidth=sizer['aidline_width'])
            ax.plot([self.zero_date, self.start_date],
                    [interface, interface],
                    color=styler['aidline_color'],
                    linestyle='solid',
                    linewidth=sizer['aidline_width'])
        ax.plot([self.dfs.start_date, self.dfs.start_date],
                [0, 4],
                color=styler['aidline_color'],
                linestyle='solid',
                linewidth=sizer['aidline_width'])

        for lost_period in self.year_sample['missing_dates']:
            start = lost_period['start_date']
            end = lost_period['end_date']
            ax.axvspan(start, end, facecolor=color4)
        ax.axvspan(np.nan, np.nan, facecolor=color4, label='missing frost data')


        # add text to plot:
        for i in range(len(layer_thickness_list)):
            if layer_thickness_list[i] <= 0.11:
                ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025),
                        layer_names[i][0],
                        fontsize=sizer['text_size'],
                        color=styler['text_color'])
            else:
                ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025 - 0.05),
                        layer_names[i][0],
                        fontsize=sizer['text_size'],
                        color=styler['text_color'])
                ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                        (interface_list[i] + layer_thickness_list[i] / 2 + 0.025 + 0.05),
                        layer_names[i][1],
                        fontsize=sizer['text_size'],
                        color=styler['text_color'])
        ax.text(self.zero_date + datetime.timedelta(self.dfs.days * 0.25 * 0.10),
                (interface_list[-1] + 0.2),
                layer_names[-1][0],
                fontsize=sizer['text_size'],
                color=styler['text_color'])

        if twinx:
            ax.plot(np.nan,
                    marker=None,
                    color=color3,
                    linestyle='solid',
                    linewidth=plotline_width,
                    label='air temperature')

        # PRE-CONFIGURATION (has to be executed before the twinx plot):
        # legend:
        legend = ax.legend(loc='lower left',
                           bbox_to_anchor=(0.13, 0.015),
                           fontsize=sizer['legend_size'],
                           handlelength=sizer['legend_length'],
                           #edgecolor=styler['legend_edge_color'],
                           frameon=False,
                           facecolor=styler['legend_face_color'],
                           labelcolor=styler['legend_text_color'])
        #legend.get_frame().set_linewidth(sizer['legend_frame_width'])
        legend.remove()

        # temperature on plots (secondary axes)
        if twinx:
            # initializer:
            ax_twinx = ax.twinx()

            # plot data:
            ax_twinx.plot_date(self.dfs.ATdata['date'],
                               self.dfs.ATdata['avg'],
                               label='air temperature',
                               marker=None,
                               color=color3,
                               linestyle='solid',
                               linewidth=plotline_width)
            ax_twinx.plot([self.dfs.start_date, self.dfs.end_date],
                          [0, 0],
                          linestyle='solid',
                          color=styler['aidline_color'],
                          linewidth=sizer['aidline_width'])
            ax_twinx.fill_between(self.dfs.ATdata['date'],
                                  self.dfs.ATdata['avg'],
                                  where=self.dfs.boolean_list,
                                  color=color5,
                                  interpolate=True,
                                  alpha=0.7)

            # TWINX CONFIGURATION
            # legend:
            ax_twinx.add_artist(legend)

            # ticks:
            ylim_twin, yticks_twin = self.generate_yaxis_twin_ticks()
            ax_twinx.set_ylim(ylim_twin)
            ax_twinx.set_yticks(yticks_twin)
            ax_twinx.tick_params(direction='in', width=1.5)
            ax_twinx.tick_params(axis='y',
                                 direction='in',
                                 width=sizer['tick_width'],
                                 labelsize=sizer['tick_size'],
                                 length=sizer['tick_length'],
                                 colors=styler['tick_color'])
            ax.tick_params(axis='both',
                           direction='in',
                           width=sizer['tick_width'],
                           labelsize=sizer['tick_size'],
                           length=sizer['tick_length'],
                           colors=styler['tick_color'],
                           top=True,)

            # label:
            ax_twinx.set_ylabel('Temperature, °C',
                                size=sizer['label_size'],
                                color=styler['label_color'])
            ax_twinx.yaxis.set_label_coords(1.05, 0.22)

            # spines:
            for spine in ['top', 'bottom', 'left', 'right']:
                ax_twinx.spines[spine].set_visible(False)

        else:
            # legend:
            ax.add_artist(legend)

            # ticks:
            ax.tick_params(axis='both',
                           direction='in',
                           width=sizer['tick_width'],
                           labelsize=sizer['tick_size'],
                           length=sizer['tick_length'],
                           color=styler['tick_color'],
                           labelcolor=styler['tick_label_color'],
                           right=True,
                           top=True)

        # MAIN CONFIGURATION:
        # ticks:
        ax.set_xlim(self.dfs.zero_date, self.dfs.end_date)
        ax.set_xticks(self.dfs.date_list)
        ax.set_ylim([3, 0])
        ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        plt.setp(ax.get_xticklabels(), rotation=sizer['tick_rotation'], ha='right')

        # label:
        ax.set_ylabel('Depth, m',
                      size=sizer['label_size'],
                      color=styler['label_color'])

        # spines:
        for spine in ['top', 'bottom', 'left', 'right']:
            ax.spines[spine].set_linewidth(sizer['spine_width'])
            ax.spines[spine].set_color(styler['spine_color'])

        # title:
        if title:
            ax.set_title(section_name)

        # save show options:
        if save_fig:
            fig.savefig('out\\' + save_name,
                        dpi=300,
                        bbox_inches='tight',
                        facecolor=fig.get_facecolor())

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
