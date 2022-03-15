orm = int(input('Выберите количество оперативной памяти 4 или 8: '))
ssd = int(input('Выберите 1 если SSD, выберите 0 если HDD: '))
hard = int(input('Выберите объем: 256, 512, 1024 Gb: '))
condition = int(input('Выберите состояние ноутбука 1 если новый, выберите 0 если б/у: '))
price = int(input('Введите цену: '))
hp = 'Hp 550x 1000$ 8Gb 256SSD новый'
samsung = 'Samsung 150 Turbo 900$ 8Gb 256SSD б/у'
acer = 'Acer Predator 600$ 4Gb 1024HDD новый'
asus = 'Asus 550x 300$ 4Gb 1024HDD б/у'
'orm ssd hard condition price'
if orm == 8 and hard >= 256 and ssd == True and price > 300 and condition == True:
    print(hp)
if orm == 8 and hard >= 256 and ssd == True and price > 300 and condition == False:
    print(samsung)
if orm == 4 and hard >= 256 and ssd == False and price > 300 and condition == True:
    print(acer)
if orm == 4 and hard >= 256 and ssd == False and price > 300 and condition == False:
    print(asus)
