"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini.
# Menggunakan list comprehension untuk membuat list bilangan genap dari 0 hingga 500
evenNumber = [num for num in range(501) if num % 2 == 0]

# Menampilkan isi variabel evenNumber
print("Bilangan genap dari 0 hingga 500:")
print(evenNumber)