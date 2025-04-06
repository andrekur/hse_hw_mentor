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


class Orders(BaseFakeGenClass):
	def __init__(self, start_order_id=1) -> None:
		self.fields = ('order_id', 'user_id', 'order_date', 'total_amount', 'payment_status', )
		self.colum_id = None
		self._start_order_id = start_order_id
		self._statuses = ('paid', 'pending', 'cancelled',)

		super().__init__()
		self.model_name = 'Orders'


	def user_id_gen_func(self):
		return random.randint(1, 1000)

	def order_date_gen_func(self):
		return self._fake.date_time_between(start_date=date(2025, 1, 1), end_date=date(2025, 5, 6))

	def comment_gen_func(self):
		return str(self._fake.text(100)).replace(',', '')

	def total_amount_gen_func(self):
		return random.randint(100, 10000)  + random.randint(0, 10) % 10

	def payment_status_gen_func(self):
		return random.choice(self._statuses)

	def _after_array_gen(self, result, *args, **kwargs):
		for i, item in enumerate(result):
			item[0] = self._start_order_id + i

		return result


class OrderItems(BaseFakeGenClass):
	def __init__(self, order_ids, start_oi_id=1) -> None:
		self.fields = ('item_id', 'order_id', 'product_name', 'product_price', 'quantity',)
		self.colum_id = None
		self._order_ids = order_ids
		self._start_oi_id= start_oi_id

		super().__init__()
		self.model_name = 'OrderItems'


	def order_id_gen_func(self):
		return random.choice(self._order_ids)

	def product_name_gen_func(self):
		return self._fake.text(12).replace(',', '').replace('.', '')

	def product_price_gen_func(self):
		return random.randint(100, 1000)  + random.randint(0, 10) % 10

	def transaction_date_gen_func(self):
		return self._fake.date_time_between(start_date=date(2022, 1, 1), end_date=date(2025, 1, 1))

	def quantity_gen_func(self):
		return random.randint(1, 100)

	def _after_array_gen(self, result, *args, **kwargs):
		for i, item in enumerate(result):
			item[0] = self._start_oi_id + i

		return result
