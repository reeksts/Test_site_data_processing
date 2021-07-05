import pandas as pd
import os
from section_parameters.SectionParametersE6 import SectionParametersE6
from modules.FilesAndDates import FilesAndDates
from modules.FrostDepthPlot import FrostDepthPlot
from modules.FigureFormatting import FigureFormatting
from modules.AnimatorPlots import AnimatorPlots
from modules.FreezingIndexPlot import FreezingIndexPlot
from modules.AirTemperaturePlot import AirTemperaturePlot
from modules.TemperatureGradientPlot import TemperatureGradientPlot
from testsite_data.TestsiteDataE6 import SampleDataE6

# Comments to fix:
# maybe when plotting the data should also be fixed to teh input start_data and end_data
# maybe change the end_date to end_date_plot
# and probably also change zero_date to zero_date_plot

# Selection of test site to analyse:
section_parameters = SectionParametersE6()

# Selection of year to analyse
sample_data = SampleDataE6()
year_sample = sample_data.year_2020_2021

# INPUT VALUES ARE HERE:
start_date = year_sample['start_date']
end_date = year_sample['end_date']

file1 = 'frost_front_progression.xlsx'
file2 = 'air_temperature.xlsx'
file3 = 'freezing_index.xlsx'

filename1 = sample_data.year_2020_2021['dir'] + file1
filename2 = sample_data.year_2020_2021['dir'] + file2
filename3 = sample_data.year_2020_2021['dir'] + file3

# Plot formatter
formatter = FigureFormatting()
sizer = formatter.paper_full_width_tall
styler = formatter.styler['light']
#sizer = formatter.paper_full_width_tall
#styler = formatter.styler['light']


# Initialize files and dates
files_and_dates = FilesAndDates(start_date, end_date, filename1, filename2, filename3)

# Plot frost depth figures
frost_depth = FrostDepthPlot(files_and_dates, year_sample)


def printingstuff():
	for section in section_parameters.section_list:  # [-1:]
		frost_depth.plot_frost_depth(sizer,
									 styler,
									 section_name=section['section_name'],
									 save_name=section['save_name'],
									 frost_front=section['frost_front'],
									 thaw_front=section['thaw_front'],
									 interface_list=section['interface_list'],
									 layer_names=section['layer_names'])
#printingstuff()


# Animated figure control
os.chdir('C:\\Users\\karlisr\\OneDrive - NTNU\\6_Project_Repos\\E6_SVV_field_meausrements\\')

df = pd.read_excel('hourly_measurements_Roros.xlsx',
                   sheet_name='sheet1',
                   index_col=0)
# start 03/12/2020  00:30:00
# end 08/04/2021  23:30:00

Ro1_sensors = ['Ro1-9', 'Ro1-8', 'Ro1-7', 'Ro1-6', 'Ro1-5', 'Ro1-4', 'Ro1-3', 'Ro1-2', 'Ro1-1']
start = pd.Timestamp(2020, 12, 3, 0, 30, 0)
end = pd.Timestamp(2021, 2, 3, 23, 30, 0)

subset = df.loc[start:end][Ro1_sensors]
Ro1_interface = [0, 19, 90, 175]
# 0 - top of asphalt
# 19 - base/subbase interface
# 90 - subbbase/frost protection interafce
# 175 - frost protectionm/subgrade interface

def plot_with_animator():
	animator = AnimatorPlots()
	animator.animated_gradient(sizer,
							   styler,
							   subset,
							   Ro1_interface)


plot_with_animator()



'''
# Plot freezing index figures
freezing_index = FreezingIndexPlot(files_and_dates)
freezing_index.plot_freezing_index()

# Plot air temperature figure
air_temperature = AirTemperaturePlot(files_and_dates)
air_temperature.plot_air_temperature()

# Plot temperature gradient figures
dates = [pd.Timestamp(2020, 10, 1),
		 pd.Timestamp(2020, 10, 2),
		 pd.Timestamp(2020, 10, 3),
		 pd.Timestamp(2020, 10, 4),
		 pd.Timestamp(2020, 10, 5)]
columns = ['F6_TC_10',
		   'F6_TC_9',
		   'F6_TC_8',
		   'F6_TC_7',
		   'F6_TC_6',
		   'F6_TC_5',
		   'F6_TC_4',
		   'F6_TC_3',
		   'F6_TC_2',
		   'F6_TC_1']
temperature_gradient = TemperatureGradientPlot(files_and_dates)
temperature_gradient.plot_temperature_gradient(dates, columns, *section_parameters.section_F1_args)
'''
