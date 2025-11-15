#3-misol
class MenyuItem:
    def tayyorlash_vaqti(self):
        raise NotImplementedError

    def narx_hisoblash(self, miqdor):
        raise NotImplementedError

    def allergiya_tekshirish(self, ingredient):
        return False  # Default


class Ovqat(MenyuItem):
    allergenlar = ["tuxum", "sut", "yong‘oq"]

    def tayyorlash_vaqti(self):
        return 15

    def narx_hisoblash(self, miqdor):
        return 25000 * miqdor

    def allergiya_tekshirish(self, ingredient):
        return ingredient in self.allergenlar


class Ichimlik(MenyuItem):
    def tayyorlash_vaqti(self):
        return 3

    def narx_hisoblash(self, miqdor):
        return 8000 * miqdor


class Desert(MenyuItem):
    def tayyorlash_vaqti(self):
        return 7

    def narx_hisoblash(self, miqdor):
        return 15000 * miqdor
