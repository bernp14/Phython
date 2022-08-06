# Premier essai de script Python
# petite programme affiche une suite de Fibonacci 

print("suite de Fibonacci :")

a,b,c = 1,1,1
print(b)
while c < 15:
    a,b,c = b, a+b, c+1
    print(b)
    
input("valider ...")