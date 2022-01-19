def halo_dunia():
    print('Halo python! Halo dunia!')


def perjumlahan(a, b):
    print(a+b)


def suhu_udara(daerah, derajat=30, satuan='celcius'):
    print(f"Suhu di {daerah} adalah {derajat} {satuan}")


def luas_persegi(sisi):
    """
    RUMUS LUAS PERSEGI
    """
    return sisi * sisi


def persentase(total, jumlah):
    if (total >= 0 and total <= jumlah):
        return total / jumlah * 100
    return False


halo_dunia()

perjumlahan(2, 3)

suhu_udara("medan", satuan="fahrenheit")

print("Luas persegi", luas_persegi(5))

# output 50
print(persentase(30, 60))

# output False
print(persentase(100, 60))
