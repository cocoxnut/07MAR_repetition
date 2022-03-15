house = input("Enter preferred area: ")
made = int(input("Select made material: 1 if Brick, 0 if Sandblock: "))
land = int(input("Enter size of land: "))
price = int(input("Select your price: "))
if house.lower() == 'ortosai' or house.lower() == 'chon-aryk' or house.lower() == 'baytik':
    print(house)
if made == 1 and land <= 4 and price <= 50000:
    print("1st option")
elif made == 0 and land <= 5 and price <= 45000:
    print("2nd option")
else:
    print('Such option is not available')
