f = open('17.txt')
a = [int(x) for x in f]
count = 0
mins = 10**10
for i in range(len(a)-2):
    sr = (a[i]+a[i+1])/2
    if sr < a[i+2]:
        count += 1
        s = a[i]+a[i+1]
        mins = min(mins,s)
print(count,mins)
