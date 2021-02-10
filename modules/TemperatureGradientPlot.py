import matplotlib.pyplot as plt


class TemperatureGradientPlot:
	def __init__(self,
				 file,
				 titles_on_plots=False,
				 save_figure=True,
				 show_figure=False):
		self.file = file
		self.title_on_plots = titles_on_plots
		self.save_figure = save_figure
		self.show_figure = show_figure

	def plot_temperature_gradient(self,
								  dates,
								  columns,
								  frost_front,
                         		  thaw_front,
                         		  interaface_list,
                         		  layer_names,
                         		  layer_thick,
                         		  title,
                         		  save_name):
		# initializer:
		fig, ax = plt.subplots(figsize=(12, 6))

		for i in dates:
			print(self.file.FDdata[self.file.FDdata['date'] == i][columns].values)