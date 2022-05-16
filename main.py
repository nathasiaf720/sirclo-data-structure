import json
class Cart:
    def __init__(self):
        self.cart={}

    def tambahProduk(self, kodeProduk, kuantitas):
        if kodeProduk in self.cart:
            oldvalue = self.cart[kodeProduk]
            self.cart[kodeProduk]= int(kuantitas) + int(oldvalue)
        else:
            self.cart[kodeProduk]=kuantitas
        file = open("data.txt", "w")
        file.write(str(self.cart))
        file.close()

    def tampilkanCart(self):
        for i in self.cart.keys():
            print(i, " (", self.cart[i], ")")

    def hapusProduk(self, kodeProduk):
        if kodeProduk in self.cart:
            del self.cart[kodeProduk]
        else:
            print(kodeProduk,'was not found in shopping cart')

    def print_menu(self):
        print('\nSIRCLO SHOPPING CHART')
        print('Menu:')
        print('1. Tambah Produk')
        print('2. Hapus Produk')
        print('3. Tampilkan Cart')
        print('4. Exit')

def main():
    shoppingCart = Cart()
    pilihan=0
    while pilihan!=4:
        shoppingCart.print_menu()
        pilihan = int(input('Input Pillihan: '))
        if pilihan==1:
            print('\nTambahkan Produk')
            kodeProduk=input('Kode Produk =')
            kuantitas=input('Kuantitas =')
            shoppingCart.tambahProduk(kodeProduk, kuantitas)
        elif pilihan==2:
            print('\nHapus Produk')
            kodeProduk=input('Kode Produk=')
            shoppingCart.hapusProduk(kodeProduk)
        elif pilihan==3:
            print('\nTampilkan Produk')
            print(shoppingCart.cart)
            shoppingCart.tampilkanCart()
            print()
        elif pilihan!=4:
            shoppingCart.print_menu()

if __name__ == '__main__':
    main()