# define class for cargo's
class cargo1:
	def __init__(self, number, kg, m3):
		self.number = number
		self.kg = int(kg)
		self.m3 = float(m3)
		self.valkg = float(kg/11895)*100
		self.valm3 = float(m3/72.05)*100

# define class for spacecrafts
class spacecraft:
	def __init__(self, name, kg, m3):
		self.name = name
		self.kg = kg
		self.m3 = m3
