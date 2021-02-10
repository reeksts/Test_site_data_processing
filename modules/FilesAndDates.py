import pandas as pd
import datetime
import math

class FilesAndDates:
	def __init__(self, start_date, end_date, filename1, filename2, filename3):
		"""
		filename1 - frost depth data file
		filename2 - air temperature data file
		filename2 - freezing index data file
		FDdata: frost depth data
		ATdata: air temperature data
		FIdata: freezing index data
		"""
		self.start_date = start_date
		self.end_date = end_date

		# Loading frost depth data
		self.FDdata = pd.read_excel(filename1, sheet_name='Sheet1', skiprows=[1])
		self.FDdata['date'] = pd.to_datetime(self.FDdata['date'])

		time_delta = end_date - start_date
		base_division = 12
		step_size = math.ceil(time_delta.days / base_division)
		self.days = step_size * base_division

		self.date_list = []
		for i in range(self.days + 1):
			if i % step_size == 0:
				self.date_list.append(self.start_date + datetime.timedelta(i))
		self.end_date = self.start_date + datetime.timedelta(self.days)
		self.zero_date = self.start_date - datetime.timedelta(self.days * 0.15)

		# Loading air temperature data
		self.ATdata = pd.read_excel(filename2, sheet_name='Sheet1')
		self.ATdata['date'] = pd.to_datetime(self.ATdata['date'])
		mask = (self.ATdata['date'] >= self.start_date) & (self.ATdata['date'] <= self.end_date)
		self.ATdata = self.ATdata.loc[mask]

		self.boolean_list = []
		for i in self.ATdata['avg']:
			if i <= 0:
				self.boolean_list.append(True)
			else:
				self.boolean_list.append(False)

		self.boolean_list_2 = []
		for i in self.ATdata['avg']:
			if i >= 0:
				self.boolean_list_2.append(True)
			else:
				self.boolean_list_2.append(False)

		# Loading freezing index data
		self.FIdata = pd.read_excel(filename3, sheet_name='Sheet1')
		self.FIdata['date'] = pd.to_datetime(self.FIdata['date'])