from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt


class AirTemperaturePlot:
	def __init__(self,
				 file,
				 FI_on_plots=False,
				 titles_on_plots=False,
				 save_figure=True,
				 show_figure=False):
		self.file = file
		self.FI_on_plots = FI_on_plots
		self.titles_on_plots = titles_on_plots
		self.save_figure = save_figure
		self.show_figure = show_figure

	def plot_air_temperature(self):
		fig, ax = plt.subplots(figsize=(12, 6))

		plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
		ax.tick_params(axis='both', direction='in', width=1, right=True, top=True)
		for j in ['top', 'bottom', 'left', 'right']:
			ax.spines[j].set_linewidth(1)

		ax.plot_date(self.file.ATdata['date'],
					 self.file.ATdata['avg'],
					 label='Air temperature',
					 marker=None,
					 linestyle='solid',
					 linewidth=2.5, color='black')
		ax.plot([self.file.start_date, self.file.date_list[-1]], [0, 0], color='black', linestyle='solid', linewidth=1)
		ax.fill_between(self.file.ATdata['date'],
						self.file.ATdata['avg'],
						label='FI',
						where=self.file.boolean_list,
						color='cornflowerblue',
						interpolate=True)
		ax.fill_between(self.file.ATdata['date'],
						self.file.ATdata['avg'],
						label='TI',
						where=self.file.boolean_list_2,
						color='indianred',
						interpolate=True)

		ax.legend(loc="upper left", bbox_to_anchor=(0, 0.7, 0.3, 0.3))
		ax.set_ylabel('Temperature [°C]', size=10)
		ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
		ax.set_xlim(self.file.date_list[0], self.file.date_list[-1])
		ax.set_xticks(self.file.date_list)
		ax.set_ylim([-20, 20])
		ax.set_yticks(range(-20, 25, 5))

		if self.FI_on_plots == True:
			ax2 = ax.twinx()
			ax2.plot_date(self.file.FIdata['date'],
						  self.file.FIdata['FIcum'] * -1,
						  label='FI cumulative',
						  marker=None,
						  linestyle='dashed',
						  linewidth=2.5,
						  color='black')
			ax2.set_ylim([-8000, 8000])
			ax2.set_yticks(range(0, 9000, 1000))
			ax2.set_ylabel('Freezing index [°C hours]', size=10)
			ax2.yaxis.set_label_coords(1.06, 0.78)
			ax2.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
			ax2.set_xlim(self.file.date_list[0], self.file.date_list[-1])
			ax2.set_xticks(self.file.date_list)
			ax2.legend()

		if self.titles_on_plots == True:
			ax.set_title('Freezing Index', fontweight='bold', fontsize=12)

		if self.save_figure == True:
			fig.savefig('out/air_temperature.png', dpi=300, bbox_inches='tight')

		if self.show_figure == True:
			plt.show()

		plt.close(fig)
