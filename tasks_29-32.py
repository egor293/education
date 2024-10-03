


class Solution:
    def reverseOnlyLetters(self, s):
        s=list(s)
        b=[]
        c={}
        for i in range(len(s)-1,0,-1):
            if s[i].isalpha==True:
                b.append(s[i])
            else:
                c[s.index(s[i])]=s[i]
        for i,o in c.items():
            b.insert(i,o)
        return ''.join(b)




        
 