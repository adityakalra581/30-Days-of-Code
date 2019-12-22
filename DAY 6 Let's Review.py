



n=int(input())

for j in range(n):
    s=input()
    e=[]
    o=[]
    for i in range(len(s)):
        if i%2==0:
            e.append(s[i])
        else:
            o.append(s[i])
    #print((*e),' ',(*o))
    print(''.join(e),''.join(o))
