import re
def cek_kata(sentence):
    sentence1 = len(re.findall(r"\D\w+\D", sentence))
    sentence2 = len(re.findall(r"\w+", sentence))
    print (sentence1,"/",sentence2)
cek_kata("2 pasang sandal hilang")