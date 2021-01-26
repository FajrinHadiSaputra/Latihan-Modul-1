lagi='y'

while lagi=='y':
    print('Konverensi suhu Celcius ke Fahrenheit')
    c = int(input('Masukkan nilai Celcius\t\t: '))
    f = c*9/5+32
    print('Nilai Suhu Dalam Fahrenheit\t:',f)
    print('')

    lagi=input("Ambil Data Lagi [y/n]? : ")
    print('')