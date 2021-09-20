x=int(input('introduceti nr de elemente din vector= '))
a=[]
if x>10:
    print('eror')
else:
    print('intoroduceti', x ,'elemente pu vectorul creat')
    for i in range(0,x):
        y=int(input('dati elemetele= '))
        a.extend([y])
    print(a)
print('a) afiseaza pe ecran comp tabloului la un interval de 5 prop;', a[0 : 5])
print('b) afiseaza pe ecran nr in ordine inversa a introduceriii in calculator' , a[::-1])
c=sorted(a)
c.sort(reverse=True)
print('c) sorteaza comp tabloului in ordine  descrescatoare;' , c)
print('d) afiseaza pe ecran doar comp pare;' ,)
d=[]
for i in range(0, len(a)):
    if a[i]%2==0:
        y=a[i]
        d.extend({y})
    print(d)
print('e) afiseaza pe ecran doar media aritmetica a comp pare:', sum(c) / len(c))
print('f) afiseaza pe ecran doar comp impare', *d)
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        f.extend({y})
print(f)
print('g) afiseaza pe ecran doar comp care sunt mari ca x si nu sunt diviziile cu y:')
g=[]
for i in range (0,len(lista)):
    if(lista[i]>x) and (lista[i]%y!= 0):
        g.append(lista[i])
print (g)
print('h) afiseaza pe ecran doar comp care sunt mari ca x si mai mici ca y:')
g=[]
for i in range (0,len(lista)):
    if(lista[i]>x) and (lista[i]<y):
        h.append(lista[i])
print(h)
print('i) afiseaza pe ecran pozitiile comp impare negative:')
i=[]
for i in range (0,len(lista)):
    if(lista[i]%x !=0) and (lista[i]<0):
        i.append(lista[i])
print(i)
print('m)creaza un tablou nou, form doar din comp pare  a tabl introdus de la tastatura:', d)
print('n)creaza un tablou nou, form doar din comp divizibile cu 3 a tabl introdus de la tastatura:')

