def tampilkanAngka(i):
    print(f'Perulangan ke {i}')


# panggil beberapa kali
tampilkanAngka(1)
tampilkanAngka(2)
tampilkanAngka(3)


def tampilkanAngka1(batas, i=1):
    """
    Fungsi yang pertama kali dipanggil, adalah fungsi yang terakhir kali selesai.
    Dan fungsi yang terakhir kali dipanggil, ia adalah fungsi yang paling pertama selesai.
    """
    prefix = '--' * (i - 1)

    print(f'{prefix} Sebelum rekursif ({i})')
    if (i < batas):
        # di sini lah rekursifitas itu terjadi
        tampilkanAngka1(batas, i + 1)

    print(f'{prefix} Setelah rekursif ({i})')


# memanggil fungsi tampilkanAngka
# untuk pertama  kali
tampilkanAngka1(5)
