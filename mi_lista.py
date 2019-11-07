my_list=["gtx 1080","rtx 2080","rtx 2080 ti","rx 580","fuente"]

while list != "end":
    list=input("what yo want? (end to finish)")
    if list!="end":
       my_list.append(list)

lenght_list=len(my_list)
indicator=0

while indicator < lenght_list:
    print("cosas q quiero como {}".format(my_list[indicator]))
    indicator += 1

for item in my_list:
    print("cosas q quiero como {}".format(item))