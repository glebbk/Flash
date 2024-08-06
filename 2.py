f = open('17.txt')
a = [int(x) for x in f]
count = 0
maxs = 0
for i in range(1,len(a)-3):
    sr1 = (max(a[i],a[i+1],a[i+2]) + min(a[i],a[i+1],a[i+2]))/2
    sr2 = (a[i-1] + a[i+3])/2
    if sr1 >= sr2:
        count += 1
        s = a[i] + a[i+1] + a[i+2]
        maxs = max(maxs,s)
print(count,maxs)
