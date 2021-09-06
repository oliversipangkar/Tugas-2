#library clear screen
import os

#fungsi menu
def main ():
    print ("\n--Menu--")
    print ("1. Daftar Kontak")
    print ("2. Tambah Kontak")
    print ("3. Keluar")
    menu = (int (input ("\nPilih Menu : ")))
    #menghilangkan menu
    os.system ('cls')
    if menu == 1 :
        print ("Daftar Kontak\n")
        for x in daftarkontak:
            print (x)
        main ()
    elif menu == 2 :
        tambahkontak ()
        print ("\nKontak Berhasil Ditambahkan\n")
        main ()
    elif menu == 3 :
        print ("Program Selesai, Sampai Jumpa!")
    else :
        print ("Menu Tidak Tersedia\n")
        main ()

#fungsi menqambahkan kontak
def tambahkontak ():
    daftarkontak.append (input ("Nama : "))
    daftarkontak.append (input ("No Telepon : "))

#main program
daftarkontak = [] #membuat list diluar fungsi agar tidak menimbulkan perbedaan data
print ("Selamat Datang!")
main ()