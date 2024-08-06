f = open('17.txt')
a = [int(x) for x in f]
count = 0
mins = 10**10
curs = 0
k = 0
for i in range(1, len(a)-2):
    k += 1
    curs += a[i-1]
    sr = curs/k
    if (sr>a[i]) + (sr>a[i+1]) + (sr>a[i+2])>=2:
        count += 1
        s = a[i]+a[i+1] + a[i+2]
        mins = min(mins,s)
print(count,mins)
