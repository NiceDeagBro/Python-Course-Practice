from dataclasses import dataclass, field
from Task3 import Food, Drink


@dataclass
class Customer:
	__name: str = field(default=0)
	__numberOfCustomers: int = field(default=0)
	__id: int = field(default=0)
	__dateOfBirth: str = field(default="Not assigned")
	__nationality: str = field(default="Not assigned")
	__shopping_list: dict = field(default="Shopping list is empty")

	def __init__(self, name, shopping_list):
		self.__name = name
		self.__shopping_list = shopping_list
		Customer.__numberOfCustomers += 1
		self.__id = (Customer.__numberOfCustomers - 1) + 1

	# method returning id of an instance
	def get_identifier(self):
		return "Id of " + self.__name + " is " + str(self.__id)

	# method returning name and id of an instance
	def get_full_info(self):
		full_info = self.__name + " with id=" + str(self.__id)
		return full_info

	# method assigning the date of birth to the customer instance (returns log of an action)
	def assign_dob(self, new_dob):
		self.__dateOfBirth = new_dob
		print("*Date of birth was set to " + new_dob + "*")

	# method returning the date of birth of the customer instance
	def retrieve_dob(self):
		return "Date of birth of " + self.__name + " is " + self.__dateOfBirth

	# method assigning the nationality to the customer instance (returns log of an action)
	def assign_nationality(self, new_nationality):
		self.__nationality = new_nationality
		print("*Nationality was set to " + new_nationality + "*")

	# method returning the nationality of the customer instance
	def retrieve_nationality(self):
		return "Nationality of " + self.__name + " is " + self.__nationality

	# method returning number of customers
	@staticmethod
	def get_number_of_customers():
		return "Number of customers is " + str(Customer.__numberOfCustomers)


c1 = Customer("Jonas Jonaitis", [Food("Bread", 2, 1.3), Drink("CocaCola", 3, 1.7)])

print(c1.get_full_info)