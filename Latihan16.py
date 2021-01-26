lagi='y'

while lagi=='y':
    t=int(input('Masukan Tinggi = '))
    a=int(input('Masukan Alas   = '))
    luas = 0.5*a*t 
    print('Luas segitiga =',luas,'cm2')
    print('')

    lagi=input("Ambil Data Lagi [y/n]? : ")
    print('')