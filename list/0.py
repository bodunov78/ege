a=[1,3,5,7,9,2,4,6,8]
# s=['1','3','5','7','9','2','4','6','8']
# m=''.join(s)
# n=''.join(map(str,a))
# m="".join(str(i) for i in a)


# x=[str(i) for i in a]
# print (a,x)


m="12345"
k=0
c=[int(v)*9**i for i,v in enumerate(m[::-1])]
print (c)


m=m.replace('23',':')

# m=list(m)
print (m,list(m.split(':')))
m=[[x+y for x in range(y)] for y in range(10,15)]
for x in m:
    for y in x:
        print (x,y)

print (m)
# print (m)
# print (n)



# b=a[::-1] #(перевернутый)
# c=a[::]
# c[0]=1
# d=a
# d[0]=-1
#
# print (id(a),id(b),id(c),id(d))
# print (a,c,d)
#a.sort(reverse=1)

print(sorted(a,reverse=1))
#print (a)
m="".join(str(i) for i in a)


print (a,m)
# print (a,b,m)

# print (m,sorted(m,reverse=1))