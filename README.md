# Homework.1








Fibonacci week1 wekk2 
a = 1
b = 1
                            *burda değişkenleri tanıtıyoruz 
print (a)
print (b)
                            *burda bir kereliğine yazdırıyoruz 
i = 2
                            *döngümüzü sayacını burda başlatıyoruz
while i <= 6 :              *while döngüsünü i'den 6'a kadar döndürücez

     a , b = b ,  a+b        *Döngüde, Python’a özgü bir çokuz ataması yapıyoruz
                              olmasaydı çoklu atama aşağıdaki gibi olucaktı.
                                           a_eski = a
                                           b_eski = b
                                           a = b_eski
                                           b = a_eski + b_eski)
    print(b)                 *b yi yazdırıyoruz
    i = i + 1                *sayacı bir arttırıyoruz
