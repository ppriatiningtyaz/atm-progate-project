class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance
#cek pin
    def cekPinAwal(self):
        return self.defaultPin
#cek saldo awal
    def cekSaldoAwal(self):
        return self.defaultBalance