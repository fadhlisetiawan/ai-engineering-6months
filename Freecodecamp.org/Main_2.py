#Build an Apply Discount Function
#https://www.freecodecamp.org/learn/python-v9/lab-discount-calculator/build-a-discount-calculator

#Cara Panjang
def cara_panjang():
    print ('--- Hasil cara panjang---')

    def apply_discount (price,discount):

        # Cek tipe data (type(...) not in otomatis menolak tipe boolean)
        if not isinstance (price, (int,float)):
            return 'The price should be a number'

        if not isinstance (discount, (int,float)):
            return 'The discount should be a number'
        
        # Cek nilai/range
        if price <= 0:
            return 'The price should be greater than 0'

        if discount < 0 or discount > 100:
            return 'The discount should be between 0 and 100'
        
        # Hitung dan kembalikan harga akhir
        return price - (price * discount/100)


    print (apply_discount(100,20))
    print (apply_discount(200,50))
    print (apply_discount(50,0))
    print (apply_discount(20,100))
    print (apply_discount(74.5, 20))


#cara pendek
def cara_pendek():
    print ('---Hasil cara pendek---')

    def apply_discount(price, discount):
        # Cek tipe data (type(...) not in otomatis menolak tipe boolean)
        if type(price) not in (int, float):
            return 'The price should be a number'
        if type(discount) not in (int, float):
            return 'The discount should be a number'

        # Cek nilai/range
        if price <= 0:
            return 'The price should be greater than 0'
        if discount < 0 or discount > 100:
            return 'The discount should be between 0 and 100'

        # Hitung dan kembalikan harga akhir
        return price - (price * discount / 100)

    print (apply_discount(100,20))
    print (apply_discount(200,50))
    print (apply_discount(50,0))
    print (apply_discount(20,100))
    print (apply_discount(74.5, 20))


cara_panjang()
cara_pendek()