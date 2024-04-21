"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.

def minimal(a, b):
    if a <= b:
        return a
    else:
        return b

# Contoh penggunaan fungsi minimal:
print(minimal(5, 3))  # Output: 3
print(minimal(7, 9))  # Output: 7
print(minimal(4, 4))  # Output: 4
