liczba=int(input("Podaj liczbe od 0-10 "))
while liczba!=5:
 if liczba<0 or liczba>10:
     print("Liczba musi być od 0 do 10!")
 elif liczba<5:
    print("Podałeś za małą liczbe!")
    
 elif liczba>5:
    print("Podałeś za dużą liczbę")
    
 liczba=int(input("Podaj liczbe od 0-10 "))