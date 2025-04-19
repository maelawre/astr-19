import random

#create class for favorite animal
class favAnimal: 

	#initialize instance
	def __init__(self, name="missingno", arms=[], legs=[], eyes=[],
		tail = False, fur = False):
		self.name = name
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.fur = fur

	def fur_and_tail(self):
		if self.tail == False :
			print(f"{self.name}s do not have tails")
		elif self.tail == True: 
			print(f"{self.name}s have tails")


		if self.fur == False: 
			print(f"{self.name}s do not have fur")
		elif self.fur ==True: 
			print(f"{self.name}s have fur. ")
