import pandas as pd

class TestsiteDataE6:
	def __init__(self):
		self.testsite_dir = {'name': 'Trondheim_E6',
							 'dir': 'C:\\Users\\karlisr\\OneDrive - NTNU\\6_Project_Repos\\E6_SVV_field_meausrements\\'
									  'input\\Trondheim_E6'}

		self.year_2018_2019 = {'year_name': '2018/2019',
							   'dir_name': 'year_2018_2019'}

		self.year_2019_2020 = {'year_name': '2019/2020',
							   'dir_name': 'year_2019_2020'}

		self.year_2020_2021 = {'year_name': '2020/2021',
							   'dir_name': 'year_2019_2020',
							   'start_date': pd.Timestamp(2020, 10, 1),
							   'end_date': pd.Timestamp(2021, 3, 16),
							   'missing_dates': [{'start_date': pd.Timestamp(2021, 1, 14),
											      'end_date': pd.Timestamp(2021, 2, 9)},
											     {'start_date': pd.Timestamp(2021, 2, 22),
											      'end_date': pd.Timestamp(2021, 3, 9)}]}

		self.year_list = [self.year_2018_2019,
						  self.year_2019_2020,
						  self.year_2020_2021]
