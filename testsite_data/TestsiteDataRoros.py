import pandas as pd

class TestsiteDataRoros:
	def __init__(self):
		self.testsite_dir = {'name': 'Roros',
							 'dir': 'C:\\Users\\karlisr\\OneDrive - NTNU\\6_Project_Repos\\Test_site_data_processing\\'
									'input\\Roros'}

		self.year_2018_2019 = {'year_name': 'rrrr2018/2019',
							   'dir': ''}

		self.year_2019_2020 = {'year_name': 'rrrr2019/2020',
							   'dir': ''}

		self.year_2020_2021 = {'year_name': 'rrrr2020/2021',
							   'dir': ''}

		self.year_list = [self.year_2018_2019,
						  self.year_2019_2020,
						  self.year_2020_2021]