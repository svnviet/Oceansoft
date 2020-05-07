def cal(x,y,step):
    if x==y:
        return 'Step=',step
    elif y<x:
        return cal(x-1,y,step+1)
    elif y%2==1:
        return cal(x,y+1,step+1)
    else:#y%2==0:
        return cal(x,y/2,step+1)
print(cal(int(input()),int(input()),step=0))                                                                        
