orm = int(input("Select preferred RAM size: 4 or 8 GB: "))
ssd = int(input("Select 1 if SSD, Select 0 if HDD: "))
hard = int(input("Select memory size: 256, 512, 1024: "))
condition = int(input("Select 1 if NEW, Select 0 if USED: "))
price = int(input("Select your price: "))

hp = 'Hp 550x 1000$ 8Gb 256SSD новый'
samsung = 'Samsung 150 Turbo 900$ 8Gb 256SSD б/у'
acer = 'Acer Predator 600$ 4Gb 1024HDD новый'
asus = 'Asus 550x 300$ 4Gb 1024HDD б/у'

if orm == 4 and hard >= 256 and ssd == False and price >= 300 and condition == False:
    print(asus)
elif orm == 4 and hard >= 256 and ssd == False and price > 500 and condition == True:
    print(acer)
elif orm == 8 and hard >= 256 and ssd == True and price <= 900 and condition == False:
    print(samsung)
elif orm == 8 and hard >= 256 and ssd == True and price >= 1000 and condition == True:
    print(hp)
else:
    print("Your option will be available within 2 weeks")
