class increment:
	def __init__(self, ini_count = 0):
		self.__count = ini_count
	
	def assign(self):
		self.__count += 1
		return self.__count - 1

def return_empty_list_of_lists(number_of_lists = 0):
	return [[] for i in range(number_of_lists)]

def get_n_digits(number, n = 2):
	mul = 1
	number_of_digits = 0
	
	while mul <= number:
		mul *= 10
		number_of_digits += 1

	difference = n - number_of_digits

	str_number = ''

	if difference >= 0:
		for i in range(difference):
			str_number += '0'
		str_number += str(number)
	else:
		difference *= -1
		mul = 1
		for i in range(difference):
			mul *= 10
		str_number = str(number % mul)

	return str_number