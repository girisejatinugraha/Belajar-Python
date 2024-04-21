"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.
# Menghitung total harga belanja setelah diskon
potongan_harga = 0.1 * dico  # Menghitung besaran potongan harga
total_harga = dico - potongan_harga  # Menghitung total harga setelah diskon

# Menampilkan total harga belanja setelah diskon
print("Total harga belanja Dico setelah diskon:", total_harga)