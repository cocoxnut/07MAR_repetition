words = ["man", "woman", "child", "parents", "siblings", "friend", "girlfriend", "boyfriend", "ancestors", 
"islam", "ortodox", "catholic", "protestant", "buddhist", "jidaism", "atheist", "induism", "sintoism", 
"milkyway", "venus", "mars", "earth", "mercury", "neptune", "saturn", "jupiter", "uranus", 
"mercedes", "honda", "toyota", "lexus", "renault", "hyundai", "citroen", "nissan", "kia", 
"flora", "fauna", "environment", "pollution", "deoxidization", "gas", "minerals", "mining", "mountains"]

love = []
religion = []
space = []
cars = []
nature = []

for i in words:
	if i in range(0, 8):
		love.append(i)
		print(love)
	if i in range(9, 17):
		religion.append(i)
		print(religion)
	if i in range(18, 26):
		space.append(i)
		print(space)
	if i in range(27, 35):
		cars.append(i)
		print(cars)
	if i in range(36, 44):
		nature.append(i)
		print(nature)
