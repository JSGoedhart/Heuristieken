weight_cap = 11895
volume_cap = 72.05

# define class for cargo's
class cargo1:
	def __init__(self, number, kg, m3):
		self.number = number
		self.kg = int(kg)
		self.m3 = float(m3)
		self.valkg = float(kg/weight_cap)*100
		self.valm3 = float(m3/volume_cap)*100
		self.valtot = self.valkg + self.valm3

# define class for spacecrafts
class spacecraft:
	def __init__(self, name, kg, m3):
		self.name = name
		self.kg = kg
		self.m3 = m3
