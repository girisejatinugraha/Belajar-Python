"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.
# Menghitung jumlah seluruh elemen array
total = sum(var_array)

# Menghitung banyaknya elemen array
jumlah_elemen = len(var_array)

# Menghitung nilai rata-rata
result = total / jumlah_elemen

# Menampilkan hasil perhitungan
print("Nilai rata-rata dari elemen array adalah:", result)