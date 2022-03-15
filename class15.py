genre = input("Select preferred film genre: ")
time = int(input("Preferred time: "))
price = int(input("Select price: "))

a = '"The Call", horror, 20, 500 som'
b = '"The Oriental Express", detective, 19, 500 som'
c = '"The Click", comedy, 19, 500 som'
d = '"The Resident Evil 5", horror, 22, 200 som'
e = '"The Supernatural", horror, 21, 300 som'
f = '"Kill the President", detective, 22, 200 som'
g = '"Daddy Nanny", comedy, 21, 300 som'

if genre.lower() == 'horror' and time < 21 and price == 500:
    print(d, "\n", e, "\n")
if genre.lower() == 'detective' and time < 21 and price == 500:
    print(f)
if genre.lower() == 'comedy' and time < 21 and price == 500:
    print(g)
elif genre.lower() == 'horror' and time >= 21 and price <= 300:
    print(d, "\n", e, "\n")
elif genre.lower() == 'detective' and time >= 21 and price <= 300:
    print(f)
elif genre.lower() == 'comedy' and time >= 21 and price <= 300:
    print(g)
else:
    print("Such option is not available")
