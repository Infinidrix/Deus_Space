def sCreation(initial_choice): #Takes in the initial choice of the user as an int. (0 - Collision, 1 - Nearby Supernova, 2 - Black hole)
	output = {}
	starSize = [small, medium, large]
	if initial_choice = 0: starsize.pop[-1]
	elif initial_choice = 1: starsize.pop[0]
	#Mass, temperature, Luminious Intensity, Radius
	output = {
	  "Small": [("1.35*10^30 - 41.2*10^30"), (f"{.85*15} MK - {1.15*15} MK"), ("3.828×10^22 W - 3.828×10^23 W"), (f"- {0.7*7}x10^8 M")],
	  "Medium": [("1.35*10^30 - 41.2*10^30"),(f"{.85*200} MK - {1.15*200} MK"), (f"{.85*3.828}×10^26 W - {1.15*3.828}×10^26 W"), (f"{0.7*7}x10^8 M - {4.5*7}x10^8 M")]
	  "Large": [("1.35*10^30 - 41.2*10^30"),(f"{.85*600} MK - {1.15*600} MK"), ("3.828×10^29 W - 3.828×10^30 W"), (f"{0.7*7}x10^8 M - {4.5*7}x10^8 M")]
	}
	return starSize, output

	#What did you think about the Brown Dwarfs? Add to Extras

class Star:
	def __init__(self, Mass, Temp, Luminious_Int, Radius):
		self.setMass(Mass)
		self.setTemp(Temp)
		self.setLum(Luminious_Int)
		self.setRadius(Radius)
	def setMass(i): self.mass = i
	def getMass(): return self.mass
	def setLum(i): self.lum = i
	def getLum(): return self.lum
	def setRadius(i): self.size = i
	def getRadius(): return self.size
	






