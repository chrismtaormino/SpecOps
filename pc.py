from Weapon import Weapon;
from ArmorSet import ArmorSet;

class playerCharacter(object):
	def __init__(self):
		self.health = 10;
		self.armor = ArmorSet();
		self.primary = PrimaryWeapon();
		self.special = SpecialWeapon();
		self.gold = 0;
	