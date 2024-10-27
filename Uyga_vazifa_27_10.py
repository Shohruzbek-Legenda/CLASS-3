from abc import ABC, abstractmethod

class Ota(ABC):
    def __init__(self, ism, yosh):
        self.ism = ism
        self._yosh = yosh
        self.kitoblar = []
        self.pul = 0
        self.yangi_uy = 4
        self.olingan_uylar = 0

        if self._yosh < 18:
            self.pul = 12000000
            print(f'{self.ism} uchun {self.pul} dan puldan foydalanish mumkin')
        else:
            print(f'{self.ism} uchun afsus, puldan foydalanish mumkin emas')

    @abstractmethod
    def haydash(self):
        pass

    @abstractmethod
    def kitob(self):
        pass

    def kitob_qidirish(self):
        return self.kitoblar

    def natijalarni_faylga_yozish(self):
        with open('natijalar.txt', 'a') as f:
            f.write(f'{self.ism} oqigan kitoblar: {self.kitoblar}\n')
            f.write(f'{self.ism} ning pul miqdori: {self.pul}\n')
            f.write(f'{self.ism} olgan uylar soni: {self.olingan_uylar}\n\n')

class Bola1(Ota):
    def __init__(self, ism, yosh, varoqlar_soni):
        super().__init__(ism, yosh)
        self.varoqlar = varoqlar_soni
        self.taboqlar = 4922000

    def haydash(self):
        print(f'{self.ism} haydashi mumkin')

    def kitob(self):
        self.taboqlar += self.varoqlar // 15
        if self.taboqlar > 0:
            self.pul += self.taboqlar * 13000
            self.kitoblar.append(self.taboqlar)

    def uy_berish(self):
        if self.pul >= 50000000 and self.yangi_uy > 0:
            self.pul -= 50000000
            self.yangi_uy -= 1
            self.olingan_uylar += 1
            print(f'{self.ism} yangi uy oldi! Qolgan uylar: {self.yangi_uy}')
        else:
            print(f'{self.ism} yangi uy olish uchun yetarlicha pul yoki uy yoq.')

class Bola2(Ota):
    def __init__(self, ism, yosh, varoqlar_soni):
        super().__init__(ism, yosh)
        self.varoqlar = varoqlar_soni
        self.taboqlar = 0

    def haydash(self):
        print(f'{self.ism} mashina haydashiga ruxsat yoq')

    def kitob(self):
        self.taboqlar += self.varoqlar // 15
        if self.taboqlar > 0:
            self.pul += self.taboqlar * 13000
            self.kitoblar.append(self.taboqlar)

    def uy_berish(self):
        if self.pul >= 50000000 and self.yangi_uy > 0:
            self.pul -= 50000000
            self.yangi_uy -= 1
            self.olingan_uylar += 1
            print(f'{self.ism} yangi uy oldi! Qolgan uylar: {self.yangi_uy}')
        else:
            print(f'{self.ism} yangi uy olish uchun yetarlicha pul yoki uy yoq.')

bola1 = Bola1('Ali', 15, 100)
bola2 = Bola2('Komil', 19, 1000)

bola1.haydash()
bola2.haydash()
bola1.kitob()
bola2.kitob()
print(f'{bola1.ism} oqigan kitoblar soni: {bola1.kitob_qidirish()}')
print(f'{bola2.ism} oqigan kitoblar soni: {bola2.kitob_qidirish()}')
bola1.uy_berish()
bola2.uy_berish()
bola1.natijalarni_faylga_yozish()
bola2.natijalarni_faylga_yozish()
