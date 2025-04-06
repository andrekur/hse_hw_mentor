from models import (Orders, OrderItems)

if __name__ == '__main__':
	order = Orders()
	order_data = order.gen_array_data(100000, False)
	order.export_to_txt(order_data)

	order_item = OrderItems(order_ids=[item[0] for item in order_data])
	order_item_data = order_item.gen_array_data(100000, False)
	order_item.export_to_txt(order_item_data)
