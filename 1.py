def triangle(n):
    if(type(n)==int and n>0):
        for i in range(0,n):
            for j in range(0,i+1):
                print("# ", end="")
            print("")
    else:
        print("Paramemeter harus angka dan positif!")

triangle(10)