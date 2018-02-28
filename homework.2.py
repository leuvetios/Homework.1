print("hesap makinesi")
a = int(input("birinci sayiyi giriniz"))
b = int(input("ikinci sayiyi giriniz"))
c = input("islemi seçiniz")


if (c == "-"):
    d = a - b
    print("islem sonucu :")
    print(d)


elif (c == "+"):
    d = a + b
    print("islem sonucu :")
    print(d)

elif (c == "/"):
    d = a / b
    print(d)

elif (c == "*"):
    d = a * b
    print("islem sonucu :")
    print(d)
elif (c == "exit"):
    print ("çıkışınız")
else :
    print ("düzgün Giriniz LÜTFEN!!!!!")
