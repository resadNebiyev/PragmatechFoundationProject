def write(x,y):
    if x<y:
        x+=1
        print(x)
        write(x,y)  
write(0,10)