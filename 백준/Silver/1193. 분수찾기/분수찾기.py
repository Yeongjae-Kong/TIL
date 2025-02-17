n = int(input())

i=1
j=1
while i+j <= n:
    i += j
    j += 1
a=n-i+1
b=j-n+i

if j % 2 == 1:
    ans = '{1}/{0}'.format(a,b)
else:
    ans = '{0}/{1}'.format(a,b)
print(ans)