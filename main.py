import pandas as pd
from modules.SectionParametersE6 import SectionParameters
from modules.FilesAndDates import FilesAndDates
from modules.FrostDepthPlot import FrostDepthPlot
from modules.FreezingIndexPlot import FreezingIndexPlot
from modules.AirTemperaturePlot import AirTemperaturePlot
from modules.TemperatureGradientPlot import TemperatureGradientPlot
from modules.SampleDataE6 import SampleDataE6

# Comments to fix:
# maybe when plotting the data should also be fixed to teh input start_data and end_data
# maybe change the end_date to end_date_plot
# and probabaly also change zero_date to zero_date_plot

# INPUT VALUES ARE HERE:
start_date = pd.Timestamp(2020, 10, 1)
end_date = pd.Timestamp(2021, 1, 10)

file1 = 'frost_front_progression.xlsx'
file2 = 'air_temperature.xlsx'
file3 = 'freezing_index.xlsx'

sample_data = SampleDataE6()

filename1 = sample_data.year_2020_2021['dir'] + file1
filename2 = sample_data.year_2020_2021['dir'] + file2
filename3 = sample_data.year_2020_2021['dir'] + file3

# Load parameter initialization
section_parameters = SectionParameters()

# Initialize files and dates
files_and_dates = FilesAndDates(start_date, end_date, filename1, filename2, filename3)

# Plot frost depth figures
frost_depth = FrostDepthPlot(files_and_dates)
frost_depth.plot_frost_depth(*section_parameters.section_F1_args)
frost_depth.plot_frost_depth(*section_parameters.section_F2_args)
frost_depth.plot_frost_depth(*section_parameters.section_F3_args)
frost_depth.plot_frost_depth(*section_parameters.section_F4_args)
frost_depth.plot_frost_depth(*section_parameters.section_F5_args)
frost_depth.plot_frost_depth(*section_parameters.section_F6_args)
frost_depth.plot_frost_depth(*section_parameters.section_F7_args)

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
