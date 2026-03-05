# NAMA  : vellyprincessia
# KELAS : ix
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
# data awal
nilai_ujian = [75, 55, 90, 85, 45, 95, 80]
# tampilkan data asli
print("Data nilai asli:", nilai_ujian)
# urutkan dari tertinggi ke terendah
nilai_urut = sorted(nilai_ujian, reverse=True)
print("Data setelah diurutkan (Descending):", nilai_urut)
# ambil 3 nilai tertinggi
tiga_tertinggi = nilai_urut[:3]
print("Tiga nilai tertinggi (Penerima Beasiswa):", tiga_tertinggi)
# hapus nilai di bawah 60
nilai_lulus = [nilai for nilai in nilai_urut if nilai >= 60]
print("Daftar nilai yang lulus:", nilai_lulus)
