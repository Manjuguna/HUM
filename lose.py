nt,mt=list(map(int,input().split()))
lit=list(map(int,input().split()))
lit.sort(reverse=True)
cat=0
for i in lit:
    if mt==0:
        break
    qr=mt // i
    cat+=qr
    mt=mt-i*qr
print(cat)
