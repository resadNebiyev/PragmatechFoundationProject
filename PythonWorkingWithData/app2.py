# #1 istifadeci adi daxil etmek
# my_list = []
# while True:
#     _name = input("adinizi daxil edin: ")
#     my_list.append(_name)
#     _emr = input("Yeni Istifadeci Daxil Edilsinmi? Y/N ")
#     if _emr.upper() == "Y":
#         pass
#     else:
#         break 
# print(my_list)
# #2 istifadeci adinin silinmesi
# while True:
#     emr2 = input("Ad silmek isteyirsinizmi? Y/N: ")
#     if emr2.upper() == "Y":
#         sual2 = input("silmek istediyiniz adi secin: ")
#         for i in my_list:
#             if i == sual2:
#                 my_list.remove(sual2)              
#     else:
#         break
# print(my_list)
# #3 istifadeci adinin deyisilmesi
# while True:
#     emr3 = input("Melumatlari deyismek isteyirsinizmi? Y/N: ")
#     if emr3.upper() == "Y":
#         sual3 = input("Deyismek istediyiniz adi daxil edin: ")
#         sual4 =input("Yeni adi daxil edin: ")
#         x = my_list.index(sual3)
#         my_list[x] = sual4 
#     else:
#         break
# print(my_list)   
                
    
# arr=[1,34,23,90,230,1400,600,300,240]
#1 En Boyuk Uc ededin Ekrana Cap Edilmesi
# def enboyukuceded(n):
#     arr.sort(reverse=True)
#     print(arr[:n])
# enboyukuceded(3)

#2 Ədədlərin ortalamasından böyük olan ədədləri ekrana çap edin
# def my_function2():
#     cem=0
#     for eded in arr:
#         cem+=eded
#     averageofarr = cem/len(arr)
#     for i in arr:
#         if i > averageofarr:
#             print(i)
# my_function2()

#3 2 rəqəmli ədədləri ekrana çap edin.
# def my_function3():
#     for eded in arr:
#         if eded>9 and eded<100:
#             print(eded)
# my_function3()

#4 Bu listin içərisində olan ədədlərin rəqəmlərinin cəmini ekrana çap edin
# def my_function4():
#     for eded in arr:
#         cem = 0
#         for reqem in str(eded):
#             cem+=int(reqem) 
#         print(cem)
# my_function4()

# countries=['Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan']
#1 Bütün ölkələrin hərf sayını tapın
# def myfunction1():
#     for country in countries:    
#         x=len(country)
#         print(f"{country} olkesinin herf sayi :{x}")
# myfunction1()
#2 Ən uzun ölkə adını tapın
# def my_function2():
#     arr_list=[]
#     for country in countries:
#         arr_list.append(len(country))
#     for country in countries:
#         if max(arr_list)==len(country):
#             print(country)
# my_function2()
#3 Daxilində A hərfi olan ölkələri tapın
# def my_function3():
#     for country in countries:
#         for herf in country:
#             if herf == "A":
#                 print(country)
# my_function3()            
