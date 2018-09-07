print ("Büyük küçük sayı bulma programı")
a= int(input("İlk sayıyı giriniz"))
b= int(input("İkinci sayıyı giriniz"))
c= int(input("Son sayıyı giriniz"))
if a<b and a<c:
    print ("En küçük sayı :",a)
    if b>c:
        print("En büyük sayı :",b)
    else:
        print("En büyük sayı :",c)
if b<a and b<c:
    print ("En küçük sayı :",b)
    if a > c:
        print("En büyük sayı :",a)
    else:
        print("En büyük sayı :",c)
if c<a and c<b:
    print ("En küçük sayı :",c)
    if a > b:
        print("En büyük sayı :",a)
    else:
        print("En büyük sayı :",b)
if a==b==c:
    print("Yazdığınız Sayılar eşit")
elif a==b:
    if c>a==b:
        print(c,"En büyük sayıdır",a,"ve",b,"en küçük sayılardır")
    else:
        print(a,"ve",b,"En Büyük sayılardır","ve",c,"en küçük sayıdır")
elif a==c:
    if b>a==c:
        print(c,"En büyük sayıdır",a,"ve",b,"eşit olup en küçük sayılardır")
    else:
        print(a,"ve",c,"En Büyük sayılardır","ve",b,"en küçük sayıdır")
elif b==c:
    if a > b == c:
        print(a, "En büyük sayıdır", c, "ve", b, "eşit olup en küçük sayılardır")
    else:
        print(b, "ve", c, "En Büyük sayılardır", "ve", a, "en küçük sayıdır")
