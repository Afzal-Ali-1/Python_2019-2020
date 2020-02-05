import pickle 
file=open("qwerty","rb")
data=pickle.load(file)
print(data)
file.close()
