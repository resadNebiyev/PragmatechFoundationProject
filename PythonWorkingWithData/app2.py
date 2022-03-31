
my_list = []
while True:
    _name = input("adinizi daxil edin: ")
    my_list.append(_name)
    _emr = input("Yeni Istifadeci Daxil Edilsinmi? Y/N ")
    if _emr.upper() == "Y":
        pass
    else:
        break 
print(my_list)

while True:
    emr2 = input("Ad silmek isteyirsinizmi? Y/N: ")
    if emr2.upper() == "Y":
        sual2 = input("silmek istediyiniz adi secin: ")
        for i in my_list:
            if i == sual2:
                my_list.remove(sual2)              
    else:
        break
print(my_list)

while True:
    emr3 = input("Melumatlari deyismek isteyirsinizmi? Y/N: ")
    if emr3.upper() == "Y":
        sual3 = input("Deyismek istediyiniz adi daxil edin: ")
        sual4 =input("Yeni adi daxil edin: ")
        x = my_list.index(sual3)
        my_list[x] = sual4 
    else:
        break
print(my_list)   
                
                
