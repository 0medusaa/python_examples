import random
secenek=["tas","kagıt","makas"]
tas= secenek [0]
kagıt= secenek [1]
makas= secenek [2]

print("Taş,Kağıt, Makas oyununa hoş geldiniz Oyunu bitirmek için q tuşuna basın")

while True:
    secim=input("taş mı ? kağıt mı? makas mı?")
    bil_secim=random.choice(secenek)
    if secim==tas:
        if bil_secim==tas:
            print("pc secimi taş  berabere kaldınız")
        elif bil_secim== kagıt:
            print("pc secimi kağıt kaybettiniz") 
        else:
            print("pc secimi makas  kazandınız")
    if secim== kagıt:
        if bil_secim==tas:
            print("pc secimi tas  kazandınız")
        elif bil_secim== kagıt:
            print("pc secimi kagıt berabere kaldınız")
        else:
            print("pc secimi makas  kaybettiniz ")
    if secim== makas:
        if bil_secim== makas:
            print("pc secimi makas  berabere kaldınız")
        elif bil_secim== tas:
            print("pc secimi tas  kazandınız")
        else:
            print("pc secimi kağıt  kaybettiniz")
    if secim=="q":
            print("cıkıs yapılıyo")
            break
