from textwrap import shorten


class calisan:
    premium =100
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
    def show_data(self):
        return "{}/{}/{}".format(self.isim,self.soyisim,self.maas)
calisan1 = calisan("Resad","nebiyev",2000)
calisan2 = calisan("Rahil","nebiyev",1200)


class yazilimci(calisan):
    premium = 120
    def __init__(self, isim, soyisim, maas,dil):
        super().__init__(isim, soyisim, maas)
        self.dil = dil
    def show_data(self):
        return "{}/{}/{}/{}".format(self.isim,self.soyisim,self.maas,self.dil)
        
calisan3 = yazilimci("x","y",3923,"python")


class yonetici(calisan):
    def __init__(self, isim, soyisim, maas,calisanlar=None):
        super().__init__(isim, soyisim, maas)
        if calisanlar == None:
            self.calisanlar=[]
        else:
            self.calisanlar = calisanlar
    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
    def calisan_dil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.show_data())        
            
            
yonetici1 = yonetici("yonetici","lider",3300)
yonetici1.calisan_ekle(calisan1)

yonetici1.calisanlari_goster()