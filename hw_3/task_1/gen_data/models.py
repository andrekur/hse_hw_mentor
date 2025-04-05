import random
from datetime import date
from datetime import timedelta
from datetime import datetime as dt

from faker import Faker
from faker_commerce import Provider
import numpy


class BaseFakeGenClass:
	def __init__(self) -> None:
		self.model_name = None
		self._fake = Faker()
		self._fake.add_provider(Provider)

	def _prepared_gen(self, *args, **kwargs):
		return []

	def _after_gen(self, result, *args, **kwargs):
		return result

	def gen_data(self, count=0):
		""" return: [{}, ...] """
		result = self._prepared_gen()

		for _ in range(count):
			result.append({
				field: getattr(self, f'{field}_gen_func')() if getattr(self, f'{field}_gen_func') else None
				for field in self.fields
			})

		return self._after_gen(result)

	def _prepared_array_gen(self, *args, **kwargs):
		return []

	def _after_array_gen(self, result, *args, **kwargs):
		return result

	def gen_array_data(self, count=0, with_headers=False):
		""" return: [[], ...] """
		result = self._prepared_array_gen()

		for _ in range(count):
			result.append([
				getattr(self, f'{field}_gen_func')() if hasattr(self, f'{field}_gen_func') else None
				for field in self.fields
			])
		result = self._after_array_gen(result)

		return [[item for item in self.fields], *result[:]] if with_headers else result
	
	def export_to_txt(self, data, path=None):
		path = f'../data/{self.model_name}_data.csv' if not path else path
		arr = numpy.asarray(data)
		numpy.savetxt(path, arr, delimiter=',', fmt='%s')


class Logs(BaseFakeGenClass):
	def __init__(self, start_log_id=1, transaction_ids=[]) -> None:
		self.fields = ('log_id', 'transaction_id', 'category', 'comment', 'log_timestamp', )
		self.colum_id = None
		self._start_log_id = start_log_id
		self._transaction_ids = transaction_ids

		self._base_categories = [
			'Home Appliances',
			'Fashion',
			'Beauty Products',
			'Sports Gear',
			'Electronics',
			'Books',
			'Toys',
			'Automotive Accessories',
			'Gardening Supplies',
			'Health'
		]

		super().__init__()
		self.model_name = 'Logs'


	def category_gen_func(self):
		return random.choice(self._base_categories)

	def comment_gen_func(self):
		return str(self._fake.text(100)).replace(',', '')

	def log_timestamp_gen_func(self):
		return self._fake.date_time_between(start_date=date(2022, 1, 1), end_date=date(2025, 1, 1))

	def _after_array_gen(self, result, *args, **kwargs):
		for i, item in enumerate(result):
			item[0] = self._start_log_id + i
			item[1] = random.choice(self._transaction_ids)

		return result


class Transactions(BaseFakeGenClass):
	def __init__(self, start_transaction_id=1) -> None:
		self.fields = ('transaction_id', 'user_id', 'amount', 'currency', 'transaction_date', 'is_fraud', )
		self.colum_id = None
		self._start_transaction_id = start_transaction_id
		self._currencies = ['RUB', 'USD', 'EUR', 'CNY', 'JPY', 'GBP']

		super().__init__()
		self.model_name = 'Transactions'


	def user_id_gen_func(self):
		return random.randint(100, 10000)

	def amount_gen_func(self):
		return (random.randint(100, 10000)  + random.randint(0, 10) % 10) * (-1 if random.randint(0, 1) else 1)

	def currency_gen_func(self):
		return random.choice(self._currencies)

	def transaction_date_gen_func(self):
		return self._fake.date_time_between(start_date=date(2022, 1, 1), end_date=date(2025, 1, 1))
	
	def is_fraud_gen_func(self):
		return random.randint(0, 1)

	def _after_array_gen(self, result, *args, **kwargs):
		for i, item in enumerate(result):
			item[0] = self._start_transaction_id + i

		return result
