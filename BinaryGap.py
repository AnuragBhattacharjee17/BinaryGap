# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    c= bin(N)
    c=c[2:]
    c=c[::-1]
    
    p=0
    if(c[0]=='0'):
        for i in range(0,len(c)):
            if(c[i]!='1'):
                p+=1
            else:
                c=c[p:]
                return(int(max(map(len,c.split("1")))))
                
    else:
        return(int(max(map(len,c.split("1")))))