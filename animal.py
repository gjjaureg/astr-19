import sys

class fox:

	def __init__(self, arms=14.0, legs=14.0, eyes=2, tail=True, fur=True):
		self.arm_length = arms
		self.leg_length = legs
		self.num_eyes = eyes
		self.tail = tail
		self.furry = fur

	def display_info(self):
		print("these are the relevent physical chracteristics of a fox")
		print(f"due to being quadrapedal both the length of arms and legs are the same")
		print(f"legs length: {self.leg_length}")
		print(f"number of eyes: {self.num_eyes}")
		print(f"does it have a tail: {self.tail}")
		print(f"is it a furry creature: {self.furry}")

animal = fox()

animal.display_info()

