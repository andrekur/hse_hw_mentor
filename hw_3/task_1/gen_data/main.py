from models import (Logs, Transactions)

if __name__ == '__main__':
	#TODO прикрутить авто загруку в облако по API


	transaction = Transactions()
	transaction_data = transaction.gen_array_data(1000, True)
	transaction.export_to_txt(transaction_data)

	log = Logs(transaction_ids=[item[0] for item in transaction_data])
	log_data = log.gen_array_data(1000, True)
	log.export_to_txt(log_data)
