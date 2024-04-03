def paircheck(s):  # search all target and match from source
    l=[]
    s=list(s)
    n = len(s)
    for i in range(0, n):
         if (s[i] != ')') & (s[i] != '(' ):
             s[i]=' '
         if  (s[i] == ')') :
             if len(l)==0:
                 s[i]='?'
             else:
                 s[l[-1]]=' '
                 s[i] = ' '
                 l.pop()
         if (s[i] == '(' ) :
             l.append(i)
             s[i]='x'

    s1 = ''.join(s)
    print(s1)
    return s1



s = input()

paircheck(s)