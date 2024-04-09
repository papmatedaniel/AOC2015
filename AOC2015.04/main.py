import hashlib

szazlo = True
while szazlo:
    for i in range(100000000):
        szam = str(i)
        szoveg = "ckczppom" + szam
        md5_hash = hashlib.md5(szoveg.encode()).hexdigest()
        if md5_hash[:6] == "000000":
            print(szam)
            szazlo = False
            break