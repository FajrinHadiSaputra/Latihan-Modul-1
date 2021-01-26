lagi='y'

while lagi=='y':

    print ('Aplikasi Perhitungan Gaji Karyawan')


    print ("===============================================================================")

    nama=input('Masukan Nama \t\t: ')

    gaji_pokok=float(input('Masukan Gaji Pokok Anda : '))

    print('1. Masa Kerja > 5 Tahun \n2. Masa Kerja < 5 Tahun')

    Masa_Kerja=input('Masukan Masa Kerja \t: ')

    print ('1. Pegawai Tetap \n2. Pegawai Magang')

    jabatan=input("Masukan Jabatan \t: ")

    print ('1. Sudah Berkeluarga \n2. Belum Menikah')

    Status=input('Masukan Status \t\t: ')

    if (jabatan=='1'):

        uang_Transport=150000

        jab='Pegawai Tetap'

    elif(jabatan=='2'):

        uang_Transport=0

        jab='Pegawai Magang'

    if(Masa_Kerja=='1'):

        bonus=float(gaji_pokok*15/100)

        kerja='Masa Kerja > 5 Tahun'

    elif(Masa_Kerja=='2'):

        bonus=0

        kerja='Masa Kerja < 5 Tahun'

    if(Status=='1'):

        tunjangan=500000

    elif(Status=='2'):

        tunjangan=250000


    gaji_bersih=float(gaji_pokok+tunjangan+bonus+uang_Transport)

    print ("")

    print ("\n")

    print ("===============================================================================")

    print ("")

    print ('Nama \t\t: ',nama)

    print ('Masa Kerja \t: ',kerja)

    print ('Jabatan \t: ',jab)

    print ('Gaji bersih \t: ','Rp. ',gaji_bersih)

    print ("")

    print ("===============================================================================")

    print ("")

    lagi=input("Ambil Data Lagi [y/n]? : ")