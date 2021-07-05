class FigureFormatting:
	def __init__(self):
		inch=2.54
		pres_scaler = 1.2

		self.dark = []
		self.ligth = []

		# What colors should styler change
			# plot background
			# axes background
			# all text color
			# legend text color
			# legend background
			#

		self.styler = {'light': {'name': 'light',
								 'facecolor': 'white',
								 'axis_color': 'white',
								 'label_color': 'black',
								 'tick_color': 'black',
								 'tick_label_color': 'black',
								 'spine_color': 'black',
								 'axis_label_color': 'black',
								 'text_color': 'black',
								 'aidline_color': 'black',
								 'legend_text_color': 'black',
								 'legend_edge_color': 'white',
								 'legend_face_color': 'white',
								 'legend_framealpha': 0.8,
								 'legend_edge_color_rgba': (0, 0, 0, 0),
								 'legend_face_color_rgba': (1, 1, 1, 0.5)},
					   'dark': {'name': 'dark',
						        'facecolor': 'black',
								'axis_color': 'black',
								'label_color': 'white',
								'tick_color': 'white',
								'tick_label_color': 'white',
								'spine_color': 'white',
								'axis_label_color': 'white',
								'text_color': 'white',
								'aidline_color': 'white',
								'legend_text_color': 'white',
								'legend_edge_color': 'white',
								'legend_face_color': 'black',
								'legend_framealpha': 0.5,
								'legend_edge_color_rgba': (1, 1, 1, 0),
								'legend_face_color_rgba': (0, 0, 0, 0.5)}}

		self.paper_full_width_tall = {'figsize': (16/inch, 10/inch),
										 	  'legend_size': 8,
										 	  'label_size': 8,
										      'tick_size': 8,
										      'tick_length': 3,
										      'tick_width': 1,
										      'tick_rotation': 45,
								              'spine_width': 1,
										      'line_width': 1,
											  'aidline_width': 0.7,
										      'legend_length': 3,
										      'labelpad': 3,
										      'legend_frame_width': 0.5,
										      'text_size': 5}

		self.pres_full_width_tall = {'figsize': (pres_scaler*16 / inch, pres_scaler*10 / inch),
									 'legend_size': 8,
									 'label_size': 8,
									 'tick_size': 8,
									 'tick_length': 3,
									 'tick_width': 0.5,
									 'tick_rotation': 45,
									 'spine_width': 0.5,
									 'line_width': 1,
									 'aidline_width': 0.5,
									 'legend_length': 3,
									 'labelpad': 3,
									 'legend_frame_width': 0.5,
									 'text_size': 5}