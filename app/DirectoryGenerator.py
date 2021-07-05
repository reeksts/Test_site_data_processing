import os


class DirectoryGenerator:
	def __init__(self):
		self.output_dir = 'C:\\Users\\karlisr\\OneDrive - NTNU\\6_Project_Repos\\Test_site_data_processing\\output\\'

	def generate_directories(self, testsite):
		parent_dir = self.output_dir + testsite.testsite_dir['name'] + '\\'

		# child subdirectories:
		regular_plots = 'regular_plots\\'
		animated_plots = 'animated_plots\\'
		child_subdirectories = [regular_plots, animated_plots]

		# Generate sample parent directory:
		if not os.path.exists(parent_dir):
			os.mkdir(parent_dir)

		# Generate child (regular, animated..)
		for child_dir in child_subdirectories:
			if not os.path.exists(parent_dir + child_dir):
				os.mkdir(parent_dir + child_dir)

	def small_test_directories(self):
		general_path = self.sample['path']  # this is a general path to large_test
		figure_output_dir = '02_measurement_figures\\'
		figure_output_path = general_path + figure_output_dir
		sample_name = self.sample['sample_name']
		self.sample = self.sample

		# child subdirectories:
		time_series_plots = '01_time_series_plots\\'
		temperature_gradient_plots = '02_temperature_gradient_plots\\'
		animated_gradient = '03_animated_gradient'
		child_subdirectories = [time_series_plots,
								temperature_gradient_plots,
								animated_gradient]

		# Generate sample parent directory:
		parent_dir = sample_name + '\\'
		if not os.path.exists(figure_output_path + parent_dir):
			os.mkdir(figure_output_path + parent_dir)

		# Generate sample child directories (MASTER, PHASE1, PHASE2.. etc):
		child_dir_names = ['PHASE_MASTER\\']
		phase_num = 1
		for phases in self.sample['phases']:
			child_dir = 'PHASE' + str(phase_num) + '_' + phases['name'] + '\\'
			child_dir_names.append(child_dir)
			if not os.path.exists(figure_output_path + parent_dir + child_dir):
				os.mkdir(figure_output_path + parent_dir + child_dir)
			phase_num += 1
		phase_master = 'PHASE_MASTER\\'
		if not os.path.exists(figure_output_path + parent_dir + phase_master):
			os.mkdir(figure_output_path + parent_dir + phase_master)

		# Generate sample child subdirectories (01_combined.., 02_time_series.., etc):
		for child_dir in child_dir_names:
			for child_sub_dir in child_subdirectories:
				if not os.path.exists(figure_output_path + parent_dir + child_dir + child_sub_dir):
					os.mkdir(figure_output_path + parent_dir + child_dir + child_sub_dir)


	def return_phase_directories(self):
		phase_directories = []
		phase_num = 1
		for phases in self.sample['phases']:
			child_dir = 'PHASE' + str(phase_num) + '_' + phases['name'] + '\\'
			phase_directories.append(child_dir)
		return phase_directories
