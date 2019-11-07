want_ice_cream=input("do you want ice cream? (yes/no)").upper()
have_money=input("do you have money? (yes/no)")
dulce_deleite=input("its dulce deleite open? (yes/no)")
fmi=input("does fmi lend you money? (yes/no)")

if want_ice_cream=="SI":
    want_ice_cream=True
elif want_ice_cream=="NO":
    want_ice_cream=False
else:
    print("ASEREJE")
    want_ice_cream=False

chau=have_money=="yes" or fmi=="yes"
hasta=dulce_deleite=="yes"

if chau and hasta:
    print("eat it")
else:
    print("poor")