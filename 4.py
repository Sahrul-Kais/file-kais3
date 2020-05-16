def findDuplicates(sentence=None):
    
    if type(sentence) == str and sentence != None:
        daftar = {}
        for i in sentence:
            daftar[i]=daftar.get(i,0)+1
            
        for k, v in list(daftar.items()):
            if v == 1 or k== " ":
                del daftar[k]
        
        hasil = "".join(("{} : {}\n".format(*i) for i in daftar.items()))    
        
        if len(daftar)>0:
            print(hasil)
        else:
            print("Tidak ada karakter yang berulang!")
    else:
        print("Harus memasukan parameter dan harus string!")

findDuplicates("sahrul kais")