# Import Module untuk mengambil data waktu
import datetime
datenow = datetime.datetime.now()
#Data tahun sekarang telah didapatkan lalu simpan ke variabel this_year
this_year = datenow.year

#Minta user untuk memasukan tahunlahir mereka
data_user = int(input("Masukan Tahun Lahir anda : "))

#Hitung umur user dengan rumus
# Tahun sekarang - Tahun Lahir sekarang
get_age = this_year - data_user

#Tampilkan umur user
print(f'''Umur anda sekarang adalah {get_age} tahun ''')