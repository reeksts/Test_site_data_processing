import pandas as pd

class SampleDataE6:
	def __init__(self):
		self.year_2018_2019 = {'dir': ''}

		self.year_2019_2020 = {'dir': 'C:\\Users\\karlisr\\OneDrive - NTNU\\2_PostDoc_NTNU\\'
									  '06_E6_project_Reports_and_data\\3_frost_penetration_and_FI\\year_2019_2020\\'}

		self.year_2020_2021 = {'dir': 'C:\\Users\\karlisr\\OneDrive - NTNU\\2_PostDoc_NTNU\\'
									  '06_E6_project_Reports_and_data\\3_frost_penetration_and_FI\\year_2020_2021\\',
							   'start_date': pd.Timestamp(2020, 10, 1),
							   'end_date': pd.Timestamp(2021, 2, 11),
							   'lost_data': [{'start_date': pd.Timestamp(2021, 1, 14),
											  'end_date': pd.Timestamp(2021, 2, 9)}]}