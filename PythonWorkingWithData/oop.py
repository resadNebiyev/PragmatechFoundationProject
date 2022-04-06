users=[]
class User:
    def __init__(self,_ad,_soyad,_email):
        self.Ad=_ad
        self.Soyad=_soyad
        self.Email=_email
    def getUserData(self):
        return f'{self.Ad} | {self.Soyad} | {self.Email}'

def UserRegistration():
    daxilEdilenAd=input('Zəhmət olmasa adınızı daxil edin:')
    daxilEdilenSoyad=input('Zəhmət olmasa soyadınızı daxil edin:')
    daxilEdilenEmail=input('Zəhmət olmasa email adresinizi daxil edin:')
    user=User(daxilEdilenAd,daxilEdilenSoyad,daxilEdilenEmail)
    users.append(user)
def ShowAllUser():
    for user in users:
        print(user.getUserData())
        
 # datani delete elemek       
def deletedata():
    x = input("adi daxil edin: ")
    for user in users:
        if user == x:
            users.pop(users.index(user)) 
        
        
while True:
    programMenyusu="""
    - Qeydiyyat üçün 1 yaz
    - İstifadəçiləri görmək üçün 2 yaz
    - Istifadeci adi silmek ucun 3 yaz 
    - Programdan çıxmaq üçün 4 yaz
    """
    print(programMenyusu)
    istifadəçininQerarı=input('Hansı əməlyatı yerinə yetirmək istəyirsən? : ')
    if istifadəçininQerarı=="1":
        UserRegistration()
    elif istifadəçininQerarı=="2":
        ShowAllUser()
    elif istifadəçininQerarı=="3":
        deletedata()
    elif istifadəçininQerarı=="4":
        break
    else:
        print('Qərarınızı anlaşılmayan qərardır.Təkrar cəhd edin')
        