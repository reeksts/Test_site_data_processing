import pandas as pd

class TestsiteDataSweden:
	def __init__(self):
		self.testsite_dir = {'name': 'Sweden',
							 'dir': 'C:\\Users\\karlisr\\OneDrive - NTNU\\6_Project_Repos\\E6_SVV_field_meausrements\\'
									'input\\Sweden'}

		self.year_2018_2019 = {'year_name': 'ssss2018/2019',
							   'dir': ''}

		self.year_2019_2020 = {'year_name': 'ssss2019/2020',
							   'dir': ''}

		self.year_2020_2021 = {'year_name': 'ssss2020/2021',
							   'dir': ''}

		self.year_list = [self.year_2018_2019,
						  self.year_2019_2020,
						  self.year_2020_2021]