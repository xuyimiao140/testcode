def findallsequence(s, t): #search all target and match from source
        count = 1  #match patch
        pos = -1 #start position
        n = len(t)
        for i in range(0,n):
            if s.find(t[i]) == -1:
                count= -1
                break

            pos = s.find(t[i], pos + 1)
            if pos == -1 :#check if is the same sequence,if not,add match number
                count+=1;
                pos = s.find(t[i])

        print (count)
        return count
s=input()
t=input()

findallsequence(s,t)




