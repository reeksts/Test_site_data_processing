from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.ticker import FormatStrFormatter
from math import ceil, floor
import numpy as np


class AnimatorPlots:
    def __init__(self):
        pass

    def animated_gradient(self,
                          sizer,
                          styler,
                          df,
                          interface_list):

        # initializer:
        fig, ax = plt.subplots(figsize=sizer['figsize'])
        fig.patch.set_facecolor(styler['facecolor'])
        ax.set_facecolor(styler['axis_color'])
        plt.tight_layout()

        # plot main data:
        line, = ax.plot([], [], lw=2)
        ax.plot([-10, 10], [-100, -100], lw=2)
        date_text = ax.text(0, 100, '')

        # plot additional data:
        ax.plot([0, 0],
                [250, 0],
                linestyle='--',
                lw=sizer['line_width'],
                color=styler['aidline_color'])
        xlim, xticks, plot_lim_right = self.generate_xaxis_ticks(df)
        ax.plot([plot_lim_right, plot_lim_right],
                [250, 0],
                lw=sizer['line_width'],
                color=styler['aidline_color'])
        for interface in interface_list[1:]:
            ax.plot([])

        # MAIN CONFIGURATION:
        # ticks:
        ax.invert_yaxis()
        ax.set_xlim(xlim)
        ax.set_xticks(xticks)
        ax.set_ylim([250, 0])
        ax.set_yticks([250, 200, 150, 100, 50, 0])
        ax.tick_params(axis='both',
                       direction='in',
                       width=sizer['tick_width'],
                       right=True,
                       top=True,
                       labelsize=sizer['tick_size'],
                       length=sizer['tick_length'],
                       color=styler['tick_color'],
                       labelcolor=styler['tick_label_color'])
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        ax.set_xlabel('Temperature, °C',
                      size=sizer['label_size'],
                      color=styler['label_color'],
                      labelpad=sizer['labelpad'])
        ax.set_ylabel('Depth, cm',
                      size=sizer['label_size'],
                      color=styler['label_color'],
                      labelpad=sizer['labelpad'])

        # legend
        legend = ax.legend(loc='lower left',
                           fontsize=sizer['legend_size'],
                           handlelength=sizer['legend_length'],
                           labelcolor=styler['legend_text_color'],
                           edgecolor=styler['legend_edge_color'])
        legend.get_frame().set_linewidth(sizer['legend_frame_width'])
        legend.get_frame().set_alpha(None)
        legend.get_frame().set_facecolor(styler['legend_face_color_rgba'])

        # spines:
        for spine in ['top', 'bottom', 'left', 'right']:
            ax.spines[spine].set_linewidth(sizer['spine_width'])
            ax.spines[spine].set_color(styler['spine_color'])


        # initialization function: plot the background of each frame
        def init():
            line.set_data([], [])
            return line,

        # animation function of dataframes' list
        def animate(i):
            name = df.iloc[i].name
            year = name.year
            month = name.month
            day = name.day
            date_text.set_text(str(year) + '-' + str(month) + '-' + str(day))
            line.set_data(df.iloc[i], [1, 5, 19, 60, 90, 122, 175, 200, 223])
            return line,

        # call the animator, animate every 300 ms
        # set number of frames to the length of your list of dataframes
        anim = animation.FuncAnimation(fig, animate, frames=len(df), init_func=init, interval=50, blit=True)
        anim.save('basic_animation.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

        plt.show()

    def generate_xaxis_ticks(self, df):
        max_val = df.max().max()
        min_val = df.min().min()

        def roundup_max(val):
            return int(ceil(val / 5) * 5)

        def rounddown_min(val):
            return int(floor(val / 5) * 5)

        max_val = roundup_max(max_val)
        min_val = rounddown_min(min_val)

        offset = (max_val - min_val) * 0.02
        layer_width = ((max_val + offset) - (min_val - offset))*0.20

        plot_lim_left = min_val - offset
        plot_lim_right = max_val + offset
        layer_lim_right = max_val + offset + layer_width

        xlim = [plot_lim_left, layer_lim_right]
        xticks = np.arange(min_val, max_val + 5, 5)

        return xlim, xticks, plot_lim_right

    def generate_yaxis_ticks(self):
        pass