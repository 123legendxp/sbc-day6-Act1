size = 5  

row = 0
while row < size:
    col = 0
    while col < size:
        if row != 0 and row != size - 1 and col != 0 and col != size - 1:
            print('', end='  ')  
        else:
            print('*', end=' ')  
        col += 1
    print()  
    row += 1
