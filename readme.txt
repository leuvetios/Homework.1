a = 1
b = 1
                            *burda deðiþkenleri tanýtýyoruz 
print (a)
print (b)
                            *burda bir kereliðine yazdýrýyoruz 
i = 2
                            *döngümüzü sayacýný burda baþlatýyoruz
while i <= 6 :              *while döngüsünü i'den 6'a kadar döndürücez

     a , b = b ,  a+b        *Döngüde, Python’a özgü bir çokuz atamasý yapýyoruz
                              olmasaydý çoklu atama aþaðýdaki gibi olucaktý.
                                           a_eski = a
                                           b_eski = b
                                           a = b_eski
                                           b = a_eski + b_eski)
    print(b)                 *b yi yazdýrýyoruz
    i = i + 1                *sayacý bir arttýrýyoruz
