import pyotp
import qrcode

key = pyotp.random_base32()

# key = "JBSWY3DPEHPK3PXP"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="Ryas-Yusenda", issuer_name="Python 2FA")

qrcode.make(uri).save("qrcode.png")

totp = pyotp.TOTP(key)

"""
1. BUKA FILE qrcode.png
2. SCAN QR CODE DENGAN APLIKASI GOOGLE AUTHENTICATOR
3. MASUKKAN KODE YANG DIBERIKAN OLEH APLIKASI GOOGLE AUTHENTICATOR

"""

while True:
    print(totp.verify(input("Enter code: ")))