data = int(input("Berapa data: "))

nama_pelanggan = []
umur_pelanggan = []

for i in range(data):
 print("Data ke {}". format(i+1))
 nama = input("Nama : ")
 umur = int(input("Umur : "))

 nama_pelanggan.append(nama)
 umur_pelanggan.append(umur)

for i in range(len(nama_pelanggan)):
  print("Pelanggan bernama {} berumur {} tahun". format(nama_pelanggan[i], umur_pelanggan[i]))
  