class ArmorSet(Object):
	def __init__(self):
		self.helm = Helm();
		self.primaryArm = Arm();
		self.specialArm = Arm();
		self.chestPlate = Plate();
		self.leftLeg = Leg();
		self.rightLeg = Leg();
		
	def getHelm():
		return self.helm;
	def getPrimaryArm():
		return self.primaryArm;
	def getSpecialArm():
		return self.specialArm
	def getChestPlate():
		return self.chestPlate;
	def getLeftLeg():
		return self.leftLeg;
	def getRightLeg():
		return self.rightLeg;