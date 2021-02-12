import pandas as pd
from section_parameters.SectionParametersE6 import SectionParametersE6
from modules.FilesAndDates import FilesAndDates
from modules.FrostDepthPlot import FrostDepthPlot
from modules.FreezingIndexPlot import FreezingIndexPlot
from modules.AirTemperaturePlot import AirTemperaturePlot
from modules.TemperatureGradientPlot import TemperatureGradientPlot
from sample_data.SampleDataE6 import SampleDataE6

# Comments to fix:
# maybe when plotting the data should also be fixed to teh input start_data and end_data
# maybe change the end_date to end_date_plot
# and probably also change zero_date to zero_date_plot

# Selection of test site to analyse:
section_parameters = SectionParametersE6()

# Selection of year to analyse
sample_data = SampleDataE6()
year_sample =  sample_data.year_2020_2021

# INPUT VALUES ARE HERE:
start_date = year_sample['start_date']
end_date = year_sample['end_date']

file1 = 'frost_front_progression.xlsx'
file2 = 'air_temperature.xlsx'
file3 = 'freezing_index.xlsx'

filename1 = sample_data.year_2020_2021['dir'] + file1
filename2 = sample_data.year_2020_2021['dir'] + file2
filename3 = sample_data.year_2020_2021['dir'] + file3

# Initialize files and dates
files_and_dates = FilesAndDates(start_date, end_date, filename1, filename2, filename3)

# Plot frost depth figures
frost_depth = FrostDepthPlot(files_and_dates)
def printingstuff():
	for section in section_parameters.section_list:
		frost_depth.plot_frost_depth(section_name=section['section_name'],
									 save_name=section['save_name'],
									 frost_front=section['frost_front'],
									 thaw_front=section['thaw_front'],
									 interface_list=section['interface_list'],
									 layer_names=section['layer_names'])
printingstuff()
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
